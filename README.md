
phishing-detection-app/
├── app/
│   ├── __pycache__/
│   ├── app.py            # FastAPI backend application
│   └── test_api.py       # API test script
├── data/
│   └── Website Phishing.csv  # Dataset
├── models/
│   ├── model_training.py     # Model training script
│   └── RFC_best_model.pkl    # Trained Random Forest model
├── UI/
│   └── appUI.py          # Streamlit frontend (not used)
├── venv/                 # Virtual environment
├── .gitignore            # Git ignore file
├── Dockerfile            # Docker configuration
├── README.md             # Project documentation
└── requirements.txt      # Project dependencies



# Phishing Detection Web Application - Setup Instructions


## Setup Options

### Option 1: Using Docker (Recommended)
1. Clone the repository:
    ```
    git clone https://github.com/username/phishing_detection.git
    cd phishing_detection
    ```

2. Build the Docker image:
   ```
   docker build -t phishing_detector .
    ```

3. Run the container:
   ```
    docker run -p 8000:8000 --name phishing-api phishing-detector
   ```

4. Access the application:
    - Start the FastAPI backend (in onather terminal)
    ```
    uvicorn app.app:app --host 0.0.0.0 --port 8000
    ```
    ```
   - FastAPI API Swagger: http://localhost:8000/docs
    ```

#### Access the Application
- Streamlit UI: http://localhost:8501
- FastAPI API Swagger: http://localhost:8000/docs

### Option 2: Using Virtual Environment on Streamlit
- Clone the repository and enter the main folder.

1. Create and activate a virtual environment:
    ```
    python -m venv venv
    ```
2. Activate the virtual environment:
    -  On Windows
        ```
        venv\Scripts\activate
        ```
    - On macOS/Linux
        ```
        source venv/bin/activate
        ```

3. Install required packages:
    ```
    pip install -r requirements.txt
    ```

4. Run the application:
 - Start the FastAPI backend (in one terminal)
    ```
    uvicorn app.app:app --host 0.0.0.0 --port 8000
    ```
- Start the Streamlit frontend (in another terminal)
    ```
    streamlit run app/appUI.py
    ```

#### Access the Application
- Streamlit UI: http://localhost:8501
- FastAPI API Swagger: http://localhost:8000/docs



## Required Files
- `RFC_best_model.joblib` (Trained machine learning model)
- `app.py` (FastAPI backend)
- `appUI.py` (Streamlit frontend)
- `requirements.txt` (Dependencies)



# Çalışan konteyneri görüntüleme
docker ps

# Konteyneri durdurma
docker stop phishing-api

# Konteyneri yeniden başlatma
docker start phishing-api

# Konteyner loglarını görüntüleme
docker logs phishing-api

# Konteyneri tamamen silme (önce durdurulmalı)
docker rm phishing-api