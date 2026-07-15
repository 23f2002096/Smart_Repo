# 🤖 Smart-Repo
### AI-Powered Source Code Knowledge Graph for Legacy System Onboarding

Smart-Repo is an AI-powered developer assistant that analyzes an uploaded source code repository, extracts its architecture using Python AST parsing, builds a knowledge graph, and enables developers to interact with the codebase using natural language.

The project is designed to help developers quickly understand unfamiliar or legacy codebases without manually reading hundreds of files.

---

## ✨ Features

### 📂 Repository Analysis
- Upload any Python repository as a ZIP file
- Automatic extraction of uploaded repositories
- Recursive repository scanning
- Python AST-based source code parsing

### 🔍 Static Code Analysis
- Detect Python files
- Extract:
  - Classes
  - Functions
  - Imports
  - Function Calls
- Preserve source code snippets
- Collect repository statistics

### 🕸 Knowledge Graph
- Build a directed knowledge graph using NetworkX
- Interactive visualization using PyVis
- Node types:
  - Files
  - Classes
  - Functions
  - Modules
- Relationship types:
  - CONTAINS
  - IMPORTS
  - CALLS

### 📊 Repository Dashboard
- Repository statistics
- Package analysis
- Import statistics
- Entry point detection
- Repository analytics

### 📁 Repository Explorer
- Browse parsed repository
- View extracted metadata
- Explore source files

### 🤖 AI Repository Assistant
Ask questions about the uploaded repository using natural language.

Examples:

- Explain RepositoryScanner
- Describe the project architecture
- How does repository upload work?
- Which files import Config?
- Explain parser package
- Where is create_app used?

### 🧠 Retrieval-Augmented Context
The AI answers using:

- Repository summary
- Relevant entities
- Source code snippets
- Retrieved files
- Project metadata

instead of relying only on the LLM.

---

# 🏗 Project Architecture

```
User
   │
   ▼
Upload Repository
   │
   ▼
Repository Scanner
   │
   ▼
AST Parser
   │
   ▼
Repository Parser
   │
   ▼
Knowledge Graph Builder
   │
   ├────────► Dashboard
   │
   ├────────► Repository Explorer
   │
   └────────► AI Context Builder
                     │
                     ▼
                Groq LLM
                     │
                     ▼
               AI Response
```

---

# 📁 Project Structure

```
Smart_Repo/
│
├── src/
│   └── smart_repo/
│       ├── parser/
│       ├── graph/
│       ├── services/
│       ├── routes/
│       ├── database/
│       ├── visualization/
│       ├── utils/
│       ├── app.py
│       └── config.py
│
├── templates/
│
├── static/
│
├── data/
│
├── tests/
│
├── requirements.txt
│
├── run.py
│
└── README.md
```

---

# ⚙ Tech Stack

## Backend

- Python
- Flask
- NetworkX
- PyVis

## AI

- Groq API
- LLM Prompt Engineering
- Retrieval-Augmented Generation (RAG)

## Frontend

- HTML
- CSS
- Bootstrap
- JavaScript

## Parsing

- Python AST
- pathlib

## Database

- SQLite

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/23f2002096/Smart_Repo.git

cd Smart_Repo
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
SECRET_KEY=your_secret_key

GROQ_API_KEY=your_groq_api_key
```

---

## Run Application

```bash
python run.py
```

Open

```
http://127.0.0.1:5000
```

---

# 🖥 Screens

- Home
- Repository Upload
- Dashboard
- Repository Explorer
- Knowledge Graph
- AI Chat

---

# 🧠 How Smart-Repo Works

## Step 1

Upload a ZIP repository.

↓

## Step 2

Repository is extracted.

↓

## Step 3

Python files are scanned.

↓

## Step 4

AST Parser extracts:

- Classes
- Functions
- Imports
- Calls

↓

## Step 5

Knowledge Graph is generated.

↓

## Step 6

Repository analytics are calculated.

↓

## Step 7

AI retrieves relevant repository context.

↓

## Step 8

Groq LLM generates repository-aware answers.

---

# 📊 Current Capabilities

✔ Repository Upload

✔ Repository Extraction

✔ Python Repository Scanner

✔ AST Parsing

✔ Class Extraction

✔ Function Extraction

✔ Import Analysis

✔ Function Call Analysis

✔ Repository Statistics

✔ Knowledge Graph Generation

✔ Interactive Graph Visualization

✔ Repository Explorer

✔ AI Repository Chat

✔ Context Retrieval

✔ Source Code Snippet Extraction

✔ Dashboard Analytics

---

# 📌 Example Questions

```
Explain RepositoryScanner

Explain upload pipeline

Describe project architecture

Which files import Config?

Where is create_app used?

Explain parser package

How are repositories parsed?

Explain GraphBuilder
```

---

# 📈 Future Improvements

- Multi-language support
- Class diagrams
- Sequence diagrams
- Dependency visualization
- Dead code detection
- Code smell detection
- README generation
- API documentation generation
- Mermaid diagram generation
- Multi-repository search
- Repository comparison
- Docker deployment

---

# 👨‍💻 Author

**Neeraj Kumar**

B.Tech Information Technology

Rajkiya Engineering College, Bijnor

---

# 📄 License

This project is licensed under the MIT License.