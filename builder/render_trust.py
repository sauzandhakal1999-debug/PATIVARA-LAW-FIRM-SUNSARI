# Trust, compliance, governance and support page renderers
from builder.templates import (
    get_base_html, render_breadcrumbs, render_faq_accordion, render_disclaimer
)

def render_about_page(config):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    city = config.get("locations", {}).get("primary", {}).get("city", "Kathmandu")
    title = f"Dedicated to Principled Advocacy & Strategic Legal Counsel in Nepal | {firm_name}"
    description = "About our law firm in Nepal. Founded on principles of meticulous procedural preparation, strict ethics compliance under the Nepal Bar Council, and client confidentiality."
    canonical = "/about/"

    crumbs = [("About Our Firm", "")]

    body = f"""
    {render_breadcrumbs(crumbs)}

    <section class="hero">
      <div class="container">
        <div class="hero-inner">
          <div>
            <div class="hero-badge">Professional Law Practice in Nepal</div>
            <h1 class="hero-title">Principled Advocacy &amp; Strategic Legal Counsel</h1>
            <p class="hero-subtitle">
              Advising domestic enterprises, property owners, and private individuals before District Courts, High Courts, and the Supreme Court of Nepal.
            </p>
          </div>
        </div>
      </div>
    </section>

    <div class="container prose" style="padding: var(--space-3xl) 0;">
      <h2 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 2rem;">Our Chambers Philosophy</h2>
      <p>
        Founded in {city}, {firm_name} is dedicated to providing rigorous, dependable legal advocacy and corporate advisory. Our legal practice is grounded in the recognition that substantive legal success requires disciplined evidentiary analysis long before a dispute enters open court.
      </p>

      <h2>Adherence to Nepal Bar Council Standards</h2>
      <p>
        We practice in strict compliance with the <strong>Nepal Bar Council Act 2050</strong> and the <strong>Nepal Bar Council Code of Conduct 2051</strong>. We hold that the profession of an advocate is an office of public trust and judicial assistance, not commercial advertising. For this reason:
      </p>
      <ul>
        <li>We provide honest, objective assessments of legal risks rather than unrealistic outcome guarantees.</li>
        <li>We conduct exhaustive limitation (Hadmyad) and evidentiary reviews under the Muluki Civil and Criminal Procedure Codes 2074.</li>
        <li>We safeguard client communications with uncompromising ethical confidentiality.</li>
      </ul>

      <h2>Court Jurisdiction &amp; Geographical Scope</h2>
      <p>
        Our advocates regularly appear before judicial benches and administrative authorities across Nepal:
      </p>
      <ul>
        <li><strong>Supreme Court of Nepal:</strong> Constitutional petitions, final appeals, and revision applications.</li>
        <li><strong>High Courts:</strong> High Court Patan (Commercial Bench), High Court Biratnagar, and appellate benches.</li>
        <li><strong>District Courts:</strong> Kathmandu, Lalitpur, Bhaktapur, Sunsari (Inaruwa), and Morang (Biratnagar).</li>
        <li><strong>Specialized Tribunals:</strong> Debt Recovery Tribunal (DRT), Labour Court, Special Court, and Land Revenue Offices (Malpot).</li>
      </ul>

      <div style="margin: 2.5rem 0;">
        <a href="/team/" class="btn btn-primary">Meet Our Legal Team →</a>
        <a href="/legal-consultation/" class="btn btn-secondary" style="margin-left: 1rem;">Schedule Consultation</a>
      </div>

      {render_disclaimer()}
    </div>
    """

    return get_base_html(title, description, canonical, body, None, config, current_url=canonical)

def render_team_index(team, config):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    title = f"Experienced Advocates & Legal Counsel Admitted in Nepal | {firm_name}"
    description = "Meet our qualified advocates and legal counsel admitted to the Nepal Bar Council. Specialized practitioners appearing regularly in Supreme Court, High Courts, and District Courts."
    canonical = "/team/"

    crumbs = [("About", "/about/"), ("Our Legal Team", "")]

    profiles_html = []
    for m in team:
        courts = "".join([f"<span class='court-tag'>{c}</span>" for c in m.court_admissions])
        practice = ", ".join(m.practice_areas)
        profiles_html.append(f"""
        <article class="card" style="padding: 2rem;">
          <div class="team-profile-header">
            <div class="team-profile-avatar">{m.name[:2]}</div>
            <div>
              <h2 style="font-size: 1.45rem; color: var(--color-primary); margin-bottom: 0.25rem;">{m.name}</h2>
              <div style="color: var(--color-accent-hover); font-weight: 600; margin-bottom: 0.5rem;">{m.role}</div>
              <p style="font-size: 0.9rem; color: var(--color-text-muted); margin-bottom: 0.5rem;"><strong>Qualifications:</strong> {m.qualifications}</p>
              <p style="font-size: 0.85rem; color: var(--color-dark);"><strong>Bar Registration:</strong> {m.bar_council_reg}</p>
            </div>
          </div>
          <p style="line-height: 1.7; color: var(--color-text); margin-bottom: 1rem;">{m.bio}</p>
          <div style="margin-bottom: 1rem;">
            <strong>Court Admissions:</strong>
            <div class="court-admissions-tags">{courts}</div>
          </div>
          <p style="font-size: 0.9rem; color: var(--color-text-muted); margin-bottom: 1.5rem;">
            <strong>Primary Practice Areas:</strong> {practice}
          </p>
          <a href="/team/senior-advocate-profile/" class="btn btn-outline" style="font-size: 0.9rem; padding: 0.5rem 1rem;">View Full Advocate Profile →</a>
        </article>""")

    body = f"""
    {render_breadcrumbs(crumbs)}

    <section class="hero">
      <div class="container">
        <div class="hero-inner">
          <div>
            <div class="hero-badge">Nepal Bar Council Admitted Counsel</div>
            <h1 class="hero-title">Our Legal Team &amp; Advocates</h1>
            <p class="hero-subtitle">
              Experienced practitioners dedicated to professional excellence, courtroom advocacy, and rigorous legal research across Nepal.
            </p>
          </div>
        </div>
      </div>
    </section>

    <div class="container" style="padding: var(--space-3xl) 0;">
      <div class="grid grid-2">{''.join(profiles_html)}</div>
    </div>

    <div class="container" style="padding-bottom: 2rem;">
      {render_disclaimer()}
    </div>
    """

    return get_base_html(title, description, canonical, body, None, config, current_url=canonical)

