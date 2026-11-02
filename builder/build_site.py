#!/usr/bin/env python3
"""
PATHIVARA LAW FIRM SUNSARI - Site Builder Orchestrator
Renders all 56 semantic pages into dist/, copies assets, and produces sitemap.xml & robots.txt.
"""

import os
import shutil
import json
import sys
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from src.data.services import SERVICES
from src.data.articles import get_articles
from src.data.team import TEAM_MEMBERS
from src.data.faqs import GLOBAL_FAQS

from builder.render_home import render_home
from builder.render_services import render_service_page, render_services_index
from builder.render_articles import render_article_page, render_resources_index
from builder.render_trust import (
    render_about_page,
    render_team_index,
    render_lawyer_profile,
    render_consultation_page,
    render_contact_page,
    render_faqs_page,
    render_testimonials_page,
    render_privacy_page,
    render_terms_page,
    render_disclaimer_page,
    render_cookie_page,
    render_accessibility_page,
    render_sitemap_page,
    render_404_page
)

DIST_DIR = os.path.join(BASE_DIR, "dist")
CONFIG_PATH = os.path.join(BASE_DIR, "config", "business.json")
BASE_PATH = os.environ.get("SITE_BASE_PATH", "").strip().rstrip("/")

def load_business_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def apply_base_path(html_content):
    if not BASE_PATH:
        return html_content
    import re
    # Prefix root-relative href and src (excluding protocol-relative //)
    html = re.sub(r'href="/(?![/])', f'href="{BASE_PATH}/', html_content)
    html = re.sub(r'src="/(?![/])', f'src="{BASE_PATH}/', html)
    return html

def write_page(url_path, html_content):
    clean_path = url_path.strip("/")
    if clean_path == "" or clean_path == "index.html":
        target_dir = DIST_DIR
        target_file = os.path.join(target_dir, "index.html")
    elif clean_path == "404" or clean_path == "404.html":
        target_dir = DIST_DIR
        target_file = os.path.join(target_dir, "404.html")
    else:
        target_dir = os.path.join(DIST_DIR, clean_path)
        target_file = os.path.join(target_dir, "index.html")

    os.makedirs(target_dir, exist_ok=True)
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(apply_base_path(html_content))

def generate_xml_sitemap(all_urls, config):
    site_url = config.get("site_url", "https://www.pathivaralawfirmsunsari.com")
    today = datetime.now().strftime("%Y-%m-%d")

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    for url, prio, changefreq in all_urls:
        clean_url = url if url.startswith("http") else f"{site_url}{url}"
        xml_lines.append(f"""  <url>
    <loc>{clean_url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{prio}</priority>
  </url>""")

    xml_lines.append('</urlset>')

    sitemap_path = os.path.join(DIST_DIR, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines))
    print(f"Generated XML sitemap with {len(all_urls)} URLs at {sitemap_path}")

def generate_robots_txt(config):
    site_url = config.get("site_url", "https://www.pathivaralawfirmsunsari.com")
    robots_content = f"""# Robots.txt for {config.get('firm_name', 'PATHIVARA LAW FIRM SUNSARI')}
User-agent: *
Allow: /

# XML Sitemap
Sitemap: {site_url}/sitemap.xml
"""
    robots_path = os.path.join(DIST_DIR, "robots.txt")
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(robots_content)
    print(f"Generated robots.txt at {robots_path}")

def copy_assets():
    src_assets = os.path.join(BASE_DIR, "assets")
    dist_assets = os.path.join(DIST_DIR, "assets")

    if os.path.exists(dist_assets):
        shutil.rmtree(dist_assets)
    shutil.copytree(src_assets, dist_assets)
    print(f"Copied static assets from {src_assets} to {dist_assets}")

def main():
    print("==================================================")
    print("Building PATHIVARA LAW FIRM SUNSARI Static Website...")
    print("==================================================")

    config = load_business_config()
    services = SERVICES
    articles = get_articles()
    team = TEAM_MEMBERS
    faqs = GLOBAL_FAQS

    os.makedirs(DIST_DIR, exist_ok=True)
    all_urls = []

    # 1. Homepage
    write_page("/", render_home(config, services, articles, team, faqs))
    all_urls.append(("/", "1.0", "weekly"))
    print("✓ Built / (Homepage)")

    # 2. Services Index
    write_page("/services/", render_services_index(services, config))
    all_urls.append(("/services/", "0.9", "monthly"))
    print("✓ Built /services/ (Practice Areas Directory)")

    # 3. 10 Core Money Pages
    for s in services:
        url = f"/services/{s.slug}/"
        write_page(url, render_service_page(s, config))
        prio = "0.9" if s.slug in ["civil-litigation", "criminal-law", "family-law", "property-land-law", "corporate-business-law"] else "0.8"
        all_urls.append((url, prio, "monthly"))
        print(f"✓ Built {url}")

    # 4. Resources Index
    write_page("/legal-resources/", render_resources_index(articles, config))
    all_urls.append(("/legal-resources/", "0.9", "weekly"))
    print("✓ Built /legal-resources/ (Knowledge Hub)")

    # 5. 30 Supporting Articles
    for a in articles:
        url = f"/legal-resources/{a.slug}/"
        write_page(url, render_article_page(a, config))
        all_urls.append((url, "0.8", "monthly"))
        print(f"✓ Built {url}")

    # 6. Trust & Governance Pages
    trust_pages = [
        ("/about/", render_about_page(config), "0.7", "monthly"),
        ("/team/", render_team_index(team, config), "0.7", "monthly"),
        ("/team/senior-advocate-profile/", render_lawyer_profile(config), "0.7", "monthly"),
        ("/legal-consultation/", render_consultation_page(config), "0.9", "monthly"),
        ("/contact/", render_contact_page(config), "0.8", "monthly"),
        ("/faqs/", render_faqs_page(faqs, config), "0.7", "monthly"),
        ("/testimonials/", render_testimonials_page(config), "0.5", "monthly"),
        ("/privacy-policy/", render_privacy_page(config), "0.4", "yearly"),
        ("/terms-of-use/", render_terms_page(config), "0.4", "yearly"),
        ("/legal-disclaimer/", render_disclaimer_page(config), "0.5", "yearly"),
        ("/cookie-policy/", render_cookie_page(config), "0.3", "yearly"),
        ("/accessibility/", render_accessibility_page(config), "0.4", "yearly"),
        ("/sitemap/", render_sitemap_page(services, articles, config), "0.6", "weekly"),
        ("/404.html", render_404_page(config), "0.1", "yearly")
    ]

    for url, html_str, prio, freq in trust_pages:
        write_page(url, html_str)
        if url != "/404.html":
            all_urls.append((url, prio, freq))
        print(f"✓ Built {url}")

    # 7. XML Sitemap & Robots.txt
    generate_xml_sitemap(all_urls, config)
    generate_robots_txt(config)

    # 8. Copy Assets
    copy_assets()

    print("==================================================")
    print(f"SUCCESS: Successfully generated all {len(all_urls)} indexable pages + 404 page into dist/")
    print("==================================================")

if __name__ == "__main__":
    main()
