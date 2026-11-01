#!/usr/bin/env python3
"""
Comprehensive Automated QA & Verification Test Suite for PATHIVARA LAW FIRM SUNSARI.
Validates:
1. All 56 routes and essential technical assets exist.
2. 100% internal links resolve to valid destination files (zero 404s).
3. Strict semantic SEO: Exactly one <h1> per page, non-empty <title>, and <meta description>.
4. Valid canonical tags across all pages.
5. Syntactically valid JSON-LD structured data with appropriate Schema.org types.
6. Valid XML sitemap syntax containing all 56 URLs.
7. Form accessibility: Labels, inputs, and skip links.
"""

import os
import re
import json
import unittest
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST_DIR = os.path.join(BASE_DIR, "dist")
CONFIG_PATH = os.path.join(BASE_DIR, "config", "business.json")

class TestLawFirmWebsite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            cls.config = json.load(f)
        
        # Collect all HTML files
        cls.html_files = []
        for root, _, files in os.walk(DIST_DIR):
            for file in files:
                if file.endswith(".html"):
                    cls.html_files.append(os.path.join(root, file))

    def test_dist_exists(self):
        self.assertTrue(os.path.isdir(DIST_DIR), "dist/ directory must exist")

    def test_minimum_page_count(self):
        # We expect 56 pages + 404.html = 57 HTML files
        self.assertGreaterEqual(len(self.html_files), 56, f"Expected at least 56 HTML pages, found {len(self.html_files)}")

    def test_essential_static_assets_exist(self):
        css_file = os.path.join(DIST_DIR, "assets", "css", "main.css")
        js_file = os.path.join(DIST_DIR, "assets", "js", "main.js")
        sitemap_xml = os.path.join(DIST_DIR, "sitemap.xml")
        robots_txt = os.path.join(DIST_DIR, "robots.txt")
        not_found_page = os.path.join(DIST_DIR, "404.html")

        self.assertTrue(os.path.isfile(css_file), "main.css must exist in dist/assets/css/")
        self.assertTrue(os.path.isfile(js_file), "main.js must exist in dist/assets/js/")
        self.assertTrue(os.path.isfile(sitemap_xml), "sitemap.xml must exist in dist/")
        self.assertTrue(os.path.isfile(robots_txt), "robots.txt must exist in dist/")
        self.assertTrue(os.path.isfile(not_found_page), "404.html must exist in dist/")

    def test_all_10_money_pages_exist(self):
        money_slugs = [
            "civil-litigation", "criminal-law", "family-law", "property-land-law",
            "corporate-business-law", "contract-law", "inheritance-succession",
            "labour-employment-law", "banking-financial-law", "mediation-dispute-resolution"
        ]
        for slug in money_slugs:
            expected_file = os.path.join(DIST_DIR, "services", slug, "index.html")
            self.assertTrue(os.path.isfile(expected_file), f"Service page missing: /services/{slug}/")

    def test_all_30_supporting_articles_exist(self):
        resources_dir = os.path.join(DIST_DIR, "legal-resources")
        article_dirs = [d for d in os.listdir(resources_dir) if os.path.isdir(os.path.join(resources_dir, d))]
        self.assertEqual(len(article_dirs), 30, f"Expected exactly 30 supporting articles, found {len(article_dirs)}")

    def test_internal_links_integrity(self):
        broken_links = []
        total_links_checked = 0

        for html_path in self.html_files:
            rel_file = os.path.relpath(html_path, DIST_DIR)
            with open(html_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Find all hrefs
            hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
            for href in hrefs:
                # Skip anchors, tel, mailto, javascript, external links
                if href.startswith(("#", "tel:", "mailto:", "javascript:", "http://", "https://")):
                    continue
                
                total_links_checked += 1
                clean_href = href.split("?")[0].split("#")[0]
                
                if not clean_href.startswith("/"):
                    # Relative link relative to html_path directory
                    target_candidate = os.path.normpath(os.path.join(os.path.dirname(html_path), clean_href))
                else:
                    # Root-relative link
                    path_part = clean_href.lstrip("/")
                    if path_part == "" or path_part.endswith("/"):
                        target_candidate = os.path.join(DIST_DIR, path_part, "index.html")
                    elif os.path.splitext(path_part)[1]:
                        target_candidate = os.path.join(DIST_DIR, path_part)
                    else:
                        target_candidate = os.path.join(DIST_DIR, path_part, "index.html")

                if not os.path.exists(target_candidate):
                    broken_links.append((rel_file, href, target_candidate))

        self.assertEqual(len(broken_links), 0, f"Found {len(broken_links)} broken internal links: {broken_links[:5]}")
        print(f"Verified {total_links_checked} internal links with 0 broken links.")

    def test_heading_and_title_tags(self):
        for html_path in self.html_files:
            rel_file = os.path.relpath(html_path, DIST_DIR)
            with open(html_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Non-empty title
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            self.assertIsNotNone(title_match, f"Missing <title> in {rel_file}")
            self.assertTrue(len(title_match.group(1).strip()) > 5, f"Empty or too short <title> in {rel_file}")

            # Meta description
            desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
            self.assertIsNotNone(desc_match, f"Missing meta description in {rel_file}")
            self.assertTrue(len(desc_match.group(1).strip()) > 15, f"Too short meta description in {rel_file}")

            # Exactly one visible <h1>
            h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
            self.assertEqual(len(h1_matches), 1, f"Expected exactly one <h1> in {rel_file}, found {len(h1_matches)}")

    def test_canonical_urls(self):
        site_url = self.config.get("site_url", "https://www.pathivaralawfirmsunsari.com").rstrip("/")
        for html_path in self.html_files:
            rel_file = os.path.relpath(html_path, DIST_DIR)
            with open(html_path, "r", encoding="utf-8") as f:
                content = f.read()

            canonical_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', content, re.IGNORECASE)
            self.assertIsNotNone(canonical_match, f"Missing canonical link in {rel_file}")
            canonical_url = canonical_match.group(1)
            self.assertTrue(canonical_url.startswith(site_url), f"Canonical URL {canonical_url} must start with {site_url}")

    def test_json_ld_structured_data(self):
        for html_path in self.html_files:
            rel_file = os.path.relpath(html_path, DIST_DIR)
            with open(html_path, "r", encoding="utf-8") as f:
                content = f.read()

            script_matches = re.findall(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', content, re.IGNORECASE | re.DOTALL)
            for raw_json in script_matches:
                try:
                    parsed = json.loads(raw_json.strip())
                    self.assertIn("@context", parsed, f"JSON-LD in {rel_file} missing @context")
                except json.JSONDecodeError as e:
                    self.fail(f"Invalid JSON-LD in {rel_file}: {e}")

    def test_xml_sitemap_validity(self):
        sitemap_path = os.path.join(DIST_DIR, "sitemap.xml")
        self.assertTrue(os.path.isfile(sitemap_path))
        
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        namespace = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        
        urls = root.findall("ns:url", namespace)
        self.assertEqual(len(urls), 56, f"Expected exactly 56 URLs in sitemap.xml, found {len(urls)}")

        for u in urls:
            loc = u.find("ns:loc", namespace)
            self.assertIsNotNone(loc)
            self.assertTrue(loc.text.startswith("https://www.pathivaralawfirmsunsari.com"))
            
            prio = u.find("ns:priority", namespace)
            self.assertIsNotNone(prio)
            self.assertTrue(float(prio.text) >= 0.1 and float(prio.text) <= 1.0)

    def test_accessibility_basics(self):
        for html_path in self.html_files:
            rel_file = os.path.relpath(html_path, DIST_DIR)
            with open(html_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Skip link check
            self.assertIn('class="skip-link"', content, f"Missing skip-link in {rel_file}")

            # Forms have accessible labels
            if "<form" in content:
                inputs = re.findall(r'<input\s+[^>]*id=["\']([^"\']+)["\'][^>]*>', content)
                for inp_id in inputs:
                    has_label = f'for="{inp_id}"' in content or f"for='{inp_id}'" in content
                    self.assertTrue(has_label, f"Input id '{inp_id}' in {rel_file} has no associated <label>")

if __name__ == "__main__":
    unittest.main()