def render_lawyer_profile(config):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    title = f"Senior Legal Counsel & Managing Advocate | {firm_name}"
    description = "Profile of Senior Legal Counsel at PATHIVARA LAW FIRM SUNSARI. Specialized in Supreme Court civil litigation, property disputes, and commercial arbitration."
    canonical = "/team/senior-advocate-profile/"

    crumbs = [
        ("About", "/about/"),
        ("Our Team", "/team/"),
        ("Senior Legal Counsel", "")
    ]

    body = f"""
    {render_breadcrumbs(crumbs)}

    <div class="container prose" style="padding: var(--space-3xl) 0;">
      <div class="team-profile-header">
        <div class="team-profile-avatar">SC</div>
        <div>
          <span class="badge badge-primary" style="margin-bottom: 0.5rem;">Managing Advocate &amp; Senior Counsel</span>
          <h1 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 2.25rem; margin-bottom: 0.25rem;">
            [VERIFIED: Senior Advocate Lead Counsel]
          </h1>
          <p style="font-size: 1rem; color: var(--color-accent-hover); font-weight: 600; margin-bottom: 0.5rem;">
            LL.M. in Commercial &amp; Procedural Law (Tribhuvan University), LL.B.
          </p>
          <p style="font-size: 0.9rem; color: var(--color-dark); margin-bottom: 0.25rem;">
            <strong>Bar Council Registration:</strong> [VERIFIED: Nepal Bar Council Advocate Reg. No. 12450]
          </p>
          <p style="font-size: 0.9rem; color: var(--color-text-muted);">
            <strong>Professional Association:</strong> Supreme Court Bar Association Member
          </p>
        </div>
      </div>

      <h2>Court Admissions &amp; Jurisdiction</h2>
      <div class="court-admissions-tags">
        <span class="court-tag">Supreme Court of Nepal</span>
        <span class="court-tag">High Court Patan (Commercial Bench)</span>
        <span class="court-tag">High Court Biratnagar</span>
        <span class="court-tag">Kathmandu District Court</span>
        <span class="court-tag">Special Court (Kathmandu)</span>
        <span class="court-tag">Nepal Council of Arbitration (NEPCA)</span>
      </div>

      <h2>Professional Practice &amp; Substantive Experience</h2>
      <p>
        With extensive courtroom experience spanning over a decade and a half, Senior Counsel has established a notable track record in high-stakes civil litigation, property title adjudication (Lalpurja and Anshabanda partition suits), and constitutional writ petitions. He regularly represents domestic corporations, foreign investors, and non-resident Nepalese (NRNs) in asset protection and complex commercial disputes.
      </p>

      <h2>Notable Contributions &amp; Publications</h2>
      <ul>
        <li><em>Procedural Evolution of Injunctions under Muluki Civil Procedure Code 2074</em> (Nepal Bar Council Journal)</li>
        <li><em>Corporate Governance &amp; Fiduciary Liabilities in Closely Held Companies</em> (Nepal Law Review)</li>
        <li><em>Due Diligence Standards in Real Estate Acquisitions in Nepal</em> (Commercial Law Journal)</li>
      </ul>

      <h2>Languages Spoken</h2>
      <p>English, Nepali (नेपाली), Bhojpuri, Hindi.</p>

      <div style="background: #f8fafc; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 1.5rem; margin: 2rem 0;">
        <h3 style="margin-top: 0;">Consultation Availability</h3>
        <p style="font-size: 0.95rem; color: var(--color-text-muted);">
          Consultations with Senior Counsel are scheduled strictly by appointment through the chambers registry to prevent conflicts of interest.
        </p>
        <a href="/legal-consultation/" class="btn btn-primary">Schedule Consultation →</a>
      </div>

      {render_disclaimer()}
    </div>
    """

    return get_base_html(title, description, canonical, body, None, config, current_url=canonical)

