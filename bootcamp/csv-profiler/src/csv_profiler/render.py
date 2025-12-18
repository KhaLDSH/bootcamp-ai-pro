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
    
    # write statics
    lines.append("\n## Statics:\n")
    lines.append("\n### TEXT data:\n")
    lines.append(f"\nMost common name: **{report['columns'][0]['most common'][0]['value']}** by **{report['columns'][0]['most common'][0]['count']}** times\n")
    lines.append(f"\nMost common city: **{report['columns'][2]['most common'][0]['value']}** by **{report['columns'][2]['most common'][0]['count']}** times\n")
    
    lines.append("\n\n### NUMERICAL  data:\n")
    lines.append("\n***AGE***")
    lines.append(f"\nMax age:\t **{report['columns'][1]['max']}**\n")
    lines.append(f"\nMin age:\t **{report['columns'][1]['min']}**\n")
    lines.append(f"\nMean for ages:\t **{report['columns'][1]['mean']:.0f}**\n")
    lines.append("\n")
    lines.append("\n***SALARY***")
    lines.append(f"\nMax salary:\t **{report['columns'][3]['max']}**\n")
    lines.append(f"\nMin salary:\t **{report['columns'][3]['min']}**\n")
    lines.append(f"\nMean of salaries:\t **{report['columns'][3]['mean']:.2f}**\n")
    
    
    
    lines.append("\n## Notes\n")
    lines.append("- Missing values are: `''`, `na`, `n/a`, `null`, `none`, `nan` (case-insensitive)")
   
    return "\n".join(lines)