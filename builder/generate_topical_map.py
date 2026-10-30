import json
import os
import sys

sys.path.insert(0, ".")
from src.data.services import SERVICES
from src.data.articles import get_articles
from src.data.team import TEAM_MEMBERS
from src.data.faqs import GLOBAL_FAQS

data_dir = "/home/sauzandhakal1999/.gemini/antigravity/scratch/nepal-law-firm/data"
docs_dir = "/home/sauzandhakal1999/.gemini/antigravity/scratch/nepal-law-firm/docs"
os.makedirs(data_dir, exist_ok=True)
os.makedirs(docs_dir, exist_ok=True)

with open("/home/sauzandhakal1999/.gemini/antigravity/scratch/nepal-law-firm/config/business.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)
firm_name = cfg.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")

trust_pages = [
    ("/", "Specialized Legal Advocacy & Trusted Advisory in Nepal", "Law Firm in Nepal", "Trust/Support", "None (Root)", "Central Law Firm Entity, Brand Identity, Full Practice Scope", "Consultation Request / Office Call", "P0"),
    ("/about/", "Dedicated to Principled Advocacy & Strategic Legal Counsel in Nepal", "About Our Law Firm", "Trust/Support", "/", "Firm Philosophy, Court Admittance, History, Bar Standards", "Schedule Consultation", "P1"),
    ("/team/", "Experienced Advocates & Legal Counsel Admitted in Nepal", "Our Legal Team & Advocates", "Trust/Support", "/about/", "Advocates, Senior Advocates, Bar Numbers, Court Admissions", "Consultation Enquiry", "P1"),
    ("/team/senior-advocate-profile/", "Senior Legal Counsel & Managing Advocate", "Senior Advocate Profile", "Trust/Support", "/team/", "Individual Advocate, Bar Registration Number, Practice Experience, Notable Areas", "Direct Case Consultation Request", "P1"),
    ("/services/", "Comprehensive Legal Practice Areas in Nepal", "Legal Services in Nepal", "Core", "/", "Full Index of Legal Services, Categorized Practice Areas", "Select Service & Consult", "P0"),
    ("/legal-consultation/", "Schedule a Structured Legal Consultation", "Legal Consultation in Nepal", "Trust/Support", "/", "Consultation Protocol, What to Expect, Preparing Documents", "Submit Consultation Request", "P0"),
    ("/contact/", "Contact Our Law Chambers in Nepal", "Contact Our Law Chambers", "Trust/Support", "/", "Contact Channels, Physical Office, Verified Phone, Email, Office Hours", "Direct Call / Contact Form", "P0"),
    ("/faqs/", "Frequently Asked Legal Questions", "Law Firm Frequently Asked Questions Nepal", "Trust/Support", "/", "Frequently Asked Questions, Advocate Fees, Court Jurisdiction, Representation", "Transition to Consultation", "P1"),
    ("/legal-resources/", "Legal Resources, Guides & Statutory Insights in Nepal", "Legal Resources and Educational Hub Nepal", "Trust/Support", "/", "Resource Hub, Legal Guides, Statutory References, Clusters", "Educate & Drive to Service Page", "P0"),
    ("/testimonials/", "Client Experiences & Professional Standards", "Client Experiences & Ethics Notice", "Trust/Support", "/about/", "Client Experiences, Bar Council Ethics Notice on Advertising", "Schedule Consultation", "P2"),
    ("/privacy-policy/", "Privacy Policy & Client Data Confidentiality", "Privacy Policy", "Trust/Support", "/", "Data Privacy, Confidentiality of Legal Inquiries, Privacy Act 2075", "Assure Confidentiality", "P2"),
    ("/terms-of-use/", "Terms of Website Use", "Terms of Use", "Trust/Support", "/", "Terms of Website Use, Intellectual Property, Limitation of Online Content", "Regulatory Compliance", "P2"),
    ("/legal-disclaimer/", "Legal Practice Disclaimer & Bar Council Notice", "Legal Practice Disclaimer", "Trust/Support", "/", "Legal Disclaimer, Nepal Bar Council Code of Conduct 2051", "Clarify Representation Boundaries", "P1"),
    ("/cookie-policy/", "Cookie and Tracking Policy", "Cookie Policy", "Trust/Support", "/", "Cookie Policy, Local Storage, Session State, User Preferences", "Transparency", "P2"),
    ("/accessibility/", "Website Accessibility Statement", "Accessibility Statement", "Trust/Support", "/", "Web Accessibility, WCAG 2.1 AA Compliance, Screen Reader Support, Keyboard Nav", "Demonstrate Inclusivity", "P2"),
    ("/sitemap/", "Complete Website Sitemap & Page Directory", "HTML Sitemap & Architecture", "Trust/Support", "/", "HTML Sitemap, Complete Hierarchical Index of All Core, Outer, Trust", "Assure Full Crawlability", "P1")
]

topical_map = []
bt = chr(96)
nl = chr(10)

# 1. Trust & Support Pages
for url, h1, kw, sec, parent, semantics, goal, prio in trust_pages:
    topical_map.append({
        "section": sec,
        "semantics": semantics,
        "semantic_relationship": "Establishes " + kw.lower() + " authority and operational governance",
        "query_template": kw.lower() + " " + firm_name.lower(),
        "primary_keyword": kw,
        "secondary_keywords": kw + " Sunsari, Koshi Province, Nepal legal counsel, Nepal Bar Council standards",
        "search_intent": "Navigational / Commercial / Trust" if ("Services" in h1 or "Consultation" in h1 or "Contact" in h1) else "Informational / Compliance",
        "user_journey_stage": "Decision" if prio == "P0" else "Evaluation / Compliance",
        "canonical_page_topic": h1,
        "parent_page": parent,
        "proposed_url": url,
        "page_title": h1 + " | " + firm_name,
        "meta_description": h1 + ". Dedicated legal guidance and professional counsel under Nepalese law.",
        "h1": h1,
        "important_attributes": "Central Entity, Nepal Jurisdiction, Nepal Bar Council Standards",
        "internal_links_in": "Sitewide header/footer",
        "internal_links_out": "/services/, /legal-consultation/, /contact/",
        "primary_conversion_goal": goal,
        "priority": prio,
        "cannibalization_group": kw.replace(" ", "")
    })

# 2. Core Service Money Pages
for s in SERVICES:
    prio = "P0" if s.slug in ["civil-litigation", "criminal-law", "family-law", "property-land-law", "corporate-business-law"] else "P1"
    topical_map.append({
        "section": "Core",
        "semantics": f"Substantive laws, procedural stages, evidence checklists, and court representation for {s.title}",
        "semantic_relationship": f"High-intent commercial service offering for {s.title} in Nepal",
        "query_template": f"{s.title.lower()} lawyer nepal / hire legal counsel {s.title.lower()} kathmandu",
        "primary_keyword": f"{s.title} Lawyer Nepal",
        "secondary_keywords": f"{s.title} Kathmandu, court representation Nepal, legal counsel {s.title} Nepal",
        "search_intent": "Commercial / Transactional",
        "user_journey_stage": "Decision",
        "canonical_page_topic": s.h1,
        "parent_page": "/services/",
        "proposed_url": f"/services/{s.slug}/",
        "page_title": f"{s.h1} | {firm_name}",
        "meta_description": s.meta_description,
        "h1": s.h1,
        "important_attributes": "Statutory Grounds, Procedural Milestones, Evidence Checklist, Fee Considerations, Ethical Disclaimers",
        "internal_links_in": "/services/, homepage, footer, related cluster articles",
        "internal_links_out": f"/legal-consultation/, /contact/, /services/, " + ", ".join([ra['url'] for ra in s.related_articles[:3]]),
        "primary_conversion_goal": s.conversion_prompt,
        "priority": prio,
        "cannibalization_group": "Service-" + s.slug
    })

# 3. Outer Supporting Cluster Articles
for a in get_articles():
    topical_map.append({
        "section": "Outer",
        "semantics": f"Educational concepts for {a.title}, statutory basis under Nepalese law, procedural rights and liabilities",
        "semantic_relationship": f"Educational supporting article directing users to {a.parent_service_url}",
        "query_template": f"{a.title.lower()} / nepalese law / legal guide",
        "primary_keyword": a.title,
        "secondary_keywords": f"{a.cluster} Nepal, legal guide Sunsari, Nepalese statutory procedure",
        "search_intent": "Informational",
        "user_journey_stage": "Awareness / Consideration",
        "canonical_page_topic": a.h1,
        "parent_page": "/legal-resources/",
        "proposed_url": f"/legal-resources/{a.slug}/",
        "page_title": f"{a.h1} | {firm_name}",
        "meta_description": a.meta_description,
        "h1": a.h1,
        "important_attributes": "Statutory Citations, Step-by-Step Practical Guidance, Exception Caveats, Contextual Links to Parent Service",
        "internal_links_in": f"/legal-resources/, {a.parent_service_url}, related cluster articles",
        "internal_links_out": f"{a.parent_service_url}, /legal-consultation/, " + ", ".join([ra['url'] for ra in a.related_articles[:2]]),
        "primary_conversion_goal": f"Consult on {a.parent_service_name}",
        "priority": "P1",
        "cannibalization_group": "Article-" + a.slug
    })

with open(os.path.join(data_dir, "topical-map.json"), "w") as f:
    json.dump(topical_map, f, indent=2)

md_lines = [
    "# Semantic Topical Map & Information Architecture: Nepal Law Firm",
    "",
    "## 1. Central Entity Definition & Jurisdiction",
    f"- **Central Entity**: Law Firm ({firm_name})",
    "- **Jurisdiction**: Nepal (District Courts of Sunsari & Morang, High Court Biratnagar, Supreme Court of Nepal)",
    "- **Primary Market / Location**: Sunsari District (Inaruwa / Itahari / Dharan), Koshi Province, Nepal",
    "- **Regulatory Authority**: Nepal Bar Council (Admitted Advocates, Act 2050 & Code of Conduct 2051)",
    "- **Total Canonical URLs Planned & Indexed**: **" + str(len(topical_map)) + "**",
    "",
    "## 2. Topical Architecture Summary",
    "- **Core Section (Money Pages)**: 10 High-Intent Commercial Service Pages",
    "- **Outer Section (Supporting Topical Clusters)**: 30 In-Depth Educational Articles across 5 Practice Clusters",
    "- **Trust, Support & Compliance Section**: 16 Governance, Team, Consultation, Legal Notices & Sitemap Pages",
    "",
    "## 3. Topical Map Matrix (20 Required Fields)",
    "",
    "| Section | Proposed URL | H1 / Canonical Topic | Primary Keyword | Search Intent | Parent Page | Primary Conversion Goal | Priority |",
    "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |"
]

for item in topical_map:
    row = "| " + item["section"] + " | " + bt + item["proposed_url"] + bt + " | " + item["h1"] + " | " + item["primary_keyword"] + " | " + item["search_intent"] + " | " + bt + item["parent_page"] + bt + " | " + item["primary_conversion_goal"] + " | " + item["priority"] + " |"
    md_lines.append(row)

md_lines.append("")
md_lines.append("---")
md_lines.append("")
md_lines.append("## 4. Entity, Query & Semantic Attributes Per Page")
md_lines.append("")

for i, item in enumerate(topical_map, 1):
    md_lines.append("### " + str(i) + ". " + item["h1"])
    md_lines.append("- **URL**: " + bt + item["proposed_url"] + bt)
    md_lines.append("- **Section**: " + item["section"])
    md_lines.append("- **Page Title**: " + item["page_title"])
    md_lines.append("- **Meta Description**: " + item["meta_description"])
    md_lines.append("- **Semantics Covered**: " + item["semantics"])
    md_lines.append("- **Semantic Relationship to Entity**: " + item["semantic_relationship"])
    md_lines.append("- **Query Template**: " + bt + item["query_template"] + bt)
    md_lines.append("- **Primary Keyword**: " + item["primary_keyword"])
    md_lines.append("- **Secondary Keywords**: " + item["secondary_keywords"])
    md_lines.append("- **Search Intent**: " + item["search_intent"])
    md_lines.append("- **User Journey Stage**: " + item["user_journey_stage"])
    md_lines.append("- **Important Attributes**: " + item["important_attributes"])
    md_lines.append("- **Internal Links In**: " + item["internal_links_in"])
    md_lines.append("- **Internal Links Out**: " + item["internal_links_out"])
    md_lines.append("- **Primary Conversion Goal**: " + item["primary_conversion_goal"])
    md_lines.append("- **Priority**: " + item["priority"])
    md_lines.append("- **Cannibalization Group**: " + item["cannibalization_group"])
    md_lines.append("")

with open(os.path.join(docs_dir, "topical-map.md"), "w") as f:
    f.write(nl.join(md_lines))

print(f"SUCCESS: Synchronized {len(topical_map)} pages in data/topical-map.json and docs/topical-map.md")
