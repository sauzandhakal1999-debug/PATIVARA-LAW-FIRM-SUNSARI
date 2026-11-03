"""
PATHIVARA LAW FIRM SUNSARI - Reusable Component Templates
Generates semantic, accessible HTML5 components with JSON-LD structured data.
"""

import json

def get_base_html(title, description, canonical_url, body_content, schema_json, config, current_url="/"):
    site_url = config.get("site_url", "https://www.pathivaralawfirmsunsari.com")
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    clean_canonical = canonical_url if canonical_url.startswith("http") else f"{site_url}{canonical_url}"

    schema_tag = ""
    if schema_json:
        schema_tag = f'<script type="application/ld+json">\n{json.dumps(schema_json, indent=2)}\n</script>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{clean_canonical}">
  <meta name="robots" content="index, follow">
  
  <!-- Open Graph / Social Sharing -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{clean_canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:site_name" content="{firm_name}">
  <meta property="og:locale" content="en_US">
  
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">

  <!-- CSS Design System -->
  <link rel="stylesheet" href="/assets/css/main.css">
  
  {schema_tag}
</head>
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>
  
  {render_header(config, current_url)}
  
  <main id="main-content">
    {body_content}
  </main>
  
  {render_footer(config)}
  
  <script src="/assets/js/main.js" defer></script>
</body>
</html>"""

def render_header(config, current_url="/"):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    tagline = config.get("firm_tagline", "Specialized Legal Advocacy & Advisory")
    mobile1 = config.get("contact", {}).get("mobile_primary", "+977-9745875449")
    mobile2 = config.get("contact", {}).get("mobile_secondary", "+977-9852057087")
    primary_city = config.get("locations", {}).get("primary", {}).get("city", "Inaruwa")
    hours = config.get("contact", {}).get("office_hours", "Monday to Friday: 9:30 AM – 5:00 PM")

    def is_active(path):
        if path == "/" and current_url == "/":
            return ' aria-current="page"'
        elif path != "/" and current_url.startswith(path):
            return ' aria-current="page"'
        return ""

    return f"""<header class="site-header">
  <div class="top-bar">
    <div class="container top-bar-inner">
      <span>Official Chambers in Inaruwa &amp; Itahari, Sunsari (Koshi Province) | {hours}</span>
      <div>
        <span>Direct Registry Mobile: <a href="tel:{mobile1}">9745875449</a> / <a href="tel:{mobile2}">9852057087</a></span>
      </div>
    </div>
  </div>
  
  <div class="container nav-container">
    <a href="/" class="site-brand" aria-label="{firm_name} Home">
      <div class="site-brand-logo" aria-hidden="true">⚖</div>
      <div class="site-brand-text">
        <span class="site-brand-title"><strong>{firm_name}</strong></span>
        <span class="site-brand-tagline">{tagline}</span>
      </div>
    </a>
    
    <button class="mobile-menu-btn" aria-label="Toggle navigation menu" aria-expanded="false" aria-controls="primary-nav">
      ☰ Menu
    </button>
    
    <nav class="main-nav" id="primary-nav" aria-label="Main Navigation">
      <ul class="nav-links">
        <li><a href="/"{is_active("/")}>Home</a></li>
        <li><a href="/services/"{is_active("/services/")}>Practice Areas</a></li>
        <li><a href="/legal-resources/"{is_active("/legal-resources/")}>Legal Resources</a></li>
        <li><a href="/about/"{is_active("/about/")}>About</a></li>
        <li><a href="/team/"{is_active("/team/")}>Our Advocates</a></li>
        <li><a href="/contact/"{is_active("/contact/")}>Contact</a></li>
      </ul>
      <a href="/legal-consultation/" class="btn btn-primary" style="padding: 0.5rem 1rem; font-size: 0.9rem;">Consultation</a>
    </nav>
  </div>
</header>"""

def render_breadcrumbs(crumbs):
    items = ['<li><a href="/">Home</a></li>']
    for label, url in crumbs:
        if url:
            items.append(f'<li><a href="{url}">{label}</a></li>')
        else:
            items.append(f'<li aria-current="page">{label}</li>')
    
    return f"""<nav class="breadcrumbs-nav" aria-label="Breadcrumb">
  <div class="container">
    <ol class="breadcrumbs-list">
      {''.join(items)}
    </ol>
  </div>
</nav>"""

def render_hero(title, subtitle, badge="Legal Representation in Nepal", actions=None):
    actions_html = ""
    if actions:
        actions_html = '<div class="hero-actions">' + ''.join(actions) + '</div>'
    else:
        actions_html = """<div class="hero-actions">
          <a href="/legal-consultation/" class="btn btn-primary">Request Consultation</a>
          <a href="/contact/" class="btn btn-secondary">Direct Chambers Contact</a>
        </div>"""

    return f"""<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div>
        <div class="hero-badge">{badge}</div>
        <h1 class="hero-title">{title}</h1>
        <p class="hero-subtitle">{subtitle}</p>
        {actions_html}
      </div>
    </div>
  </div>
</section>"""

def render_timeline(steps):
    step_items = []
    for i, (title, desc) in enumerate(steps, 1):
        step_items.append(f"""<div class="timeline-step">
  <div class="timeline-number">{i}</div>
  <h3 class="timeline-title">{title}</h3>
  <p class="timeline-desc">{desc}</p>
</div>""")
    return f"""<div class="timeline">{''.join(step_items)}</div>"""

def render_checklist(title, items):
    list_items = []
    for item in items:
        list_items.append(f"""<li class="checklist-item">
  <span class="checklist-icon" aria-hidden="true">✔</span>
  <span>{item}</span>
</li>""")
    return f"""<div class="checklist">
  <h3 class="checklist-title">{title}</h3>
  <ul class="checklist-items">{''.join(list_items)}</ul>
</div>"""

def render_comparison_table(headers, rows):
    th_html = "".join([f"<th>{h}</th>" for h in headers])
    tr_html = []
    for row in rows:
        td_html = "".join([f"<td>{cell}</td>" for cell in row])
        tr_html.append(f"<tr>{td_html}</tr>")
    
    return f"""<div class="comparison-container">
  <table class="comparison-table">
    <thead>
      <tr>{th_html}</tr>
    </thead>
    <tbody>
      {''.join(tr_html)}
    </tbody>
  </table>
</div>"""

def render_faq_accordion(faqs):
    faq_items = []
    for q, a in faqs:
        faq_items.append(f"""<details class="faq-item">
  <summary class="faq-question">{q}</summary>
  <div class="faq-answer"><p>{a}</p></div>
</details>""")
    return f"""<div class="faq-list">{''.join(faq_items)}</div>"""

def render_cta_banner(service_name="Legal Advisory", prompt="Speak with an advocate about your specific circumstances."):
    return f"""<section class="cta-banner" aria-label="Consultation Request">
  <h2>Need Strategic Legal Counsel Regarding {service_name}?</h2>
  <p>{prompt} Our legal team provides objective, structured assessments in full compliance with Nepal Bar Council ethical regulations.</p>
  <div class="cta-banner-actions">
    <a href="/legal-consultation/" class="btn btn-primary">Book Confidential Consultation</a>
    <a href="/contact/" class="btn btn-secondary">Contact Chambers Office</a>
  </div>
</section>"""

def render_author_box():
    return f"""<div class="author-box" aria-label="Author Credentials">
  <div class="author-avatar">AL</div>
  <div class="author-info">
    <h4>Prepared by Legal Counsel | PATHIVARA LAW FIRM SUNSARI</h4>
    <div class="author-title">Admitted to Nepal Bar Council | Regular Appearance in District, High & Supreme Courts</div>
    <p class="author-bio">Researched in strict adherence to current Nepalese statutory law, including the Muluki Civil Code 2074 and Muluki Criminal Code 2074. Reviewed for procedural accuracy.</p>
  </div>
</div>"""

def render_disclaimer(custom_text=None):
    text = custom_text or "General Legal Information Notice: The legal analysis, procedural outlines, and statutory summaries on this website are published strictly for educational and public informational awareness in Nepal. This content does not constitute formal legal advice, nor does reviewing it establish an advocate-client relationship. Legal representation is only formed upon executing a formal Vakalatnama and retainer agreement under the Nepal Bar Council Code of Conduct 2051."
    return f"""<aside class="legal-notice" role="note">
  <strong>Nepal Legal Notice & Ethical Disclosure:</strong> {text}
</aside>"""

def render_footer(config):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    primary_loc = config.get("locations", {}).get("primary", {})
    branch_loc = config.get("locations", {}).get("branch", {})
    mobile1 = config.get("contact", {}).get("mobile_primary", "+977-9745875449")
    mobile2 = config.get("contact", {}).get("mobile_secondary", "+977-9852057087")
    branch_mobile = config.get("contact", {}).get("branch_mobile", "+977-9852059106")
    branch_mobile_display = config.get("contact", {}).get("branch_mobile_display", "9852059106")
    email = config.get("contact", {}).get("email", "sauzandhakal1999@gmail.com")
    address = primary_loc.get("formatted_address", "Adalat Road, Inaruwa, Sunsari, Nepal")
    branch_address = branch_loc.get("formatted_address", "Itahari-4 (Bagaicha Tole), Sunsari, Nepal")
    hours = config.get("contact", {}).get("office_hours", "Monday to Friday: 9:30 AM – 5:00 PM (Closed on Saturdays, Sundays & Public Holidays)")
    bar_info = config.get("regulatory", {}).get("bar_registration_number", "Nepal Bar Council Registered")

    return f"""<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-col">
      <h3><strong>{firm_name}</strong></h3>
      <p style="color: #94a3b8; font-size: 0.95rem; line-height: 1.6; margin-bottom: 1rem;">
        Dedicated legal advocacy, commercial counsel, and dispute resolution across Nepal. Operating in strict accordance with the Nepal Bar Council Code of Conduct (2051).
      </p>
      <div class="footer-contact">
        <p><strong>Primary Office:</strong> {address}</p>
        <p><strong>Branch Office:</strong> {branch_address}</p>
        <p><strong>Primary Mobile:</strong> <a href="tel:{mobile1}">9745875449</a> / <a href="tel:{mobile2}">9852057087</a></p>
        <p><strong>Branch Mobile:</strong> <a href="tel:{branch_mobile}">{branch_mobile_display}</a></p>
        <p><strong>Registry Email:</strong> <a href="mailto:{email}">{email}</a></p>
        <p><strong>Office Hours:</strong> {hours}</p>
        <p><strong>Regulatory:</strong> {bar_info}</p>
      </div>
    </div>
    
    <div class="footer-col">
      <h3>Core Practice Areas</h3>
      <ul class="footer-links">
        <li><a href="/services/civil-litigation/">Civil Litigation</a></li>
        <li><a href="/services/criminal-law/">Criminal Defence</a></li>
        <li><a href="/services/family-law/">Family & Divorce</a></li>
        <li><a href="/services/property-land-law/">Property & Land Law</a></li>
        <li><a href="/services/corporate-business-law/">Corporate & Commercial</a></li>
        <li><a href="/services/contract-law/">Contract Drafting</a></li>
        <li><a href="/services/inheritance-succession/">Inheritance & Succession</a></li>
        <li><a href="/services/mediation-dispute-resolution/">Mediation & ADR</a></li>
        <li><a href="/services/">View All Practice Areas →</a></li>
      </ul>
    </div>
    
    <div class="footer-col">
      <h3>Legal Resources</h3>
      <ul class="footer-links">
        <li><a href="/legal-resources/">Resource Hub</a></li>
        <li><a href="/legal-resources/what-is-a-civil-case-nepal/">Civil Law Guides</a></li>
        <li><a href="/legal-resources/bail-eligibility-procedure-nepal-courts/">Criminal Law Guides</a></li>
        <li><a href="/legal-resources/divorce-procedure-muluki-civil-code-nepal/">Family Law Guides</a></li>
        <li><a href="/legal-resources/how-to-check-land-ownership-lalpurja-nepal/">Land & Property Guides</a></li>
        <li><a href="/legal-resources/steps-registering-company-ocr-nepal/">Corporate Legal Guides</a></li>
        <li><a href="/faqs/">Frequently Asked Questions</a></li>
        <li><a href="/sitemap/">HTML Sitemap</a></li>
      </ul>
    </div>
    
    <div class="footer-col">
      <h3>Trust & Governance</h3>
      <ul class="footer-links">
        <li><a href="/about/">About Our Firm</a></li>
        <li><a href="/team/">Advocates & Counsel</a></li>
        <li><a href="/team/senior-advocate-profile/">Managing Counsel Profile</a></li>
        <li><a href="/legal-consultation/">Book Legal Consultation</a></li>
        <li><a href="/contact/">Contact Our Chambers</a></li>
        <li><a href="/testimonials/">Client Feedback & Ethics</a></li>
        <li><a href="/legal-disclaimer/">Legal Practice Disclaimer</a></li>
        <li><a href="/privacy-policy/">Privacy & Confidentiality</a></li>
        <li><a href="/terms-of-use/">Terms of Website Use</a></li>
        <li><a href="/cookie-policy/">Cookie Policy</a></li>
        <li><a href="/accessibility/">Accessibility Statement</a></li>
      </ul>
    </div>
  </div>
  
  <div class="footer-bottom">
    <div class="container footer-bottom-inner">
      <span>© 2026 {firm_name}. All rights reserved under the laws of Nepal.</span>
      <div style="display: flex; gap: 1rem;">
        <a href="/privacy-policy/">Privacy</a>
        <a href="/terms-of-use/">Terms</a>
        <a href="/legal-disclaimer/">Disclaimer</a>
        <a href="/sitemap/">Sitemap</a>
      </div>
    </div>
  </div>
</footer>"""
