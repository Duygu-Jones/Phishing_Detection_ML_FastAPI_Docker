# test_api.py
import requests
import json

# API endpoint (adjust if deployed elsewhere)
API_URL = "http://localhost:8000/predict/"

# Test case 1: Likely phishing URL
phishing_features = {
    "sfh": -1,
    "popupwidnow": -1,
    "sslfinal_state": -1,
    "request_url": -1,
    "url_of_anchor": -1,
    "web_traffic": -1,
    "url_length": -1,
    "age_of_domain": -1,
    "having_ip_address": 1
}

# Test case 2: Likely legitimate URL
legitimate_features = {
    "sfh": 1,
    "popupwidnow": 1,
    "sslfinal_state": 1,
    "request_url": 1,
    "url_of_anchor": 1,
    "web_traffic": 1,
    "url_length": 1,
    "age_of_domain": 1,
    "having_ip_address": 0
}

# Function to test prediction
def test_prediction(features, expected_type):
    try:
        response = requests.post(API_URL, json=features)
        
        if response.status_code == 200:
            result = response.json()
            print(f"Test for {expected_type} URL:")
            print(f"  Prediction: {result['prediction_text']}")
            print(f"  Confidence: {result['probability']:.4f}")
            print(f"  Raw response: {json.dumps(result, indent=2)}")
            print("")
            return result
        else:
            print(f"Error: Received status code {response.status_code}")
            print(response.text)
            return None
    except Exception as e:
        print(f"Error connecting to API: {str(e)}")
        return None

if __name__ == "__main__":
    print("Testing Phishing Detection API...")
    print("-" * 50)
    
    # Test both cases
    test_prediction(phishing_features, "phishing")
    test_prediction(legitimate_features, "legitimate")