import streamlit as st
import pandas as pd
import joblib

# Lodad the pre-trained model
model = joblib.load('mental_health_model.pkl')
st.title('Mental Health Prediction App')

# user input frame

age = st.number_input('Age',10,100)
daily_time = st.number_input('Daily Screen time(min)',0,1000)
social_time = st.number_input('Social Media Time(min)',0,1000)
neg = st.number_input('Negative Interactions Count',0,100)
pos = st.number_input('Positive Interactions Count',0,100)
sleep = st.number_input('Sleep Hours', 0.0, 30.0)
physical = st.number_input('Physical Activity(min)',0,300)

# Convert categorical using same encoder

encoder = joblib.load('label_encoder.pkl')

# Prepare input row

data = pd.DataFrame({
    "age":[age],
    "daily_screen_time_min":[daily_time],
    "social_media_time_min":[social_time],
    "negative_interactions_count":[neg],
    "positive_interactions_count":[pos],
    "sleep_hours":[sleep],
    "physical_activity_min":[physical]
    
    
    
})

# Predict

if st.button('Predict Mental Health State'):
    prediction = model.predict(data)[0]
    st.success(f'Predicted Mental State: {encoder.inverse_transform([prediction])[0]}')