def render_consultation_page(config):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    phone = config.get("contact", {}).get("telephone_display", "+977 (01) 4XXXXXX")
    tel_link = config.get("contact", {}).get("telephone", "+97714000000")
    title = f"Schedule a Structured Legal Consultation | {firm_name}"
    description = "Book an initial legal consultation in Kathmandu or Koshi Province. Understand consultation protocols, what documents to prepare, and professional fee policies."
    canonical = "/legal-consultation/"

    crumbs = [("Legal Consultation", "")]

    body = f"""
    {render_breadcrumbs(crumbs)}

    <section class="hero">
      <div class="container">
        <div class="hero-inner">
          <div>
            <div class="hero-badge">Confidential &amp; Structured Process</div>
            <h1 class="hero-title">Schedule a Legal Consultation in Nepal</h1>
            <p class="hero-subtitle">
              Structured statutory review, documentary analysis, and procedural risk assessment by admitted advocates before District Courts, High Courts, and the Supreme Court.
            </p>
          </div>
        </div>
      </div>
    </section>

    <div class="container" style="padding: var(--space-3xl) 0;">
      <div class="grid" style="grid-template-columns: 1.3fr 1fr; gap: var(--space-2xl);">
        <div>
          <h2 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 1.85rem; margin-bottom: 1rem;">
            How Consultations Work at Our Chambers
          </h2>
          <p style="font-size: 1.05rem; line-height: 1.7; color: var(--color-text); margin-bottom: 1.5rem;">
            We conduct consultations to provide prospective clients with an objective evaluation of their legal position. We do not provide hurried informal opinions; our advocates review documentary evidence under the Evidence Act 2031 and examine statutory limitation periods (Hadmyad) under the Muluki Codes.
          </p>

          <h3 style="color: var(--color-primary); font-size: 1.3rem; margin-bottom: 0.75rem;">What to Expect During Your Consultation</h3>
          <ul class="checklist-items" style="margin-bottom: 2rem;">
            <li class="checklist-item"><span class="checklist-icon">✔</span><span>Confidential assessment under Nepal Bar Council professional ethics standards.</span></li>
            <li class="checklist-item"><span class="checklist-icon">✔</span><span>Exhaustive limitation period calculation to protect your legal remedies.</span></li>
            <li class="checklist-item"><span class="checklist-icon">✔</span><span>Comparative evaluation of out-of-court mediation versus court litigation.</span></li>
            <li class="checklist-item"><span class="checklist-icon">✔</span><span>Clear explanation of court fees under the Court Fee Act 2017 and expected timelines.</span></li>
          </ul>

          <h3 style="color: var(--color-primary); font-size: 1.3rem; margin-bottom: 0.75rem;">What Documents to Bring</h3>
          <ul class="checklist-items" style="margin-bottom: 2rem;">
            <li class="checklist-item"><span class="checklist-icon">📋</span><span>Government photo identification (Citizenship Certificate or Passport).</span></li>
            <li class="checklist-item"><span class="checklist-icon">📋</span><span>All original contracts, receipts, promissory notes, or bank statements involved.</span></li>
            <li class="checklist-item"><span class="checklist-icon">📋</span><span>Prior court notices, police inquiry papers, or ward recommendation letters.</span></li>
            <li class="checklist-item"><span class="checklist-icon">📋</span><span>A concise 1-page chronological timeline of key events and dates.</span></li>
          </ul>

          <div style="background: #f8fafc; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 1.5rem;">
            <h4 style="color: var(--color-primary); font-size: 1.1rem; margin-bottom: 0.5rem;">Consultation Fees &amp; Retainer Policy</h4>
            <p style="font-size: 0.95rem; color: var(--color-text-muted); line-height: 1.6; margin: 0;">
              Chambers consultations are billed based on advocate seniority and the time required for pre-consultation document review. Retainer fees for court litigation are formally agreed upon in writing before executing a Vakalatnama. We do not accept contingency fees where prohibited by law.
            </p>
          </div>
        </div>

        <div>
          <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 2rem; box-shadow: var(--shadow-md);">
            <h3 style="color: var(--color-primary); font-size: 1.45rem; margin-bottom: 0.5rem;">Book an Appointment</h3>
            <p style="font-size: 0.9rem; color: var(--color-text-muted); margin-bottom: 1.5rem;">
              Fill out this confidential enquiry. Our coordinator will contact you to verify details and schedule your appointment.
            </p>

            <form data-validate="true" novalidate>
              <div class="form-group">
                <label for="consult-name" class="form-label">Full Name *</label>
                <input type="text" id="consult-name" name="client_name" class="form-control" placeholder="E.g., Bimal Adhikari" required>
              </div>

              <div class="form-group">
                <label for="consult-contact" class="form-label">Phone Number or Email *</label>
                <input type="text" id="consult-contact" name="contact_info" class="form-control" placeholder="E.g., +977-98XXXXXXXX or email@domain.com" required>
              </div>

              <div class="form-group">
                <label for="consult-service" class="form-label">Primary Practice Area *</label>
                <select id="consult-service" name="service_interest" class="form-control" required>
                  <option value="">Select Relevant Legal Service...</option>
                  <option value="civil">Civil Litigation &amp; Dispute Resolution</option>
                  <option value="criminal">Criminal Law &amp; Defence</option>
                  <option value="family">Family Law &amp; Divorce</option>
                  <option value="property">Property &amp; Land Law (Lalpurja)</option>
                  <option value="corporate">Corporate &amp; Business Law</option>
                  <option value="contracts">Contract Drafting &amp; Review</option>
                  <option value="inheritance">Inheritance &amp; Succession</option>
                  <option value="labour">Labour &amp; Employment Law</option>
                  <option value="banking">Banking &amp; Financial Law</option>
                  <option value="mediation">Mediation &amp; ADR</option>
                </select>
              </div>

              <div class="form-group">
                <label for="consult-mode" class="form-label">Preferred Consultation Format</label>
                <select id="consult-mode" name="consultation_mode" class="form-control">
                  <option value="kathmandu">In-Person (Kathmandu Chambers)</option>
                  <option value="itahari">In-Person (Koshi / Itahari Office)</option>
                  <option value="virtual">Secure Virtual Meeting (Google Meet / Zoom)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="consult-summary" class="form-label">Brief Summary of Legal Matter *</label>
                <textarea id="consult-summary" name="legal_inquiry" class="form-control" rows="4" placeholder="Describe the factual situation without including trade secrets or sensitive confessions..." required></textarea>
                <span class="form-note">Please do not submit highly confidential or self-incriminating details via web forms.</span>
              </div>

              <div class="form-group" style="display: flex; gap: 0.5rem; align-items: flex-start;">
                <input type="checkbox" id="consult-consent" name="ethics_consent" style="margin-top: 0.25rem;" required>
                <label for="consult-consent" style="font-size: 0.8rem; color: var(--color-text-muted);">
                  I acknowledge that submitting this form does not establish an advocate-client relationship. Formal representation commences only upon executing a Vakalatnama under the Nepal Bar Council Code of Conduct.
                </label>
              </div>

              <div class="form-status"></div>
              <button type="submit" class="btn btn-primary" style="width: 100%;">Submit Consultation Request</button>
            </form>

            <div style="margin-top: 1.5rem; text-align: center; font-size: 0.85rem; color: var(--color-text-muted);">
              Or call our chambers registry directly at <a href="tel:{tel_link}">{phone}</a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="container" style="padding-bottom: 2rem;">
      {render_disclaimer()}
    </div>
    """

    return get_base_html(title, description, canonical, body, None, config, current_url=canonical)

