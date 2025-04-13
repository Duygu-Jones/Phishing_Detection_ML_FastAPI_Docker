# appUI.py
import streamlit as st
import requests
import re
from urllib.parse import urlparse
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🛡️",
    layout="centered"
)

# Function to extract features from URL
def extract_features_from_url(url):
    features = {}
    
    # Initialize with default values
    features["sfh"] = -1  
    features["popupwidnow"] = 0  
    features["sslfinal_state"] = -1  
    features["request_url"] = -1  
    features["url_of_anchor"] = -1  
    features["web_traffic"] = 0  
    features["url_length"] = -1 
    features["age_of_domain"] = -1  
    features["having_ip_address"] = 0 
    
    # Basic feature extraction logic
    # URL length
    if len(url) < 54:
        features["url_length"] = 1
    elif len(url) >= 54 and len(url) <= 75:
        features["url_length"] = 0
    else:
        features["url_length"] = -1
    
    # Having IP address
    ip_pattern = r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
    if re.search(ip_pattern, url):
        features["having_ip_address"] = 1
    else:
        features["having_ip_address"] = -1
    
    # SSL final state
    if url.startswith('https'):
        features["sslfinal_state"] = 1
    else:
        features["sslfinal_state"] = -1
    
    # More sophisticated feature extraction would go here for a production app
    
    return features

# Function to predict using the API
def predict_url(url_features):
    try:
        response = requests.post(
            "http://localhost:8000/predict/",
            json=url_features
        )
        return response.json()
    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to the API. Make sure the FastAPI backend is running.")
        return None

# Header
st.title("🛡️ Phishing URL Detector")
st.write("Enter a URL to check if it's legitimate or a phishing attempt.")

# URL Input
url = st.text_input("Enter URL:", placeholder="https://example.com")

# Check button
if st.button("Check URL"):
    if url:
        with st.spinner("Analyzing URL..."):
            # Extract features from URL
            features = extract_features_from_url(url)
            
            # Call API for prediction
            result = predict_url(features)
            
            if result:
                # Display results
                if result["prediction"] == 1:
                    st.success(f"**Result: {result['prediction_text']}**")
                else:
                    st.error(f"**Result: {result['prediction_text']}**")
                
                # Display probability
                st.write(f"Confidence: {result['probability']*100:.2f}%")
                
                # Display extracted features
                with st.expander("View URL Features"):
                    st.write("Features extracted from URL:")
                    df = pd.DataFrame([features])
                    st.dataframe(df)
    else:
        st.warning("Please enter a URL to check.")

# Information about the app
with st.expander("About this app"):
    st.write("""
    This application uses machine learning to detect phishing URLs. 
    The model analyzes several features of the provided URL to determine if it's legitimate or a phishing attempt.
    
    **How it works:**
    1. Enter a complete URL including http:// or https://
    2. Click "Check URL"
    3. The app will extract features from the URL and send them to the prediction API
    4. Results will show whether the URL is legitimate or potentially malicious
    """)

# Footer
st.markdown("---")
st.markdown("Developed with Streamlit, FastAPI and Machine Learning")