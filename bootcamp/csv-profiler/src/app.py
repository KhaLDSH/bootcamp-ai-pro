import streamlit as st
import csv
import json
from io import StringIO
from pathlib import Path

# Local imports from your package
from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown

# 1. Page Configuration
st.set_page_config(page_title="CSV Profiler 📊", layout="wide")
st.title("CSV Profiler")
st.caption("Upload CSV → profile → export JSON + Markdown")

# 2. Sidebar Setup
st.sidebar.header("Settings & Inputs")
show_preview = st.sidebar.checkbox("Show data preview", value=True)

# 3. File Upload Logic
uploaded = st.file_uploader("Upload a CSV file", type=["csv"])

rows = None
if uploaded:
    # Use utf-8-sig to handle Excel BOM markers safely
    text = uploaded.getvalue().decode("utf-8-sig")
    rows = list(csv.DictReader(StringIO(text)))

    if show_preview:
        st.subheader("📄 Data Preview (Top 5 rows)")
        st.write(rows[:5])
else:
    st.info("👋 Please upload a CSV file to get started.")

# 4. Report Generation Logic
if rows:
    st.divider()
    if st.button("Generate Profile Report", type="primary"):
        with st.spinner("Analyzing data..."):
            st.session_state["report"] = profile_rows(rows)
            st.success("Report generated!")

# 5. Display Results
# We pull from session_state so the report stays visible during exports
report = st.session_state.get("report")

if report:
    st.header("Profile Summary")
    
    # High-level metrics
    m1, m2 = st.columns(2)
    m1.metric("Total Rows", report["n_rows"])
    m2.metric("Total Columns", report["n_cols"])
    
    # Detailed Column Table
    st.subheader("Column Analysis")
    st.table(report["columns"])
    
    # Markdown Preview Expander
    with st.expander("View Markdown Report Preview"):
        st.markdown(render_markdown(report))

    # 6. Export & Saving Section
    st.divider()
    st.subheader("Export Report")
    
    # Sidebar input for custom naming
    report_name = st.sidebar.text_input("Export filename", value="data_profile")
    
    # Prepare export data
    json_text = json.dumps(report, indent=2, ensure_ascii=False)
    md_text = render_markdown(report)
    
    # UI Columns for Download Buttons
    btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 2])
    
    btn_col1.download_button(
        label="📥 Download JSON",
        data=json_text,
        file_name=f"{report_name}.json",
        mime="application/json"
    )
    
    btn_col2.download_button(
        label="📥 Download Markdown",
        data=md_text,
        file_name=f"{report_name}.md",
        mime="text/markdown"
    )

    # Local storage button
    if btn_col3.button("📂 Save to 'outputs/' folder"):
        out_dir = Path("outputs")
        out_dir.mkdir(parents=True, exist_ok=True)
        
        json_path = out_dir / f"{report_name}.json"
        md_path = out_dir / f"{report_name}.md"
        
        json_path.write_text(json_text, encoding="utf-8")
        md_path.write_text(md_text, encoding="utf-8")
        
        st.toast(f"Saved to {out_dir}/", icon="✅")
        st.success(f"Files successfully written to local disk: **{json_path}** and **{md_path}**")