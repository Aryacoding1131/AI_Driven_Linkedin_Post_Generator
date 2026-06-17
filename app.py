import os
import streamlit as st
from PIL import Image

from modules.graph_builder import graph

# ----------------------------------------
# Page Configuration
# ----------------------------------------
st.set_page_config(
    page_title="AI LinkedIn Post Generator",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ----------------------------------------
# Custom CSS
# ----------------------------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg,#0f172a,#1e293b);
}

h1 {
    color: #ffffff;
    text-align: center;
    font-size: 42px;
}

.subtitle {
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
    margin-bottom:30px;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

div[data-testid="stFileUploader"] {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 15px;
    border: 2px dashed #38bdf8;
}

.stButton>button {
    width:100%;
    background-color:#2563eb;
    color:white;
    border-radius:10px;
    height:50px;
    font-size:18px;
    border:none;
}

.stButton>button:hover {
    background-color:#1d4ed8;
    color:white;
}

.result-box {
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    border-left:5px solid #38bdf8;
    color:white;
    font-size:17px;
}

.css-1d391kg {
    background-color: #111827;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------
# Header
# ----------------------------------------
st.markdown("<h1>🚀 AI LinkedIn Post Generator</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <div class='subtitle'>
    Upload your certification and let AI generate a professional LinkedIn post using
    <b>Groq + LangChain + LangGraph + NLP</b>.
    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------------------------
# Sidebar
# ----------------------------------------
st.sidebar.title("⚙️ Settings")

style = st.sidebar.selectbox(
    "Post Style",
    [
        "Professional",
        "Technical",
        "Inspirational",
        "Casual"
    ]
)

include_hashtags = st.sidebar.checkbox(
    "Include Hashtags",
    value=True
)

include_gratitude = st.sidebar.checkbox(
    "Include Gratitude Message",
    value=True
)

# ----------------------------------------
# Main Layout
# ----------------------------------------
left, right = st.columns([1, 1])

with left:

    uploaded_file = st.file_uploader(
        "📂 Upload Certificate",
        type=["jpg", "jpeg", "png", "pdf"]
    )

    if uploaded_file is not None:

        file_path = os.path.join(
            UPLOAD_FOLDER,
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        extension = uploaded_file.name.split(".")[-1].lower()

        if extension in ["jpg", "jpeg", "png"]:
            image = Image.open(uploaded_file)
            st.image(
                image,
                caption="Certificate Preview",
                use_container_width=True
            )
        else:
            st.success("📄 PDF uploaded successfully.")

with right:

    st.markdown("### 📝 Generated LinkedIn Post")

    if uploaded_file is not None:

        if st.button("✨ Generate Post"):

            with st.spinner("🔍 Reading certificate and generating content..."):

                initial_state = {
                    "file_path": file_path,
                    "extracted_text": "",
                    "processed_text": {},
                    "prompt": "",
                    "linkedin_post": "",
                    "style": style
                }

                result = graph.invoke(initial_state)

                st.markdown(
                    f"""
                    <div class="result-box">
                    {result["linkedin_post"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.download_button(
                    label="💾 Download LinkedIn Post",
                    data=result["linkedin_post"],
                    file_name="linkedin_post.txt",
                    mime="text/plain"
                )

                with st.expander("📄 View Extracted Certificate Text"):
                    st.write(result["extracted_text"])

    else:
        st.info("Upload a certificate to get started!")

# ----------------------------------------
# Footer
# ----------------------------------------
st.markdown("---")
st.caption(
    "Built with ❤️ using Streamlit, LangChain, LangGraph, Groq LLMs, and NLP."
)
