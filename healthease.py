import streamlit as st

st.set_page_config(page_title="Medical Report Summarizer", layout="wide")

st.title("🩺 Medical Report Summarizer")
st.write("Upload a medical report and get a simplified explanation in easy language.")

uploaded_file = st.file_uploader("Upload your medical report (PDF, TXT, or DOCX)", type=["pdf", "txt", "docx"])

if uploaded_file:
    st.success(f"✅ File uploaded: {uploaded_file.name}")
    
    # For now, we will just display file content if it's text
    try:
        file_text = uploaded_file.read().decode("utf-8")
        st.subheader("📄 Original Report Content")
        st.text(file_text)

        st.subheader("🧾 Simplified Summary")
        st.write("This is where your AI-generated summary will appear after integration.")
    except:
        st.warning("⚠ Cannot display this file type directly yet. Processing coming soon!")

st.sidebar.title("About This App")
st.sidebar.info(
    """
    This prototype converts medical reports into easy-to-understand summaries.  
    Future features:  
    - AI-based language simplification  
    - Translation into local languages  
    - Highlighting important health terms
    """
)
