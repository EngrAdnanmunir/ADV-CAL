import streamlit as st
import numpy as np

# Title of the app
st.title("Advanced Calculator")

# Subtitle with your name
st.subheader("Created by Engr. Adnan Munir")

# Input fields for the two numbers
num1 = st.number_input("Enter the first number:", step=1.0)
num2 = st.number_input("Enter the second number (optional):", step=1.0)

# Dropdown to select the operation
operation = st.selectbox("Select Operation:", [
    "Add", "Subtract", "Multiply", "Divide",
    "Exponentiation (num1 ^ num2)", "Square Root (√num1)", 
    "Sine (sin(num1))", "Cosine (cos(num1))", "Tangent (tan(num1))"
])

# Perform the calculation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.write(f"The result of {num1} + {num2} is {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.write(f"The result of {num1} - {num2} is {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.write(f"The result of {num1} * {num2} is {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.write(f"The result of {num1} / {num2} is {result}")
        else:
            st.write("Error: Division by zero is not allowed.")
    elif operation == "Exponentiation (num1 ^ num2)":
        result = num1 ** num2
        st.write(f"The result of {num1} ^ {num2} is {result}")
    elif operation == "Square Root (√num1)":
        if num1 >= 0:
            result = np.sqrt(num1)
            st.write(f"The square root of {num1} is {result}")
        else:
            st.write("Error: Square root of a negative number is not real.")
    elif operation == "Sine (sin(num1))":
        result = np.sin(np.radians(num1))
        st.write(f"The sine of {num1} degrees is {result}")
    elif operation == "Cosine (cos(num1))":
        result = np.cos(np.radians(num1))
        st.write(f"The cosine of {num1} degrees is {result}")
    elif operation == "Tangent (tan(num1))":
        result = np.tan(np.radians(num1))
        st.write(f"The tangent of {num1} degrees is {result}")

