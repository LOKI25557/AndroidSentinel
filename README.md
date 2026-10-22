# AndroidSentinel
AI-assisted Android application security and forensic analysis platform.

# AndroidSentinel
### AI-Assisted Android Application Security and Forensic Analysis Platform

AndroidSentinel is a web-based cybersecurity platform designed to analyze Android APK files using static analysis. It identifies potentially risky permissions, insecure configurations, suspicious code patterns, and embedded indicators. It generates explainable findings, an indicator-based risk score, and a forensic-style PDF report.

> **Important:** AndroidSentinel is designed to analyze APKs without installing or executing them. Uploaded files should be processed in a restricted worker environment.

## 🚀 Features

- **APK Upload:** Upload Android APK files for security analysis.
- **File Validation:** Validate file size and APK/ZIP structure.
- **SHA-256 Hashing:** Generate a cryptographic hash to identify the APK.
- **Manifest Analysis:** Extract package metadata, permissions, and components.
- **Static Code Analysis:** Identify selected potentially insecure code patterns.
- **Indicator Extraction:** Extract URLs, domains, IP addresses, and other investigation indicators.
- **Rule-Based Detection:** Generate findings with severity, confidence, and supporting evidence.
- **Risk Scoring:** Calculate a transparent indicator-based risk score.
- **Database Storage:** Store scan records, findings, indicators, and events in PostgreSQL.
- **Forensic Reports:** Generate downloadable PDF reports.
- **AI-Assisted Explanations:** Optionally explain existing findings using an LLM.
- **Scan History:** Review previous scans and compare results.
- **Security-First Design:** Process APKs without executing them.

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Frontend | React, TypeScript, Vite, Tailwind CSS, Recharts |
| Backend | Python, FastAPI, Pydantic, Uvicorn |
| APK Analysis | Androguard |
| File Processing | hashlib, zipfile, XML parsing |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Database Migrations | Alembic |
| Detection Rules | YAML, optional YARA |
| PDF Reports | ReportLab |
| Testing | Pytest, HTTPX |
| Deployment | Docker, Docker Compose |
| Version Control | Git and GitHub |
| Optional AI | LLM API |

## 🏗️ System Architecture

The platform consists of a React frontend, FastAPI backend, isolated analysis worker, PostgreSQL database, and PDF report generator.

```text
User / Analyst
      |
      v
React Frontend
      |
      v
FastAPI Backend
      |
      v
File Validation and SHA-256
      |
      v
Scan Creation and Queue
      |
      v
Isolated Analysis Worker
      |
      v
Androguard APK Parser
      |
      v
+----------------------------+
| Static Analysis Pipeline   |
|                            |
| Manifest Analysis          |
| Permission Analysis        |
| Code-Pattern Analysis      |
| Indicator Extraction       |
| Detection Rule Engine      |
| Risk Scoring               |
+----------------------------+
      |
      v
Structured Findings
      |
      v
PostgreSQL Database
      |
      +-------------------+
      |                   |
      v                   v
PDF Report Generator   React Dashboard
      |                   |
      v                   v
Downloadable Report   Results and Findings

Optional: Structured Findings --> AI Explanation Service
```

## 🔄 End-to-End Workflow

1. The user uploads an APK.
2. The backend validates the file and enforces upload limits.
3. The system calculates the SHA-256 hash and generates a unique scan ID.
4. A scan record is created and the APK is passed to an isolated worker.
5. Androguard parses the APK and extracts available metadata.
6. The analyzer examines manifest settings, permissions, and selected code patterns.
7. URLs, domains, IP addresses, and other selected indicators are extracted.
8. The rule engine generates findings with evidence, severity, and confidence.
9. The risk-scoring module calculates an indicator-based score.
10. Results are saved in PostgreSQL.
11. ReportLab generates a forensic-style PDF report.
12. The frontend displays the results and allows the user to download the report.
13. Optional AI assistance explains supplied findings without changing the scanner's evidence or severity.

## 📂 Project Structure

