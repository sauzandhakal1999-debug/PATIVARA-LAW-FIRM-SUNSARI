# Article and Legal Resources page renderers for Pathivara Law Firm Itahari
from src.data.articles import ArticlePage
from builder.templates import (
    get_base_html, render_breadcrumbs, render_checklist, render_faq_accordion,
    render_author_box, render_disclaimer, render_cta_banner
)

def render_article_page(article: ArticlePage, config: dict):
    firm_name = config.get("firm_name", "Pathivara Law Firm Itahari")
    site_url = config.get("site_url", "https://www.pathivaralawfirmitahari.com")
    canonical = f"/legal-resources/{article.slug}/"

    crumbs = [
        ("Legal Resources", "/legal-resources/"),
        (article.title, "")
    ]

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "@id": f"{site_url}{canonical}#article",
                "headline": article.h1,
                "description": article.meta_description,
                "datePublished": f"{article.published_date}T09:00:00+05:45",
                "dateModified": f"{article.updated_date}T10:00:00+05:45",
                "author": {
                    "@type": "Person",
                    "name": "Legal Research Department",
                    "affiliation": firm_name
                },
                "publisher": {
                    "@type": "LegalService",
                    "name": firm_name,
                    "url": site_url
                },
                "mainEntityOfPage": f"{site_url}{canonical}"
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{site_url}{canonical}#breadcrumbs",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": site_url},
                    {"@type": "ListItem", "position": 2, "name": "Legal Resources", "item": f"{site_url}/legal-resources/"},
                    {"@type": "ListItem", "position": 3, "name": article.title, "item": f"{site_url}{canonical}"}
                ]
            }
        ]
    }

    takeaways_html = "".join([f"<li>{kt}</li>" for kt in article.key_takeaways])

    statute_rows = []
    for sc in article.statutory_citations:
        statute_rows.append(f"""
        <tr>
          <td><strong>{sc.get('act', '')}</strong></td>
          <td><code>{sc.get('section', '')}</code></td>
          <td>{sc.get('relevance', '')}</td>
        </tr>""")

    rel_html = []
    for ra in article.related_articles:
        rel_html.append(f"""
        <div style="background: #f8fafc; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 1.25rem;">
          <h4 style="font-size: 1.05rem; margin-bottom: 0.5rem;"><a href="{ra['url']}">{ra['title']}</a></h4>
          <span style="font-size: 0.85rem; color: var(--color-accent-hover); font-weight: 600;">Read Related Guide →</span>
        </div>""")

    faq_items = [(f.question, f.answer) for f in article.faqs]

    body = f"""
    {render_breadcrumbs(crumbs)}

    <article style="padding: var(--space-2xl) 0 var(--space-3xl) 0;">
      <div class="container prose">
        
        <header style="margin-bottom: 2rem;">
          <span class="badge badge-primary" style="margin-bottom: 0.75rem;">{article.cluster} Practice Guide</span>
          <h1 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 2.35rem; line-height: 1.25; margin-bottom: 1rem;">
            {article.h1}
          </h1>
          
          <div class="article-meta-bar">
            <div class="article-meta-item">📅 Published: {article.published_date}</div>
            <div class="article-meta-item">🔄 Updated: {article.updated_date}</div>
            <div class="article-meta-item">⏱ {article.reading_time}</div>
            <div class="article-meta-item">🔍 Review: {article.reviewed_by}</div>
          </div>
        </header>

        <div class="direct-answer-box" role="region" aria-label="Summary Answer">
          <div class="direct-answer-label">Direct Legal Answer &amp; Overview</div>
          <p class="direct-answer-text">{article.summary_direct_answer}</p>
        </div>

        <div class="key-takeaways">
          <h3>Key Practical Takeaways</h3>
          <ul>{takeaways_html}</ul>
        </div>

        <div class="article-body-content" style="line-height: 1.8; font-size: 1.05rem; color: var(--color-text);">
          {article.content_html}
        </div>

        <section style="margin: 2.5rem 0;">
          <h3 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 1.45rem; margin-bottom: 1rem;">
            Statutory Citations &amp; Governing Nepal Legislation
          </h3>
          <div class="comparison-container">
            <table class="statute-table">
              <thead>
                <tr>
                  <th>Statute / Act</th>
                  <th>Section / Rule</th>
                  <th>Legal Significance</th>
                </tr>
              </thead>
              <tbody>{''.join(statute_rows)}</tbody>
            </table>
          </div>
        </section>

        <section style="margin: 2.5rem 0;">
          {render_checklist("Documentary Checklist for this Procedure", article.document_checklist)}
        </section>

        <aside class="parent-service-banner" role="complementary">
          <div>
            <h3>Need Professional Legal Representation in {article.parent_service_name}?</h3>
            <p>Our admitted advocates represent clients before District Courts, High Courts, and judicial registries across Nepal.</p>
          </div>
          <a href="{article.parent_service_url}" class="btn btn-primary" style="white-space: nowrap;">Explore Service Charter →</a>
        </aside>

        <section style="margin: 2.5rem 0;">
          <h3 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 1.45rem; margin-bottom: 1rem;">
            Frequently Asked Questions on this Topic
          </h3>
          {render_faq_accordion(faq_items)}
        </section>

        <section style="margin: 2.5rem 0;">
          <h3 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 1.45rem; margin-bottom: 1rem;">
            Related Educational Guides in {article.cluster}
          </h3>
          <div class="grid grid-2">{''.join(rel_html)}</div>
        </section>

        {render_author_box()}
        {render_disclaimer()}

      </div>
    </article>
    """

    return get_base_html(article.meta_title, article.meta_description, canonical, body, schema, config, current_url=canonical)

