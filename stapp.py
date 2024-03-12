# Load the joblib model
model = joblib.load('your_model.joblib')

# Create the Streamlit app
def main():
    st.title("Heart Failure Prediction")

    # Input form for user data
    st.header("Enter Patient Information")
    age = st.slider("Age", min_value=18, max_value=100, value=49)
    anaemia = st.selectbox("Anaemia", options=["No", "Yes"])
    creatinine_phosphokinase = st.number_input("Creatinine Phosphokinase", min_value=0, value=208)
    diabetes = st.selectbox("Diabetes", options=["No", "Yes"])
    ejection_fraction = st.slider("Ejection Fraction", min_value=0, max_value=100, value=17)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, value=68)
    platelets = st.number_input("Platelets", min_value=0, value=176)
    serum_creatinine = st.number_input("Serum Creatinine", min_value=0, value=40)
    serum_sodium = st.number_input("Serum Sodium", min_value=0, value=27)
    sex = st.selectbox("Sex", options=["Female", "Male"])
    smoking = st.selectbox("Smoking", options=["No", "Yes"])
    time = st.number_input("Time", min_value=0, value=148)

    # Preprocess user input
    anaemia = 1 if anaemia == "Yes" else 0
    diabetes = 1 if diabetes == "Yes" else 0
    sex = 1 if sex == "Male" else 0
    smoking = 1 if smoking == "Yes" else 0

    # Make predictions
    if st.button("Predict"):
        features = np.array([age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction,
                             blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time]).reshape(1, -1)
        prediction = model.predict(features)
        if prediction[0] == 1:
            st.error("The patient is predicted to have a heart failure.")
        else:
            st.success("The patient is predicted to not have a heart failure.")

if __name__ == "__main__":
    main()