```text
AndroidSentinel/
├── frontend/
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── services/
│       └── types/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── api/
│   │   │   ├── scans.py
│   │   │   ├── findings.py
│   │   │   └── reports.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   │   ├── hashing.py
│   │   │   ├── apk_parser.py
│   │   │   ├── manifest_analysis.py
│   │   │   ├── code_analysis.py
│   │   │   ├── indicator_extraction.py
│   │   │   ├── rule_engine.py
│   │   │   ├── risk_scoring.py
│   │   │   ├── scanner.py
│   │   │   ├── ai_explainer.py
│   │   │   └── report_generator.py
│   │   └── db/
│   ├── tests/
│   │   ├── unit/
│   │   └── integration/
│   ├── requirements.txt
│   ├── alembic.ini
│   └── alembic/
├── worker/
│   ├── scan_job.py
│   └── Dockerfile
├── rules/
│   └── android_rules.yaml
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API_CONTRACT.md
│   ├── DATABASE_SCHEMA.md
│   └── TEST_PLAN.md
├── storage/
│   └── .gitkeep
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
```

This is the planned structure. Files should be added incrementally as the corresponding modules are implemented.

## ⚙️ Installation and Setup

### Prerequisites

Install the following tools:

- Python
- Git
- PostgreSQL
- Node.js and npm
- Visual Studio Code or another code editor

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AndroidSentinel
```

Replace the placeholder with your actual repository URL.

### 2. Create a Python Virtual Environment

**Windows PowerShell:**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

If PowerShell blocks activation in the current terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 3. Install Backend Dependencies

```bash
pip install fastapi "uvicorn[standard]" pydantic pydantic-settings
pip install python-multipart sqlalchemy alembic "psycopg[binary]"
pip install androguard lxml PyYAML reportlab pytest httpx
```

After verifying compatible versions, record them in `backend/requirements.txt`.

To install pinned dependencies later:

```bash
pip install -r backend/requirements.txt
```

### 4. Configure PostgreSQL

Create a PostgreSQL database named:

```text
androidsentinel
```

Create a local `backend/.env` file:

```dotenv
APP_NAME=AndroidSentinel
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/androidsentinel
MAX_UPLOAD_SIZE_MB=50
STORAGE_DIR=../storage
```

Replace `YOUR_PASSWORD` with your local database password.

Never commit `.env` files, database credentials, API keys, uploaded APKs, or sensitive reports. Provide an `.env.example` with placeholder values for collaborators.

### 5. Start the Backend

After the FastAPI application has been implemented:

```bash
cd backend
uvicorn app.main:app --reload
```

Open the following URLs:

- API health: http://127.0.0.1:8000/api/health
- Swagger API documentation: http://127.0.0.1:8000/docs

These endpoints require the corresponding routes to exist in the implementation.

### 6. Start the Frontend

After the frontend has been implemented:

```bash
cd frontend
npm install
npm run dev
```

### 7. Run Tests

From the backend directory:

```bash
python -m pytest
```

## 🔌 API Endpoints

The planned REST API includes:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Check API health |
| POST | `/api/scans` | Upload an APK and create a scan |
| GET | `/api/scans` | Retrieve scan history |
| GET | `/api/scans/{scan_id}` | Retrieve scan status and summary |
| GET | `/api/scans/{scan_id}/findings` | Retrieve detailed findings |
| GET | `/api/scans/{scan_id}/indicators` | Retrieve extracted indicators |
| GET | `/api/scans/{scan_id}/report` | Download the generated PDF report |

A scan response may contain:

```json
{
  "scan_id": "generated-unique-id",
  "status": "queued",
  "sha256": "computed-sha256-value",
  "filename": "sample.apk",
  "file_size": 123456
}
```

The values above are illustrative. The application must calculate the actual hash, generate the scan ID, and determine the status.

## 🔍 Finding Structure

Each detection rule should produce structured findings containing evidence and remediation guidance.

Example:

```json
{
  "rule_id": "PERM-001",
  "rule_version": "1.0",
  "title": "Sensitive permission requested",
  "severity": "medium",
  "confidence": 0.85,
  "description": "The application requests a sensitive permission.",
  "evidence": {
    "permission": "android.permission.READ_CONTACTS",
    "source": "AndroidManifest.xml"
  },
  "recommendation": "Verify that the permission is necessary for the app's intended functionality."
}
```

Each finding should contain:

- `rule_id`: Stable detection rule identifier
- `rule_version`: Version of the rule
- `title`: Short finding name
- `severity`: Critical, high, medium, low, or informational
- `confidence`: Value between 0 and 1 with a documented interpretation
- `description`: Explanation of the observed indicator
- `evidence`: Extracted data and source location, where available
- `recommendation`: Suggested defensive investigation or remediation

A permission request or code reference alone does not prove malicious behavior.

## 📊 Risk Scoring

Proposed example severity weights:

| Severity | Weight |
|---|---:|
| Critical | 10 |
| High | 7 |
| Medium | 4 |
| Low | 2 |
| Informational | 0 |

Example scoring formula:

```text
score = min(100, sum(weights of distinct findings))
```

Deduplicate repeated instances of the same underlying issue to avoid inflating the score.

| Score | Risk Level |
|---|---|
| 0–19 | Low |
| 20–39 | Moderate |
| 40–69 | High |
| 70–100 | Very High |

These thresholds must be validated through testing.

**Important:** The score is an indicator-based risk score, not a probability of malware. A score of 80 does not mean an application has an 80% chance of being malicious.

## 📄 Forensic Report

The PDF report should contain:

- Scan ID, timestamp, and analysis-tool version
- APK filename, file size, package name, and SHA-256
- Summary of findings by severity
- Detailed findings and evidence
- Extracted URLs, domains, and IP addresses
- Risk score and scoring explanation
- Optional AI-generated summary, clearly labelled
- Limitations and recommended next steps

Original scanner findings must remain separate from AI-generated explanations.

## 🧪 Testing and Validation

Use APKs you own or are authorized to examine. Begin with benign APKs and purpose-built test samples. Do not use live malware on an everyday machine.

Recommended test cases:

- Benign APK with ordinary permissions
- APK requesting sensitive permissions
- APK with a known insecure configuration
- APK containing test URLs and domains
- Malformed APK or ZIP archive
- File that is not an APK
- Oversized upload
- Interrupted or failed scan
- Repeated upload of the same file

For each test, compare expected and actual findings and verify the supporting evidence.

Track rule-level precision, recall when labelled ground truth is available, false-positive rate, scan completion rate, and processing time. Do not claim overall malware-detection accuracy without a suitable labelled dataset and reproducible methodology.

## 🔐 Security Considerations

- **Do not execute uploaded APKs.**
- Validate file structure and enforce size and decompression limits.
- Run parsing in a restricted worker with resource limits.
- Disable unrestricted worker network access.
- Keep credentials and API keys out of source code.
- Define retention periods for APKs, temporary files, and reports.
- Enforce authentication and authorization when required.
- Record scan events and tool/rule versions without logging secrets.
- Treat APK strings, comments, and resources as untrusted input.
- Restrict AI explanations to supplied evidence.
- Do not automatically visit every URL extracted from an APK.

## 🗓️ Six-Week Development Roadmap

| Week | Focus | Deliverable |
|---|---|---|
| 1 | Foundation | Repository, API setup, database connection, upload validation, hashing, scan record |
| 2 | APK Analysis | Androguard integration, manifest extraction, permissions, metadata |
| 3 | Detection Rules | Rule engine, indicators, evidence, scoring, unit tests |
| 4 | Integration | Scan history, result APIs, persistence, status tracking |
| 5 | Reports and AI | PDF reports and optional evidence-grounded explanations |
| 6 | Validation | Regression tests, worker isolation, documentation, security review, demonstration |

The timeline is a target and depends on the team's experience and available time. If the deadline is short, prioritize a reliable upload-to-report MVP and postpone AI and dynamic analysis.

## ⚠️ Limitations

- Static analysis cannot observe every runtime behavior.
- Obfuscated or dynamically loaded code may be difficult to inspect.
- Permissions and API references may be legitimate.
- Extracted indicators are not automatically malicious.
- Threat-intelligence services may be incomplete or outdated.
- AI explanations may be wrong and require verification.
- SHA-256 identifies file contents but does not prove authenticity or safety.
- Risk scores depend on the quality of detection rules and validation.

## 🤝 Contributing

1. Create a feature branch from the agreed base branch.
2. Work on your assigned module.
3. Follow the agreed API and finding contracts.
4. Add or update tests for every behavior change.
5. Run the test suite before pushing.
6. Open a pull request with a description of changes and test results.
7. Never commit credentials, `.env` files, sensitive reports, or uploaded APK samples.

## 📜 License

No license has been specified yet. Add a `LICENSE` file before distributing the project publicly, and verify that dependencies and included assets permit the intended use.

---

**AndroidSentinel's core principle:** Build a reliable and explainable static-analysis platform first. Make the upload → analyze → show evidence → score → report workflow dependable before introducing AI assistance or advanced analysis.
