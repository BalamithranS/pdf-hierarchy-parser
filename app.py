import streamlit as st
import json

# Set up the webpage layout
st.set_page_config(page_title="PDF Document Viewer", layout="centered")

try:
    # Load your JSON data
    with open("output.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Display the main document title
    st.title(data.get("title", "Document Viewer"))
    st.markdown("---")

    # Function to display sections and their sub-sections beautifully
    def display_section(section):
        level = section.get("level", 1)
        number = section.get("number", "")
        title = section.get("title", "")
        heading_text = f"{number} {title}".strip()

        # Format the visual size based on the section level
        if level == 1:
            st.markdown(f"## {heading_text}")
        elif level == 2:
            st.markdown(f"### {heading_text}")
        else:
            st.markdown(f"#### {heading_text}")

        # Print the actual paragraph text cleanly
        for item in section.get("content", []):
            if item.get("type") == "paragraph":
                st.write(item.get("text", ""))
        
        st.write("")  # Add a small spacing spacer

        # Recursively handle any nested subsections (children)
        for child in section.get("children", []):
            display_section(child)

    # Loop through and display all sections
    for section in data.get("sections", []):
        display_section(section)

except FileNotFoundError:
    st.error("Required data files not found. Please ensure output.json is in your repository.")
except Exception as e:
    st.error(f"An error occurred while loading the data: {e}")
