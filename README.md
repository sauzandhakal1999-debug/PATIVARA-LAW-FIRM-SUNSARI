# PATHIVARA LAW FIRM SUNSARI

A complete, production-grade, semantic SEO website and legal content architecture for **PATHIVARA LAW FIRM SUNSARI**, serving Sunsari District (Inaruwa/Itahari), Morang District, High Court Biratnagar, and the Supreme Court of Nepal.

---

## 🏛️ Project Overview

- **Firm Identity**: **PATHIVARA LAW FIRM SUNSARI**
- **Aesthetic**: Dignified, minimalist classical legal design with deep barrister navy (`#0f1c2e`), warm gold/brass accents (`#b58d2b`), parchment tones, and classical serif typography (`Merriweather`, `Playfair Display`).
- **Indexable Pages**: 56 canonical HTML routes + custom 404 error page.
- **Topical Authority**: Comprehensive legal coverage across Civil Law, Criminal Defense, Family & Divorce, Corporate & Commercial Law, Property & Land Conveyancing, Banking & Labor litigation.
- **Regulatory Ethics**: Built in strict adherence to the **Nepal Bar Council Act 2050** and **Code of Conduct 2051** (no false case guarantees, fee transparency under Court Fee Act 2017).

---

## 🚀 Quick Start

### 1. Requirements
- Python 3.10+
- Standard library modules (no third-party heavy dependencies required)

### 2. Build the Static Site
```bash
python3 builder/build_site.py
```
This generates all 56 canonical HTML pages, `sitemap.xml`, and `robots.txt` into the `dist/` directory.

### 3. Run Automated QA Tests
```bash
python3 -m unittest tests/test_site.py
```
Validates:
- All 56 canonical files exist and are populated.
- 2,800+ internal links crawled with 0 broken links.
- Schema.org structured data (LegalService, Attorney, FAQPage, Article, BreadcrumbList).
- Semantic headings (H1 uniqueness, H2/H3 nesting).

### 4. Serve Locally
```bash
python3 -m http.server 8080 --directory dist
```
Navigate to `http://localhost:8080/` in your browser.

---

## 📁 Repository Structure

```text
├── assets/                  # CSS styles, images (scales of justice hero background), JS
├── builder/                 # Static site generation engine
│   ├── build_site.py        # Master build script
│   ├── render_home.py       # Homepage renderer
│   ├── render_services.py   # Practice area pages renderer
│   ├── render_articles.py   # Legal guides & knowledge base renderer
│   ├── render_locations.py  # Court & office location renderer
│   └── templates.py         # Classical minimal layout templates
├── config/                  # Business & firm metadata configuration
│   └── business.json        # Centralized NAP (Name, Address, Phone) & Court details
├── dist/                    # Compiled, production-ready website
├── src/                     # Core data models and schemas
│   ├── config/              # Site configuration
│   ├── data/                # Practice areas, articles, lawyers, and courts data
│   └── seo/                 # Schema generators and meta tags
└── tests/                   # Automated validation suite
    └── test_site.py         # Link crawling, schema, and layout tests
```

---

## ⚖️ Legal & Regulatory Compliance
This repository and its templates are designed in full compliance with the guidelines of the Nepal Bar Council:
- Information is strictly informational and educational.
- No client-lawyer relationship is established solely by website viewing.
- Court litigation outcomes are never guaranteed.
