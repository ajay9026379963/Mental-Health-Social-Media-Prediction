# Mental-Health-Social-Media-Prediction

# Project Overview
This project leverages  Supervised Machine Learning to detect signs of mental health conditions (such as Depression, Anxiety, or Stress) from social media posts. By analyzing linguistic patterns, sentiment, and emotional cues, the model identifies individuals who may be at risk, providing a foundation for early intervention and support tools.

# Tech Stack
Language: Python

Libraries: Scikit-Learn, NLTK, Spacy, Pandas, Matplotlib
ML Models: Logistic Regression, Random Forest, Support Vector Machines (SVM)
Deployment: Streamlit (Web Dashboard)

# Dataset
The model was trained on datasets sourced from platforms like Reddit (r/Depression, r/Anxiety) and Twitter, containing thousands of labeled instances of mental health-related statements.

Target Classes: Anxiety, Depression, Stress, Normal.

# Project Pipeline
Data Extraction: Mining text data using APIs or public datasets (Kaggle).

Preprocessing: Removing URLs, HTML tags, and performing lemmatization.

Feature Extraction: Transforming text into numerical vectors using TF-IDF.

Model Training: Training multiple classifiers and performing Hyperparameter Tuning.

Evaluation: Using Confusion Matrices and ROC-AUC curves to validate performance.
