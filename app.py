import streamlit as st
import pickle
import numpy as np

# Student information
student_info = """
**My Customer Churn Prediction Model**

Academic Year: 2023/24

**Student Name:** NJOKU CHINWENDU EDITH

**Aim:**

The project aims to enhance customer churn prediction in the retail industry using big data and machine learning techniques, comparing different models based on their computational speed to improve accuracy and efficiency in predicting customer churn. The final model deployed was an hybrid of SVM and RF with accuracy of 86.05."""


# Attempt to load the model
try:
    with open('voting_clf.pkl', 'rb') as f:
        model = pickle.load(f)
    st.write("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")

# Streamlit UI
st.title('Customer Churn Prediction')
st.markdown(student_info)

st.write('Enter customer details:')

# Input fields based on the variable data type
credit_score = st.number_input('Credit Score', min_value=300, max_value=850, value=600)
geography = st.selectbox('Geography', ['France', 'Spain', 'Germany'])
gender = st.selectbox('Gender', ['Male', 'Female'])
age = st.number_input('Age', min_value=18, max_value=100, value=30)
tenure = st.number_input('Tenure', min_value=0, max_value=10, value=5)
balance = st.number_input('Balance', min_value=0.0, value=1000.0, format="%.2f")
num_of_products = st.selectbox('Number of Products', [1, 2, 3, 4])
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])
estimated_salary = st.number_input('Estimated Salary', min_value=0.0, value=50000.0, format="%.2f")

# Prediction button
if st.button('Predict'):
    try:
        # Encode categorical variables
        geography_dict = {'France': 0, 'Spain': 1, 'Germany': 2}
        gender_dict = {'Male': 0, 'Female': 1}
        
        geography_encoded = geography_dict[geography]
        gender_encoded = gender_dict[gender]

        # Create a feature array for prediction
        features = np.array([[credit_score, geography_encoded, gender_encoded, age, tenure, balance, num_of_products, has_cr_card, is_active_member, estimated_salary]])
        
        # Perform prediction
        prediction = model.predict(features)
        
        # Display prediction result with color-coded box
        if prediction[0] == 1:
            st.markdown('<div style="background-color: red; padding: 10px; border-radius: 5px;"><h3 style="color: white;">Prediction: Customer will churn</h3></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="background-color: green; padding: 10px; border-radius: 5px;"><h3 style="color: white;">Prediction: Customer will stay</h3></div>', unsafe_allow_html=True)
            
    except Exception as e:
        st.error(f"Error predicting churn: {e}")