def render_contact_page(config):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    phone = config.get("contact", {}).get("telephone_display", "+977 (01) 4XXXXXX")
    tel_link = config.get("contact", {}).get("telephone", "+97714000000")
    email = config.get("contact", {}).get("email", "info@pathivaralawfirmsunsari.com")
    hours = config.get("contact", {}).get("office_hours", "Sun–Fri 9:30 AM–5:30 PM")
    primary_loc = config.get("locations", {}).get("primary", {})
    address = primary_loc.get("formatted_address", "Kathmandu, Nepal")

    title = f"Contact Our Law Chambers in Nepal | {firm_name}"
    description = "Contact PATHIVARA LAW FIRM SUNSARI in Kathmandu and Koshi Province. Verified telephone, office hours, email, and accessible legal inquiry form."
    canonical = "/contact/"

    crumbs = [("Contact Chambers", "")]

    body = f"""
    {render_breadcrumbs(crumbs)}

    <section class="hero">
      <div class="container">
        <div class="hero-inner">
          <div>
            <div class="hero-badge">Direct Chambers Communication</div>
            <h1 class="hero-title">Contact Our Law Chambers in Nepal</h1>
            <p class="hero-subtitle">
              Reach our registry in Kathmandu and Koshi Province for case consultations, corporate retainer inquiries, and court appointment coordination.
            </p>
          </div>
        </div>
      </div>
    </section>

    <div class="container" style="padding: var(--space-3xl) 0;">
      <div class="grid grid-2" style="gap: var(--space-2xl);">
        <div>
          <h2 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 1.85rem; margin-bottom: 1.5rem;">
            Chambers Registry Details
          </h2>

          <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 1.75rem; margin-bottom: 1.5rem; box-shadow: var(--shadow-sm);">
            <h3 style="color: var(--color-primary); font-size: 1.25rem; margin-bottom: 0.75rem;">Primary Kathmandu Chambers</h3>
            <p style="margin-bottom: 0.5rem;"><strong>Address:</strong> {address}</p>
            <p style="margin-bottom: 0.5rem;"><strong>Telephone:</strong> <a href="tel:{tel_link}">{phone}</a></p>
            <p style="margin-bottom: 0.5rem;"><strong>Registry Email:</strong> <a href="mailto:{email}">{email}</a></p>
            <p style="margin-bottom: 0.5rem;"><strong>Office Hours:</strong> {hours}</p>
            <p style="font-size: 0.85rem; color: var(--color-text-muted); margin: 0;">
              Serving Supreme Court of Nepal, High Court Patan, and District Courts of Kathmandu, Lalitpur, and Bhaktapur.
            </p>
          </div>

          <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 1.75rem; margin-bottom: 1.5rem; box-shadow: var(--shadow-sm);">
            <h3 style="color: var(--color-primary); font-size: 1.25rem; margin-bottom: 0.75rem;">Koshi Province Office (Itahari / Sunsari)</h3>
            <p style="margin-bottom: 0.5rem;"><strong>Address:</strong> Main Road, Itahari-6, Sunsari, Nepal</p>
            <p style="margin-bottom: 0.5rem;"><strong>Branch Telephone:</strong> +977-25-580000</p>
            <p style="margin-bottom: 0.5rem;"><strong>Office Hours:</strong> Sunday – Friday: 9:30 AM – 5:00 PM</p>
            <p style="font-size: 0.85rem; color: var(--color-text-muted); margin: 0;">
              Serving High Court Biratnagar, Sunsari District Court (Inaruwa), and Morang District Court.
            </p>
          </div>

          <div style="background: #f8fafc; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 1.5rem;">
            <h4 style="color: var(--color-primary); font-size: 1.1rem; margin-bottom: 0.5rem;">Important Notice Regarding Electronic Inquiries</h4>
            <p style="font-size: 0.9rem; line-height: 1.6; color: var(--color-text-muted); margin: 0;">
              In accordance with Nepal Bar Council ethical regulations, transmitting an electronic message does not create an advocate-client relationship. Please refrain from submitting confidential or privileged documents until our registry confirms that no conflict of interest exists.
            </p>
          </div>
        </div>

        <div>
          <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 2rem; box-shadow: var(--shadow-md);">
            <h3 style="color: var(--color-primary); font-size: 1.45rem; margin-bottom: 0.5rem;">Direct Chambers Inquiry</h3>
            <p style="font-size: 0.9rem; color: var(--color-text-muted); margin-bottom: 1.5rem;">
              Send an enquiry to our registry coordinator. We respond to verified inquiries during business hours.
            </p>

            <form data-validate="true" novalidate>
              <div class="form-group">
                <label for="contact-name" class="form-label">Full Name *</label>
                <input type="text" id="contact-name" name="client_name" class="form-control" placeholder="E.g., Suman Poudel" required>
              </div>

              <div class="form-group">
                <label for="contact-email" class="form-label">Email Address *</label>
                <input type="email" id="contact-email" name="contact_email" class="form-control" placeholder="E.g., suman@example.com" required>
              </div>

              <div class="form-group">
                <label for="contact-phone" class="form-label">Phone / Mobile *</label>
                <input type="text" id="contact-phone" name="contact_info" class="form-control" placeholder="E.g., +977-98XXXXXXXX" required>
              </div>

              <div class="form-group">
                <label for="contact-inquiry" class="form-label">General Nature of Inquiry *</label>
                <textarea id="contact-inquiry" name="legal_inquiry" class="form-control" rows="4" placeholder="Brief outline of your query..." required></textarea>
              </div>

              <div class="form-group" style="display: flex; gap: 0.5rem; align-items: flex-start;">
                <input type="checkbox" id="contact-consent" name="ethics_consent" style="margin-top: 0.25rem;" required>
                <label for="contact-consent" style="font-size: 0.8rem; color: var(--color-text-muted);">
                  I acknowledge that this contact form is for preliminary registry communications and does not constitute formal legal representation.
                </label>
              </div>

              <div class="form-status"></div>
              <button type="submit" class="btn btn-primary" style="width: 100%;">Send Chambers Inquiry</button>
            </form>
          </div>
        </div>
      </div>
    </div>

    <div class="container" style="padding-bottom: 2rem;">
      {render_disclaimer()}
    </div>
    """

    return get_base_html(title, description, canonical, body, None, config, current_url=canonical)

