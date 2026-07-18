import streamlit as st
import json

st.set_page_config(page_title="PDF Hierarchy Viewer", layout="wide")
st.title("PDF Hierarchy Parser Results")

# Display the JSON file
st.subheader("Extracted JSON Hierarchy")
try:
    with open("output.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        st.json(data)
except FileNotFoundError:
    st.error("output.json not found. Run your parser script first!")

# Display the Markdown file
st.subheader("Generated Markdown")
try:
    with open("output.md", "r", encoding="utf-8") as f:
        st.markdown(f.read())
except FileNotFoundError:
    st.error("output.md not found.")