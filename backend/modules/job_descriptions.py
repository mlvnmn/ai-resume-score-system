"""
Job Descriptions Dataset
Comprehensive library of roles with descriptions and required skills.
"""

JOB_DESCRIPTIONS = {
    # ─── Software & Engineering ──────────────────────────────────────────
    "software_engineer": {
        "title": "Software Engineer",
        "category": "Engineering",
        "description": "Design, develop, and maintain scalable software solutions. Collaborate with cross-functional teams, write clean code, build RESTful APIs, and deploy using CI/CD pipelines.",
        "required_skills": ["Python", "JavaScript", "React", "Node.js", "SQL", "Git", "Docker", "REST", "CI/CD", "AWS"],
    },
    "senior_software_engineer": {
        "title": "Senior Software Engineer",
        "category": "Engineering",
        "description": "Lead technical design and implementation of complex systems. Mentor junior developers, drive architectural decisions, and ensure code quality across the team.",
        "required_skills": ["Python", "Java", "Microservices", "Docker", "Kubernetes", "AWS", "SQL", "Git", "CI/CD", "REST"],
    },
    "frontend_developer": {
        "title": "Frontend Developer",
        "category": "Engineering",
        "description": "Build responsive and performant user interfaces with modern JavaScript frameworks. Work closely with designers and backend engineers on seamless experiences.",
        "required_skills": ["JavaScript", "TypeScript", "React", "HTML", "CSS", "Tailwind", "Git", "REST", "Figma", "Angular"],
    },
    "backend_developer": {
        "title": "Backend Developer",
        "category": "Engineering",
        "description": "Build robust server-side applications, APIs, and database architectures. Ensure performance, scalability, and security of backend services.",
        "required_skills": ["Python", "Node.js", "Java", "SQL", "PostgreSQL", "MongoDB", "Docker", "REST", "GraphQL", "Redis"],
    },
    "fullstack_developer": {
        "title": "Full Stack Developer",
        "category": "Engineering",
        "description": "Build end-to-end web applications covering frontend UIs and backend services. Manage databases and deploy to cloud environments.",
        "required_skills": ["JavaScript", "TypeScript", "React", "Node.js", "Python", "SQL", "MongoDB", "Docker", "Git", "REST"],
    },
    "mobile_developer": {
        "title": "Mobile App Developer",
        "category": "Engineering",
        "description": "Develop native or cross-platform mobile applications for iOS and Android. Optimise for performance, battery life, and user experience.",
        "required_skills": ["React Native", "Flutter", "Swift", "Kotlin", "JavaScript", "REST", "Firebase", "Git", "CI/CD", "Figma"],
    },
    "ios_developer": {
        "title": "iOS Developer",
        "category": "Engineering",
        "description": "Design and build applications for Apple's iOS platform. Write clean Swift code, integrate with APIs, and publish to the App Store.",
        "required_skills": ["Swift", "Objective-C", "Xcode", "UIKit", "SwiftUI", "REST", "Git", "CI/CD", "Firebase", "Core Data"],
    },
    "android_developer": {
        "title": "Android Developer",
        "category": "Engineering",
        "description": "Build high-quality Android applications using Kotlin or Java. Work with Jetpack libraries, API integration, and material design principles.",
        "required_skills": ["Kotlin", "Java", "Android SDK", "Jetpack Compose", "REST", "Firebase", "Git", "CI/CD", "SQL", "MVVM"],
    },
    "embedded_systems_engineer": {
        "title": "Embedded Systems Engineer",
        "category": "Engineering",
        "description": "Develop firmware and software for embedded devices. Work with microcontrollers, RTOS, and hardware-software integration.",
        "required_skills": ["C", "C++", "Embedded C", "RTOS", "ARM", "Linux", "Python", "UART", "SPI", "I2C"],
    },
    "game_developer": {
        "title": "Game Developer",
        "category": "Engineering",
        "description": "Design and implement gameplay mechanics, physics, and rendering systems. Collaborate with artists and designers to create engaging experiences.",
        "required_skills": ["C#", "Unity", "Unreal Engine", "C++", "3D Math", "Physics", "Git", "Blender", "Shader Programming", "AI"],
    },
    "blockchain_developer": {
        "title": "Blockchain Developer",
        "category": "Engineering",
        "description": "Build decentralised applications and smart contracts. Work with blockchain protocols, tokenomics, and Web3 technologies.",
        "required_skills": ["Solidity", "Ethereum", "Web3.js", "JavaScript", "Smart Contracts", "DeFi", "Rust", "Go", "Docker", "Git"],
    },
    "qa_engineer": {
        "title": "QA / Test Engineer",
        "category": "Engineering",
        "description": "Design and execute test plans, automate regression tests, and ensure software quality. Work with CI/CD pipelines and testing frameworks.",
        "required_skills": ["Selenium", "Python", "JavaScript", "Jest", "Cypress", "CI/CD", "SQL", "Jira", "Git", "API Testing"],
    },
    "site_reliability_engineer": {
        "title": "Site Reliability Engineer (SRE)",
        "category": "Engineering",
        "description": "Ensure reliability, availability, and performance of production systems. Automate incident response, manage SLOs, and improve system resilience.",
        "required_skills": ["Linux", "Python", "Kubernetes", "Docker", "AWS", "Terraform", "Prometheus", "Grafana", "CI/CD", "Git"],
    },

    # ─── DevOps & Cloud ──────────────────────────────────────────────────
    "devops_engineer": {
        "title": "DevOps Engineer",
        "category": "DevOps & Cloud",
        "description": "Build and maintain CI/CD pipelines, manage cloud infrastructure, and ensure system reliability. Automate deployments and monitor performance.",
        "required_skills": ["Docker", "Kubernetes", "AWS", "Terraform", "Linux", "CI/CD", "Jenkins", "Git", "Python", "Nginx"],
    },
    "cloud_architect": {
        "title": "Cloud Architect",
        "category": "DevOps & Cloud",
        "description": "Design cloud-native architectures, migrate legacy systems, and optimise cloud costs. Define best practices for security, scalability, and disaster recovery.",
        "required_skills": ["AWS", "Azure", "GCP", "Terraform", "Kubernetes", "Docker", "Microservices", "Serverless", "Networking", "Security"],
    },
    "cloud_engineer": {
        "title": "Cloud Engineer",
        "category": "DevOps & Cloud",
        "description": "Provision and manage cloud infrastructure. Implement automation, monitoring, and security across cloud environments.",
        "required_skills": ["AWS", "Azure", "GCP", "Terraform", "Ansible", "Docker", "Linux", "Python", "Networking", "CI/CD"],
    },
    "platform_engineer": {
        "title": "Platform Engineer",
        "category": "DevOps & Cloud",
        "description": "Build internal developer platforms and tooling. Improve developer experience through automation, self-service infrastructure, and observability.",
        "required_skills": ["Kubernetes", "Docker", "Terraform", "Go", "Python", "CI/CD", "AWS", "Linux", "Prometheus", "GitOps"],
    },

    # ─── Data & Analytics ────────────────────────────────────────────────
    "data_scientist": {
        "title": "Data Scientist",
        "category": "Data & Analytics",
        "description": "Extract insights from large datasets, build predictive models, and communicate findings. Proficient in machine learning and data visualisation.",
        "required_skills": ["Python", "Machine Learning", "Deep Learning", "SQL", "Pandas", "NumPy", "TensorFlow", "Statistics", "Data Analysis", "AWS"],
    },
    "data_analyst": {
        "title": "Data Analyst",
        "category": "Data & Analytics",
        "description": "Analyse business data, create dashboards, and deliver actionable insights. Support decision-making with statistical analysis and reporting.",
        "required_skills": ["SQL", "Python", "Excel", "Tableau", "Power BI", "Statistics", "Data Analysis", "R", "Pandas", "Communication"],
    },
    "data_engineer": {
        "title": "Data Engineer",
        "category": "Data & Analytics",
        "description": "Build and maintain data pipelines, ETL processes, and data warehouses. Ensure data quality, reliability, and accessibility at scale.",
        "required_skills": ["Python", "SQL", "Spark", "Airflow", "Kafka", "AWS", "BigQuery", "Docker", "Data Engineering", "Big Data"],
    },
    "business_intelligence_analyst": {
        "title": "Business Intelligence Analyst",
        "category": "Data & Analytics",
        "description": "Transform raw data into meaningful business insights through dashboards and reports. Partner with stakeholders to drive data-informed decisions.",
        "required_skills": ["SQL", "Tableau", "Power BI", "Excel", "Python", "Data Analysis", "Statistics", "ETL", "Communication", "Analytical"],
    },
    "database_administrator": {
        "title": "Database Administrator",
        "category": "Data & Analytics",
        "description": "Manage, optimise, and secure database systems. Handle backups, replication, performance tuning, and capacity planning.",
        "required_skills": ["SQL", "PostgreSQL", "MySQL", "MongoDB", "Redis", "Oracle", "Linux", "Python", "Backup", "Performance Tuning"],
    },

    # ─── AI & Machine Learning ───────────────────────────────────────────
    "ml_engineer": {
        "title": "Machine Learning Engineer",
        "category": "AI & Machine Learning",
        "description": "Design, train, and deploy ML models at scale. Build inference pipelines, optimise model performance, and integrate with production systems.",
        "required_skills": ["Python", "TensorFlow", "PyTorch", "Machine Learning", "Docker", "AWS", "MLOps", "SQL", "NumPy", "Deep Learning"],
    },
    "ai_research_scientist": {
        "title": "AI Research Scientist",
        "category": "AI & Machine Learning",
        "description": "Conduct cutting-edge research in artificial intelligence. Publish papers, develop novel algorithms, and push the boundaries of AI capabilities.",
        "required_skills": ["Python", "PyTorch", "Deep Learning", "NLP", "Computer Vision", "Mathematics", "Statistics", "TensorFlow", "Research", "Machine Learning"],
    },
    "nlp_engineer": {
        "title": "NLP Engineer",
        "category": "AI & Machine Learning",
        "description": "Build natural language processing systems for text classification, sentiment analysis, chatbots, and information extraction.",
        "required_skills": ["Python", "NLP", "Transformers", "BERT", "spaCy", "NLTK", "Deep Learning", "TensorFlow", "PyTorch", "Machine Learning"],
    },
    "computer_vision_engineer": {
        "title": "Computer Vision Engineer",
        "category": "AI & Machine Learning",
        "description": "Develop image and video processing pipelines. Build object detection, segmentation, and recognition systems using deep learning.",
        "required_skills": ["Python", "OpenCV", "Computer Vision", "Deep Learning", "TensorFlow", "PyTorch", "CNN", "NumPy", "Docker", "AWS"],
    },
    "ai_product_manager": {
        "title": "AI Product Manager",
        "category": "AI & Machine Learning",
        "description": "Define product vision and roadmap for AI-powered products. Bridge the gap between technical ML teams and business stakeholders.",
        "required_skills": ["Product Management", "Machine Learning", "Agile", "Data Analysis", "Communication", "SQL", "Python", "Jira", "Leadership", "Statistics"],
    },

    # ─── Cybersecurity ───────────────────────────────────────────────────
    "cybersecurity_analyst": {
        "title": "Cybersecurity Analyst",
        "category": "Cybersecurity",
        "description": "Monitor security systems, investigate threats, and respond to incidents. Implement security best practices and conduct vulnerability assessments.",
        "required_skills": ["Security", "SIEM", "Linux", "Networking", "Firewall", "Python", "Penetration Testing", "SOC", "Compliance", "Incident Response"],
    },
    "penetration_tester": {
        "title": "Penetration Tester",
        "category": "Cybersecurity",
        "description": "Simulate cyberattacks to identify vulnerabilities. Perform web, network, and application security testing and provide remediation guidance.",
        "required_skills": ["Penetration Testing", "Burp Suite", "Linux", "Python", "Networking", "OWASP", "Kali", "Metasploit", "Security", "SQL"],
    },
    "security_engineer": {
        "title": "Security Engineer",
        "category": "Cybersecurity",
        "description": "Design and implement security controls for applications and infrastructure. Automate security processes and manage identity/access management.",
        "required_skills": ["Security", "AWS", "Linux", "Docker", "Python", "IAM", "Encryption", "CI/CD", "Networking", "Terraform"],
    },

    # ─── Design & UX ─────────────────────────────────────────────────────
    "ui_ux_designer": {
        "title": "UI/UX Designer",
        "category": "Design",
        "description": "Design intuitive user interfaces and experiences. Conduct user research, create wireframes, prototypes, and design systems.",
        "required_skills": ["Figma", "UI/UX", "Prototyping", "User Research", "Wireframing", "Adobe XD", "Design Systems", "HTML", "CSS", "Communication"],
    },
    "product_designer": {
        "title": "Product Designer",
        "category": "Design",
        "description": "Own the end-to-end design process from research to polished UI. Collaborate with engineers and PMs to ship user-centric products.",
        "required_skills": ["Figma", "UI/UX", "Prototyping", "User Research", "Design Systems", "Interaction Design", "Usability Testing", "HTML", "CSS", "Communication"],
    },
    "graphic_designer": {
        "title": "Graphic Designer",
        "category": "Design",
        "description": "Create visual assets for digital and print media. Design logos, marketing materials, social media content, and brand identities.",
        "required_skills": ["Photoshop", "Illustrator", "Figma", "InDesign", "Typography", "Branding", "Color Theory", "Communication", "Creativity", "UI/UX"],
    },

    # ─── Product & Management ────────────────────────────────────────────
    "product_manager": {
        "title": "Product Manager",
        "category": "Product & Management",
        "description": "Define product strategy, prioritise features, and drive product development. Work with engineering, design, and business teams to deliver value.",
        "required_skills": ["Product Management", "Agile", "Scrum", "Data Analysis", "SQL", "Jira", "Communication", "Leadership", "A/B Testing", "Analytics"],
    },
    "technical_product_manager": {
        "title": "Technical Product Manager",
        "category": "Product & Management",
        "description": "Bridge engineering and business teams. Define technical requirements, manage APIs, and drive platform strategy with deep technical knowledge.",
        "required_skills": ["Product Management", "API", "SQL", "Agile", "Python", "System Design", "Communication", "Jira", "Data Analysis", "Leadership"],
    },
    "engineering_manager": {
        "title": "Engineering Manager",
        "category": "Product & Management",
        "description": "Lead and grow engineering teams. Drive technical excellence, manage sprint planning, and balance engineering velocity with code quality.",
        "required_skills": ["Leadership", "Agile", "Scrum", "Python", "System Design", "CI/CD", "Communication", "Mentoring", "Project Management", "Git"],
    },
    "scrum_master": {
        "title": "Scrum Master",
        "category": "Product & Management",
        "description": "Facilitate agile ceremonies, remove blockers, and coach teams on scrum best practices. Drive continuous improvement and team velocity.",
        "required_skills": ["Scrum", "Agile", "Jira", "Communication", "Leadership", "Facilitation", "Kanban", "Project Management", "Retrospectives", "Coaching"],
    },
    "project_manager": {
        "title": "Project Manager",
        "category": "Product & Management",
        "description": "Plan, execute, and deliver projects on time and within budget. Manage stakeholders, risks, and resources across teams.",
        "required_skills": ["Project Management", "Agile", "Jira", "Communication", "Leadership", "Risk Management", "Budgeting", "Scrum", "MS Project", "Stakeholder Management"],
    },
    "technical_writer": {
        "title": "Technical Writer",
        "category": "Product & Management",
        "description": "Create clear technical documentation, API guides, and user manuals. Translate complex technical concepts into accessible content.",
        "required_skills": ["Technical Writing", "Documentation", "Markdown", "API", "Git", "Communication", "HTML", "Jira", "Analytical", "Research"],
    },

    # ─── Marketing & Growth ──────────────────────────────────────────────
    "digital_marketing_manager": {
        "title": "Digital Marketing Manager",
        "category": "Marketing",
        "description": "Plan and execute digital marketing campaigns across channels. Manage SEO, SEM, social media, and email marketing to drive growth.",
        "required_skills": ["SEO", "SEM", "Google Analytics", "Social Media", "Content Marketing", "Email Marketing", "PPC", "Communication", "Analytics", "A/B Testing"],
    },
    "seo_specialist": {
        "title": "SEO Specialist",
        "category": "Marketing",
        "description": "Optimise web content for search engines. Conduct keyword research, technical SEO audits, and link building to improve organic rankings.",
        "required_skills": ["SEO", "Google Analytics", "Keyword Research", "HTML", "Content Marketing", "Ahrefs", "Google Search Console", "Technical SEO", "Communication", "Analytics"],
    },
    "content_strategist": {
        "title": "Content Strategist",
        "category": "Marketing",
        "description": "Develop content strategy and editorial calendars. Create compelling content that drives engagement, leads, and brand awareness.",
        "required_skills": ["Content Marketing", "SEO", "Communication", "Analytics", "Social Media", "Copywriting", "CMS", "Research", "Creativity", "Strategy"],
    },
    "growth_hacker": {
        "title": "Growth Hacker",
        "category": "Marketing",
        "description": "Drive rapid user acquisition and retention through data-driven experimentation. Run A/B tests, optimise funnels, and scale growth channels.",
        "required_skills": ["Analytics", "A/B Testing", "SQL", "Python", "SEO", "Growth Marketing", "Data Analysis", "Communication", "Automation", "Product Management"],
    },

    # ─── Sales & Business ────────────────────────────────────────────────
    "business_analyst": {
        "title": "Business Analyst",
        "category": "Business",
        "description": "Analyse business processes, gather requirements, and translate them into technical specifications. Bridge the gap between business and IT teams.",
        "required_skills": ["Business Analysis", "SQL", "Excel", "Communication", "Requirements Gathering", "Jira", "Agile", "Data Analysis", "Process Mapping", "Analytical"],
    },
    "solutions_architect": {
        "title": "Solutions Architect",
        "category": "Business",
        "description": "Design technical solutions that meet client requirements. Present architectures, conduct POCs, and support sales engineering efforts.",
        "required_skills": ["AWS", "Azure", "System Design", "Microservices", "API", "Docker", "Kubernetes", "Communication", "Python", "Networking"],
    },
    "technical_support_engineer": {
        "title": "Technical Support Engineer",
        "category": "Business",
        "description": "Provide technical assistance to customers, troubleshoot issues, and escalate complex problems. Maintain knowledge bases and support documentation.",
        "required_skills": ["Troubleshooting", "Linux", "Networking", "Communication", "SQL", "Python", "Jira", "Customer Service", "Documentation", "API"],
    },

    # ─── Finance & Fintech ───────────────────────────────────────────────
    "quantitative_analyst": {
        "title": "Quantitative Analyst",
        "category": "Finance",
        "description": "Develop mathematical models for trading, risk, and pricing. Apply statistical methods and programming to financial data.",
        "required_skills": ["Python", "R", "Statistics", "Mathematics", "Machine Learning", "SQL", "Finance", "NumPy", "Pandas", "C++"],
    },
    "fintech_developer": {
        "title": "Fintech Developer",
        "category": "Finance",
        "description": "Build financial technology applications including payment systems, banking, and trading platforms. Ensure security and regulatory compliance.",
        "required_skills": ["Python", "Java", "SQL", "REST", "Docker", "Microservices", "Security", "AWS", "Git", "Kafka"],
    },

    # ─── Healthcare & Biotech ────────────────────────────────────────────
    "health_informatics_specialist": {
        "title": "Health Informatics Specialist",
        "category": "Healthcare",
        "description": "Manage healthcare data systems, ensure interoperability, and apply data analytics to improve patient outcomes and operational efficiency.",
        "required_skills": ["SQL", "Python", "HL7", "FHIR", "Data Analysis", "EHR", "Healthcare", "Statistics", "Communication", "Excel"],
    },
    "bioinformatics_engineer": {
        "title": "Bioinformatics Engineer",
        "category": "Healthcare",
        "description": "Develop pipelines for genomic data analysis. Work with biological datasets, sequence alignment tools, and statistical methods.",
        "required_skills": ["Python", "R", "Bioinformatics", "Linux", "Statistics", "Machine Learning", "SQL", "Git", "Docker", "AWS"],
    },

    # ─── Education ───────────────────────────────────────────────────────
    "instructional_designer": {
        "title": "Instructional Designer",
        "category": "Education",
        "description": "Design e-learning courses and training materials. Apply learning theories to create engaging educational content and assessments.",
        "required_skills": ["Instructional Design", "LMS", "E-Learning", "Communication", "Creativity", "HTML", "Video Editing", "Assessment Design", "Research", "Analytical"],
    },

    # ─── Legal ───────────────────────────────────────────────────────────
    "legal_tech_specialist": {
        "title": "Legal Tech Specialist",
        "category": "Legal",
        "description": "Implement and manage legal technology solutions. Automate contract review, e-discovery, and compliance workflows.",
        "required_skills": ["Legal Tech", "Python", "SQL", "NLP", "Communication", "Data Analysis", "Compliance", "Project Management", "Documentation", "Analytical"],
    },

    # ─── HR ──────────────────────────────────────────────────────────────
    "hr_analyst": {
        "title": "HR Analyst",
        "category": "Human Resources",
        "description": "Analyse workforce data, develop HR metrics, and support people strategy with data-driven insights and reporting.",
        "required_skills": ["Excel", "SQL", "Power BI", "HR Analytics", "Communication", "Data Analysis", "Statistics", "Python", "HRIS", "Analytical"],
    },
    "talent_acquisition_specialist": {
        "title": "Talent Acquisition Specialist",
        "category": "Human Resources",
        "description": "Source, screen, and recruit top talent. Manage the full hiring lifecycle and build employer brand through outreach and engagement.",
        "required_skills": ["Recruiting", "Communication", "LinkedIn", "ATS", "Interviewing", "Employer Branding", "HR", "Negotiation", "Sourcing", "Analytical"],
    },

    # ─── Operations ──────────────────────────────────────────────────────
    "supply_chain_analyst": {
        "title": "Supply Chain Analyst",
        "category": "Operations",
        "description": "Optimise supply chain operations through data analysis, demand forecasting, and process improvement. Manage vendor relationships and logistics.",
        "required_skills": ["Excel", "SQL", "Supply Chain", "Data Analysis", "SAP", "Communication", "Python", "Logistics", "Analytical", "Operations"],
    },
}


def get_job_description(role_key: str) -> dict | None:
    """Retrieve a job description by its key."""
    return JOB_DESCRIPTIONS.get(role_key)


def list_available_roles() -> list[dict]:
    """Return all available roles with key, title, and category."""
    return [
        {"key": key, "title": val["title"], "category": val.get("category", "Other")}
        for key, val in JOB_DESCRIPTIONS.items()
    ]
