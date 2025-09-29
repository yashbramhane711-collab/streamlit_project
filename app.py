import streamlit as st
import pickle 

st.title('Health Insurance Premium Prediction') 

age = st.number_input('Age', min_value=0)
bmi = st.number_input('BMI', min_value=0.0)
children = st.number_input('Number of Children:', min_value=0, step=1)  # ✅ Only integers
gender = st.selectbox('Gender', ['Male', 'Female'])
smoker = st.selectbox('Do You Smoke?', ['Yes', 'No'])

model = pickle.load(open('model.pkl','rb'))

if st.button('Predict'):
    gender_val = 0 if gender == 'Male' else 1
    smoker_val = 1 if smoker == 'Yes' else 0
    X_test = [[age, bmi, children, gender_val, smoker_val]]
    yp = str(round(model.predict(X_test)[0], 2))
    st.write('Your Premium is: ' + yp)