def render_faqs_page(faqs, config):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    title = f"Frequently Asked Legal Questions | {firm_name}"
    description = "Frequently asked legal questions in Nepal. Insights on advocate fees, court jurisdiction, bail eligibility, divorce procedures, and land registration."
    canonical = "/faqs/"

    crumbs = [("Frequently Asked Questions", "")]

    categories = {}
    for f in faqs:
        categories.setdefault(f.category, []).append(f)

    sections_html = []
    for cat, cat_faqs in categories.items():
        items = [(f.question, f.answer) for f in cat_faqs]
        sections_html.append(f"""
        <section style="margin-bottom: var(--space-2xl);">
          <h2 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 1.5rem; border-bottom: 2px solid var(--color-accent); padding-bottom: 0.5rem; margin-bottom: 1.25rem;">
            {cat}
          </h2>
          {render_faq_accordion(items)}
        </section>""")

    body = f"""
    {render_breadcrumbs(crumbs)}

    <section class="hero">
      <div class="container">
        <div class="hero-inner">
          <div>
            <div class="hero-badge">Answers to Common Inquiries</div>
            <h1 class="hero-title">Frequently Asked Legal Questions in Nepal</h1>
            <p class="hero-subtitle">
              Clear, statutory explanations regarding litigation stages, advocate engagement, fee principles, and judicial procedures.
            </p>
          </div>
        </div>
      </div>
    </section>

    <div class="container" style="padding: var(--space-3xl) 0; max-width: 900px;">
      {''.join(sections_html)}
      <div style="margin-top: 3rem; text-align: center;">
        <p style="font-size: 1.1rem; color: var(--color-text-muted);">Have a specific inquiry not answered here?</p>
        <a href="/legal-consultation/" class="btn btn-primary">Schedule a Detailed Case Consultation →</a>
      </div>
    </div>

    <div class="container" style="padding-bottom: 2rem;">
      {render_disclaimer()}
    </div>
    """

    return get_base_html(title, description, canonical, body, None, config, current_url=canonical)

def render_testimonials_page(config):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    title = f"Client Experiences & Professional Standards | {firm_name}"
    description = "Client experiences and ethical disclosure regarding legal advertising in Nepal. Learn about our commitment to Nepal Bar Council standards and client confidentiality."
    canonical = "/testimonials/"

    crumbs = [("About", "/about/"), ("Professional Standards", "")]

    body = f"""
    {render_breadcrumbs(crumbs)}

    <section class="hero">
      <div class="container">
        <div class="hero-inner">
          <div>
            <div class="hero-badge">Nepal Bar Council Code of Conduct 2051</div>
            <h1 class="hero-title">Client Experiences &amp; Professional Ethics Notice</h1>
            <p class="hero-subtitle">
              Our professional policy regarding client testimonials, legal advertising restrictions, and confidential representation.
            </p>
          </div>
        </div>
      </div>
    </section>

    <div class="container prose" style="padding: var(--space-3xl) 0;">
      <h2>Regulatory Restrictions on Legal Advertising in Nepal</h2>
      <p>
        Under the laws of Nepal—specifically the <strong>Nepal Bar Council Act 2050</strong> and the <strong>Nepal Bar Council Code of Conduct 2051</strong>—advocates and legal firms are strictly prohibited from commercial advertising, solicitations, or disseminating exaggerated claims of judicial success.
      </p>

      <h2>Our Policy on Client Confidentiality</h2>
      <p>
        Legal matters handled by our chambers frequently involve sensitive family disputes, corporate negotiations, or contested property titles. Out of profound respect for client privacy under the <strong>Individual Privacy Act 2075</strong>, our chambers do not publish client names, confidential settlement amounts, or identifying case details.
      </p>

      <h2>Principles of Client Service</h2>
      <ul>
        <li><strong>No False Promises:</strong> We will never guarantee an acquittal, a favorable bail grant, or an assured court verdict. Judicial discretion rests exclusively with the presiding judge.</li>
        <li><strong>Procedural Rigor:</strong> We guarantee diligent research, timely pleading filing within statutory limitation (Hadmyad), and principled courtroom advocacy.</li>
        <li><strong>Fee Transparency:</strong> Retainer terms and court filing expenditures are documented in writing prior to initiating representation.</li>
      </ul>

      <div style="background: var(--color-accent-soft); border-left: 4px solid var(--color-accent); padding: 1.5rem; margin: 2rem 0; border-radius: 0 var(--radius-md) var(--radius-md) 0;">
        <h3 style="margin-top: 0; color: var(--color-primary);">Need an Objective Legal Evaluation?</h3>
        <p style="margin-bottom: 1rem; color: var(--color-dark);">
          To discuss your legal matter under strict advocate-client confidentiality, schedule a consultation with our chambers counsel.
        </p>
        <a href="/legal-consultation/" class="btn btn-primary">Book Consultation →</a>
      </div>

      {render_disclaimer()}
    </div>
    """

    return get_base_html(title, description, canonical, body, None, config, current_url=canonical)

