from datetime import datetime

def render_markdown(report: dict) -> str:
    lines: list[str] = []
    lines.append(f"# CSV Profiling Report\n")
    lines.append(f"Generated: {datetime.now().isoformat(timespec='seconds')}\n")
    lines.append("## Summary\n")
    lines.append(f"- Rows: **{report['n_rows']}**")
    lines.append(f"- Columns: **{report['n_cols']}**\n")
    lines.append("## Columns\n")
    lines.append("| name | type | missing | missing_pct | unique |")
    lines.append("|---|---:|---:|---:|---:|")
    lines.extend([
    f"| {c['name']} | {c['type']} | {c['missing']} | {c['missing_pct']:.1f}% | {c['unique']} |"
    for c in report["columns"]
    ])
    
    lines.append("\n## Notes\n")
    lines.append("- Missing values are: `''`, `na`, `n/a`, `null`, `none`, `nan` (case-insensitive)")
   
    return "\n".join(lines)