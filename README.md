<h1 align="center">
Phishing Detection Web Application 🛡️
  
FastAPI - Streamlit - Docker
</h1>

<p align="center">
  <img src="![alt text](image-1.png)">
</p>

## Introduction

This project aims to detect phishing websites using machine learning algorithms. The application provides an easy-to-use interface for checking websites based on their features to determine if they are legitimate or potential phishing attempts.


## Problem Statement

Phishing attacks remain one of the most common cybersecurity threats, with millions of people falling victim each year. These attacks trick users into revealing sensitive information through fake websites that look legitimate. Traditional detection methods often rely on blocklists, which cannot identify new phishing sites.

This project addresses this challenge by developing a machine learning model that can identify potential phishing websites based on their URL features. The application is deployed as a web service using FastAPI for the backend and Streamlit for the user interface, making it accessible to users who need to verify suspicious URLs.


## Project Steps

1. **Data Collection & Preprocessing**: Cleaned and prepared website data for model training.
2. **Feature Engineering**: Extracted relevant features from URLs to identify phishing patterns.
3. **Model Development**: Trained a Random Forest Classifier for phishing detection.
4. **API Development**: Created a FastAPI backend to serve predictions.
5. **UI Creation**: Built a user-friendly interface with Streamlit.
6. **Containerization**: Packaged the application with Docker for easy deployment.
7. **Testing**: Developed test scripts to ensure the API works correctly.


## 🛠️ Tech Stack

- **Backend**: FastAPI - Fast, modern Python web framework for building APIs with automatic documentation.
- **Frontend**: Streamlit - Python library for creating interactive web applications for data science and machine learning.
- **Machine Learning**: Scikit-learn - For training the Random Forest Classifier model.
- **Data Processing**: Pandas, NumPy - For data manipulation and processing.
- **Containerization**: Docker - For packaging the application and its dependencies.
- **Visualization**: Matplotlib, Seaborn - For data visualization and model insights.


## ⬇️ Installation

### Option 1: Using Docker (Recommended)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/username/phishing_detection.git
   cd phishing_detection
   ```

2. **Build the Docker Image**
   ```bash
   docker build -t phishing_detector .
   ```

3. **Run the Container**
   ```bash
   docker run -p 8000:8000 --name phishing-api phishing-detector
   ```

4. **Access the API**
   - FastAPI Swagger UI: http://localhost:8000/docs

### Option 2: Using Virtual Environment

1. **Clone the Repository and Enter the Main Folder**
   ```bash
   git clone https://github.com/username/phishing_detection.git
   cd phishing_detection
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate on Windows
   venv\Scripts\activate
   
   # Activate on macOS/Linux
   source venv/bin/activate
   ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   # Start the FastAPI backend (in one terminal)
   uvicorn app.app:app --host 0.0.0.0 --port 8000
   
   # Start the Streamlit frontend (in another terminal)
   streamlit run app/appUI.py
   ```

5. **Access the Application**
   - Streamlit UI: http://localhost:8501
   - FastAPI API Swagger: http://localhost:8000/docs

### Managing Docker Containers

```bash
# View running containers
docker ps

# Stop the container
docker stop phishing-api

# Restart the container
docker start phishing-api

# View container logs
docker logs phishing-api

# Remove the container (must stop it first)
docker rm phishing-api
```


## 📂 Project Structure

```
phishing-detection-app/
├── app/
│   ├── app.py            # FastAPI backend application
│   └── test_api.py       # API test script
├── data/
│   └── Website Phishing.csv  # Dataset
├── models/
│   ├── model_training.py     # Model training script
│   └── RFC_best_model.pkl    # Trained Random Forest model
├── UI/
│   └── appUI.py          # Streamlit frontend
├── venv/                 # Virtual environment
├── .gitignore            # Git ignore file
├── Dockerfile            # Docker configuration
├── README.md             # Project documentation
└── requirements.txt      # Project dependencies
```


## 🔗 Related Links

- **Kaggle Notebook**: [URL Phishing Detection](https://www.kaggle.com/notebooks)
- **Medium Article**: [Building a Phishing Detection Web App with FastAPI and Streamlit](https://medium.com)
- **GitHub Repository**: [Phishing Detection Web Application](https://github.com/username/phishing_detection)


## 🌱 About Me

I'm a data scientist and machine learning engineer passionate about cybersecurity and AI applications.

You can find more about me and my work through the following links:

- **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/username/)
- **Website**: [Personal Website](https://website.com)
- **Kaggle**: [Kaggle Profile](https://www.kaggle.com/username)
- **GitHub**: [GitHub Profile](https://github.com/username)
- **Medium**: [Medium Blog](https://medium.com/@username)

Feel free to connect with me!


## 📚 References

- FastAPI. (2023). *FastAPI Framework*. https://fastapi.tiangolo.com/
- Streamlit. (2023). *Streamlit Documentation*. https://docs.streamlit.io/
- Docker Inc. (2023). *Docker Documentation*. https://docs.docker.com/
- Scikit-learn. (2023). *Random Forest Documentation*. https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html


## ✨ Acknowledgements

I would like to thank the open-source community for providing the tools and libraries that made this project possible. Special thanks to the FastAPI and Streamlit teams for their excellent documentation and user-friendly frameworks.

If you find this repository helpful, don't forget to give it a ⭐ star.

Happy coding! 👩‍💻✨

---

##### 📜 License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.