def render_privacy_page(config):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    title = f"Privacy Policy & Client Data Confidentiality | {firm_name}"
    description = "Privacy policy for PATHIVARA LAW FIRM SUNSARI. How we protect client information under the Individual Privacy Act 2075 and professional advocate-client privilege."
    canonical = "/privacy-policy/"

    crumbs = [("Privacy Policy", "")]

    body = f"""
    {render_breadcrumbs(crumbs)}

    <div class="container prose" style="padding: var(--space-3xl) 0;">
      <h1 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 2.25rem;">Privacy Policy &amp; Client Data Protection</h1>
      <p><em>Last Updated: January 2026 | Compliant with Individual Privacy Act 2075 (Nepal)</em></p>

      <p>
        {firm_name} ("we", "our", or "the firm") is committed to safeguarding the privacy and confidentiality of visitors, prospective clients, and retained clients who interact with our website and chambers services.
      </p>

      <h2>1. Legal Framework: Individual Privacy Act 2075</h2>
      <p>
        Our collection, processing, and retention of personal data strictly adhere to the provisions of the <strong>Individual Privacy Act 2075 (२०७५)</strong> of Nepal. Under Nepalese law, personal privacy regarding identity, communication, and legal documents is an inviolable fundamental right guaranteed under Article 28 of the Constitution of Nepal.
      </p>

      <h2>2. Information Collected via Website</h2>
      <p>When you submit a consultation request or contact enquiry through our website, we may collect:</p>
      <ul>
        <li>Your full name and contact information (telephone number, email address).</li>
        <li>The general subject matter or practice area of your inquiry.</li>
        <li>Your preferred format and location for consultation.</li>
      </ul>
      <p>
        We strongly urge users <strong>not</strong> to submit sensitive corporate secrets, confidential financial records, or detailed factual disclosures via unsecured online forms.
      </p>

      <h2>3. Advocate-Client Privilege &amp; Confidentiality</h2>
      <p>
        Upon execution of a formal Vakalatnama and retainer agreement, all communications between the client and our legal team are protected by statutory legal professional privilege under Section 45 of the Evidence Act 2031 (Nepal). Such information will not be disclosed to any third party without explicit client consent, except where mandated by a lawful order of a competent Nepalese court.
      </p>

      <h2>4. Non-Disclosure &amp; Security Measures</h2>
      <p>
        We do not sell, rent, or lease personal or contact data to commercial third parties. All electronic records are protected with industry-standard encryption and access controls.
      </p>

      <h2>5. Contact for Privacy Inquiries</h2>
      <p>
        For inquiries regarding our privacy standards or to request correction of your personal data, contact our chambers data compliance officer at <code>info@pathivaralawfirmsunsari.com</code>.
      </p>

      {render_disclaimer()}
    </div>
    """

    return get_base_html(title, description, canonical, body, None, config, current_url=canonical)

def render_terms_page(config):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    title = f"Terms of Website Use | {firm_name}"
    description = "Terms of website use for PATHIVARA LAW FIRM SUNSARI. Conditions governing access, intellectual property, and jurisdictional applicability in Nepal."
    canonical = "/terms-of-use/"

    crumbs = [("Terms of Use", "")]

    body = f"""
    {render_breadcrumbs(crumbs)}

    <div class="container prose" style="padding: var(--space-3xl) 0;">
      <h1 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 2.25rem;">Terms of Website Use</h1>
      <p><em>Effective Date: January 2026 | Jurisdiction: Nepal</em></p>

      <h2>1. Acceptance of Terms</h2>
      <p>
        By accessing or using this website, you agree to be bound by these Terms of Use and all applicable laws and regulations of Nepal. If you do not agree with any of these terms, you are prohibited from using or accessing this site.
      </p>

      <h2>2. Nature of Online Information</h2>
      <p>
        All articles, guides, statutory references, and explanations published on this website are provided strictly for general public informational and educational purposes in Nepal. <strong>Nothing on this website constitutes formal legal advice.</strong> Laws change frequently, and statutory provisions must be interpreted in light of the specific facts of each case.
      </p>

      <h2>3. No Advocate-Client Relationship Formed</h2>
      <p>
        Accessing this website, reading educational guides, submitting an electronic form, or transmitting an email does not create an advocate-client relationship between you and {firm_name}. Representation is established exclusively upon formal execution of a Vakalatnama and retainer agreement.
      </p>

      <h2>4. Intellectual Property</h2>
      <p>
        All content, articles, design assets, and logos published on this website are the intellectual property of {firm_name} and are protected under the Copyright Act 2059 (Nepal). Reproduction without prior written authorization is prohibited.
      </p>

      <h2>5. Governing Law &amp; Jurisdiction</h2>
      <p>
        These Terms of Use are governed by and construed in accordance with the laws of the Federal Democratic Republic of Nepal. Any dispute arising out of or related to this website shall be subject to the exclusive jurisdiction of the competent courts of Kathmandu, Nepal.
      </p>

      {render_disclaimer()}
    </div>
    """

    return get_base_html(title, description, canonical, body, None, config, current_url=canonical)

