# not ready to be evaluated

# CSV Profiler 📊

A fast, reliable tool to analyze CSV files and generate data profiles in JSON and Markdown formats. This project features both a Command Line Interface (CLI) and a Streamlit Web UI.

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have [uv](https://github.com/astral-sh/uv) installed.

### 2. Setup
Clone the repository and navigate to the project root:

**bash**

`git clone https://github.com/KhaLDSH/bootcamp-ai-pro.git`

cd bootcamp-ai-pro/bootcamp/csv-profiler

Install dependencies and set up the local environment:
**bash**
`uv sync
`

### 3. Usage

#### **CLI Mode**
**bash**
`uv run python -m csv_profiler.cli data/sample.csv --preview`


#### **Web UI Mode**
**bash**
`uv run streamlit run src/csv_profiler/app.py
`

---

## 🛠️ Project Structure
\`\`\`text
csv-profiler/
├── data/               # Sample CSV files
├── src/
│   └── csv_profiler/   # Core package code
├── pyproject.toml      # Project metadata
└── uv.lock             # Lockfile
\`\`\`

---

## 📄 License
MIT
