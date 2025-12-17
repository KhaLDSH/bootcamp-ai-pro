import csv
from io import StringIO
import streamlit as st
import pandas as pd

from csv_profiler.profiling import profile_rows

# 1. Page Configuration
st.set_page_config(page_title="CSV Profiler", layout="wide")
st.title("CSV Profiler")

# 2. Sidebar/Inputs
uploaded = st.file_uploader("Upload a CSV", type=["csv"])
show_preview = st.checkbox("Show preview", value=True)
disply_as_md = st.checkbox("display as markdown", value=True)

    
# 3. Processing Logic
if uploaded is not None:
    # Use a try-block to catch decoding errors
    try:

        
        # Streamlit uploaded files are 'BytesIO'. 
        text = uploaded.getvalue().decode("utf-8-sig")
        
        # Convert text to a file-like object and then to a list of dicts
        # Note: We use list() here because we need to access the data 
        rows = list(csv.DictReader(StringIO(text)))

        # 4. Display Metadata
        st.write(f"**Filename:** {uploaded.name}")
        st.write(f"**Rows loaded:** {len(rows)}")

        # 5. Conditional Preview
        if show_preview and rows:
            st.subheader("Data Preview (Top 5 Rows)")
            if disply_as_md:
                st.markdown(rows[:7]) # st.table or st.dataframe looks better than st.write
            else:
                st.dataframe(rows[:7]) # st.table or st.dataframe looks better than st.write
        
        if st.button("Generate Report") and rows is not None:
            report = profile_rows(rows)
            
            st.write(report["columns"])
            with st.expander("Raw JSON (debug)", expanded=False):
                st.json(report)
            
            st.session_state["report"] = report
            st.dataframe(report)
            
    except Exception as e:
        st.error(f"Error processing file: {e}")

else:
    st.info("Upload a CSV to begin.")