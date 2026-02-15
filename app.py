import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("🎓 Student Performance Prediction System")
st.write("Machine Learning Based Prediction")

data = {
    'Hours_Studied': [1,2,3,4,5,6,7,8,9,10],
    'Attendance': [60,65,70,75,80,85,90,95,100,100],
    'Previous_Score': [50,55,60,65,70,75,80,85,90,95],
    'Final_Score': [52,57,63,68,74,78,85,88,92,98]
}

df = pd.DataFrame(data)

X = df[['Hours_Studied', 'Attendance', 'Previous_Score']]
y = df['Final_Score']

model = LinearRegression()
model.fit(X, y)

st.subheader("Enter Student Details")

hours = st.slider("Hours Studied", 0, 12, 5)
attendance = st.slider("Attendance (%)", 0, 100, 75)
previous = st.slider("Previous Score", 0, 100, 60)

if st.button("Predict"):
    prediction = model.predict([[hours, attendance, previous]])
    st.success(f"Predicted Final Score: {prediction[0]:.2f}")