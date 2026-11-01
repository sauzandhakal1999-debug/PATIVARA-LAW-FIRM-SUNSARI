"""Comprehensive Core Money Pages Data for Nepal Law Firm Website.
Contains full structured content for all 10 services satisfying all 22 required sections.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class ServiceStage:
    step_number: int
    title: str
    description: str
    duration_estimate: str

@dataclass
class ServiceFAQ:
    question: str
    answer: str

@dataclass
class ServicePage:
    slug: str
    title: str
    h1: str
    meta_title: str
    meta_description: str
    service_code: str
    short_intro: str
    hero_badge: str
    hero_image: str
    legal_problem_overview: str
    relevant_situations: List[str]
    scope_of_assistance: List[str]
    stages: List[ServiceStage]
    required_documents: List[str]
    governing_laws: List[Dict[str, str]]
    rights_duties_limitations: List[str]
    fee_factors: List[str]
    consultation_preparation: List[str]
    faqs: List[ServiceFAQ]
    related_articles: List[Dict[str, str]]
    adjacent_services: List[Dict[str, str]]
    lead_advocate_slug: str
    trust_signals: List[str]
    conversion_prompt: str

SERVICES: List[ServicePage] = [
    ServicePage(
        slug="civil-litigation",
        title="Civil Litigation & Dispute Resolution",
        h1="Civil Litigation & Dispute Resolution Legal Services in Nepal",
        meta_title="Civil Litigation & Dispute Resolution Lawyers in Nepal | PATHIVARA LAW FIRM SUNSARI",
        meta_description="Experienced civil litigation advocates in Nepal handling contract disputes, recovery claims, property civil suits, and court injunctions in District and High Courts.",
        service_code="CIVIL-01",
        short_intro=(
            "We provide robust, strategic representation in civil disputes across District Courts, High Courts, "
            "and the Supreme Court of Nepal. Our civil litigation practice helps individuals, property owners, and businesses "
            "assert legal rights, recover monetary claims, obtain urgent court injunctions, and defend against civil claims "
            "under the National Civil Code and Civil Procedure Code 2074."
        ),
        hero_badge="District, High & Supreme Court Representation",
        hero_image="/assets/images/civil-litigation-nepal.svg",
        legal_problem_overview=(
            "Civil disputes in Nepal frequently arise from breached commercial agreements, contested land ownership, "
            "unpaid monetary dues, or boundary trespass. When informal negotiations fail, procedural rigor in court is essential. "
            "The Muluki Civil Procedure Code 2074 strictly enforces rigid limitation periods (Hadmyad), mandatory pleading standards, "
            "and formal rules of evidence. Missing a procedural deadline or failing to present admissible evidence at the initial "
            "plaint stage can permanently prejudice your legal remedy."
        ),
        relevant_situations=[
            "Commercial contract breaches, supplier non-performance, and partnership fallout",
            "Monetary recovery suits under promissory notes (Tamassuk), loan acknowledgments, or commercial invoices",
            "Contested immovable property title, unlawful dispossession, and boundary encroachment",
            "Urgent applications for interim orders and prohibitory injunctions (Nishedhajna / Antarim Aadesh)",
            "Execution of court judgments (Faisala Karyanvayan) and auction enforcement",
            "Appeals (Punaravedan) against District Court decisions before the High Court and Supreme Court"
        ],
        scope_of_assistance=[
            "Thorough procedural and evidentiary case merits assessment prior to institution of litigation",
            "Drafting of formal legal notices (such as demand notices and cure-period warnings)",
            "Drafting and filing of comprehensive Plaints (Firdi-patra) and Petitions before competent courts",
            "Formulation and filing of Written Statements of Defence (Pratiuttar-patra) within statutory limitation periods",
            "Representation during interlocutory hearings, injunction arguments, and discovery of evidence",
            "Witness preparation, evidence examination (Praman Parikshan), and cross-examination in open court",
            "Substantive final arguments (Bahas) before judicial benches across Kathmandu, Lalitpur, Bhaktapur, and Sunsari",
            "Enforcement of court decrees, recovery execution, and post-judgment asset attachment"
        ],
        stages=[
            ServiceStage(
                step_number=1,
                title="Case Assessment & Limitation Review",
                description="We review all agreements, receipts, title documents, and communications to calculate applicable statutory limitation periods (Hadmyad) under the Muluki Civil Procedure Code 2074.",
                duration_estimate="2 – 5 Working Days"
            ),
            ServiceStage(
                step_number=2,
                title="Pre-Litigation Notice & Pleadings Formulation",
                description="Issuing formal legal demand notices and formulating the formal Plaint (Firdi-patra) or Defence (Pratiuttar-patra), supported by documentary exhibits and court fee calculations.",
                duration_estimate="1 – 2 Weeks"
            ),
            ServiceStage(
                step_number=3,
                title="Filing, Summons & Interlocutory Relief",
                description="Lodging the case at court, obtaining registration (Darta), securing service of judicial summons (Myad Tameli) upon the opponent, and arguing urgent applications for interim injunctions.",
                duration_estimate="2 – 6 Weeks"
            ),
            ServiceStage(
                step_number=4,
                title="Evidence Submission & Witness Examination",
                description="Presenting certified original documents, summoning official government records from Land Revenue or Municipal offices, and examining witnesses before the registrar or judge.",
                duration_estimate="3 – 9 Months"
            ),
            ServiceStage(
                step_number=5,
                title="Final Arguments, Judgment & Decree Enforcement",
                description="Delivering formal legal oral arguments (Bahas) grounded in Nepalese statutory codes and Supreme Court precedents, obtaining the final judgment (Faisala), and executing the decree.",
                duration_estimate="1 – 4 Months post-trial"
            )
        ],
        required_documents=[
            "Original or notarized contracts, agreements, promissory notes (Tamassuk), or purchase orders",
            "Official Land Ownership Certificate (Lalpurja), Blue Print, and tax payment receipts (for land suits)",
            "Bank statements, payment vouchers, swift receipts, or audit reports evidencing debt or transaction",
            "All exchanged notices, letters, emails, SMS/messaging records, and proof of postage/delivery",
            "Copy of Nepali Citizenship Certificate (Nagrikta) or Company Registration Certificate & Board Resolution"
        ],
        governing_laws=[
            {"act": "Muluki Civil Code 2074 (मुलुकी देवानी संहिता, २०७४)", "relevance": "Substantive principles of contracts, property ownership, torts, and civil obligations"},
            {"act": "Muluki Civil Procedure Code 2074 (मुलुकी देवानी कार्यविधि संहिता, २०७४)", "relevance": "Court procedure, jurisdiction, limitation periods, injunctions, and execution of decrees"},
            {"act": "Court Fee Act 2017 (कोर्ट फी ऐन, २०१७)", "relevance": "Statutory court fee scales required for money claims and property valuations"},
            {"act": "Evidence Act 2031 (प्रमाण ऐन, २०३१)", "relevance": "Admissibility, burden of proof, electronic records, and witness testimony standards"}
        ],
        rights_duties_limitations=[
            "Limitation Period Caution: Most civil claims under Nepalese law carry strict statutory limitation periods (commonly ranging between 6 months to 2 years from cause of action); delay may extinguish the legal remedy.",
            "Mandatory Court Fees: Civil plaints claiming monetary damages require upfront payment of graduated court fees under the Court Fee Act 2017.",
            "Compulsory Mediation Referral: Under the Muluki Civil Procedure Code 2074, courts actively refer appropriate civil disputes to court-annexed mediation before commencing full trial.",
            "Burden of Proof: The party alleging a civil fact carries the primary legal burden to establish it through admissible documentary proof or credible testimony under the Evidence Act 2031."
        ],
        fee_factors=[
            "Complexity of the factual dispute, volume of documentation, and number of opposing parties",
            "Judicial level of the forum (District Court, High Court bench, Supreme Court, or Special Tribunal)",
            "Need for urgent interim relief applications, court commissions, or external expert testimony",
            "Statutory court fees, process server fees, and stamp duties mandated by Nepalese court regulations",
            "Whether representation is structured on a per-stage retainer or comprehensive matter agreement"
        ],
        consultation_preparation=[
            "Prepare a 1-page chronological timeline listing dates, interactions, agreements, and breaches",
            "Assemble all relevant agreements, correspondence, and payment proofs in chronological sequence",
            "Formulate a clear statement of your primary objective (e.g. monetary recovery, contract cancellation, property possession, or injunction)",
            "Identify the full names, registered addresses, and contact details of all adverse parties"
        ],
        faqs=[
            ServiceFAQ(
                question="What is the difference between a temporary injunction and a permanent injunction in Nepal?",
                answer="Under Chapter 13 of the Muluki Civil Procedure Code 2074, an interim or temporary injunction (Antarim Aadesh) is granted during ongoing litigation to preserve the status quo and prevent irreparable harm before trial concludes. A permanent injunction (Nishedhajna) is a final judicial decree awarded at judgment, permanently restraining the opposing party from violating the plaintiff legal rights."
            ),
            ServiceFAQ(
                question="Can a civil dispute in Nepal be referred to mediation during court proceedings?",
                answer="Yes. Under Section 193 of the Muluki Civil Procedure Code 2074 and the Mediation Act 2068, courts in Nepal have a statutory obligation to encourage parties to resolve civil disputes through court-annexed mediation. If a settlement (Milapatra) is reached, it is recorded as a binding court decree with no further appeal."
            ),
            ServiceFAQ(
                question="What happens if the defendant refuses to receive court summons (Myad)?",
                answer="Under Nepalese civil procedure, if a defendant evades personal service, the court process server (Tameldar) executes service by pasting the summons at the defendant official residence or municipal ward office in the presence of local ward representatives and witnesses (Riti Purvak Myad Tameli). Once executed, the notice is legally deemed served."
            ),
            ServiceFAQ(
                question="How long does a civil suit take from filing to judgment in District Courts?",
                answer="While statutory guidelines contemplate resolution within one year, contested civil cases in busy jurisdictions (such as Kathmandu or Sunsari) typically span between 10 to 24 months, depending on interlocutory appeals, court attendance, witness availability, and court dockets."
            )
        ],
        related_articles=[
            {"title": "What is a Civil Case under Nepalese Law?", "url": "/legal-resources/what-is-a-civil-case-nepal/"},
            {"title": "Stages of a Civil Lawsuit in District and High Courts of Nepal", "url": "/legal-resources/stages-of-civil-lawsuit-nepal/"},
            {"title": "Key Documents to Prepare Before Consulting a Civil Lawyer", "url": "/legal-resources/documents-to-prepare-civil-lawyer-nepal/"},
            {"title": "Mediation vs. Civil Litigation in Nepal: Key Differences", "url": "/legal-resources/mediation-vs-civil-litigation-nepal/"},
            {"title": "Injunctions under Nepalese Civil Procedure: Types & Procedures", "url": "/legal-resources/injunctions-under-nepal-civil-procedure/"}
        ],
        adjacent_services=[
            {"title": "Contract Drafting & Review", "url": "/services/contract-law/"},
            {"title": "Property & Land Law", "url": "/services/property-land-law/"},
            {"title": "Mediation & Alternative Dispute Resolution", "url": "/services/mediation-dispute-resolution/"}
        ],
        lead_advocate_slug="senior-advocate-lead",
        trust_signals=[
            "Advocates admitted to the Supreme Court Bar Association and High Court Bar Association",
            "Transparent procedural counsel adhering strictly to Nepal Bar Council ethical standards",
            "Comprehensive litigation management across Kathmandu Valley and Koshi Province courts"
        ],
        conversion_prompt="Schedule a confidential case assessment to review your civil claim, limitation deadlines, and strategic court options."
    ),
    ServicePage(
        slug="criminal-law",
        title="Criminal Law & Defence Representation",
        h1="Criminal Law & Defence Representation Legal Services in Nepal",
        meta_title="Criminal Defence Lawyers in Nepal | Bail & Court Representation | PATHIVARA LAW FIRM SUNSARI",
        meta_description="Experienced criminal defence advocates in Nepal. Legal consultation for police custody, remand hearings, bail applications, and court trials under Muluki Criminal Code 2074.",
        service_code="CRIM-02",
        short_intro=(
            "We offer vigilant, ethical criminal defence representation for individuals, corporate officers, and accused persons "
            "facing investigation or formal prosecution by the Nepal Police and Office of the Attorney General. From police questioning "
            "and judicial remand (Thap Myad) to bail hearings (Dharauti/Jamanat) and District Court trials, we safeguard your constitutional "
            "rights under the National Criminal Procedure Code 2074."
        ),
        hero_badge="Constitutional Rights & Criminal Defence Advocacy",
        hero_image="/assets/images/criminal-defence-nepal.svg",
        legal_problem_overview=(
            "Facing a criminal investigation or arrest in Nepal is an urgent, high-stakes crisis. The first 24 hours of detention "
            "are critical for asserting constitutional rights under Article 20 of the Constitution of Nepal, including the right "
            "to remain silent and the right to consult legal counsel without delay. Statements coerced without legal representation "
            "can jeopardize freedom. Navigating police custody, judicial remand extensions, bail hearings, and charge-sheet scrutiny "
            "requires deep technical knowledge of the Muluki Criminal Code and Criminal Procedure Code 2074."
        ),
        relevant_situations=[
            "Police questioning, notices to appear, or urgent arrest and detention by Nepal Police",
            "Judicial remand hearings (Thap Myad) before the District Court within the statutory 24-hour window",
            "Bail applications (Dharauti / Jamanat / Sadharan Tarekh) at the preliminary hearing (Thunseka Bahas)",
            "Defence against financial crimes, fraud (Thagi), forgery (Kirtiye), and cybercrime complaints",
            "Representation in corporate criminal liability, customs offenses, and foreign exchange violations",
            "Victims representation and legal counsel for lodging First Information Reports (FIR / Jaheri Darkhwast)",
            "Appeals against conviction or challenging denial of bail before the High Court and Supreme Court"
        ],
        scope_of_assistance=[
            "Immediate legal consultation and counsel visits during police custody and detention",
            "Ensuring strict compliance with constitutional protections against unlawful detention and torture",
            "Legal assistance during the recording of statements before the Investigating Police Officer and Public Prosecutor",
            "Appearance and arguments during judicial remand extension proceedings before the District Judge",
            "Formulation and presentation of persuasive bail arguments (Thunseka Bahas) at the charge-sheet stage",
            "Scrutinizing charge-sheets (Abhiyog-patra), police investigation files, and forensic evidence for procedural infirmities",
            "Cross-examining prosecution witnesses, police officers, and medical/forensic experts during trial",
            "Filing interlocutory bail review petitions under Section 73 of the Muluki Criminal Procedure Code before High Courts"
        ],
        stages=[
            ServiceStage(
                step_number=1,
                title="Immediate Counsel & Police Custody Representation",
                description="Visiting the detainee at the police station (Prahari Karyalaya), reviewing arrest grounds, and ensuring statements are given voluntarily and truthfully without coercion.",
                duration_estimate="Within 24 Hours of Arrest"
            ),
            ServiceStage(
                step_number=2,
                title="Judicial Remand Hearings (Thap Myad)",
                description="Appearing before the District Court when police request custody extensions, opposing arbitrary detention, and requesting medical examinations.",
                duration_estimate="Investigation Period (Up to 25 to 60 days depending on offense)"
            ),
            ServiceStage(
                step_number=3,
                title="Charge-Sheet Scrutiny & Preliminary Hearing (Thunseka)",
                description="Once the Government Attorney files the formal Charge-Sheet (Abhiyog-patra), presenting arguments on whether the accused should be released on bail, general date (Tarekh), or remanded to judicial custody (Pukpak).",
                duration_estimate="1 – 3 Days upon Charge-Sheet Filing"
            ),
            ServiceStage(
                step_number=4,
                title="Trial, Evidence & Cross-Examination",
                description="Submitting defense evidence, examining prosecution witnesses, contesting forensic reports, and proving absence of criminal intent (Mens Rea) or reasonable doubt.",
                duration_estimate="4 – 12 Months"
            ),
            ServiceStage(
                step_number=5,
                title="Final Arguments, Verdict & Appellate Review",
                description="Delivering final legal arguments before the bench, reviewing judgment rationale, and filing timely appeals before the High Court or Supreme Court.",
                duration_estimate="1 – 3 Months post-verdict"
            )
        ],
        required_documents=[
            "Official copy of arrest notice, seizure memo (Baramadka Muchulka), or search warrant",
            "Copy of the First Information Report (FIR / Jaheri Darkhwast) and Police Investigation Report",
            "Formal Charge-Sheet (Abhiyog-patra) filed by the District Government Attorney Office",
            "Detainee citizenship certificate, proof of permanent residence, and employment/family ties",
            "Documentary alibi evidence, receipts, travel tickets, or electronic communication logs"
        ],
        governing_laws=[
            {"act": "Constitution of Nepal 2072 (नेपालको संविधान)", "relevance": "Article 20 (Right relating to justice: right to be informed of arrest grounds, right to counsel, protection against torture)"},
            {"act": "Muluki Criminal Code 2074 (मुलुकी अपराध संहिता, २०७४)", "relevance": "Substantive penal code defining offenses, degrees of liability, and statutory sentencing parameters"},
            {"act": "Muluki Criminal Procedure Code 2074 (मुलुकी फौजदारी कार्यविधि संहिता, २०७४)", "relevance": "Investigation, arrest, remand extensions, bail parameters (Sections 67, 68, 69, 73), and trial conduct"},
            {"act": "National Human Rights Commission Act 2068", "relevance": "Protections against custodial torture and unlawful detention"}
        ],
        rights_duties_limitations=[
            "Strict Ethical Notice: In compliance with the Nepal Bar Council Code of Conduct, we strictly do not promise or guarantee bail grants, acquittals, or case dismissal. Decisions rest entirely with the judicial bench.",
            "24-Hour Production Requirement: Under Article 20(3) of the Constitution of Nepal, every arrested person must be produced before the nearest judicial authority within 24 hours (excluding transit time).",
            "Right to Legal Consultation: The accused possesses an absolute constitutional right to consult and be defended by a licensed advocate of their choice from the moment of arrest.",
            "Presumption of Innocence: Every accused person is presumed innocent until proven guilty beyond reasonable doubt by a competent court of law."
        ],
        fee_factors=[
            "Severity of the offense, statutory penalties, and whether offense falls under State Schedule 1, 2, or 3",
            "Stage of engagement (Police investigation custody, District Court trial, or High Court appeal)",
            "Frequency of court remand hearings, emergency weekend or after-hours counsel visits",
            "Volume of prosecution evidence, number of co-defendants, and complex financial or digital forensic audits"
        ],
        consultation_preparation=[
            "Bring the exact name of the police station (e.g. Kathmandu Valley Police Office, Ward Police Office) where the person is held",
            "Obtain the official FIR number (Jaheri number) and name of the investigating police officer (Anusandhan Adhikrit)",
            "Gather identification documents and contact details of family members ready to act as bail guarantors (Jamanatdar)",
            "Write down the precise time, location, and circumstances of the arrest or police contact"
        ],
        faqs=[
            ServiceFAQ(
                question="What should someone do immediately if arrested by Nepal Police?",
                answer="The arrested person should politely state their name and identification, ask for the legal grounds of arrest, request immediate notification of their family or lawyer, and exercise their constitutional right under Article 20 not to be coerced into giving a self-incriminating statement until their advocate is present."
            ),
            ServiceFAQ(
                question="What factors do judges in Nepal consider when granting bail (Dharauti)?",
                answer="Under Sections 67, 68, and 69 of the Muluki Criminal Procedure Code 2074, judges evaluate: the gravity of the alleged offense; maximum imprisonment prescribed; previous criminal record; risk of flight; risk of witness tampering or destruction of evidence; and the health, age, or physical condition of the accused."
            ),
            ServiceFAQ(
                question="Can an accused appeal if the District Court refuses bail and sends them to judicial custody?",
                answer="Yes. Under Section 73 of the Muluki Criminal Procedure Code 2074, an order remanding the accused to judicial custody (Pukpak) or demanding an excessive bail amount can be challenged immediately before the competent High Court through an interlocutory appeal."
            ),
            ServiceFAQ(
                question="Can a criminal complaint in Nepal be withdrawn once filed?",
                answer="For State-prosecuted crimes (Schedule 1 offenses like forgery, murder, or banking fraud), the individual complainant cannot simply withdraw the complaint. The Government of Nepal, represented by the Public Prosecutor, controls prosecution. In minor compoundable individual offenses, statutory reconciliation (Milapatra) may be accepted by the court."
            )
        ],
        related_articles=[
            {"title": "What to Know When Contacted by Nepal Police", "url": "/legal-resources/what-to-know-when-contacted-by-nepal-police/"},
            {"title": "Arrest, Detention & Remand under Nepal Criminal Code", "url": "/legal-resources/arrest-detention-remand-nepal-criminal-code/"},
            {"title": "Bail Eligibility & Procedures in Nepal Courts", "url": "/legal-resources/bail-eligibility-procedure-nepal-courts/"},
            {"title": "Rights of an Accused Person under Constitution of Nepal", "url": "/legal-resources/rights-of-accused-person-constitution-nepal/"},
            {"title": "Criminal Court Proceedings: Charge-Sheet to Verdict", "url": "/legal-resources/criminal-court-proceedings-nepal-charge-sheet-to-verdict/"}
        ],
        adjacent_services=[
            {"title": "Civil Litigation & Dispute Resolution", "url": "/services/civil-litigation/"},
            {"title": "Banking & Financial Disputes", "url": "/services/banking-financial-law/"}
        ],
        lead_advocate_slug="senior-advocate-lead",
        trust_signals=[
            "Strict adherence to Nepal Bar Council ethical rules prohibiting outcome guarantees",
            "Direct intervention during police questioning and remand hearings across Kathmandu and Koshi",
            "Thorough analysis of prosecution charge-sheets, forensics, and evidentiary admissibility"
        ],
        conversion_prompt="If you or a family member face investigation or arrest, contact our office immediately for urgent legal representation."
    ),
    ServicePage(
        slug="family-law",
        title="Family Law & Divorce Representation",
        h1="Family Law, Divorce & Matrimonial Dispute Representation in Nepal",
        meta_title="Family Law & Divorce Lawyers in Nepal | PATHIVARA LAW FIRM SUNSARI",
        meta_description="Compassionate, discreet family and divorce lawyers in Nepal. Legal counsel for mutual consent divorce, contested proceedings, child custody, and spousal maintenance.",
        service_code="FAM-03",
        short_intro=(
            "Family disputes require high legal precision handled with privacy and compassion. Our family law practice assists "
            "spouses and families navigating divorce (Sambandh Bichhed), child custody and guardianship, spousal maintenance (Kharacha), "
            "and matrimonial property partition (Ansha) under the Muluki Civil Code 2074. We represent clients in District Courts "
            "as well as confidential structured mediation."
        ),
        hero_badge="Discreet & Compassionate Matrimonial Counsel",
        hero_image="/assets/images/family-law-nepal.svg",
        legal_problem_overview=(
            "The dissolution of a marriage in Nepal touches deeply sensitive personal and economic realities. Under Part 3, Chapter 3 "
            "of the Muluki Civil Code 2074, both men and women possess explicit statutory grounds to initiate divorce before the District "
            "Court. Crucial legal issues frequently accompany divorce: determining whether a 1-year reconciliation period is mandatory, "
            "partition of matrimonial property (Anshabanda), child custody arrangements, and ongoing child maintenance. Without informed "
            "legal counsel, spouses risk forfeiting vital economic protections or experiencing protracted adversarial litigation."
        ),
        relevant_situations=[
            "Mutual consent divorce where both spouses agree on settlement terms and wish to conclude swiftly",
            "Contested divorce petitions initiated by either husband or wife on statutory grounds",
            "Child custody disputes, visitation rights, and parental guardianship determinations",
            "Spousal maintenance (Kharacha) and educational/living support for minor children",
            "Matrimonial property division, disclosure of hidden assets, and ancestral partition claims",
            "Legal counsel for non-resident Nepalese (NRN) seeking divorce or marital recognition in Nepal",
            "Drafting binding matrimonial settlement deeds (Milapatra) and child welfare agreements"
        ],
        scope_of_assistance=[
            "Confidential consultation assessing statutory grounds for divorce under Sections 94 and 95 of the Muluki Civil Code 2074",
            "Negotiating and drafting comprehensive Mutual Consent Divorce Deeds covering property, alimony, and custody",
            "Representation before District Courts for expedited mutual consent proceedings",
            "Drafting and filing contested divorce Petitions (Mudda) or Written Statements of Defence",
            "Representation throughout statutory court-mandated conciliation and mediation sessions",
            "Filing interlocutory applications for interim maintenance (Antarim Kharacha) during ongoing court litigation",
            "Advocating for child custody centered on the paramount best interests of the minor child",
            "Securing court decrees (Faisala) and registration of marital status changes with municipal authorities"
        ],
        stages=[
            ServiceStage(
                step_number=1,
                title="Confidential Consultation & Fact Assessment",
                description="Evaluating the marriage background, grounds for dissolution, presence of minor children, and identifying whether mutual consent or a contested petition is legally appropriate.",
                duration_estimate="1 – 3 Days"
            ),
            ServiceStage(
                step_number=2,
                title="Settlement Negotiation / Pleadings Formulation",
                description="Drafting the mutual agreement deed (Milapatra) or preparing the formal Plaint (Firdi-patra) with statutory grounds and property claims.",
                duration_estimate="1 – 2 Weeks"
            ),
            ServiceStage(
                step_number=3,
                title="District Court Filing & Formal Registration",
                description="Registering the petition at the competent District Court (where marriage took place, where wife resides, or where husband resides).",
                duration_estimate="1 – 3 Working Days"
            ),
            ServiceStage(
                step_number=4,
                title="Court Conciliation / Hearing Proceedings",
                description="For mutual consent: joint court appearance, recording of statements, and immediate decree. For contested suits: court-mandated 1-year mediation cooling period.",
                duration_estimate="2 – 5 Days (Mutual) / 1 Year (Contested Mediation)"
            ),
            ServiceStage(
                step_number=5,
                title="Final Decree, Property Partition & Custody Order",
                description="Issuance of the final divorce decree (Sambandh Bichhed Faisala), execution of property division, and issuance of formal certificate.",
                duration_estimate="1 – 3 Weeks post-settlement"
            )
        ],
        required_documents=[
            "Official Marriage Registration Certificate (Bibaha Darta Pramanpatra) or wedding card/social proof",
            "Citizenship Certificates of both spouses (or Passport/visa copies for NRNs)",
            "Birth Registration Certificates of minor children (if applicable)",
            "Detailed inventory and ownership certificates of properties subject to partition (Lalpurja, bank statements)",
            "Recent passport-sized photographs of the applicant(s)"
        ],
        governing_laws=[
            {"act": "Muluki Civil Code 2074 (मुलुकी देवानी संहिता, २०७४)", "relevance": "Part 3, Chapter 3: Provisions relating to Divorce (Sections 93 to 104); Chapter on Guardianship & Custody (Sections 114 to 121)"},
            {"act": "Muluki Civil Procedure Code 2074", "relevance": "Court procedure, conciliation protocols, and recording of mutual settlement statements"},
            {"act": "Children Act 2075 (बालबालिका सम्बन्धी ऐन, २०७५)", "relevance": "Welfare of the child as the supreme criterion in custody decisions"}
        ],
        rights_duties_limitations=[
            "1-Year Conciliation Mandate: Under Section 97 of the Muluki Civil Code 2074, if a contested divorce petition is filed, the court must mandate a conciliation period of up to one year to attempt reconciliation before proceeding to final trial, unless statutory exceptions apply.",
            "Equal Right to Seek Divorce: Both husband and wife hold statutory rights to petition for divorce on specific enumerated grounds under the Civil Code.",
            "Best Interest of the Child: Under Nepalese law, child custody is not an absolute proprietary right of either parent; it is determined by the child age (under 5 typically resides with mother) and supreme welfare.",
            "Property Division Timing: If the wife is entitled to partition (Ansha) upon divorce, the property share must be calculated or lump-sum maintenance agreed before final dissolution."
        ],
        fee_factors=[
            "Whether the matter is amicable mutual consent or contested litigation requiring multiple court hearings",
            "Complexity of ancestral and matrimonial asset verification, valuation, and partition claims",
            "Jurisdiction and court location (Kathmandu District Court, Lalitpur, Sunsari, Morang, etc.)",
            "Involvement of cross-border or foreign marriage recognition issues"
        ],
        consultation_preparation=[
            "Assemble marriage registration certificate and children birth certificates",
            "Compile a frank, objective list of shared property, bank accounts, and liabilities",
            "Consider your core preferences regarding child custody, living arrangements, and financial maintenance",
            "Formulate specific questions for the advocate regarding court timelines and mediation options"
        ],
        faqs=[
            ServiceFAQ(
                question="How fast can a mutual consent divorce be completed in Nepal?",
                answer="When both husband and wife mutually agree to divorce and execute a comprehensive settlement deed, the District Court can finalize the divorce decree within 2 to 5 working days from registration."
            ),
            ServiceFAQ(
                question="Can a husband file for divorce directly in Nepal under current law?",
                answer="Yes. Under Section 94 of the Muluki Civil Code 2074, a husband can directly file for divorce in the District Court on grounds including: living separately for three or more consecutive years without consent, depriving of maintenance, committing physical or mental cruelty, or adultery."
            ),
            ServiceFAQ(
                question="How is child custody determined under Nepalese family law?",
                answer="Under Section 115 of the Muluki Civil Code 2074: a child under five years of age typically remains under the custody of the mother unless otherwise agreed; a child above five years may remain with either parent based on mutual agreement or court assessment of the best welfare of the child. The non-custodial parent retains visitation rights and maintenance duties."
            ),
            ServiceFAQ(
                question="Is a wife entitled to property share (Ansha) upon divorce in Nepal?",
                answer="Yes. Under Section 99 of the Muluki Civil Code 2074, if divorce occurs due to the fault of the husband, the wife is entitled to claim her partition share from the husband property before divorce is granted, or receive a lump-sum amount or periodic maintenance based on the husband income."
            )
        ],
        related_articles=[
            {"title": "Divorce Procedure under Muluki Civil Code 2074", "url": "/legal-resources/divorce-procedure-muluki-civil-code-nepal/"},
            {"title": "Mutual Consent vs. Contested Divorce in Nepal", "url": "/legal-resources/mutual-consent-vs-contested-divorce-nepal/"},
            {"title": "Child Custody & Guardianship Principles in Nepal", "url": "/legal-resources/child-custody-guardianship-laws-nepal/"},
            {"title": "Essential Documents Required for Initiating Divorce in Nepal", "url": "/legal-resources/documents-required-for-divorce-nepal/"},
            {"title": "Matrimonial Property Division (Ansha) in Divorce", "url": "/legal-resources/matrimonial-property-anshabanda-divorce-nepal/"},
            {"title": "Spousal & Child Maintenance (Kharacha) Legal Guidelines", "url": "/legal-resources/spousal-child-maintenance-laws-nepal/"}
        ],
        adjacent_services=[
            {"title": "Inheritance & Succession Law", "url": "/services/inheritance-succession/"},
            {"title": "Mediation & Alternative Dispute Resolution", "url": "/services/mediation-dispute-resolution/"},
            {"title": "Property & Land Law", "url": "/services/property-land-law/"}
        ],
        lead_advocate_slug="senior-advocate-lead",
        trust_signals=[
            "Strict professional confidentiality and sensitive client handling",
            "Transparent advice prioritizing amicable resolution and protecting children welfare",
            "Complete end-to-end assistance from initial consultation to final court decree and municipality updates"
        ],
        conversion_prompt="Book a confidential legal consultation to discuss divorce, custody, or property options with discretion."
    ),
    ServicePage(
        slug="property-land-law",
        title="Property & Land Law Representation",
        h1="Property, Real Estate & Land Law Legal Services in Nepal",
        meta_title="Property & Land Law Advocates in Nepal | Title Due Diligence & Disputes",
        meta_description="Trusted property and real estate lawyers in Nepal. Title deed verification (Lalpurja), Malpot transfer representation, partition (Anshabanda) disputes, and land litigation.",
        service_code="PROP-04",
        short_intro=(
            "Land and real estate represent the most valuable asset class in Nepal, yet they are fraught with administrative "
            "complexity and inheritance disputes. We provide rigorous legal due diligence for property purchases, title deed verification "
            "(Lalpurja examination), representation at the Land Revenue Office (Malpot Karyalaya), ancestral partition litigation "
            "(Anshabanda Mudda), and boundary dispute resolution under the Land Act 2021 and Muluki Civil Code 2074."
        ),
        hero_badge="Land Revenue Due Diligence & Property Litigation",
        hero_image="/assets/images/property-law-nepal.svg",
        legal_problem_overview=(
            "Purchasing or holding real estate in Nepal without comprehensive legal verification carries severe risks. Land records "
            "are maintained across dual governmental agencies: the Survey Office (Napi Karyalaya) for cadastral maps and the Land "
            "Revenue Office (Malpot Karyalaya) for ownership ledgers (Shrestha). Common pitfalls include purchasing land subject to an "
            "unregistered court freeze (Rokka), unpartitioned ancestral rights (Anshiyar share claims), Guthi trust restrictions, "
            "tenant tenancy claims (Mohi rights), or inaccurate boundary mappings. Once a fraudulent transfer occurs, rectifying title "
            "involves years of court litigation."
        ),
        relevant_situations=[
            "Pre-purchase title due diligence, ownership chain verification, and Malpot record verification",
            "Drafting and registering official Land Sale and Purchase Deeds (Rajinama Likhit) at the Malpot Office",
            "Ancestral property partition disputes (Anshabanda Mudda) between legal co-heirs",
            "Challenging fraudulent gift deeds (Bakaspatra) or unauthorized land alienation",
            "Boundary disputes, encroachment, right-of-way easement claims (Bato Chhadne), and Napi re-survey discrepancies",
            "Releasing mortgages and institutional bank liens (Rokka Phukuwa) upon loan clearance",
            "Tenant rights (Mohi Hak) verification, settlement, and statutory compensation claims",
            "Commercial property leasing agreements, build-to-suit contracts, and joint venture developer agreements"
        ],
        scope_of_assistance=[
            "Conducting exhaustive physical searches of the official Shrestha register at Malpot offices across Kathmandu, Lalitpur, Bhaktapur, and Sunsari",
            "Verifying official cadastral maps (Blue Prints) and Trace maps at the Survey Office (Napi Karyalaya)",
            "Issuing formal Legal Title Due Diligence Reports identifying encumbrances, litigation risks, or Guthi reservations",
            "Drafting customized property purchase agreements, earnest money deeds (Byna-patra), and registered deeds",
            "Representing property owners during formal partition proceedings before District Courts",
            "Filing lawsuits for cancellation of fraudulent deeds (Likhit Badr Mudda) and recovery of possession",
            "Representation during municipal building permit (Naksa Paas) disputes and easement rights litigation"
        ],
        stages=[
            ServiceStage(
                step_number=1,
                title="Document Collection & Initial Review",
                description="Reviewing the client copy of the Land Ownership Registration Certificate (Lalpurja), citizenship, and property tax payment slips.",
                duration_estimate="1 – 2 Days"
            ),
            ServiceStage(
                step_number=2,
                title="Malpot & Survey Office On-Site Verification",
                description="Visiting the competent Land Revenue Office (Malpot) and Survey Office (Napi) to inspect the official register (Shrestha), verify Rokka status, and review the cadastral map.",
                duration_estimate="3 – 7 Working Days"
            ),
            ServiceStage(
                step_number=3,
                title="Due Diligence Report / Agreement Drafting",
                description="Delivering a formal Title Due Diligence Opinion and preparing the formal deed (Rajinama, Anshabanda, or Byna-patra) compliant with statutory formatting rules.",
                duration_estimate="2 – 4 Days"
            ),
            ServiceStage(
                step_number=4,
                title="Malpot Registration / Court Plaint Filing",
                description="For transactions: accompanying parties to the Malpot Office for biometric verification and registration. For disputes: filing the plaint in District Court.",
                duration_estimate="1 Day (Transfer) / 2 – 4 Weeks (Litigation filing)"
            ),
            ServiceStage(
                step_number=5,
                title="Title Mutation & Final Lalpurja Issuance",
                description="Obtaining the freshly mutated Lalpurja in the buyer or rightful heir name and updating municipal property tax records (Dakhil Kharij).",
                duration_estimate="1 – 2 Weeks post-execution"
            )
        ],
        required_documents=[
            "Original Land Ownership Registration Certificate (Lalpurja)",
            "Cadastral Map / Blue Print / Trace Map issued by the competent Survey Office (Napi Karyalaya)",
            "Latest land revenue and municipal property tax payment receipts (Tiro Tireko Rasid)",
            "Citizenship Certificate copies of buyers, sellers, or co-heirs",
            "Citizenship and family relation certificate (Nata Pramanit) for partition and succession matters",
            "Official certificate of no-objection / municipal road access certificate (Sadak Pramanikaran)"
        ],
        governing_laws=[
            {"act": "Land Act 2021 (भूमि सम्बन्धी ऐन, २०२१)", "relevance": "Land ceilings, tenancy rights (Mohi), land classifications, and agricultural protections"},
            {"act": "Land Revenue Act 2034 (मालपोत ऐन, २०३४)", "relevance": "Registration of land deeds, mutation of records, Shrestha maintenance, and Malpot office powers"},
            {"act": "Muluki Civil Code 2074 (मुलुकी देवानी संहिता, २०७४)", "relevance": "Part 4: Law relating to Property; provisions on ownership, possession, easement rights, and partition (Anshabanda)"},
            {"act": "Survey and Measurement Act 2019 (जग्गा नापजाँच ऐन, २०१९)", "relevance": "Cadastral surveying, boundary demarcation, and resolving survey errors"}
        ],
        rights_duties_limitations=[
            "Mandatory Deed Registration: Under Section 36 of the Land Revenue Act 2034, any deed transferring title, gift, or partition of land must be registered at the Malpot Office to hold legal validity against third parties.",
            "Co-heir Partition Consent: Disposing of ancestral property without obtaining written consent or executing formal partition (Anshabanda) with all lawful heirs can result in the sale being legally voided in court.",
            "Ceiling Restrictions (Hadbandi): Individual and family landholdings in Nepal are subject to statutory acreage ceilings depending on geographic zones (Terai, Hills, Kathmandu Valley).",
            "Guthi Land Classifications: Rajguthi and private Guthi lands carry distinct statutory limitations and cannot be freely transferred without Guthi Sansthan clearance."
        ],
        fee_factors=[
            "Nature of service: standard transactional due diligence vs. high-stakes court litigation",
            "Geographic location of property (Kathmandu Valley, Koshi Province, Sunsari/Morang, etc.)",
            "Volume of historical deed chains, missing genealogical documentation, or multiple co-defendants",
            "Government registration charges, capital gains tax (CGT), and municipal valuation tariffs"
        ],
        consultation_preparation=[
            "Bring clear photocopies of the Lalpurja (showing plot numbers / Kitta number and area)",
            "Bring the cadastral blue print showing road connectivity and adjoining plots",
            "Assemble tax receipts and genealogical family tree (Bansawali) if the dispute involves inheritance",
            "Prepare a concise summary of current possession (who physically occupies the land)"
        ],
        faqs=[
            ServiceFAQ(
                question="What is a 'Rokka' on land, and how can a buyer check for it in Nepal?",
                answer="A 'Rokka' is a formal legal freeze placed on a land parcel in the Malpot Office records, typically by a commercial bank (as loan collateral), a judicial court (due to pending litigation), or the Commission for the Investigation of Abuse of Authority (CIAA). A buyer can verify Rokka status by conducting a formal search of the Shrestha ledger at the competent Land Revenue Office."
            ),
            ServiceFAQ(
                question="Can a father or mother sell ancestral property in Nepal without the consent of children?",
                answer="Under Chapter 10 of the Muluki Civil Code 2074, parents cannot alienate ancestral property (Paitrik Sampatti) without the formal written consent of all adult coparceners (Anshiyars), except for necessary family survival or medical emergencies as strictly defined by statute. Self-acquired property (Swaparjita Sampatti), however, may be disposed of freely."
            ),
            ServiceFAQ(
                question="What is the legal difference between Bakaspatra (Gift Deed) and Rajinama (Sale Deed)?",
                answer="A Rajinama is a registered commercial deed where ownership transfers for financial consideration (purchase price). A Bakaspatra is a registered voluntary gift deed transferring property without monetary exchange, commonly executed between family relations. Conditional gift deeds (Haldekhibako Bakaspatra) are irrevocable once executed in accordance with statutory conditions."
            ),
            ServiceFAQ(
                question="What should an owner do if a neighbor encroaches on their land boundary?",
                answer="The owner should first apply to the local Survey Office (Napi Karyalaya) for official re-measurement and demarcation based on the permanent cadastral field book. If the encroachment persists, the owner can lodge an application with the local Municipal Ward Judicial Committee (Nyarik Samiti) or file an unlawful possession suit in District Court."
            )
        ],
        related_articles=[
            {"title": "How to Verify Land Ownership & Title Records (Lalpurja)", "url": "/legal-resources/how-to-check-land-ownership-lalpurja-nepal/"},
            {"title": "Legal Due Diligence Checklist for Buying Real Estate in Nepal", "url": "/legal-resources/legal-due-diligence-buying-land-nepal/"},
            {"title": "Official Land Registration & Malpot Deed Transfer Procedures", "url": "/legal-resources/land-registration-malpot-deed-transfer-nepal/"},
            {"title": "Ancestral Property Partition (Anshabanda) Disputes in Nepal", "url": "/legal-resources/property-partition-anshabanda-disputes-nepal/"},
            {"title": "Inheritance & Bakaspatra (Gift Deed) Real Estate Laws", "url": "/legal-resources/inheritance-bakaspatra-land-laws-nepal/"},
            {"title": "Land Boundary Conflicts & Encroachment Remedies in Nepal", "url": "/legal-resources/land-boundary-encroachment-remedies-nepal/"}
        ],
        adjacent_services=[
            {"title": "Civil Litigation & Dispute Resolution", "url": "/services/civil-litigation/"},
            {"title": "Inheritance & Succession Law", "url": "/services/inheritance-succession/"},
            {"title": "Contract Drafting & Review", "url": "/services/contract-law/"}
        ],
        lead_advocate_slug="senior-advocate-lead",
        trust_signals=[
            "Hands-on title due diligence at Land Revenue Offices across Kathmandu Valley and Sunsari",
            "Proven track record resolving complex ancestral property and boundary partition suits",
            "Clear, written legal opinions detailing risks before any financial commitments are made"
        ],
        conversion_prompt="Verify property title or resolve an ongoing land dispute with experienced Nepalese land advocates."
    ),
    ServicePage(
        slug="corporate-business-law",
        title="Corporate & Business Law Advisory",
        h1="Corporate, Business & Commercial Legal Advisory in Nepal",
        meta_title="Corporate & Business Lawyers in Nepal | PATHIVARA LAW FIRM SUNSARI",
        meta_description="Full-service corporate law firm in Nepal. Company incorporation, OCR compliance, shareholder agreements, foreign investment advisory, and commercial litigation.",
        service_code="CORP-05",
        short_intro=(
            "We serve as trusted outside corporate counsel to startups, private enterprises, joint ventures, and international investors "
            "operating in Nepal. Our corporate legal practice encompasses company incorporation at the Office of Company Registrar (OCR), "
            "Foreign Direct Investment (FDI) approvals, corporate restructuring, regulatory compliance, commercial contracts, and "
            "shareholder dispute resolution under the Companies Act 2063."
        ),
        hero_badge="Company Registrar (OCR) & Commercial Legal Counsel",
        hero_image="/assets/images/corporate-law-nepal.svg",
        legal_problem_overview=(
            "Doing business in Nepal requires navigating an evolving regulatory framework across multiple ministries and statutory bodies, "
            "including the Office of Company Registrar (OCR), Department of Industry (DOI), Nepal Rastra Bank (NRB), and the Inland Revenue "
            "Department (IRD). Non-compliance with mandatory annual filings, shareholder meeting protocols, director fiduciary duties, "
            "or foreign investment repatriation rules can trigger severe financial penalties, corporate deadlock, or director disqualification. "
            "Strategic corporate structuring from the outset shields promoters and creates a scalable foundation for growth."
        ),
        relevant_situations=[
            "Incorporating Private Limited Companies, Public Companies, or Branch/Liaison Offices in Nepal",
            "Foreign Direct Investment (FDI) advisory, Department of Industry approvals, and NRB capital repatriation",
            "Drafting customized Articles of Association (Prabandhapatra) and Memorandum of Association (Niyamawali)",
            "Drafting robust Shareholder Agreements (SHA), Joint Venture Agreements (JVA), and Founder Charters",
            "Advising company directors on fiduciary duties, statutory liabilities, and conflict-of-interest compliance",
            "Resolving corporate deadlocks, minority shareholder oppression claims, and board of directors disputes",
            "Corporate legal restructuring, share capital increases, share transfers, and cross-border mergers",
            "Ongoing corporate retainer advisory covering routine commercial contracts, NDAs, and regulatory filings"
        ],
        scope_of_assistance=[
            "Conducting company name clearance, drafting MOA/AOA, and completing full OCR digital registration",
            "Procuring foreign investment approvals under the Foreign Investment and Technology Transfer Act (FITTA 2075)",
            "Liaising with Nepal Rastra Bank (NRB) for inward foreign currency approval and outward royalty/dividend repatriation",
            "Structuring complex equity investments, convertible instruments, and employee stock option plans (ESOPs)",
            "Conducting comprehensive corporate legal due diligence audits for acquisitions and mergers",
            "Representing shareholders or management in corporate oppression petitions before the High Court Commercial Bench",
            "Drafting standard corporate policies, employment handbooks, and commercial vendor agreements",
            "Managing post-incorporation tax registration (PAN/VAT), ward registration, and annual compliance returns"
        ],
        stages=[
            ServiceStage(
                step_number=1,
                title="Business Structuring Consultation",
                description="Assessing business objectives, capital requirements, shareholder equity split, and selecting the optimal legal form (Pvt Ltd, Public, Branch, or Partnership).",
                duration_estimate="2 – 4 Days"
            ),
            ServiceStage(
                step_number=2,
                title="Charter Drafting & Name Reservation",
                description="Reserving the proposed company name on the OCR digital portal and drafting tailored Memorandum and Articles of Association (Prabandhapatra & Niyamawali).",
                duration_estimate="3 – 7 Working Days"
            ),
            ServiceStage(
                step_number=3,
                title="OCR Incorporation & Certificate Issuance",
                description="Filing charter documents, promoter KYC, and power of attorney with the OCR, paying statutory stamp registration fees, and securing the Certificate of Incorporation.",
                duration_estimate="1 – 2 Weeks"
            ),
            ServiceStage(
                step_number=4,
                title="Post-Registration Licensing & Tax Setup",
                description="Obtaining Inland Revenue PAN/VAT registration, municipal ward business registration, and Department of Industry approval where applicable.",
                duration_estimate="1 – 2 Weeks"
            ),
            ServiceStage(
                step_number=5,
                title="Ongoing Corporate Compliance & Retainer",
                description="Filing mandatory statutory forms (Forms 9, 10, 16, 21), maintaining minute books, holding AGMs, and ongoing commercial agreement advisory.",
                duration_estimate="Annual Recurring"
            )
        ],
        required_documents=[
            "Copies of Nepali Citizenship Certificates or Passports for all promoters and directors",
            "Passport-sized photographs of all promoters and authorized representatives",
            "Proposed company name options and registered office address proof (lease agreement or title)",
            "Draft Memorandum and Articles of Association (or our firm can draft custom versions)",
            "Board resolution and certificate of incorporation of parent company (if promoter is an existing entity)",
            "Foreign investment approval letter and source of funds documentation (for foreign promoters)"
        ],
        governing_laws=[
            {"act": "Companies Act 2063 (कम्पनी ऐन, २०६३)", "relevance": "Core company legislation governing incorporation, director duties, shareholder rights, meetings, and winding up"},
            {"act": "Foreign Investment and Technology Transfer Act 2075 (FITTA 2075)", "relevance": "Rules governing foreign equity, minimum capital thresholds, negative list, and technology transfer"},
            {"act": "Industrial Enterprises Act 2076", "relevance": "Industry classification, licensing, incentives, and Department of Industry oversight"},
            {"act": "Income Tax Act 2058", "relevance": "Corporate tax compliance, withholding tax, transfer pricing, and corporate returns"}
        ],
        rights_duties_limitations=[
            "Directors Fiduciary Standard: Under Section 99 of the Companies Act 2063, directors owe strict fiduciary duties to the company and are personally liable for actions taken in conflict of interest or in breach of statutory limits.",
            "Mandatory Annual Filings: Companies must submit audited balance sheets, auditor reports, and annual return forms to the OCR within six months of fiscal year close; late filings incur compounding statutory fines.",
            "Foreign Investment Thresholds: Foreign direct investment is subject to statutory minimum investment thresholds and negative list restrictions established by the Government of Nepal.",
            "Separate Legal Entity Principle: The corporate veil protects shareholders from personal liability for company obligations, provided corporate governance formalities are duly observed."
        ],
        fee_factors=[
            "Scope of service: standalone company incorporation vs. comprehensive ongoing corporate retainer",
            "Involvement of foreign investment (FDI approvals, NRB liaison, bilingual charter drafting)",
            "Share capital tier (OCR statutory registration fees scale progressively based on authorized capital)",
            "Complexity of custom Shareholder Agreements, drag-along/tag-along clauses, and dispute mechanisms"
        ],
        consultation_preparation=[
            "Identify the proposed primary business objectives and activities to be undertaken in Nepal",
            "Define the initial authorized and paid-up capital of the proposed enterprise",
            "Outline the proposed shareholder cap table (promoters, equity percentages, and directorship roles)",
            "Assemble identification documents and passport photographs for all promoters"
        ],
        faqs=[
            ServiceFAQ(
                question="How long does it take to register a Private Limited Company in Nepal?",
                answer="With all promoter identification and charter documents prepared, company registration at the Office of Company Registrar (OCR) typically completes within 5 to 10 working days, followed by approximately 3 to 5 days for PAN/VAT and ward registration."
            ),
            ServiceFAQ(
                question="Can a foreign individual or foreign entity own 100% of a company in Nepal?",
                answer="Yes, in most commercial sectors, 100% foreign equity ownership is permitted under FITTA 2075, subject to minimum statutory capital thresholds (currently NPR 20 million per foreign investor) and compliance with the negative list (which excludes sectors like primary agriculture, retail trade, and arms)."
            ),
            ServiceFAQ(
                question="What are the essential annual filings required for companies at the OCR in Nepal?",
                answer="Every registered company must file annual returns including: notice of Annual General Meeting (Form 21/16); list of shareholders and directors (Form 9); audited financial statements; and auditor appointment notices within six months of fiscal year completion."
            ),
            ServiceFAQ(
                question="How are shareholder disputes resolved under the Companies Act 2063?",
                answer="Shareholder disputes can be resolved through provisions defined in a customized Shareholder Agreement, internal board dispute mechanisms, or by filing an oppression petition before the High Court Commercial Bench under Sections 139 and 140 of the Companies Act 2063."
            )
        ],
        related_articles=[
            {"title": "Step-by-Step Guide to Registering a Company at the OCR", "url": "/legal-resources/steps-registering-company-ocr-nepal/"},
            {"title": "Proprietorship vs. Partnership vs. Private Limited in Nepal", "url": "/legal-resources/proprietorship-vs-partnership-vs-private-limited-nepal/"},
            {"title": "Essential Clauses Every Commercial Contract Must Contain", "url": "/legal-resources/essential-clauses-commercial-contracts-nepal/"},
            {"title": "Key Legal Considerations in Contract Drafting in Nepal", "url": "/legal-resources/legal-considerations-contract-drafting-nepal/"},
            {"title": "Directors Duties and Liabilities under Companies Act 2063", "url": "/legal-resources/directors-duties-liabilities-companies-act-nepal/"},
            {"title": "Resolving Shareholder and Partnership Disputes in Nepal", "url": "/legal-resources/shareholder-partnership-dispute-resolution-nepal/"}
        ],
        adjacent_services=[
            {"title": "Contract Drafting & Review", "url": "/services/contract-law/"},
            {"title": "Labour & Employment Law", "url": "/services/labour-employment-law/"},
            {"title": "Banking & Financial Disputes", "url": "/services/banking-financial-law/"}
        ],
        lead_advocate_slug="advocate-associate-corporate",
        trust_signals=[
            "Specialized corporate advocates handling OCR, DOI, and NRB regulatory processes",
            "Trusted legal advisors to high-growth tech enterprises, joint ventures, and international investors",
            "Tailored corporate governance and dispute mitigation strategies"
        ],
        conversion_prompt="Consult with our corporate legal practice to structure your business, file company charters, or resolve commercial disputes."
    ),
    ServicePage(
        slug="contract-law",
        title="Contract Drafting & Agreement Review",
        h1="Contract Drafting, Legal Review & Dispute Advisory in Nepal",
        meta_title="Contract Drafting & Agreement Review Lawyers in Nepal | PATHIVARA LAW FIRM SUNSARI",
        meta_description="Protect your interests with expert contract drafting and legal review in Nepal. Commercial agreements, employment contracts, leases, and breach enforcement.",
        service_code="CONT-06",
        short_intro=(
            "A well-drafted contract is your primary shield against future disputes. We draft, review, and negotiate commercial agreements, "
            "vendor contracts, non-disclosure agreements (NDAs), joint venture covenants, and leases under the Muluki Civil Code 2074. "
            "Our contracts are meticulously tailored to Nepalese statutory requirements to ensure full enforceability in court."
        ),
        hero_badge="Enforceable Commercial Agreements & Risk Mitigation",
        hero_image="/assets/images/contract-law-nepal.svg",
        legal_problem_overview=(
            "Informal agreements, internet templates, or poorly drafted contracts frequently fail when put to the test in Nepalese courts. "
            "Under Part 5, Chapter 1 of the Muluki Civil Code 2074, agreements missing essential elements (such as lawful consideration, mutual consent, "
            "and legal capacity) are void ab initio. Ambiguous dispute resolution clauses, unaddressed force majeure events, or missing "
            "indemnity covenants can leave businesses exposed to severe financial loss and endless litigation."
        ),
        relevant_situations=[
            "Drafting commercial vendor agreements, supply chain contracts, and service level agreements (SLAs)",
            "Reviewing real estate commercial lease deeds, franchise agreements, and distribution agreements",
            "Drafting Non-Disclosure Agreements (NDAs), non-compete covenants, and intellectual property assignments",
            "Advising on breach of contract claims, liquidated damages clauses, and formal termination notices",
            "Translating, adapting, and aligning foreign-law commercial contracts to Nepalese statutory frameworks"
        ],
        scope_of_assistance=[
            "Comprehensive legal audit of existing contracts to identify commercial vulnerabilities and regulatory non-compliance",
            "Drafting bespoke bilateral and multilateral agreements tailored to specific commercial operations",
            "Negotiating contractual terms with counterparty legal counsel to protect your financial and liability interests",
            "Formulating clear dispute escalation mechanisms, including mediation covenants and arbitration clauses",
            "Drafting formal contractual breach notices, demand letters, and termination deeds"
        ],
        stages=[
            ServiceStage(
                step_number=1,
                title="Commercial Term Sheet Review",
                description="Analyzing the business deal structure, key deliverables, consideration, payment milestones, and risk factors.",
                duration_estimate="1 – 2 Days"
            ),
            ServiceStage(
                step_number=2,
                title="Bespoke Drafting & Legal Alignment",
                description="Drafting customized agreement provisions compliant with Part 5 of the Muluki Civil Code 2074.",
                duration_estimate="3 – 5 Working Days"
            ),
            ServiceStage(
                step_number=3,
                title="Client Review & Revisions",
                description="Walking through key clauses with the client, clarifying risk allocations, and incorporating commercial adjustments.",
                duration_estimate="2 – 3 Days"
            ),
            ServiceStage(
                step_number=4,
                title="Counterparty Negotiation",
                description="Engaging with the counterparty legal counsel to resolve disputed clauses and finalize execution versions.",
                duration_estimate="3 – 7 Days"
            ),
            ServiceStage(
                step_number=5,
                title="Execution & Registration Compliance",
                description="Advising on valid signing protocols, board authorizations, witness requirements, and notarization or stamp duties.",
                duration_estimate="1 Day"
            )
        ],
        required_documents=[
            "Commercial term sheet, memorandum of understanding (MOU), or email agreement summaries",
            "Existing agreement drafts or standard template versions requiring revision",
            "Corporate registration certificates and identity documents of all executing parties",
            "Relevant licenses or regulatory approvals required for the commercial subject matter"
        ],
        governing_laws=[
            {"act": "Muluki Civil Code 2074 (मुलुकी देवानी संहिता, २०७४)", "relevance": "Part 5: Law relating to Contracts and other Obligations (Sections 503 to 542)"},
            {"act": "Evidence Act 2031 (प्रमाण ऐन, २०३१)", "relevance": "Provisions on admissibility of written documents, signatures, and electronic records"},
            {"act": "Arbitration Act 2055 (मध्यस्थ ऐन, २०५५)", "relevance": "Validity and enforcement of contractual arbitration agreements"}
        ],
        rights_duties_limitations=[
            "Void Agreements: Contracts contrary to public policy, restraining trade unlawfully, or lacking lawful consideration are void under Section 517 of the Civil Code.",
            "Limitation on Breach Suits: Suits claiming damages for breach of contract must be instituted within strict statutory limitation periods (generally 2 years from breach date).",
            "Specific Performance: Nepalese courts may decree specific performance only in cases where monetary compensation does not afford adequate relief, subject to statutory conditions."
        ],
        fee_factors=[
            "Complexity and transaction value of the commercial agreement",
            "Turnaround urgency (standard timeline vs. expedited 24-hour review)",
            "Involvement in active multi-party commercial negotiations"
        ],
        consultation_preparation=[
            "Provide a bullet-point summary of the core deal terms (deliverables, prices, dates, payment terms)",
            "Identify the key concerns or risks you wish to mitigate in the agreement",
            "Specify whether disputes should be resolved through mediation, arbitration, or court litigation"
        ],
        faqs=[
            ServiceFAQ(
                question="Are electronic contracts and digital signatures legally enforceable in Nepal?",
                answer="Yes. Under the Electronic Transactions Act 2063 (ETA 2063) and provisions of the Muluki Civil Code 2074, contracts formed through electronic communications and executed via verified digital or electronic signatures are legally valid and admissible as evidence in Nepalese courts."
            ),
            ServiceFAQ(
                question="What remedies are available if the other party breaches a commercial contract in Nepal?",
                answer="The non-breaching party can pursue: 1) A suit for monetary compensation/damages (Kshatipurti) under Section 537 of the Civil Code; 2) Specific performance of the contract (where applicable); 3) Immediate contract termination and restitution; or 4) Interim court injunctions preventing further breach."
            )
        ],
        related_articles=[
            {"title": "Essential Clauses Every Commercial Contract Must Contain", "url": "/legal-resources/essential-clauses-commercial-contracts-nepal/"},
            {"title": "Key Legal Considerations in Contract Drafting in Nepal", "url": "/legal-resources/legal-considerations-contract-drafting-nepal/"}
        ],
        adjacent_services=[
            {"title": "Corporate & Business Law", "url": "/services/corporate-business-law/"},
            {"title": "Civil Litigation & Dispute Resolution", "url": "/services/civil-litigation/"}
        ],
        lead_advocate_slug="advocate-associate-corporate",
        trust_signals=[
            "Precision commercial drafting avoiding ambiguous boilerplate language",
            "Protection of intellectual property, proprietary assets, and financial covenants",
            "Thorough alignment with the Muluki Civil Code 2074"
        ],
        conversion_prompt="Have your commercial agreement professionally drafted or vetted by experienced Nepalese contract lawyers."
    ),
    ServicePage(
        slug="inheritance-succession",
        title="Inheritance & Succession Law",
        h1="Inheritance, Succession & Ancestral Estate Legal Services in Nepal",
        meta_title="Inheritance & Succession Lawyers in Nepal | Estate & Anshabanda Counsel",
        meta_description="Specialized legal representation for inheritance disputes, succession rights, ancestral partition (Anshabanda), and Bakaspatra under Muluki Civil Code 2074.",
        service_code="INHER-07",
        short_intro=(
            "Succession and ancestral property partition represent the most frequent civil disputes in Nepalese society. We assist heirs, "
            "surviving spouses, daughters, and families in determining lawful inheritance rights (Apunstrali / Hakwala), formalizing "
            "ancestral partition (Anshabanda), drafting wills (Ichhapatra), and executing property mutations under the Muluki Civil Code 2074."
        ),
        hero_badge="Ancestral Estate Rights & Succession Advisory",
        hero_image="/assets/images/inheritance-law-nepal.svg",
        legal_problem_overview=(
            "The enactment of the Muluki Civil Code 2074 fundamentally modernized inheritance law in Nepal, establishing equal inheritance "
            "rights for daughters and sons regardless of marital status. However, ancestral property (Paitrik Sampatti) disputes remain "
            "fraught with tension. Issues regularly arise over unpartitioned properties, concealed assets, fraudulent gift deeds (Bakaspatra), "
            "contested wills, or the rights of elderly parents to maintenance. Resolving inheritance matters requires reconciling complex "
            "genealogical lineages with strict statutory succession hierarchies."
        ),
        relevant_situations=[
            "Partition of ancestral estate (Anshabanda) among lawful co-heirs (Anshiyars)",
            "Asserting equal inheritance rights of married or unmarried daughters under current law",
            "Challenging fraudulent transfer or alienation of unpartitioned family property",
            "Settling succession rights following the death of a property owner without a will (Apunstrali)",
            "Drafting and registering legally binding Wills (Ichhapatra) or Family Settlement Deeds",
            "Representation in property mutation and transfer of title at the Land Revenue Office (Malpot)"
        ],
        scope_of_assistance=[
            "Conducting comprehensive genealogical verification (Bansawali audit) and identifying all statutory co-heirs",
            "Negotiating and drafting formal Partition Deeds (Anshabanda Likhit) for registration at the Malpot Office",
            "Representing heirs in contested Partition Suits (Anshabanda Mudda) before District Courts",
            "Filing lawsuits for invalidation of fraudulent deeds (Likhit Badr) executed without co-heir consent",
            "Assisting non-resident Nepalese (NRNs) in claiming, protecting, or transferring ancestral property in Nepal"
        ],
        stages=[
            ServiceStage(
                step_number=1,
                title="Genealogical & Estate Assessment",
                description="Examining family relation certificates (Nata Pramanit), family tree (Bansawali), and listing all real estate and financial assets.",
                duration_estimate="2 – 4 Days"
            ),
            ServiceStage(
                step_number=2,
                title="Asset Search & Valuation",
                description="Verifying land title records (Lalpurja) at competent Malpot offices and identifying any concealed or encumbered properties.",
                duration_estimate="1 – 2 Weeks"
            ),
            ServiceStage(
                step_number=3,
                title="Amicable Partition Negotiation / Deed Drafting",
                description="Drafting fair partition shares complying with statutory equal-share mandates and presenting deed for co-heir approval.",
                duration_estimate="1 – 3 Weeks"
            ),
            ServiceStage(
                step_number=4,
                title="Malpot Registration / Court Litigation",
                description="Registering the agreed deed at the Land Revenue Office or, if contested, initiating a formal Anshabanda lawsuit in District Court.",
                duration_estimate="1 Day (Deed) / 10 – 18 Months (Litigation)"
            ),
            ServiceStage(
                step_number=5,
                title="Mutation & Individual Title Issuance",
                description="Securing separate Lalpurjas in each heir individual name following court decree or registered deed execution.",
                duration_estimate="2 – 4 Weeks"
            )
        ],
        required_documents=[
            "Official Family Relationship Certificate (Nata Pramanit Pramanpatra) issued by local ward office",
            "Genealogical Family Tree (Bansawali) verified by local authorities",
            "Death Certificates of deceased property owners",
            "Land Ownership Certificates (Lalpurja) and cadastral blue prints of all ancestral holdings",
            "Citizenship Certificates of all co-heirs"
        ],
        governing_laws=[
            {"act": "Muluki Civil Code 2074 (मुलुकी देवानी संहिता, २०७४)", "relevance": "Part 3, Chapter 10: Provisions relating to Partition (Anshabanda); Chapter 16: Provisions relating to Succession (Apunstrali)"},
            {"act": "Land Revenue Act 2034", "relevance": "Procedures for mutation and registration of inherited property records at the Malpot Office"}
        ],
        rights_duties_limitations=[
            "Equal Partition Rights: Under Section 205 of the Muluki Civil Code 2074, father, mother, husband, wife, son, and daughter are deemed equal co-heirs (Anshiyar) with equal shares in ancestral property.",
            "Care of Elderly Parents: Under statutory provisions, co-heirs taking their partition share are legally obligated to provide maintenance and care for elderly parents.",
            "Right of Self-Acquired Property: An individual possesses absolute liberty to bequeath or dispose of self-acquired property without partition constraints."
        ],
        fee_factors=[
            "Number of co-heirs, disputed holdings, and court jurisdiction",
            "Amicable partition deed registration vs. full contested court litigation",
            "Need for archival searches at distant Land Revenue Offices"
        ],
        consultation_preparation=[
            "Bring official relationship certificates and death certificates of former owners",
            "Prepare a full list of all children, surviving spouses, and known ancestral land plots",
            "Identify whether any previous partition deeds or family agreements were executed"
        ],
        faqs=[
            ServiceFAQ(
                question="Do married daughters have an equal right to ancestral property in Nepal?",
                answer="Yes. Under the Muluki Civil Code 2074, both married and unmarried daughters hold equal coparcenary rights to ancestral property alongside sons, father, and mother. The previous restriction depriving married daughters of partition rights has been abolished."
            ),
            ServiceFAQ(
                question="What happens if a co-heir sells family land without the knowledge of other heirs?",
                answer="If a co-heir alienates unpartitioned ancestral property without obtaining the written consent of all co-heirs, the aggrieved heirs can file a lawsuit for cancellation of deed (Likhit Badr Mudda) within statutory limitation periods to nullify the sale."
            )
        ],
        related_articles=[
            {"title": "Ancestral Property Partition (Anshabanda) Disputes in Nepal", "url": "/legal-resources/property-partition-anshabanda-disputes-nepal/"},
            {"title": "Inheritance & Bakaspatra (Gift Deed) Real Estate Laws", "url": "/legal-resources/inheritance-bakaspatra-land-laws-nepal/"}
        ],
        adjacent_services=[
            {"title": "Property & Land Law", "url": "/services/property-land-law/"},
            {"title": "Family Law & Divorce", "url": "/services/family-law/"}
        ],
        lead_advocate_slug="senior-advocate-lead",
        trust_signals=[
            "Comprehensive genealogical audits and statutory partition share calculations",
            "Deep experience defending equal inheritance rights under the Muluki Civil Code 2074",
            "Seamless execution of title mutations across Land Revenue Offices"
        ],
        conversion_prompt="Protect your rightful inheritance or structure an amicable family estate partition with trusted advocates."
    ),
    ServicePage(
        slug="labour-employment-law",
        title="Labour & Employment Law Representation",
        h1="Labour & Employment Law Legal Advisory & Representation in Nepal",
        meta_title="Labour & Employment Lawyers in Nepal | Labour Court & HR Compliance",
        meta_description="Comprehensive employment and labour law services in Nepal. Labour Act 2074 compliance, employment dispute defense, termination counseling, and Labour Court representation.",
        service_code="LAB-08",
        short_intro=(
            "Balancing fair employee relations with regulatory compliance is vital for any commercial enterprise. We provide comprehensive "
            "employment legal counsel to corporations, organizations, and senior executives under the Labour Act 2074 and Social Security "
            "Act 2074. Our practice spans employment agreement drafting, workplace policy audits, disciplinary procedures, termination "
            "counseling, and representation before the Labour Court and Labour Offices."
        ),
        hero_badge="Labour Act 2074 & Labour Court Representation",
        hero_image="/assets/images/labour-law-nepal.svg",
        legal_problem_overview=(
            "Nepal labour jurisprudence enforces strict protections for employees and workers. Under the Labour Act 2074, employment cannot "
            "be terminated at will without strictly adhering to statutory disciplinary grounds, prior written warnings, and procedural "
            "due process. Failing to register with the Social Security Fund (SSF), misclassifying permanent workers as outsourced staff, "
            "or executing unlawful retrenchments exposes employers to substantial back-pay awards, reinstatement decrees, and statutory fines."
        ),
        relevant_situations=[
            "Drafting employment contracts, executive service agreements, and consultancy covenants",
            "Formulating comprehensive Employee Handbooks, HR bylaws, and disciplinary protocols",
            "Advising employers on statutory Social Security Fund (SSF) registration and contribution compliance",
            "Managing performance improvement plans (PIPs), misconduct inquiries, and legal termination procedures",
            "Representing employers or employees in collective bargaining negotiations and trade union disputes",
            "Representation in wrongful termination and wage claims before the Labour Office and Labour Court"
        ],
        scope_of_assistance=[
            "Conducting comprehensive HR and labour law compliance audits for corporate employers",
            "Drafting legally compliant employment agreements with enforceable confidentiality and non-compete terms",
            "Structuring lawful retrenchment, redundancy, or mutual separation agreements (MSAs)",
            "Conducting formal domestic inquiry proceedings for employee misconduct under the Labour Act",
            "Appearing and advocating before the Labour Court (Shram Adalat) and Department of Labour"
        ],
        stages=[
            ServiceStage(
                step_number=1,
                title="Employment Matter Assessment",
                description="Reviewing employment contracts, job descriptions, HR policies, and statutory compliance status under Labour Act 2074.",
                duration_estimate="1 – 3 Days"
            ),
            ServiceStage(
                step_number=2,
                title="Policy Formulation / Disciplinary Protocol",
                description="Drafting compliant HR bylaws or structuring formal show-cause notices (Spastikaran) adhering to due process rules.",
                duration_estimate="3 – 7 Working Days"
            ),
            ServiceStage(
                step_number=3,
                title="Conciliation at Labour Office",
                description="Representing management or workers during statutory conciliation meetings before the competent Labour Officer.",
                duration_estimate="2 – 4 Weeks"
            ),
            ServiceStage(
                step_number=4,
                title="Labour Court Litigation",
                description="If conciliation fails, submitting formal pleadings and arguing before the Labour Court bench in Kathmandu.",
                duration_estimate="4 – 10 Months"
            ),
            ServiceStage(
                step_number=5,
                title="Decree Enforcement / Settlement Execution",
                description="Executing binding settlements or implementing court decrees regarding severance or reinstatement.",
                duration_estimate="2 – 4 Weeks post-verdict"
            )
        ],
        required_documents=[
            "Executed employment agreements, appointment letters, and job descriptions",
            "Official company HR Bylaws, Employee Handbook, and code of conduct",
            "All exchanged warning letters, show-cause notices (Spastikaran), and employee explanations",
            "Payroll slips, Social Security Fund (SSF) contribution records, and leave registers",
            "Minutes of Labour Relations Committee meetings"
        ],
        governing_laws=[
            {"act": "Labour Act 2074 (श्रम ऐन, २०७४)", "relevance": "Core employment statute: employment categories, working hours, minimum wage, termination procedures, and labour court powers"},
            {"act": "Labour Rules 2075 (श्रम नियमावली, २०७५)", "relevance": "Procedural regulations governing domestic inquiries, safety standards, and collective bargaining"},
            {"act": "Social Security Act 2074 (सामाजिक सुरक्षा ऐन, २०७४)", "relevance": "Mandatory employer-employee contributions to the Social Security Fund (SSF)"}
        ],
        rights_duties_limitations=[
            "Procedural Due Process Mandatory: Under Section 131 of the Labour Act 2074, an employer cannot terminate an employee for misconduct without issuing a formal show-cause notice providing at least seven days for written explanation.",
            "Mandatory SSF Registration: Employers are legally mandated to register all employees with the Social Security Fund from day one of employment.",
            "Probationary Period Limit: Statutory probation is strictly limited to six months under the Labour Act 2074; exceeding this timeline automatically confirms employment."
        ],
        fee_factors=[
            "Corporate retainer vs. individual employment dispute representation",
            "Number of affected employees (individual grievance vs. collective bargaining retrenchment)",
            "Forum of dispute (Labour Office conciliation vs. Labour Court trial)"
        ],
        consultation_preparation=[
            "Assemble the current employment contract and official job description",
            "Gather written records of all communications, warnings, and salary payment proofs",
            "Prepare a timeline of key events leading to the dispute or termination"
        ],
        faqs=[
            ServiceFAQ(
                question="Can an employer terminate an employee without notice in Nepal?",
                answer="No. Under the Labour Act 2074, termination without cause ('at-will') is prohibited. Termination can occur only on specific statutory grounds (such as grave misconduct, continued poor performance following notice, or lawful retrenchment approved by the Labour Office) with mandatory notice periods or pay in lieu."
            ),
            ServiceFAQ(
                question="Is enrollment in the Social Security Fund (SSF) compulsory for private companies?",
                answer="Yes. Under the Social Security Act 2074 and government notifications, all registered commercial entities in Nepal are legally mandated to enroll their employees and remit monthly statutory contributions (20% employer and 11% employee)."
            )
        ],
        related_articles=[
            {"title": "Proprietorship vs. Partnership vs. Private Limited in Nepal", "url": "/legal-resources/proprietorship-vs-partnership-vs-private-limited-nepal/"},
            {"title": "Essential Clauses Every Commercial Contract Must Contain", "url": "/legal-resources/essential-clauses-commercial-contracts-nepal/"}
        ],
        adjacent_services=[
            {"title": "Corporate & Business Law", "url": "/services/corporate-business-law/"},
            {"title": "Contract Drafting & Review", "url": "/services/contract-law/"}
        ],
        lead_advocate_slug="advocate-associate-corporate",
        trust_signals=[
            "Expert counsel on Labour Act 2074 compliance and Labour Court representation",
            "Trusted legal advisors to corporate HR teams and institutional employers",
            "Strategic risk mitigation balancing workplace harmony and legal compliance"
        ],
        conversion_prompt="Consult our employment law advocates to review HR bylaws, manage terminations, or defend Labour Court claims."
    ),
    ServicePage(
        slug="banking-financial-law",
        title="Banking & Financial Dispute Representation",
        h1="Banking, Financial Dispute & Cheque Dishonor Legal Representation in Nepal",
        meta_title="Banking & Financial Dispute Lawyers in Nepal | Cheque Bounce & DRT",
        meta_description="Legal counsel for banking disputes, cheque dishonor cases under Banking Offence Act 2064, loan recovery defense, and Debt Recovery Tribunal representation in Nepal.",
        service_code="BANK-09",
        short_intro=(
            "Financial disputes demand strategic evaluation of both civil recovery remedies and criminal penal provisions. We represent "
            "businesses, commercial creditors, borrowers, and corporate entities in banking disputes, cheque dishonor (cheque bounce) cases, "
            "loan recovery proceedings before the Debt Recovery Tribunal (DRT), and collateral auction disputes under the Banking Offence "
            "and Punishment Act 2064 and Negotiable Instruments Act 2034."
        ),
        hero_badge="Banking Offence Defense & DRT Tribunal Representation",
        hero_image="/assets/images/banking-law-nepal.svg",
        legal_problem_overview=(
            "Dishonored commercial cheques and contested bank recovery actions represent a major source of legal liability in Nepal. "
            "Crucially, a bounced cheque gives rise to two distinct legal avenues with fundamentally different procedures and timelines: "
            "a civil recovery lawsuit under the Negotiable Instruments Act 2034, or a state-investigated criminal proceeding under the Banking "
            "Offence and Punishment Act 2064. Missing statutory notice deadlines, failing to obtain bank dishonor memos, or mishandling "
            "Debt Recovery Tribunal summons can lead to severe asset auction or custodial arrest."
        ),
        relevant_situations=[
            "Recovering funds from dishonored commercial cheques via criminal or civil legal remedies",
            "Defending against malicious or exaggerated cheque bounce complaints before the High Court Commercial Bench",
            "Representation before the Debt Recovery Tribunal (Karja Vasuli Nyayadhikaran) in loan recovery disputes",
            "Challenging arbitrary bank interest calculations, penalty charges, or unlawful blacklisting (Kalo Suchi)",
            "Challenging irregular property public auctions conducted by commercial banks under the BAFIA 2073",
            "Structuring formal commercial loan security documentation and debt restructuring agreements"
        ],
        scope_of_assistance=[
            "Strategic comparative assessment advising clients between Negotiable Instruments Act vs. Banking Offence Act routes",
            "Drafting and serving statutory formal demand notices within strict legal timeframes",
            "Filing First Information Reports (FIRs) with Nepal Police Central Investigation Bureau (CIB) for banking fraud",
            "Formulating and filing civil money recovery plaints before competent District Courts",
            "Representing borrowers or creditors in ongoing Debt Recovery Tribunal (DRT) hearings in Kathmandu",
            "Filing writ petitions before the High Court or Supreme Court to stay arbitrary public auctions of collateral"
        ],
        stages=[
            ServiceStage(
                step_number=1,
                title="Cheque & Transaction Legal Audit",
                description="Examining the original cheque, bank return memo (stating insufficient funds), account details, and calculating statutory limitation deadlines.",
                duration_estimate="1 – 2 Days"
            ),
            ServiceStage(
                step_number=2,
                title="Statutory Legal Notice Issuance",
                description="Issuing formal demand notice giving the drawer the statutory period to pay, establishing legal proof of notice service.",
                duration_estimate="3 – 7 Working Days"
            ),
            ServiceStage(
                step_number=3,
                title="Filing Criminal FIR or Civil Lawsuit",
                description="Filing formal complaint with police under Banking Offence Act or filing civil recovery suit in District Court under Negotiable Instruments Act.",
                duration_estimate="1 – 3 Weeks"
            ),
            ServiceStage(
                step_number=4,
                title="Investigation / Court Trial Hearings",
                description="Police investigation, remand proceedings, charge-sheet submission, or court evidentiary trials before the High Court or District Bench.",
                duration_estimate="3 – 10 Months"
            ),
            ServiceStage(
                step_number=5,
                title="Verdict, Restitution & Asset Attachment",
                description="Securing judgment decree, executing full monetary restitution, or releasing seized collateral.",
                duration_estimate="1 – 3 Months post-verdict"
            )
        ],
        required_documents=[
            "Original dishonored cheque(s) with clear signatures and dates",
            "Official Bank Dishonor Memo / Return Slip issued by the drawee bank showing reason for dishonor",
            "Underlying contracts, invoices, bills, delivery challans, or promissory notes explaining the debt",
            "Proof of formal legal demand notice served upon the drawer (postal receipts, tracking slips)",
            "Citizenship or corporate registration documents of the complainant"
        ],
        governing_laws=[
            {"act": "Banking Offence and Punishment Act 2064 (बैंकिङ्ग कसूर तथा सजाय ऐन, २०६४)", "relevance": "Criminal penalties, police investigation, and High Court commercial bench trial for bounced cheques and banking fraud"},
            {"act": "Negotiable Instruments Act 2034 (विनिमय अधिकारपत्र ऐन, २०३४)", "relevance": "Civil remedy for cheque dishonor: principal recovery, statutory interest, and court decree"},
            {"act": "Bank and Financial Institutions Act 2073 (BAFIA 2073)", "relevance": "Banking operations, collateral auctions, and debtor obligations"},
            {"act": "Debt Recovery Act 2058 (ऋण असुली ऐन, २०५८)", "relevance": "Debt Recovery Tribunal procedures and enforcement of bank debt claims"}
        ],
        rights_duties_limitations=[
            "Strict Limitation Deadlines: Claims under both the Banking Offence Act and Negotiable Instruments Act carry strict statutory limitation periods starting from the date of cheque dishonor.",
            "Dual-Track Choice: Choosing between the Banking Offence route (penal custody focus) and the Negotiable Instruments route (pure civil asset recovery) requires careful strategic alignment with your ultimate objective.",
            "DRT Specialized Jurisdiction: Commercial bank recovery suits exceeding statutory loan amounts fall under the exclusive jurisdiction of the Debt Recovery Tribunal."
        ],
        fee_factors=[
            "Total transaction value and number of dishonored cheques",
            "Choice of legal pathway (Police investigation / High Court vs. District Court civil lawsuit)",
            "Urgency of seeking interim court stay orders against bank auction proceedings"
        ],
        consultation_preparation=[
            "Bring the original dishonored cheque and official bank dishonor slip",
            "Assemble all invoices, delivery receipts, or loan contracts proving the lawful origin of the debt",
            "Provide the full contact details and permanent address of the drawer"
        ],
        faqs=[
            ServiceFAQ(
                question="What is the difference between filing under the Banking Offence Act and the Negotiable Instruments Act?",
                answer="Under the Banking Offence and Punishment Act 2064, the case is investigated by the Nepal Police and prosecuted as a state criminal case before the High Court Commercial Bench, carrying potential imprisonment and full fine restitution. Under the Negotiable Instruments Act 2034, it is a private civil lawsuit filed directly in District Court seeking recovery of the cheque amount plus interest and statutory fines."
            ),
            ServiceFAQ(
                question="Can a commercial bank in Nepal auction property without court approval?",
                answer="Under BAFIA 2073, commercial banks possess statutory powers to initiate non-judicial public auctions of pledged collateral if the borrower defaults following mandatory 35-day and 15-day public notices. However, if the bank violates valuation rules, ignores loan agreements, or acts arbitrarily, the borrower can challenge the auction before the High Court through a writ petition."
            )
        ],
        related_articles=[
            {"title": "Essential Clauses Every Commercial Contract Must Contain", "url": "/legal-resources/essential-clauses-commercial-contracts-nepal/"},
            {"title": "What is a Civil Case under Nepalese Law?", "url": "/legal-resources/what-is-a-civil-case-nepal/"}
        ],
        adjacent_services=[
            {"title": "Civil Litigation & Dispute Resolution", "url": "/services/civil-litigation/"},
            {"title": "Criminal Law & Defence Representation", "url": "/services/criminal-law/"},
            {"title": "Corporate & Business Law", "url": "/services/corporate-business-law/"}
        ],
        lead_advocate_slug="senior-advocate-lead",
        trust_signals=[
            "Proven strategic success handling high-value cheque bounce and banking recovery matters",
            "Deep procedural experience appearing before High Court Commercial Benches and the DRT",
            "Fast, rigorous demand notice issuance and enforcement of financial rights"
        ],
        conversion_prompt="Consult our banking dispute advocates to recover funds or defend against cheque bounce claims."
    ),
    ServicePage(
        slug="mediation-dispute-resolution",
        title="Mediation & Alternative Dispute Resolution (ADR)",
        h1="Mediation, Arbitration & Alternative Dispute Resolution (ADR) in Nepal",
        meta_title="Mediation & Arbitration Lawyers in Nepal | Alternative Dispute Resolution",
        meta_description="Cost-effective, confidential mediation and arbitration representation in Nepal. Resolve commercial, property, and family disputes out of court under Mediation Act 2068.",
        service_code="ADR-10",
        short_intro=(
            "Court litigation can be time-consuming, adversarial, and public. We offer skilled, confidential Alternative Dispute "
            "Resolution (ADR) representation in commercial arbitration and professional mediation under the Mediation Act 2068 "
            "and Arbitration Act 2055. We help corporate entities, partners, and families resolve high-stakes disputes amicably, "
            "efficiently, and with binding legal enforceability."
        ),
        hero_badge="Certified Mediators & Commercial Arbitration Counsel",
        hero_image="/assets/images/mediation-adr-nepal.svg",
        legal_problem_overview=(
            "Traditional court proceedings in Nepal often stretch over several years through multiple layers of appeal, straining "
            "commercial relationships and eroding capital. Alternative Dispute Resolution offers a sophisticated, private, and expedited "
            "alternative. Under the Mediation Act 2068, mediated settlement deeds (Milapatra) carry the full binding force of a final court "
            "decree with zero risk of subsequent appeal. In commercial agreements, incorporating modern arbitration clauses under the "
            "Arbitration Act 2055 ensures disputes are resolved before neutral industry experts rather than congested court dockets."
        ),
        relevant_situations=[
            "Commercial partnership and shareholder disputes requiring confidential resolution without public exposure",
            "Contractual construction, supplier, and joint venture disputes with arbitration covenants",
            "Family matrimonial property, inheritance, and business succession disputes requiring delicate handling",
            "Court-annexed mediation mandated during ongoing District Court civil lawsuits",
            "Drafting customized dispute escalation, mediation, and institutional arbitration clauses in commercial contracts",
            "Enforcing domestic arbitral awards or executing mediated settlement agreements in court"
        ],
        scope_of_assistance=[
            "Representing corporate or individual parties in domestic commercial arbitration proceedings under NEPCA rules",
            "Acting as trained party advocates or neutral court-appointed mediators under the Mediation Act 2068",
            "Drafting binding, unambiguous Mediated Settlement Agreements (Milapatra Likhit)",
            "Submitting mediated settlement deeds to competent courts for immediate formal decree registration",
            "Challenging or enforcing arbitral awards before the High Court under the Arbitration Act 2055",
            "Conducting pre-dispute settlement negotiations and structured conciliation meetings"
        ],
        stages=[
            ServiceStage(
                step_number=1,
                title="Dispute Analysis & ADR Appropriateness",
                description="Assessing whether the dispute is legally eligible for mediation or arbitration, reviewing contract arbitration clauses, and identifying common interests.",
                duration_estimate="2 – 4 Days"
            ),
            ServiceStage(
                step_number=2,
                title="Mediator / Arbitrator Selection",
                description="Agreeing upon certified mediators or constituting the arbitral tribunal under the Arbitration Act 2055 or NEPCA rules.",
                duration_estimate="1 – 2 Weeks"
            ),
            ServiceStage(
                step_number=3,
                title="Mediation Sessions / Arbitral Hearings",
                description="Conducting structured, confidential dialogue, interest-based bargaining, and presenting legal arguments and factual submissions.",
                duration_estimate="2 Weeks – 3 Months"
            ),
            ServiceStage(
                step_number=4,
                title="Settlement Deed Drafting / Arbitral Award",
                description="Formulating comprehensive, legally binding settlement terms (Milapatra) or receiving the formal Arbitral Award.",
                duration_estimate="1 – 2 Weeks"
            ),
            ServiceStage(
                step_number=5,
                title="Court Formalization & Decree Execution",
                description="Recording the settlement with the court or enforcing the arbitral award as a final judicial decree.",
                duration_estimate="1 – 2 Weeks post-execution"
            )
        ],
        required_documents=[
            "Underlying contracts, leases, or deeds containing the arbitration or dispute resolution clause",
            "Chronological summary of disputed claims, financial figures, and communications",
            "Identification documents and board resolutions authorizing representation in mediation/arbitration",
            "Copies of court pleadings (if mediation is court-annexed)"
        ],
        governing_laws=[
            {"act": "Mediation Act 2068 (मध्यस्थता ऐन, २०६८)", "relevance": "Legal framework for community and institutional mediation, mediator duties, confidentiality, and enforceability of settlement deeds"},
            {"act": "Arbitration Act 2055 (मध्यस्थ ऐन, २०५५)", "relevance": "Constitution of arbitral tribunals, arbitration proceedings, awards, and High Court enforcement/challenge"},
            {"act": "Muluki Civil Procedure Code 2074", "relevance": "Statutory mandates requiring courts to refer eligible civil suits to court-annexed mediation"}
        ],
        rights_duties_limitations=[
            "Strict Confidentiality: Under Section 22 of the Mediation Act 2068, all statements, admissions, and settlement proposals made during mediation are strictly confidential and inadmissible in subsequent court litigation.",
            "Finality of Settlement: Once a mediated settlement deed (Milapatra) is recorded before a court, it carries the status of a final decree and cannot be appealed.",
            "Arbitrability Limits: Matters involving criminal prosecution, fundamental constitutional rights, or non-compoundable public interest issues cannot be resolved through arbitration."
        ],
        fee_factors=[
            "Format of dispute resolution (informal commercial mediation vs. full institutional arbitration tribunal)",
            "Number of hearing sessions, mediator/arbitrator honorariums, and venue logistics",
            "Complexity and financial quantum of the commercial claims"
        ],
        consultation_preparation=[
            "Review your commercial contract to see if it mandates arbitration or mediation prior to court action",
            "Define your walk-away position, core business priorities, and acceptable settlement compromises",
            "Prepare a clean schedule of damages or financial claims"
        ],
        faqs=[
            ServiceFAQ(
                question="Is a mediated settlement deed legally binding and enforceable in Nepal?",
                answer="Yes. Under the Mediation Act 2068 and Muluki Civil Procedure Code 2074, a settlement deed (Milapatra) agreed upon by parties and endorsed by the court has the exact same legal force as a judgment decree issued after a full trial, and can be directly executed through court bailiffs."
            ),
            ServiceFAQ(
                question="How does commercial arbitration differ from ordinary court litigation in Nepal?",
                answer="Arbitration is a private, confidential process where parties select expert arbitrators (often senior advocates, retired judges, or engineers) to adjudicate disputes under flexible procedural timetables. Unlike court litigation which can face multi-tiered appeals, an arbitral award is final and subject to very narrow challenge grounds under the Arbitration Act 2055."
            )
        ],
        related_articles=[
            {"title": "Mediation vs. Civil Litigation in Nepal: Key Differences", "url": "/legal-resources/mediation-vs-civil-litigation-nepal/"},
            {"title": "Resolving Shareholder and Partnership Disputes in Nepal", "url": "/legal-resources/shareholder-partnership-dispute-resolution-nepal/"}
        ],
        adjacent_services=[
            {"title": "Civil Litigation & Dispute Resolution", "url": "/services/civil-litigation/"},
            {"title": "Corporate & Business Law", "url": "/services/corporate-business-law/"},
            {"title": "Contract Drafting & Review", "url": "/services/contract-law/"}
        ],
        lead_advocate_slug="senior-advocate-lead",
        trust_signals=[
            "Certified mediators trained in interest-based commercial dispute negotiation",
            "Experience before the Nepal Council of Arbitration (NEPCA) and institutional tribunals",
            "Pragmatic approach focused on preserving commercial relationships and cutting litigation expenses"
        ],
        conversion_prompt="Explore confidential mediation or arbitration to resolve your dispute out of court efficiently."
    )
]
