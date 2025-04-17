import streamlit as st

st.title("BMI Calculator")

height = st.number_input("Enter your height (in cm)", min_value=0.0, format="%.2f")
weight = st.number_input("Enter your weight (in kg)", min_value=0.0, format="%.2f")

if st.button("Calculate BMI"):
    if height > 0:
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            st.info("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Height must be greater than zero.")
