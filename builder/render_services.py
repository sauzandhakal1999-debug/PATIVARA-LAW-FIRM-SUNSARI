# Service page renderers for PATHIVARA LAW FIRM SUNSARI
from src.data.services import ServicePage
from builder.templates import (
    get_base_html, render_breadcrumbs, render_timeline, render_checklist,
    render_faq_accordion, render_cta_banner, render_disclaimer
)

def render_service_page(service: ServicePage, config: dict):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    phone = config.get("contact", {}).get("telephone_display", "+977 (01) 4XXXXXX")
    tel_link = config.get("contact", {}).get("telephone", "+97714000000")
    site_url = config.get("site_url", "https://www.pathivaralawfirmsunsari.com")

    crumbs = [("Practice Areas", "/services/"), (service.title, "")]
    canonical = f"/services/{service.slug}/"

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "@id": f"{site_url}{canonical}#service",
                "name": service.title,
                "description": service.meta_description,
                "provider": {
                    "@type": "LegalService",
                    "name": firm_name,
                    "url": site_url
                },
                "areaServed": "Nepal",
                "serviceType": "Legal Service"
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{site_url}{canonical}#breadcrumbs",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": site_url},
                    {"@type": "ListItem", "position": 2, "name": "Practice Areas", "item": f"{site_url}/services/"},
                    {"@type": "ListItem", "position": 3, "name": service.title, "item": f"{site_url}{canonical}"}
                ]
            }
        ]
    }

    steps = [(s.title, f"{s.description} <br><small><strong>Estimated Timeline:</strong> {s.duration_estimate}</small>") for s in service.stages]

    statute_rows = []
    for g in service.governing_laws:
        statute_rows.append(f"""
        <tr>
          <td><strong>{g.get('act', '')}</strong></td>
          <td><code>{g.get('sections', '')}</code></td>
          <td>{g.get('summary', '')}</td>
        </tr>""")

    situations_html = "".join([f"<li class='checklist-item'><span class='checklist-icon'>⚖</span><span>{sit}</span></li>" for sit in service.relevant_situations])
    scope_html = "".join([f"<li class='checklist-item'><span class='checklist-icon'>✔</span><span>{sc}</span></li>" for sc in service.scope_of_assistance])
    rights_html = "".join([f"<li style='margin-bottom: 0.65rem;'><strong>•</strong> {rd}</li>" for rd in service.rights_duties_limitations])
    fees_html = "".join([f"<li style='margin-bottom: 0.65rem;'><strong>•</strong> {ff}</li>" for ff in service.fee_factors])
    service_faqs = [(f.question, f.answer) for f in service.faqs]

    rel_art_cards = []
    for ra in service.related_articles:
        rel_art_cards.append(f"""
        <div style="background: #f8fafc; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 1.25rem;">
          <h4 style="font-size: 1.05rem; margin-bottom: 0.5rem;"><a href="{ra['url']}">{ra['title']}</a></h4>
          <span style="font-size: 0.85rem; color: var(--color-accent-hover); font-weight: 600;">Read Statutory Guide →</span>
        </div>""")

    adj_service_cards = []
    for adj in service.adjacent_services:
        adj_service_cards.append(f"""
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 1.25rem;">
          <h4 style="font-size: 1.05rem; margin-bottom: 0.5rem;"><a href="{adj['url']}">{adj['title']}</a></h4>
          <span style="font-size: 0.85rem; color: var(--color-secondary);">Related Practice Area →</span>
        </div>""")

    trust_html = "".join([f"<div style='background: #f1f5f9; padding: 0.85rem 1rem; border-radius: var(--radius-sm); font-size: 0.9rem;'><strong>🛡 Factual Standard:</strong> {ts}</div>" for ts in service.trust_signals])

    svg_embed = ""
    if service.slug == "civil-litigation":
        svg_embed = '<div style="margin: 2rem 0; background: white; padding: 1.5rem; border: 1px solid var(--color-border); border-radius: var(--radius-md);"><img src="/assets/img/civil-litigation-process.svg" alt="Civil Litigation Procedural Stages in Nepal" width="900" height="240" loading="lazy"></div>'
    elif service.slug == "criminal-law":
        svg_embed = '<div style="margin: 2rem 0; background: white; padding: 1.5rem; border: 1px solid var(--color-border); border-radius: var(--radius-md);"><img src="/assets/img/criminal-procedure-flow.svg" alt="Criminal Law Procedure Workflow in Nepal" width="900" height="240" loading="lazy"></div>'
    elif service.slug == "property-land-law":
        svg_embed = '<div style="margin: 2rem 0; background: white; padding: 1.5rem; border: 1px solid var(--color-border); border-radius: var(--radius-md);"><img src="/assets/img/land-due-diligence.svg" alt="Land Due Diligence Workflow in Nepal" width="900" height="240" loading="lazy"></div>'
    elif service.slug == "corporate-business-law":
        svg_embed = '<div style="margin: 2rem 0; background: white; padding: 1.5rem; border: 1px solid var(--color-border); border-radius: var(--radius-md);"><img src="/assets/img/company-registration-steps.svg" alt="Company Registration Workflow at OCR Nepal" width="900" height="240" loading="lazy"></div>'

    body = f"""
    {render_breadcrumbs(crumbs)}

    <section class="hero">
      <div class="container">
        <div class="hero-inner">
          <div>
            <div class="hero-badge">{service.hero_badge}</div>
            <h1 class="hero-title">{service.h1}</h1>
            <p class="hero-subtitle">{service.short_intro}</p>
            <div class="hero-actions">
              <a href="/legal-consultation/" class="btn btn-primary">Request a Consultation</a>
              <a href="tel:{tel_link}" class="btn btn-secondary">Call Chambers: {phone}</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <div class="container" style="padding: var(--space-3xl) 0;">
      <div class="grid" style="grid-template-columns: 2.2fr 1fr; gap: var(--space-2xl); align-items: flex-start;">
        <div>
          <section style="margin-bottom: var(--space-2xl);">
            <h2 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 1.85rem; margin-bottom: 1rem;">
              Understanding the Legal Problem &amp; Client Need
            </h2>
            <p style="font-size: 1.05rem; line-height: 1.7; color: var(--color-text);">
              {service.legal_problem_overview}
            </p>
          </section>

          <section style="margin-bottom: var(--space-2xl);">
            <h2 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 1.6rem; margin-bottom: 1rem;">
              Situations Where this Service is Relevant
            </h2>
            <ul class="checklist-items">{situations_html}</ul>
          </section>

          <section style="margin-bottom: var(--space-2xl);">
            <h2 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 1.6rem; margin-bottom: 1rem;">
              Scope of Legal Assistance Offered by our Chambers
            </h2>
            <ul class="checklist-items">{scope_html}</ul>
          </section>

          <section style="margin-bottom: var(--space-2xl);">
            <h2 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 1.6rem; margin-bottom: 1rem;">
              Typical Legal Process &amp; Procedural Stages in Nepal
            </h2>
            <p style="color: var(--color-text-muted); margin-bottom: 1.5rem;">
              Our advocates guide clients step-by-step through each statutory stage mandated by Nepalese court rules:
            </p>
            {svg_embed}
            {render_timeline(steps)}
          </section>

          <section style="margin-bottom: var(--space-2xl);">
            {render_checklist("Documents &amp; Information Clients May Need to Provide", service.required_documents)}
          </section>

          <section style="margin-bottom: var(--space-2xl);">
            <h2 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 1.6rem; margin-bottom: 1rem;">
              Applicable Nepal Legislation &amp; Statutory Authority
            </h2>
            <div class="comparison-container">
              <table class="statute-table">
                <thead>
                  <tr>
                    <th>Statute / Act</th>
                    <th>Key Provisions / Sections</th>
                    <th>Legal Relevance</th>
                  </tr>
                </thead>
                <tbody>{''.join(statute_rows)}</tbody>
              </table>
            </div>
          </section>

          <section style="margin-bottom: var(--space-2xl);">
            <h2 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 1.6rem; margin-bottom: 1rem;">
              Important Legal Rights, Duties &amp; Procedural Limitations
            </h2>
            <ul style="list-style: none; padding: 0; line-height: 1.6; color: var(--color-text);">
              {rights_html}
            </ul>
          </section>

          <section style="margin-bottom: var(--space-2xl); background: #f8fafc; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 1.5rem;">
            <h3 style="font-size: 1.3rem; color: var(--color-primary); margin-bottom: 0.75rem;">Factors Affecting Legal Fees &amp; Costs</h3>
            <p style="font-size: 0.95rem; color: var(--color-text-muted); line-height: 1.6; margin-bottom: 1rem;">
              In accordance with ethical practice in Nepal, our chambers do not publish arbitrary flat fees because every dispute is shaped by distinct evidentiary factors:
            </p>
            <ul style="list-style: none; padding: 0; font-size: 0.95rem; line-height: 1.6; color: var(--color-text);">{fees_html}</ul>
          </section>

          <section style="margin-bottom: var(--space-2xl);">
            {render_checklist("What Information to Prepare Before Your Consultation", service.consultation_preparation)}
          </section>

          <section style="margin-bottom: var(--space-2xl);">
            <h2 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 1.6rem; margin-bottom: 1rem;">
              Common Questions Regarding {service.title}
            </h2>
            {render_faq_accordion(service_faqs)}
          </section>

          <section style="margin-bottom: var(--space-2xl);">
            <h2 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 1.6rem; margin-bottom: 1rem;">
              Related Educational Articles &amp; Legal Guides
            </h2>
            <div class="grid grid-2">{''.join(rel_art_cards)}</div>
          </section>

          <section style="margin-bottom: var(--space-2xl);">
            <h3 style="font-size: 1.3rem; color: var(--color-primary); margin-bottom: 1rem;">Adjacent Legal Practice Areas</h3>
            <div class="grid grid-2">{''.join(adj_service_cards)}</div>
          </section>
        </div>

        <div>
          <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 1.5rem; margin-bottom: 1.5rem; box-shadow: var(--shadow-sm); position: sticky; top: 1rem;">
            <div style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; color: var(--color-accent-hover); margin-bottom: 0.5rem;">
              Practice Area Lead
            </div>
            <h3 style="font-size: 1.2rem; color: var(--color-primary); margin-bottom: 0.25rem;">[VERIFIED: Senior Legal Counsel]</h3>
            <p style="font-size: 0.85rem; color: var(--color-text-muted); margin-bottom: 1rem;">
              Admitted Advocate, Nepal Bar Council<br>
              Regular Appearance in Supreme Court &amp; High Courts
            </p>
            <div style="border-top: 1px solid var(--color-border); padding-top: 1rem; margin-bottom: 1.25rem;">
              <span style="font-size: 0.85rem; display: block; margin-bottom: 0.35rem;"><strong>Chambers Line:</strong> <a href="tel:{tel_link}">{phone}</a></span>
              <span style="font-size: 0.85rem; display: block;"><strong>Direct Email:</strong> consult@pathivaralawfirmsunsari.com</span>
            </div>
            <a href="/legal-consultation/" class="btn btn-primary" style="width: 100%; text-align: center; font-size: 0.9rem;">Schedule Consultation</a>
          </div>

          <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 1.5rem; margin-bottom: 1.5rem;">
            <h4 style="font-size: 1.05rem; color: var(--color-primary); margin-bottom: 0.75rem;">Chambers Trust Signals</h4>
            <div style="display: flex; flex-direction: column; gap: 0.65rem;">{trust_html}</div>
          </div>
        </div>
      </div>
    </div>

    <div class="container">
      {render_cta_banner(service.title, service.conversion_prompt)}
    </div>

    <div class="container" style="padding: 1.5rem 0;">
      {render_disclaimer()}
    </div>
    """

    return get_base_html(service.meta_title, service.meta_description, canonical, body, schema, config, current_url=canonical)

