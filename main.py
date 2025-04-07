import streamlit as st

# st.markdown("""
#     <style>
#         .reportview-container {
#             background-color: #f44444;  /* Light background color */
#         }
#         .sidebar .sidebar-content {
#             background-color: #E0E0E0;  /* Secondary background color for sidebar */
#         }
#         .stButton>button {
#             background-color: #1E88E5;  /* Button primary color */
#             color: white;  /* Button text color */
#         }
#         .stTextInput>div>input {
#             background-color: #FFFFFF;  /* Input background color */
#             color: #000000;  /* Input text color */
#         }
#         h1 {
#             color: #1E88E5;  /* Header color */
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Set the page configuration
# st.set_page_config(page_title="Unit Converter", layout="centered")

# Title of the app
st.title("🔄 Unit Converter")

# Sidebar for selecting the category of conversion
category = st.sidebar.selectbox("Select conversion category", ("Length", "Mass", "Temperature"))

# Conversion functions
def length_converter(value, from_unit, to_unit):
    units = {
        "meters": 1,
        "kilometers": 1000,
        "miles": 1609.34,
        "feet": 0.3048,
        "inches": 0.0254
    }
    return value * units[to_unit] / units[from_unit]

def mass_converter(value, from_unit, to_unit):
    units = {
        "grams": 1,
        "kilograms": 1000,
        "pounds": 453.592,
        "ounces": 28.3495
    }
    return value * units[to_unit] / units[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return ((value - 32) * 5/9) + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return ((value - 273.15) * 9/5) + 32
    else:
        return value  # If the same units are selected

# Input fields for the converter
value = st.number_input("Enter value", min_value=0.0, step=0.1)

# Based on category, show appropriate unit options
if category == "Length":
    length_units = ["meters", "kilometers", "miles", "feet", "inches"]
    from_unit = st.selectbox("From unit", length_units)
    to_unit = st.selectbox("To unit", length_units)
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

elif category == "Mass":
    mass_units = ["grams", "kilograms", "pounds", "ounces"]
    from_unit = st.selectbox("From unit", mass_units)
    to_unit = st.selectbox("To unit", mass_units)
    if st.button("Convert"):
        result = mass_converter(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

elif category == "Temperature":
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From unit", temperature_units)
    to_unit = st.selectbox("To unit", temperature_units)
    if st.button("Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

