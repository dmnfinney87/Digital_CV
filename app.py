from pathlib import Path
import streamlit as st
from PIL import Image

# General Settings
PAGE_TITLE = "Digital CV | David Finney"
PAGE_ICON = ":wave:"
NAME = 'David Finney'
DESCRIPTION = """
Hydrogeologist, Data Scientist, Project Manager finding solutions to client needs.
"""
EMAIL = 'dmnfinney87@gmail.com'

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/david-f-332611156/",
    "GitHub": "https://github.com/dmnfinney87"
}

PROJECTS = {
    "Master's Thesis - Using borehole geophysics to map groundwater salinity in San Joaquin Oil field": "https://csu-csus.esploro.exlibrisgroup.com/esploro/outputs/99257831002601671?skipUsageReporting=true",
    "Senior Thesis - Stable-Isotopic Record of the Younger Dryas Warming at Foy Lake, Montana": "https://www.researchgate.net/publication/301485455_STABLE-ISOTOPIC_RECORD_OF_THE_YOUNGER_DRYAS_WARMING_AT_FOY_LAKE_MONTANA"
}

# Set page configuration
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# path settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile_pic_path = current_dir / "picture.png"

# Print the absolute path for debugging
print("Absolute path of the image:", profile_pic_path.resolve())

# Check if the image file exists and open it
if profile_pic_path.is_file():
    profile_image = Image.open(profile_pic_path)
else:
    st.error(f"Image not found at {profile_pic_path}")
    profile_image = None

st.title("Hello there!🏞️")

# Layout with columns
col1, col2 = st.columns(2, gap="small")

# Display Profile Picture
with col1:
    if profile_image:
        st.image(profile_image, width=230)

# Display Profile Information
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(EMAIL)

    # Display Social Media Links
    for platform, link in SOCIAL_MEDIA.items():
        st.markdown(f"[{platform}]({link})", unsafe_allow_html=True)

    # Display Project Information
    st.subheader("Projects")
    for project_title, project_link in PROJECTS.items():
        st.markdown(f"[{project_title}]({project_link})", unsafe_allow_html=True)
