import streamlit as st
import requests
import os

API_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(page_title="SmartSDLC - AI-Powered Requirement Analyzer")
st.title("📄 SmartSDLC - AI-Powered Requirement Analyzer")
st.write("Upload a requirement document (PDF) to classify it into SDLC phases.")

uploaded_file = st.file_uploader("Upload a requirement document (PDF)", type=["pdf"])

if uploaded_file:
    st.write(f"✅ File selected: {uploaded_file.name}")

    if st.button("Analyze Document"):
        with st.spinner("Analyzing... Please wait."):
            files = {"file": (uploaded_file.name, uploaded_file.read(), "application/pdf")}
            try:
                response = requests.post(API_URL, files=files)
                data = response.json()

                if "pdf_path" in data:
                    pdf_path = data["pdf_path"]
                    st.success("✅ Document processed successfully!")

                    if os.path.exists(pdf_path):
                        with open(pdf_path, "rb") as f:
                            pdf_bytes = f.read()
                            st.download_button(
                                label="📥 Download SDLC Output PDF",
                                data=pdf_bytes,
                                file_name=os.path.basename(pdf_path),
                                mime="application/pdf"
                            )
                    else:
                        st.error("The output PDF file was not found on the backend.")
                else:
                    st.error(data.get("error", "Unexpected response from the server."))

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