def render_services_index(services, config):
    title = "Comprehensive Legal Practice Areas in Nepal | PATHIVARA LAW FIRM SUNSARI"
    description = "Complete directory of professional legal services in Nepal. Civil litigation, criminal defence, family law, property disputes, and corporate advisory."
    canonical = "/services/"
    site_url = config.get("site_url", "https://www.pathivaralawfirmsunsari.com")

    crumbs = [("Practice Areas", "")]

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": f"{site_url}{canonical}",
                "url": f"{site_url}{canonical}",
                "name": title,
                "description": description
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{site_url}{canonical}#breadcrumbs",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": site_url},
                    {"@type": "ListItem", "position": 2, "name": "Practice Areas", "item": f"{site_url}{canonical}"}
                ]
            }
        ]
    }

    cards_html = []
    for s in services:
        cards_html.append(f"""
        <article class="card">
          <div class="card-badge">Core Practice Area</div>
          <h2 class="card-title" style="font-size: 1.35rem;"><a href="/services/{s.slug}/">{s.title}</a></h2>
          <p class="card-body">{s.short_intro}</p>
          <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px solid var(--color-border); font-size: 0.875rem; color: var(--color-text-muted);">
            <strong>Key Focus:</strong> {s.relevant_situations[0]}
          </div>
          <div style="margin-top: 1rem;">
            <a href="/services/{s.slug}/" class="card-link">Review Full Practice Scope &amp; Legal Process →</a>
          </div>
        </article>""")

    body = f"""
    {render_breadcrumbs(crumbs)}

    <section class="hero">
      <div class="container">
        <div class="hero-inner">
          <div>
            <div class="hero-badge">Comprehensive Legal Capabilities</div>
            <h1 class="hero-title">Legal Practice Areas in Nepal</h1>
            <p class="hero-subtitle">
              Structured legal advisory, contract drafting, and courtroom advocacy across all major civil, criminal, commercial, and property disciplines under Nepalese law.
            </p>
          </div>
        </div>
      </div>
    </section>

    <section style="padding: var(--space-3xl) 0;">
      <div class="container">
        <div class="grid grid-2">{''.join(cards_html)}</div>
      </div>
    </section>

    <div class="container">
      {render_cta_banner("Your Specific Legal Requirements", "Consult with an advocate to determine the exact procedural strategy for your matter.")}
    </div>

    <div class="container" style="padding: 1.5rem 0;">
      {render_disclaimer()}
    </div>
    """

    return get_base_html(title, description, canonical, body, schema, config, current_url=canonical)