def render_disclaimer_page(config):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    title = f"Legal Practice Disclaimer & Bar Council Notice | {firm_name}"
    description = "Legal practice disclaimer for PATHIVARA LAW FIRM SUNSARI. Notice regarding advocate-client privilege, lack of outcome guarantees, and Nepal Bar Council ethics compliance."
    canonical = "/legal-disclaimer/"

    crumbs = [("Legal Practice Disclaimer", "")]

    body = f"""
    {render_breadcrumbs(crumbs)}

    <div class="container prose" style="padding: var(--space-3xl) 0;">
      <h1 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 2.25rem;">Legal Practice Disclaimer &amp; Bar Council Notice</h1>
      <p><em>Nepal Bar Council Code of Conduct 2051 Compliance Disclosure</em></p>

      <div class="legal-notice" style="margin: 2rem 0;">
        <strong>Notice to All Visitors:</strong> The contents of this website are intended solely to provide general legal information and educational materials to the public in Nepal. Reviewing this website or communicating with our chambers electronically does NOT establish an advocate-client relationship.
      </div>

      <h2>1. General Legal Information Only</h2>
      <p>
        Substantive laws, procedural regulations, and limitation periods (Hadmyad) under the Muluki Civil Code 2074, Muluki Criminal Code 2074, and related Nepalese statutes are subject to legislative amendments and ongoing judicial interpretation by the Supreme Court of Nepal. While our research team endeavors to maintain accurate materials, you should never act or refrain from acting based solely on general website articles.
      </p>

      <h2>2. No Advocate-Client Privilege via Electronic Contact</h2>
      <p>
        Transmitting an email, calling our chambers telephone, or submitting an online consultation enquiry does not establish advocate-client privilege. An advocate-client relationship is created only after:
      </p>
      <ul>
        <li>A thorough conflict-of-interest review has been completed by our registry;</li>
        <li>Our advocates have formally agreed to accept representation; and</li>
        <li>A legally binding engagement agreement and formal Vakalatnama (Power of Representation) have been executed in writing.</li>
      </ul>

      <h2>3. Absolute Prohibition of Outcome Guarantees</h2>
      <p>
        In accordance with Rule 32 of the Nepal Bar Council Code of Conduct 2051, advocates are strictly prohibited from guaranteeing judicial outcomes, case dismissals, bail grants, or financial awards. Every legal dispute depends on its specific documentary evidence, witness credibility, and judicial discretion.
      </p>

      <h2>4. Fee Estimates Subject to Statutory Court Rules</h2>
      <p>
        Any discussions of legal expenses or court fees on this site are descriptive only. Official court fees are governed strictly by the <strong>Court Fee Act 2017</strong> (अदालती शुल्क ऐन, २०१७) and procedural rules of the relevant court.
      </p>

      <div style="margin-top: 2.5rem;">
        <a href="/legal-consultation/" class="btn btn-primary">Schedule a Formal Consultation →</a>
        <a href="/contact/" class="btn btn-secondary" style="margin-left: 1rem;">Contact Our Chambers</a>
      </div>
    </div>
    """

    return get_base_html(title, description, canonical, body, None, config, current_url=canonical)

def render_cookie_page(config):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    title = f"Cookie and Tracking Policy | {firm_name}"
    description = "Cookie and tracking policy for PATHIVARA LAW FIRM SUNSARI. How we use local storage, session state, and respect user privacy."
    canonical = "/cookie-policy/"

    crumbs = [("Cookie Policy", "")]

    body = f"""
    {render_breadcrumbs(crumbs)}

    <div class="container prose" style="padding: var(--space-3xl) 0;">
      <h1 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 2.25rem;">Cookie and Tracking Policy</h1>

      <p>
        {firm_name} believes in digital transparency. Our website does not utilize invasive third-party tracking cookies, advertising remarketing pixels, or commercial data profiling.
      </p>

      <h2>1. What Are Cookies?</h2>
      <p>
        Cookies are small text files stored on your browser to facilitate seamless site functionality, navigation preferences, and session security.
      </p>

      <h2>2. What We Use</h2>
      <ul>
        <li><strong>Strictly Necessary Technical Cookies:</strong> Used for accessible navigation state and CSRF security.</li>
        <li><strong>Preference Storage:</strong> Saving user theme or font readability settings in local storage.</li>
        <li><strong>Anonymous Analytics:</strong> Privacy-preserving aggregated traffic metrics without recording IP addresses or personal identifiers.</li>
      </ul>

      <h2>3. Managing Your Browser Cookies</h2>
      <p>
        You can block or delete cookies through your web browser settings. Disabling cookies will not hinder your ability to browse our legal guides or practice area pages.
      </p>

      {render_disclaimer()}
    </div>
    """

    return get_base_html(title, description, canonical, body, None, config, current_url=canonical)

def render_accessibility_page(config):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    title = f"Website Accessibility Statement | {firm_name}"
    description = "Accessibility statement for PATHIVARA LAW FIRM SUNSARI. Our commitment to WCAG 2.1 AA standards, keyboard navigation, and screen reader compatibility."
    canonical = "/accessibility/"

    crumbs = [("Accessibility", "")]

    body = f"""
    {render_breadcrumbs(crumbs)}

    <div class="container prose" style="padding: var(--space-3xl) 0;">
      <h1 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 2.25rem;">Website Accessibility Statement</h1>

      <p>
        {firm_name} is dedicated to ensuring that our digital resources are accessible to individuals of all abilities, including users with visual, auditory, motor, or cognitive disabilities.
      </p>

      <h2>1. Standards &amp; Conformance</h2>
      <p>
        This website is engineered to conform with the <strong>Web Content Accessibility Guidelines (WCAG) 2.1 Level AA</strong> standards. Key features implemented include:
      </p>
      <ul>
        <li><strong>Keyboard Navigation:</strong> All interactive elements, forms, and navigation menus can be operated completely via keyboard (Tab, Enter, Escape).</li>
        <li><strong>Skip to Content Link:</strong> A dedicated skip link allows screen reader and keyboard users to bypass global navigation directly to main content.</li>
        <li><strong>High Contrast Color Palette:</strong> Deep Navy (#0d1b2a) on white/light neutral surfaces exceeds the 4.5:1 contrast ratio required for readable body text.</li>
        <li><strong>Semantic HTML5 Structure:</strong> Proper use of landmarks (<code>&lt;header&gt;</code>, <code>&lt;main&gt;</code>, <code>&lt;footer&gt;</code>, <code>&lt;article&gt;</code>, <code>&lt;section&gt;</code>) and strict logical heading hierarchies (H1 to H3).</li>
        <li><strong>Descriptive Form Labels:</strong> Every input field has explicit label associations and accessible status announcements.</li>
      </ul>

      <h2>2. Feedback &amp; Assistance</h2>
      <p>
        If you experience any accessibility barrier while browsing our site or need assistance with any legal guide, please contact our accessibility coordinator:
      </p>
      <p>
        Email: <code>accessibility@pathivaralawfirmsunsari.com</code><br>
        Chambers Registry: <code>+977 (01) 4XXXXXX</code>
      </p>

      {render_disclaimer()}
    </div>
    """

    return get_base_html(title, description, canonical, body, None, config, current_url=canonical)