def render_resources_index(articles, config):
    title = "Legal Resources, Guides & Statutory Insights in Nepal | Pathivara Law Firm Itahari"
    description = "Browse 30 in-depth legal guides and procedural breakdowns across Nepalese civil litigation, criminal defence, divorce law, property verification, and corporate compliance."
    canonical = "/legal-resources/"
    site_url = config.get("site_url", "https://www.pathivaralawfirmitahari.com")

    crumbs = [("Legal Resources", "")]

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
                    {"@type": "ListItem", "position": 2, "name": "Legal Resources", "item": f"{site_url}/legal-resources/"}
                ]
            }
        ]
    }

    clusters = {}
    for a in articles:
        clusters.setdefault(a.cluster, []).append(a)

    cluster_sections = []
    for cname, c_articles in clusters.items():
        cards = []
        for a in c_articles:
            cards.append(f"""
            <article class="card">
              <h3 class="card-title" style="font-size: 1.15rem;"><a href="/legal-resources/{a.slug}/">{a.title}</a></h3>
              <p class="card-body" style="font-size: 0.925rem;">{a.summary_direct_answer[:140]}...</p>
              <div style="margin-top: 1rem; display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; color: var(--color-text-muted);">
                <span>⏱ {a.reading_time}</span>
                <a href="/legal-resources/{a.slug}/" class="card-link">Read Guide →</a>
              </div>
            </article>""")

        cluster_sections.append(f"""
        <section style="margin-bottom: var(--space-3xl);">
          <div style="display: flex; justify-content: space-between; align-items: baseline; border-bottom: 2px solid var(--color-accent); padding-bottom: 0.5rem; margin-bottom: 1.5rem;">
            <h2 style="font-family: var(--font-serif); color: var(--color-primary); font-size: 1.65rem; margin: 0;">
              {cname} Guides ({len(c_articles)} Articles)
            </h2>
            <span style="font-size: 0.875rem; color: var(--color-text-muted);">Muluki Codification &amp; Procedural Rules</span>
          </div>
          <div class="grid grid-3">{''.join(cards)}</div>
        </section>""")

    body = f"""
    {render_breadcrumbs(crumbs)}

    <section class="hero">
      <div class="container">
        <div class="hero-inner">
          <div>
            <div class="hero-badge">Public Legal Education &amp; Statutory Guidance</div>
            <h1 class="hero-title">Nepalese Legal Resources &amp; Practice Guides</h1>
            <p class="hero-subtitle">
              Researched and reviewed by admitted advocates. 30 comprehensive, plain-language guides explaining court proceedings, statutory rights, land due diligence, and company compliance in Nepal.
            </p>
          </div>
        </div>
      </div>
    </section>

    <div class="container" style="padding: var(--space-3xl) 0;">
      {''.join(cluster_sections)}
    </div>

    <div class="container">
      {render_cta_banner("Your Case Specifics", "Educational articles provide general clarity. For individualized case assessment, schedule an advocate consultation.")}
    </div>

    <div class="container" style="padding: 1.5rem 0;">
      {render_disclaimer()}
    </div>
    """

    return get_base_html(title, description, canonical, body, schema, config, current_url=canonical)
