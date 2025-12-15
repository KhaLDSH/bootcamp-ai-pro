from __future__ import annotations

import json
from pathlib import Path

def write_json(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")


def write_markdown(report: dict, path: str | Path) -> None:    
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    cols = report.get("columns", [])
    missing = report.get("missing", {})
    non_missing = report.get("non_empty_counts", {})

    lines: list[str] = []
    lines.append("# CSV Profiling Report\n")
    lines.append(f"- Rows: **{report.get('rows', 0)}**")
    
    lines.append("## Overview\n")
    lines.append(f"- Total Rows: **{report.get('rows', 0)}**\n")
    
    
    lines.append("## Column Details\n")
    
    if not cols:
        lines.append("*No column data available to display.*\n")
    else:
        lines.append("| Column | Missing Count | non missing count | type | max age | max salary")
        lines.append("| :--- | :---: | :---: | :---: | :---: | :---: |")
        for col in cols:
            if col == 'age':
                lines.append(f'| {col} | {missing[col]} | {non_missing[col]} | {report["types"][col]} | {report["max age"]}')      
            else:
                lines.append(f'| {col} | {missing[col]} | {non_missing[col]} | {report["types"][col]} | { 0 }')      
        lines.append("\n") # Add a newline after the table
        
    full_content = "\n".join(lines)
    
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(full_content)
            
    except Exception as e:
        print(f"Error writing Markdown file: {e}")