def render_sitemap_page(services, articles, config):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    title = f"Complete Website Sitemap & Page Directory | {firm_name}"
    description = "Complete HTML sitemap of PATHIVARA LAW FIRM SUNSARI. Comprehensive hierarchical index of all 10 core service pages, 30 legal guides, and trust pages."
    canonical = "/sitemap/"

    crumbs = [("HTML Sitemap", "")]

    clusters = {}
    for a in articles:
        clusters.setdefault(a.cluster, []).append(a)

    services_li = "".join([f"<li><a href='/services/{s.slug}/'><strong>{s.title}</strong></a> – {s.h1}</li>" for s in services])

    cluster_blocks = []
    for cname, c_articles in clusters.items():
        art_li = "".join([f"<li><a href='/legal-resources/{a.slug}/'>{a.title}</a> (Published: {a.published_date})</li>" for a in c_articles])
        cluster_blocks.append(f"""
        <li>
          <strong>{cname} Practice Cluster ({len(c_articles)} Guides):</strong>
          <ul>{art_li}</ul>
        </li>""")

    body = f"""
    {render_breadcrumbs(crumbs)}

    <section class="hero">
      <div class="container">
        <div class="hero-inner">
          <div>
            <div class="hero-badge">Information Architecture Directory</div>
            <h1 class="hero-title">Complete Website Sitemap</h1>
            <p class="hero-subtitle">
              A comprehensive hierarchical index of all 56 published pages across our core service landing pages, educational resources, and chambers governance.
            </p>
          </div>
        </div>
      </div>
    </section>

    <div class="container" style="padding: var(--space-3xl) 0;">
      <div class="sitemap-section">
        <h2>1. Core Practice Area Landing Pages (10 Money Pages)</h2>
        <ul class="sitemap-list">
          <li><a href="/services/"><strong>All Practice Areas Overview</strong></a></li>
          {services_li}
        </ul>
      </div>

      <div class="sitemap-section">
        <h2>2. Educational Practice Guides &amp; Resources (30 Supporting Articles)</h2>
        <ul class="sitemap-list">
          <li><a href="/legal-resources/"><strong>Legal Resources Knowledge Hub</strong></a></li>
          {''.join(cluster_blocks)}
        </ul>
      </div>

      <div class="sitemap-section">
        <h2>3. Chambers Governance, Team &amp; Compliance Pages (16 Trust Pages)</h2>
        <ul class="sitemap-list">
          <li><a href="/"><strong>Homepage: Specialized Legal Advocacy in Nepal</strong></a></li>
          <li><a href="/about/">About Our Law Firm</a></li>
          <li><a href="/team/">Our Legal Team &amp; Advocates</a>
            <ul>
              <li><a href="/team/senior-advocate-profile/">Senior Legal Counsel &amp; Managing Advocate Profile</a></li>
            </ul>
          </li>
          <li><a href="/legal-consultation/">Schedule a Structured Legal Consultation</a></li>
          <li><a href="/contact/">Contact Our Law Chambers (Kathmandu &amp; Koshi)</a></li>
          <li><a href="/faqs/">Frequently Asked Questions (FAQs)</a></li>
          <li><a href="/testimonials/">Client Experiences &amp; Ethics Notice</a></li>
          <li><a href="/privacy-policy/">Privacy Policy &amp; Client Data Confidentiality</a></li>
          <li><a href="/terms-of-use/">Terms of Website Use</a></li>
          <li><a href="/legal-disclaimer/">Legal Practice Disclaimer &amp; Bar Council Notice</a></li>
          <li><a href="/cookie-policy/">Cookie and Tracking Policy</a></li>
          <li><a href="/accessibility/">Website Accessibility Statement</a></li>
          <li><a href="/sitemap/">HTML Sitemap &amp; Directory</a></li>
        </ul>
      </div>
    </div>

    <div class="container" style="padding-bottom: 2rem;">
      {render_disclaimer()}
    </div>
    """

    return get_base_html(title, description, canonical, body, None, config, current_url=canonical)

def render_404_page(config):
    firm_name = config.get("firm_name", "PATHIVARA LAW FIRM SUNSARI")
    title = f"Page Not Found (404) | {firm_name}"
    description = "The requested page could not be located. Browse our practice areas, legal guides, or contact our chambers registry."
    canonical = "/404.html"

    body = f"""
    <section class="hero" style="min-height: 60vh; display: flex; align-items: center;">
      <div class="container" style="text-align: center;">
        <div class="hero-badge">Status 404: Page Not Found</div>
        <h1 class="hero-title" style="font-size: 2.75rem; margin-top: 1rem;">The Requested Resource Does Not Exist</h1>
        <p class="hero-subtitle" style="margin: 1rem auto 2rem auto; max-width: 600px;">
          The legal article, practice charter, or resource you are searching for may have been relocated or updated under our semantic architecture.
        </p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
          <a href="/" class="btn btn-primary">Return to Homepage</a>
          <a href="/services/" class="btn btn-secondary">Explore Practice Areas</a>
          <a href="/legal-resources/" class="btn btn-outline">Search Legal Guides</a>
          <a href="/contact/" class="btn btn-outline">Contact Chambers Registry</a>
        </div>
      </div>
    </section>
    """

    return get_base_html(title, description, canonical, body, None, config, current_url=canonical)
