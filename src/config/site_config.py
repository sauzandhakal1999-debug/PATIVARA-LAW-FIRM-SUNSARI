"""Central Business Configuration for PATHIVARA LAW FIRM SUNSARI.

All business information, locations, contact details, and compliance data
are stored here. Changing values here updates the entire website uniformly.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class OfficeLocation:
    city: str
    province: str
    address: str
    is_primary: bool = False
    phone: str = ""
    email: str = ""
    map_url: str = ""
    court_jurisdictions: List[str] = field(default_factory=list)

@dataclass
class SiteConfig:
    # 1. Firm Identity
    firm_name: str = "PATHIVARA LAW FIRM SUNSARI"
    firm_name_ne: str = "पाथीभरा कानून व्यवसायी फर्म सुनसरी"
    tagline: str = "Specialized Legal Advocacy, Advisory & Dispute Resolution in Sunsari & Koshi Province"
    founding_year: str = "[CONFIGURABLE: 2015]"
    site_url: str = "https://www.pathivaralawfirmsunsari.com"
    default_locale: str = "en_NP"
    jurisdiction: str = "Federal Democratic Republic of Nepal"

    # 2. Primary Contact & Locations
    primary_phone: str = "9745875449 / 9852057087"
    primary_email: str = "sauzandhakal1999@gmail.com"
    consultation_email: str = "sauzandhakal1999@gmail.com"
    emergency_phone: str = "+977-9852057087"
    office_hours: str = "Monday – Friday: 9:30 AM – 5:00 PM (Closed Saturdays, Sundays & Public Holidays)"
    whatsapp_number: str = "+9779852057087"

    # Locations
    offices: List[OfficeLocation] = field(default_factory=lambda: [
        OfficeLocation(
            city="Inaruwa",
            province="Koshi Province",
            address="Adalat Road, Inaruwa, Sunsari, Nepal",
            is_primary=True,
            phone="9745875449 / 9852057087",
            email="sauzandhakal1999@gmail.com",
            court_jurisdictions=["Sunsari District Court (Inaruwa)", "Morang District Court", "High Court Biratnagar", "Supreme Court of Nepal"]
        ),
        OfficeLocation(
            city="Itahari",
            province="Koshi Province",
            address="Itahari-4 (Bagaicha Tole), Sunsari, Nepal",
            is_primary=False,
            phone="+977-9852059106",
            email="sauzandhakal1999@gmail.com",
            court_jurisdictions=["High Court Biratnagar", "Sunsari District Court (Inaruwa)", "Morang District Court"]
        )
    ])

    secondary_service_areas: List[str] = field(default_factory=lambda: [
        "Inaruwa (Sunsari District Court)", "Biratnagar (High Court Biratnagar)", "Dharan", "Damak", "Kathmandu"
    ])

    # 3. Bar Registration & Professional Compliance (Nepal Bar Council)
    bar_council_reg: str = "[VERIFIED_BAR_REG: Nepal Bar Council Reg. No. / Sunsari District Bar]"
    supreme_court_bar_membership: str = "[VERIFIED_BAR: Supreme Court Bar Association Member]"
    high_court_bar_membership: str = "[VERIFIED_BAR: High Court Bar Association Biratnagar Member]"

    # 4. Strict Legal Ethics Disclaimers (Nepal Bar Council Code of Ethics Compliance)
    disclaimer_text: str = (
        "General Legal Information Disclaimer: The materials and content on this website are provided for "
        "informational and educational purposes only and do not constitute formal legal advice, solicitation, "
        "or an advertisement. Accessing this site, reading articles, or transmitting an enquiry does not create "
        "an advocate-client relationship. You should consult a licensed advocate in Nepal regarding your specific legal situation."
    )

    no_outcome_guarantee_notice: str = (
        "In accordance with Nepal Bar Council ethical regulations, our firm strictly does not guarantee specific "
        "judicial outcomes, bail grants, court decrees, or case settlements. Every legal matter depends entirely "
        "upon its individual facts, applicable statutory provisions, and judicial discretion."
    )

    items_flagged_for_verification: List[Dict[str, str]] = field(default_factory=lambda: [
        {"item": "Official Firm Registered Name", "status": "PATHIVARA LAW FIRM SUNSARI", "action": "Confirm exact name registered with Nepal Bar Council / OCR"},
        {"item": "Primary Physical Office Address", "status": "Sunsari (Inaruwa / Itahari) Main Road", "action": "Verify ward number, street name, and GPS coordinates"},
        {"item": "Official Telephone & Mobile Numbers", "status": "+977 (025) 580000", "action": "Insert verified landline and consultation mobile"},
        {"item": "Advocate License Numbers", "status": "Placeholder Used", "action": "Provide verified Nepal Bar Council certificates"},
        {"item": "Court Fee Estimates", "status": "Descriptive Only", "action": "Subject to Court Fee Act 2017 & Muluki Civil Procedure Rules"}
    ])

SITE = SiteConfig()
