"""Central Frequently Asked Questions (FAQs) Repository for Nepal Law Firm."""

from dataclasses import dataclass
from typing import List, Dict

@dataclass
class FAQItem:
    question: str
    answer: str
    category: str
    related_service_url: str = ""

GLOBAL_FAQS: List[FAQItem] = [
    FAQItem(
        question="How do I schedule an initial legal consultation in Nepal?",
        answer="You can schedule an initial consultation by calling our office (+977-1-4240000), using the confidential consultation request form on our website, or emailing consult@pathivaralawfirmsunsari.com. We offer in-person consultations at our Kathmandu and Itahari offices, as well as secure virtual consultations via Google Meet or Zoom for clients outside these cities or residing abroad.",
        category="General & Consultation",
        related_service_url="/legal-consultation/"
    ),
    FAQItem(
        question="Does submitting an enquiry or reading this website establish an advocate-client relationship?",
        answer="No. Under Nepal Bar Council professional ethics rules, accessing this website, reading our educational resources, or transmitting an electronic enquiry does not create an advocate-client relationship. A formal relationship is created only after an initial conflict check is completed and a formal vakalatnama (power of attorney/engagement agreement) is executed.",
        category="General & Consultation",
        related_service_url="/legal-disclaimer/"
    ),
    FAQItem(
        question="What documents should I bring to my first legal consultation?",
        answer="You should bring government-issued photo identification (Citizenship Certificate or Passport), all original or clear photocopies of relevant contracts, notices, court orders, property documents (such as Lalpurja or blue prints), police reports, and a concise chronological summary of the facts and key dates involved in your matter.",
        category="General & Consultation",
        related_service_url="/legal-consultation/"
    ),
    FAQItem(
        question="What are the typical stages of a civil lawsuit in Nepal District Courts?",
        answer="A civil lawsuit under the Muluki Civil Procedure Code 2074 generally follows six stages: 1) Filing of the Plaint (Firdi-patra); 2) Service of Notice / Summons (Myad Jari) to the opposing party; 3) Filing of Written Statement of Defence (Pratiuttar-patra); 4) Evidence Submission & Witness Examination (Praman Parikshan); 5) Final Legal Arguments (Bahas); and 6) Judgment (Faisala) and Decree Execution (Faisala Karyanvayan).",
        category="Civil Litigation",
        related_service_url="/services/civil-litigation/"
    ),
    FAQItem(
        question="Can criminal charges or police complaints be settled out of court in Nepal?",
        answer="In Nepal, criminal offenses are strictly divided into State-prosecuted offenses (Government of Nepal is the plaintiff under Schedule 1 of the National Criminal Procedure Code 2074) and Individual-party offenses (Schedule 2/3). State offenses such as fraud, forgery, homicide, and narcotics cannot be legally settled privately. Minor individual offenses or civil-nature disputes may be eligible for statutory reconciliation (Milapatra) where specifically authorized by law.",
        category="Criminal Law",
        related_service_url="/services/criminal-law/"
    ),
    FAQItem(
        question="How long does a mutual consent divorce take in Nepal?",
        answer="Under the Muluki Civil Code 2074, a mutual consent divorce filed jointly by both husband and wife before the competent District Court can typically be concluded within 2 to 5 working days, provided all settlement terms regarding property partition, custody, and maintenance are agreed upon and both parties appear before the judge to record their statements.",
        category="Family Law",
        related_service_url="/services/family-law/"
    ),
    FAQItem(
        question="How can I verify whether a land parcel in Nepal is free of legal disputes or encumbrances?",
        answer="To verify land title in Nepal: 1) Verify the original Land Ownership Registration Certificate (Lalpurja); 2) Inspect the official Field Book, Plot Map (Napi Naksa), and Shrestha register at the Land Revenue Office (Malpot Karyalaya); 3) Obtain a formal Rokka (encumbrance/mortgage freeze) search certificate from the Malpot Office to confirm no bank liens or court injunctions exist; and 4) Confirm that the land is not reserved as Guthi or government forest land.",
        category="Property & Land Law",
        related_service_url="/services/property-land-law/"
    ),
    FAQItem(
        question="What is the legal difference between registering a Private Limited Company and a Sole Proprietorship in Nepal?",
        answer="A Private Limited Company (registered at the Office of Company Registrar under the Companies Act 2063) is a separate legal entity with perpetual succession and limited liability, meaning shareholders' personal assets are shielded from business liabilities. A Sole Proprietorship (registered at the Department of Commerce or local municipal ward) has no separate corporate personality, and the owner possesses unlimited personal liability for business debts.",
        category="Corporate & Business Law",
        related_service_url="/services/corporate-business-law/"
    ),
    FAQItem(
        question="What remedies exist if someone issues a cheque that bounces due to insufficient funds in Nepal?",
        answer="Victims of bounced cheques in Nepal possess two alternative legal remedies: 1) A civil recovery suit under the Negotiable Instruments Act 2034 for the principal amount plus statutory interest; or 2) A criminal complaint under the Banking Offence and Punishment Act 2064, which involves Nepal Police Central Investigation Bureau (CIB) investigation, criminal trial at the High Court Commercial Bench, imprisonment, and full restitution.",
        category="Banking & Finance",
        related_service_url="/services/banking-financial-law/"
    ),
    FAQItem(
        question="Do lawyers in Nepal guarantee case results or winning verdicts?",
        answer="No. The Nepal Bar Council Code of Conduct strictly prohibits advocates from guaranteeing any judicial outcome, bail verdict, court order, or financial recovery. Legal practitioners provide professional assessment, procedural representation, and diligent advocacy, but decisions rest exclusively with the presiding judicial bench.",
        category="Legal Ethics & Compliance",
        related_service_url="/legal-disclaimer/"
    )
]
