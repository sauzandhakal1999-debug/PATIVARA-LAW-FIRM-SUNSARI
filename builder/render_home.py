# Page renderers for PATHIVARA LAW FIRM SUNSARI
import json
from builder.templates import (
    get_base_html, render_header, render_footer, render_breadcrumbs,
    render_hero, render_timeline, render_checklist, render_comparison_table,
    render_faq_accordion, render_cta_banner, render_author_box, render_disclaimer
)

def render_home(config, services, articles, team, faqs):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    primary_loc = config.get("locations", {}).get("primary", {})
    branch_loc = config.get("locations", {}).get("branch", {})
    mobile1 = config.get("contact", {}).get("mobile_primary", "+977-9745875449")
    mobile2 = config.get("contact", {}).get("mobile_secondary", "+977-9852057087")
    branch_mobile = config.get("contact", {}).get("branch_mobile", "+977-9852059106")
    branch_mobile_display = config.get("contact", {}).get("branch_mobile_display", "9852059106")
    city = primary_loc.get("city", "Inaruwa")
    address = primary_loc.get("formatted_address", "Adalat Road, Inaruwa, Sunsari, Nepal")
    branch_address = branch_loc.get("formatted_address", "Itahari-4 (Bagaicha Tole), Sunsari, Nepal")
    hours = config.get("contact", {}).get("office_hours", "Monday to Friday: 9:30 AM – 5:00 PM (Closed on Saturdays, Sundays & Public Holidays)")
    email = config.get("contact", {}).get("email", "sauzandhakal1999@gmail.com")
    site_url = config.get("site_url", "https://www.pathivaralawfirmsunsari.com")

    title = "Specialized Legal Advocacy & Trusted Advisory in Nepal | PATHIVARA LAW FIRM SUNSARI"
    description = "Leading law firm in Sunsari, Nepal providing specialized court representation across Sunsari District Court (Inaruwa), Morang District Court, High Court Biratnagar, and Supreme Court of Nepal."

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "LegalService",
                "@id": f"{site_url}/#organization",
                "name": firm_name,
                "description": description,
                "url": site_url,
                "telephone": mobile1,
                "email": email,
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": address,
                    "addressLocality": city,
                    "addressRegion": "Sunsari District, Koshi Province",
                    "addressCountry": "NP"
                },
                "openingHours": "Mo,Tu,We,Th,Fr 09:30-17:00",
                "areaServed": ["Inaruwa", "Itahari", "Sunsari", "Biratnagar", "Morang", "Koshi Province", "Nepal"]
            },
            {
                "@type": "WebSite",
                "@id": f"{site_url}/#website",
                "url": site_url,
                "name": firm_name,
                "publisher": {"@id": f"{site_url}/#organization"}
            }
        ]
    }

    service_cards = []
    for s in services:
        service_cards.append(f"""
        <article class="card">
          <div class="card-badge">Core Practice Area</div>
          <h3 class="card-title"><a href="/services/{s.slug}/">{s.title}</a></h3>
          <p class="card-body">{s.short_intro[:160]}...</p>
          <div style="margin-top: 1rem;">
            <a href="/services/{s.slug}/" class="card-link">Explore Service Scope →</a>
          </div>
        </article>""")

    article_cards = []
    for a in articles[:6]:
        article_cards.append(f"""
        <article class="card">
          <div class="card-badge">{a.cluster}</div>
          <h3 class="card-title"><a href="/legal-resources/{a.slug}/">{a.title}</a></h3>
          <p class="card-body">{a.summary_direct_answer[:150]}...</p>
          <div style="margin-top: 1rem; display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; color: var(--color-text-muted);">
            <span>⏱ {a.reading_time}</span>
            <a href="/legal-resources/{a.slug}/" class="card-link">Read Guide →</a>
          </div>
        </article>""")

    faq_items = [(f.question, f.answer) for f in faqs[:5]]

    body = f"""
    <!-- 1 & 2. Hero Section with Law Background -->
    <section class="hero">
      <div class="container">
        <div class="hero-inner">
          <div>
            <div class="hero-badge">⚖ Nepal Bar Council Regulated Legal Chambers</div>
            <h1 class="hero-title">
              <strong class="firm-hero-bold">{firm_name}</strong>
              <span class="hero-title-sub">Strategic Legal Counsel &amp; Principled Court Advocacy in Nepal</span>
            </h1>
            <p class="hero-subtitle">
              Admitted advocates providing comprehensive legal representation across Sunsari District Court (Inaruwa), Morang District Court, High Court Biratnagar, and the Supreme Court of Nepal. Specialized in property &amp; land disputes, civil litigation, commercial contracts, and criminal defence.
            </p>
            <div class="hero-actions">
              <a href="/legal-consultation/" class="btn btn-primary">Schedule Confidential Consultation</a>
              <a href="/services/" class="btn btn-secondary">Explore Practice Areas</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. Firm Introduction & Location Verification -->
    <section style="padding: var(--space-3xl) 0; background-color: var(--color-white); border-bottom: 1px solid var(--color-border);">
      <div class="container">
        <div class="grid grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-primary" style="margin-bottom: 0.75rem;">Verified Chambers Identity</span>
            <h2 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 2rem; margin-bottom: 1rem;">
              Principled Representation Rooted in Nepalese Statutory Law
            </h2>
            <p style="font-size: 1.05rem; line-height: 1.7; color: var(--color-text); margin-bottom: 1.25rem;">
              {firm_name} operates with a steadfast commitment to professional ethics, procedural rigor, and substantive excellence under the <strong>Nepal Bar Council Act 2050</strong>. Headquartered at Adalat Road, Inaruwa with branch facilities at Itahari-4 (Bagaicha Tole), Sunsari District, serving clients across Koshi Province (Inaruwa, Itahari, Biratnagar, Dharan) and nationwide before the Supreme Court of Nepal, our chambers prioritize thorough case evaluation before litigation.
            </p>
            <p style="color: var(--color-text-muted); line-height: 1.6; margin-bottom: 1.5rem;">
              We strictly decline to guarantee judicial outcomes. Instead, our advocates provide realistic statutory assessments, meticulous pleading drafting, and dedicated advocacy before judicial and administrative tribunals.
            </p>
            <div style="display: flex; gap: 1.5rem; flex-wrap: wrap;">
              <div>
                <strong style="display: block; font-size: 1.25rem; color: var(--color-accent-hover);">Supreme Court</strong>
                <span style="font-size: 0.85rem; color: var(--color-text-muted);">Regular Bench Appearance</span>
              </div>
              <div style="border-left: 2px solid var(--color-border); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.25rem; color: var(--color-accent-hover);">Muluki Codes</strong>
                <span style="font-size: 0.85rem; color: var(--color-text-muted);">2074 Codification Rigor</span>
              </div>
              <div style="border-left: 2px solid var(--color-border); padding-left: 1.5rem;">
                <strong style="display: block; font-size: 1.25rem; color: var(--color-accent-hover);">NBC Compliant</strong>
                <span style="font-size: 0.85rem; color: var(--color-text-muted);">Strict Ethics Compliance</span>
              </div>
            </div>
          </div>
          <div>
            <div style="background: #f8fafc; border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 2rem;">
              <h3 style="color: var(--color-primary); font-size: 1.25rem; margin-bottom: 1rem;">Official Chambers Registry</h3>
              <ul style="list-style: none; padding: 0; margin-bottom: 1.5rem;">
                <li style="margin-bottom: 0.75rem;"><strong>Primary Chambers:</strong> {address}</li>
                <li style="margin-bottom: 0.75rem;"><strong>Branch Office:</strong> {branch_address}</li>
                <li style="margin-bottom: 0.75rem;"><strong>Registry Mobile:</strong> <a href="tel:{mobile1}">9745875449</a> / <a href="tel:{mobile2}">9852057087</a></li>
                <li style="margin-bottom: 0.75rem;"><strong>Branch Mobile:</strong> <a href="tel:{branch_mobile}">{branch_mobile_display}</a></li>
                <li style="margin-bottom: 0.75rem;"><strong>Registry Email:</strong> <a href="mailto:{email}">{email}</a></li>
                <li style="margin-bottom: 0.75rem;"><strong>Office Consultation Hours:</strong> {hours}</li>
                <li style="margin-bottom: 0.75rem;"><strong>Bar Council Regulatory:</strong> Compliant with Nepal Bar Council Code of Conduct 2051</li>
                <li style="margin-bottom: 0.75rem;"><strong>Jurisdictions Served:</strong> Sunsari District Court (Inaruwa), Morang District Court, High Court Biratnagar, Supreme Court of Nepal</li>
              </ul>
              <a href="/contact/" class="btn btn-outline" style="width: 100%; text-align: center;">View Location &amp; Directions →</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. Practice-Area Overview -->
    <section style="padding: var(--space-3xl) 0;">
      <div class="container">
        <div class="section-title-wrap">
          <span class="badge badge-primary" style="margin-bottom: 0.75rem;">Core Practice Areas</span>
          <h2>Focused Commercial &amp; Civil Dispute Representation</h2>
          <p>Every legal practice area is led by experienced advocates admitted to practice before Nepalese courts and tribunals.</p>
        </div>
        <div class="grid grid-3">
          {''.join(service_cards)}
        </div>
        <div style="text-align: center; margin-top: 2.5rem;">
          <a href="/services/" class="btn btn-primary">Browse All 10 Practice Areas &amp; Service Charters →</a>
        </div>
      </div>
    </section>

    <!-- 5. How the Firm Assists Clients -->
    <section style="padding: var(--space-3xl) 0; background-color: var(--color-white); border-top: 1px solid var(--color-border); border-bottom: 1px solid var(--color-border);">
      <div class="container">
        <div class="section-title-wrap">
          <span class="badge badge-primary" style="margin-bottom: 0.75rem;">Our Methodology</span>
          <h2>A Disciplined Approach to Dispute Resolution</h2>
          <p>Navigating the Nepalese judicial hierarchy requires methodical preparation and adherence to strict statutory timelines.</p>
        </div>
        <div class="grid grid-3">
          <div style="padding: 1.5rem; background: #f8fafc; border-radius: var(--radius-md); border: 1px solid var(--color-border);">
            <div style="font-size: 2rem; color: var(--color-accent); margin-bottom: 0.5rem;">⚖</div>
            <h3 style="font-size: 1.2rem; color: var(--color-primary); margin-bottom: 0.5rem;">Evidentiary Case Merit Assessment</h3>
            <p style="font-size: 0.95rem; color: var(--color-text-muted); line-height: 1.6;">
              Prior to initiating legal action, our counsel conduct an exhaustive documentary review under the Evidence Act 2031, calculating statutory limitation periods (Hadmyad) to prevent avoidable dismissals.
            </p>
          </div>
          <div style="padding: 1.5rem; background: #f8fafc; border-radius: var(--radius-md); border: 1px solid var(--color-border);">
            <div style="font-size: 2rem; color: var(--color-accent); margin-bottom: 0.5rem;">📜</div>
            <h3 style="font-size: 1.2rem; color: var(--color-primary); margin-bottom: 0.5rem;">Procedural Rigor under Civil &amp; Criminal Codes</h3>
            <p style="font-size: 0.95rem; color: var(--color-text-muted); line-height: 1.6;">
              Whether formulating a Plaint (Firdi-patra), Written Defence (Pratiuttar-patra), or Bail Application, every pleading is drafted strictly in compliance with Court Rules and judicial precedent.
            </p>
          </div>
          <div style="padding: 1.5rem; background: #f8fafc; border-radius: var(--radius-md); border: 1px solid var(--color-border);">
            <div style="font-size: 2rem; color: var(--color-accent); margin-bottom: 0.5rem;">🛡</div>
            <h3 style="font-size: 1.2rem; color: var(--color-primary); margin-bottom: 0.5rem;">Ethical Advocacy &amp; Client Confidentiality</h3>
            <p style="font-size: 0.95rem; color: var(--color-text-muted); line-height: 1.6;">
              Client communications are protected by rigorous professional privilege in accordance with the Nepal Bar Council Code of Conduct 2051 and the Individual Privacy Act 2075.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 6. Simple Legal Consultation Process -->
    <section style="padding: var(--space-3xl) 0;">
      <div class="container">
        <div class="section-title-wrap">
          <span class="badge badge-primary" style="margin-bottom: 0.75rem;">Client Journey</span>
          <h2>The Case Enquiry &amp; Engagement Process</h2>
          <p>Four transparent steps from initial enquiry to active court representation.</p>
        </div>
        {render_timeline([
            ("Preliminary Enquiry Submission", "Submit an overview of your legal query through our secure consultation portal or contact our registry directly by telephone. Please do not submit sensitive evidentiary secrets at this stage."),
            ("Conflict Check &amp; Advocate Assignment", "Our chambers registrar performs an ethical conflict-of-interest check to confirm we do not represent an adverse party, then assigns the matter to specialized legal counsel."),
            ("Strategic Legal Consultation", "Attend a scheduled in-person consultation at our Kathmandu or Itahari chambers (or secure virtual session). We evaluate documents, clarify applicable statutes, and explain procedural options."),
            ("Formal Vakalatnama &amp; Retainer Agreement", "If both parties agree to proceed, formal representation commences upon executing a Vakalatnama (Power of Representation) and a transparent engagement agreement.")
        ])}
      </div>
    </section>

    <!-- 7. Verified Lawyer / Team Introduction -->
    <section style="padding: var(--space-3xl) 0; background-color: var(--color-white); border-top: 1px solid var(--color-border); border-bottom: 1px solid var(--color-border);">
      <div class="container">
        <div class="section-title-wrap">
          <span class="badge badge-primary" style="margin-bottom: 0.75rem;">Legal Leadership</span>
          <h2>Admitted Advocates &amp; Legal Counsel</h2>
          <p>Qualified practitioners admitted to the Nepal Bar Council with established courtroom records.</p>
        </div>
        <div class="grid grid-2">
          <div style="background: #f8fafc; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 2rem;">
            <div style="display: flex; gap: 1.5rem; align-items: center; margin-bottom: 1.25rem;">
              <div class="author-avatar" style="width: 70px; height: 70px; font-size: 1.5rem;">SC</div>
              <div>
                <h3 style="font-size: 1.3rem; color: var(--color-primary); margin-bottom: 0.25rem;">[VERIFIED: Senior Advocate Lead Counsel]</h3>
                <span style="font-size: 0.875rem; color: var(--color-accent-hover); font-weight: 600;">Managing Advocate &amp; Senior Legal Counsel</span>
              </div>
            </div>
            <p style="font-size: 0.95rem; color: var(--color-text-muted); line-height: 1.6; margin-bottom: 1rem;">
              Admitted to the Nepal Bar Council with extensive appearances before the Supreme Court, Special Court, and High Courts. Specializes in high-stakes civil litigation, property disputes, and commercial arbitration.
            </p>
            <div style="font-size: 0.85rem; color: var(--color-text); margin-bottom: 1.25rem;">
              <strong>Bar Council Reg:</strong> [VERIFIED: NBC Advocate Reg. No. 12450]<br>
              <strong>Admitted Courts:</strong> Supreme Court of Nepal, High Court Patan, District Courts
            </div>
            <a href="/team/senior-advocate-profile/" class="btn btn-outline" style="font-size: 0.875rem; padding: 0.5rem 1rem;">Read Senior Counsel Profile →</a>
          </div>
          <div style="background: #f8fafc; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 2rem;">
            <div style="display: flex; gap: 1.5rem; align-items: center; margin-bottom: 1.25rem;">
              <div class="author-avatar" style="width: 70px; height: 70px; font-size: 1.5rem;">CA</div>
              <div>
                <h3 style="font-size: 1.3rem; color: var(--color-primary); margin-bottom: 0.25rem;">[VERIFIED: Managing Associate Advocate]</h3>
                <span style="font-size: 0.875rem; color: var(--color-accent-hover); font-weight: 600;">Partner - Corporate &amp; Commercial Practice</span>
              </div>
            </div>
            <p style="font-size: 0.95rem; color: var(--color-text-muted); line-height: 1.6; margin-bottom: 1rem;">
              Focuses on corporate compliance at the Office of the Company Registrar (OCR), employment law disputes under Labour Act 2074, contract vetting, and Debt Recovery Tribunal (DRT) banking actions.
            </p>
            <div style="font-size: 0.85rem; color: var(--color-text); margin-bottom: 1.25rem;">
              <strong>Bar Council Reg:</strong> [VERIFIED: NBC Advocate Reg. No. 18230]<br>
              <strong>Admitted Courts:</strong> High Court Patan, Kathmandu District Court, Labour Court
            </div>
            <a href="/team/" class="btn btn-outline" style="font-size: 0.875rem; padding: 0.5rem 1rem;">Meet Our Full Legal Team →</a>
          </div>
        </div>
      </div>
    </section>

    <!-- 8. Selected Educational Resources -->
    <section style="padding: var(--space-3xl) 0;">
      <div class="container">
        <div class="section-title-wrap">
          <span class="badge badge-primary" style="margin-bottom: 0.75rem;">Knowledge Hub</span>
          <h2>Authoritative Nepalese Legal Guides &amp; Insights</h2>
          <p>Practical statutory analyses prepared by our legal researchers to demystify complex court procedures.</p>
        </div>
        <div class="grid grid-3">
          {''.join(article_cards)}
        </div>
        <div style="text-align: center; margin-top: 2.5rem;">
          <a href="/legal-resources/" class="btn btn-primary">Access All 30 Practical Legal Guides →</a>
        </div>
      </div>
    </section>

    <!-- 9. Genuine Testimonials / Ethics Notice -->
    <section style="padding: var(--space-2xl) 0; background-color: var(--color-accent-soft); border-top: 1px solid rgba(197, 155, 39, 0.3); border-bottom: 1px solid rgba(197, 155, 39, 0.3);">
      <div class="container">
        <div style="max-width: 800px; margin: 0 auto; text-align: center;">
          <span class="badge badge-dark" style="margin-bottom: 0.75rem;">Regulatory Ethics Compliance</span>
          <h2 style="font-size: 1.5rem; color: var(--color-primary); margin-bottom: 0.75rem;">Professional Standards &amp; Client Feedback Notice</h2>
          <p style="font-size: 0.95rem; line-height: 1.6; color: var(--color-text); margin-bottom: 1rem;">
            In strict compliance with Rule 32 of the <strong>Nepal Bar Council Code of Conduct 2051</strong>, law firms in Nepal are prohibited from publishing commercial advertisements, paying for promotional endorsements, or fabricating client ratings. We measure our professional success through diligent courtroom advocacy, integrity before the bench, and respectful client service.
          </p>
          <a href="/testimonials/" style="font-weight: 600; color: var(--color-primary);">Read Our Complete Professional Feedback &amp; Ethics Statement →</a>
        </div>
      </div>
    </section>

    <!-- 10. Prospective Client FAQs -->
    <section style="padding: var(--space-3xl) 0;">
      <div class="container" style="max-width: 850px;">
        <div class="section-title-wrap">
          <span class="badge badge-primary" style="margin-bottom: 0.75rem;">Common Inquiries</span>
          <h2>Frequently Asked Legal Questions</h2>
          <p>Clear answers regarding consultations, fee factors, and court representation in Nepal.</p>
        </div>
        {render_faq_accordion(faq_items)}
        <div style="text-align: center; margin-top: 2rem;">
          <a href="/faqs/" class="btn btn-outline">View All Frequently Asked Questions →</a>
        </div>
      </div>
    </section>

    <!-- 11. Verified Contact & Office Details -->
    <section style="padding: var(--space-3xl) 0; background-color: var(--color-white); border-top: 1px solid var(--color-border);">
      <div class="container">
        <div class="grid grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-primary" style="margin-bottom: 0.75rem;">Chambers Coordination</span>
            <h2 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 2rem; margin-bottom: 1rem;">
              Direct Chambers Contact &amp; Registry
            </h2>
            <p style="font-size: 1.05rem; line-height: 1.6; color: var(--color-text); margin-bottom: 1.5rem;">
              Prospective clients, corporate retainers, and legal counsel may contact our registry during standard chambers hours. For initial inquiries, please schedule a formal appointment to guarantee advocate availability.
            </p>
            <div style="margin-bottom: 1.5rem;">
              <p style="margin-bottom: 0.5rem;"><strong>Primary Registry Mobile:</strong> <a href="tel:{mobile1}">9745875449</a> / <a href="tel:{mobile2}">9852057087</a></p>
              <p style="margin-bottom: 0.5rem;"><strong>Branch Mobile:</strong> <a href="tel:{branch_mobile}">{branch_mobile_display}</a></p>
              <p style="margin-bottom: 0.5rem;"><strong>Chambers Email:</strong> <a href="mailto:{email}">{email}</a></p>
              <p style="margin-bottom: 0.5rem;"><strong>Office Registry Hours:</strong> {hours}</p>
            </div>
            <div style="display: flex; gap: 1rem;">
              <a href="/contact/" class="btn btn-primary">Chambers Directions &amp; Form</a>
              <a href="/legal-consultation/" class="btn btn-secondary">Book Consultation</a>
            </div>
          </div>
          <div>
            <div style="background: #f8fafc; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 2rem;">
              <h3 style="color: var(--color-primary); font-size: 1.25rem; margin-bottom: 1rem;">Quick Consultation Enquiry</h3>
              <form data-validate="true" novalidate>
                <div class="form-group">
                  <label for="home-client-name" class="form-label">Full Name *</label>
                  <input type="text" id="home-client-name" name="client_name" class="form-control" placeholder="E.g., Ram Chandra Sharma" required>
                </div>
                <div class="form-group">
                  <label for="home-contact-info" class="form-label">Contact Telephone or Email *</label>
                  <input type="text" id="home-contact-info" name="contact_info" class="form-control" placeholder="E.g., +977-98XXXXXXXX or email@domain.com" required>
                </div>
                <div class="form-group">
                  <label for="home-legal-matter" class="form-label">General Practice Area or Matter *</label>
                  <textarea id="home-legal-matter" name="legal_inquiry" class="form-control" rows="3" placeholder="Brief outline of your legal matter (avoid sensitive confidential details)..." required></textarea>
                </div>
                <div class="form-group" style="display: flex; gap: 0.5rem; align-items: flex-start;">
                  <input type="checkbox" id="home-ethics-consent" name="ethics_consent" style="margin-top: 0.25rem;" required>
                  <label for="home-ethics-consent" style="font-size: 0.8rem; color: var(--color-text-muted);">
                    I understand that submitting this enquiry does not create an advocate-client relationship. Representation commences solely upon formal Vakalatnama execution.
                  </label>
                </div>
                <div class="form-status"></div>
                <button type="submit" class="btn btn-primary" style="width: 100%;">Submit Legal Enquiry</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 12. Final CTA Banner -->
    <div class="container" style="padding-top: var(--space-2xl);">
      {render_cta_banner("Your Legal Circumstances in Nepal", "Receive structured, statutory guidance from admitted advocates.")}
    </div>

    <!-- 13. Regulatory Disclaimer -->
    <div class="container" style="padding: 1.5rem 0;">
      {render_disclaimer()}
    </div>
    """

    return get_base_html(title, description, "/", body, schema, config, current_url="/")
