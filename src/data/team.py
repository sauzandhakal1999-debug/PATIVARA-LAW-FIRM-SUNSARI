"""Team and Lawyer Profiles Data for Nepal Law Firm."""

from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class LawyerProfile:
    slug: str
    name: str
    name_ne: str
    role: str
    qualifications: str
    bar_council_reg: str
    court_admissions: List[str]
    practice_areas: List[str]
    bio: str
    languages: List[str]
    experience_summary: str
    publications: List[str]
    email: str
    phone: str
    is_lead: bool = False

TEAM_MEMBERS: List[LawyerProfile] = [
    LawyerProfile(
        slug="senior-advocate-lead",
        name="[VERIFIED_NAME: Senior Advocate Lead Counsel]",
        name_ne="वरिष्ठ अधिवक्ता मुख्य सल्लाहकार",
        role="Founding Partner & Senior Advocate",
        qualifications="LL.M. in Commercial & Procedural Law (Tribhuvan University), LL.B.",
        bar_council_reg="[VERIFIED_REG: Nepal Bar Council Advocate Reg. No. 12450]",
        court_admissions=[
            "Supreme Court of Nepal",
            "High Court Patan & Biratnagar",
            "Special Court (Kathmandu)",
            "District Courts of Nepal"
        ],
        practice_areas=[
            "Civil Litigation & Commercial Disputes",
            "Criminal Defence & Constitutional Law",
            "Property & Land Title Disputes",
            "Corporate Governance & FDI"
        ],
        bio=(
            "Admitted to the Nepal Bar Council with extensive courtroom advocacy experience across District Courts, "
            "High Courts, and the Supreme Court of Nepal. Focuses on complex commercial disputes, constitutional petitions, "
            "and sensitive property litigation. Regularly advises domestic enterprises and non-resident Nepalese on cross-border "
            "investments, inheritance disputes, and civil remedies under the Muluki Codes 2074."
        ),
        languages=["English", "Nepali (नेपाली)", "Bhojpuri", "Hindi"],
        experience_summary="Over 15 years of courtroom practice and institutional legal advisory across Kathmandu and Koshi Province.",
        publications=[
            "Procedural Evolution of Injunctions under Muluki Civil Procedure Code 2074 (Nepal Bar Council Journal)",
            "Corporate Governance & Fiduciary Liabilities in Closely Held Companies (Nepal Law Review)",
            "Due Diligence Standards in Real Estate Acquisitions in Nepal (Commercial Law Journal)"
        ],
        email="lead.counsel@pathivaralawfirmitahari.com",
        phone="+977-1-4240000",
        is_lead=True
    ),
    LawyerProfile(
        slug="advocate-associate-corporate",
        name="[VERIFIED_NAME: Managing Associate Advocate]",
        name_ne="अधिवक्ता प्रबन्ध सहयोगी",
        role="Partner - Corporate & Commercial Practice",
        qualifications="B.A. LL.B. (Hons.) (Kathmandu School of Law), Master of Commercial Law",
        bar_council_reg="[VERIFIED_REG: Nepal Bar Council Advocate Reg. No. 18230]",
        court_admissions=[
            "High Court Patan",
            "Kathmandu District Court",
            "Labour Court",
            "Debt Recovery Tribunal (DRT)"
        ],
        practice_areas=[
            "Corporate Registration & Compliance",
            "Employment & Labour Law (Labour Act 2074)",
            "Commercial Contracts & NDAs",
            "Banking & Cheque Dishonor Proceedings"
        ],
        bio=(
            "Focuses on corporate setup, foreign direct investment approvals, regulatory compliance with the Office of "
            "Company Registrar (OCR) and Department of Industry, and complex contract negotiation. Also leads the firm's "
            "employment law practice, representing both corporate employers and management before the Labour Court."
        ),
        languages=["English", "Nepali (नेपाली)", "Maithili"],
        experience_summary="Over 9 years of transactional advisory, regulatory filings, and tribunal advocacy.",
        publications=[
            "Labour Act 2074 & Social Security Compliance: Practical Guidelines for Employers",
            "Negotiable Instruments Act vs. Banking Offence Act: Navigating Cheque Dishonor Remedies in Nepal"
        ],
        email="corporate@pathivaralawfirmitahari.com",
        phone="+977-1-4240001",
        is_lead=False
    )
]
