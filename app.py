import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
heart_disease_model = pickle.load(open(r'trained_heart_disease_model.sav', 'rb'))
diabetes_model = pickle.load(open(r'trained_diabeties_model.sav', 'rb'))
stroke_model = pickle.load(open(r'trained_brain_stroke_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Disease Prediction System',
                           ['Home',
                            'Heart Disease Prediction',
                            'Diabetes Prediction',
                            'Stroke Prediction'],
                           icons=['house', 'heart', 'person', 'activity'],
                           default_index=0)

# Home page
if selected == 'Home':
    st.title('Welcome to the Disease Prediction System')
    st.write("""
        This application helps in predicting the likelihood of various diseases based on user input data.
        \nSelect a prediction option from the sidebar to get started.
        \nThe available options are:
        - **Heart Disease Prediction**
        - **Diabetes Prediction**
        - **Stroke Prediction**
        \nMake sure to enter accurate data to get the best predictions.
    """)
    st.image("health-medical-healthcare-health.jpg", use_column_width=True)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction')
    st.write("""
        This section allows you to input your health data to predict the likelihood of heart disease.
        \nPlease provide accurate values for each of the following health metrics.
    """)

    # Splitting the input fields into two columns for better layout
    col1, col2 = st.columns(2)

    with col1:
        age = st.text_input('Age')
        sex = st.text_input('Sex (1 = male; 0 = female)')
        cp = st.text_input('Chest Pain Type (cp)')
        trestbps = st.text_input('Resting Blood Pressure (trestbps in mm Hg)')
        chol = st.text_input('Cholesterol (chol in mg/dl)')
        fbs = st.text_input('Fasting Blood Sugar (fbs > 120 mg/dl, 1 = true; 0 = false)')
        restecg = st.text_input('Resting Electrocardiographic Results (restecg)')

    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved (thalach)')
        exang = st.text_input('Exercise Induced Angina (exang, 1 = yes; 0 = no)')
        oldpeak = st.text_input('ST Depression Induced by Exercise Relative to Rest (oldpeak)')
        slope = st.text_input('Slope of the Peak Exercise ST Segment (slope)')
        ca = st.text_input('Number of Major Vessels Colored by Fluoroscopy (ca)')
        thal = st.text_input('Thalassemia (thal, 3 = normal; 6 = fixed defect; 7 = reversible defect)')

    # Prediction logic
    heart_disease_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            # Convert input data to float
            input_data = [
                float(age),
                float(sex),
                float(cp),
                float(trestbps),
                float(chol),
                float(fbs),
                float(restecg),
                float(thalach),
                float(exang),
                float(oldpeak),
                float(slope),
                float(ca),
                float(thal)
            ]

            # Make a prediction
            heart_disease_prediction = heart_disease_model.predict([input_data])

            if heart_disease_prediction[0] == 1:
                heart_disease_diagnosis = 'The patient is likely to have heart disease.'
            else:
                heart_disease_diagnosis = 'The patient is not likely to have heart disease.'

        except ValueError:
            heart_disease_diagnosis = 'Please enter valid numeric values for all fields.'

        st.success(heart_disease_diagnosis)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')
    st.write("""
        This section allows you to input your health data to predict the likelihood of diabetes.
        \nPlease provide accurate values for each of the following health metrics.
    """)

    col1, col2 = st.columns(2)

    with col1:
        pregnancies = st.text_input('Pregnancies')
        glucose = st.text_input('Glucose Level')
        blood_pressure = st.text_input('Blood Pressure (mm Hg)')
        skin_thickness = st.text_input('Skin Thickness (mm)')

    with col2:
        insulin = st.text_input('Insulin Level (mu U/ml)')
        bmi = st.text_input('BMI (Body Mass Index)')
        diabetes_pedigree_function = st.text_input('Diabetes Pedigree Function')
        age = st.text_input('Age')

    # Prediction logic
    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            # Convert input data to float
            input_data = [
                float(pregnancies),
                float(glucose),
                float(blood_pressure),
                float(skin_thickness),
                float(insulin),
                float(bmi),
                float(diabetes_pedigree_function),
                float(age)
            ]

            # Make a prediction
            diab_prediction = diabetes_model.predict([input_data])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The patient is likely to have diabetes.'
            else:
                diab_diagnosis = 'The patient is not likely to have diabetes.'

        except ValueError:
            diab_diagnosis = 'Please enter valid numeric values for all fields.'

        st.success(diab_diagnosis)

# Stroke Prediction Page
if selected == 'Stroke Prediction':
    st.title('Stroke Prediction')
    st.write("""
        This section allows you to input your health data to predict the likelihood of a stroke.
        \nPlease provide accurate values for each of the following health metrics.
    """)

    col1, col2 = st.columns(2)

    with col1:
        gender = st.text_input('Gender (1 = Male, 0 = Female)')
        age = st.text_input('Age')
        hypertension = st.text_input('Hypertension (1 = Yes, 0 = No)')
        heart_disease = st.text_input('Heart Disease (1 = Yes, 0 = No)')
        ever_married = st.text_input('Ever Married (1 = Yes, 0 = No)')

    with col2:
        work_type = st.text_input('Work Type (0 = Private, 1 = Self-employed, 2 = Govt Job, 3 = Children, 4 = Never worked)')
        residence_type = st.text_input('Residence Type (1 = Urban, 0 = Rural)')
        avg_glucose_level = st.text_input('Average Glucose Level (mg/dL)')
        bmi = st.text_input('BMI (Body Mass Index)')
        smoking_status = st.text_input('Smoking Status (0 = Never smoked, 1 = Formerly smoked, 2 = Smokes, 3 = Unknown)')

    # Prediction logic
    stroke_diagnosis = ''

    if st.button('Stroke Test Result'):
        try:
            # Convert input data to float
            input_data = [
                float(gender),
                float(age),
                float(hypertension),
                float(heart_disease),
                float(ever_married),
                float(work_type),
                float(residence_type),
                float(avg_glucose_level),
                float(bmi),
                float(smoking_status)
            ]

            # Make a prediction
            stroke_prediction = stroke_model.predict([input_data])

            # Convert the prediction to an integer
            stroke_prediction_value = int(stroke_prediction[0])

            # Use the integer directly for comparison
            if stroke_prediction_value == 1:
                stroke_diagnosis = 'The patient is likely to have a stroke.'
            else:
                stroke_diagnosis = 'The patient is not likely to have a stroke.'

        except ValueError:
            stroke_diagnosis = 'Please enter valid numeric values for all fields.'

        st.success(stroke_diagnosis)  