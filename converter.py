import streamlit as st
import time

# Custom Styling
st.markdown(
    """
    <style>
        .main-title { 
            font-size: 3rem; 
            font-weight: bold; 
            text-align: center; 
            color: white;
            background: linear-gradient(45deg, #ff416c, #ff4b2b);
            padding: 20px;
            border-radius: 10px;
        }
        .stButton > button { 
            background: linear-gradient(90deg, #ff9966, #ff5e62);
            border-radius: 8px;
            color: white;
            font-size: 1.2rem;
            padding: 10px 20px;
        }
        .stButton > button:hover {
            background: linear-gradient(90deg, #ff5e62, #ff9966);
            transform: scale(1.05);
            transition: 0.3s ease-in-out;
        }
        .result-box {
            padding: 20px;
            background: #e3f2fd;
            border-radius: 8px;
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
            color: #1565c0;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            padding: 10px;
            font-size: 1.1rem;
            color: #666;
        }
        .footer a {
            margin: 0 10px;
            text-decoration: none;
            color: #1565c0;
            font-weight: bold;
        }
        .footer a:hover {
            color: #ff416c;
            transform: scale(1.1);
            transition: 0.3s ease-in-out;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page Title
st.markdown('<h1 class="main-title">🌟 Unit Converter 🌟</h1>', unsafe_allow_html=True)

# Conversion Functions
def convert_units(value, from_unit, to_unit, conversion_dict):
    return value * conversion_dict[from_unit] / conversion_dict[to_unit]

# Categories
conversion_types = {
    "Length 📏": {
        "units": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
        "values": {"Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001, "Mile": 1609.34, "Yard": 0.9144, "Foot": 0.3048, "Inch": 0.0254},
    },
    "Mass ⚖️": {
        "units": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"],
        "values": {"Kilogram": 1, "Gram": 0.001, "Milligram": 0.000001, "Pound": 0.453592, "Ounce": 0.0283495},
    },
    "Temperature 🌡️": {
        "units": ["Celsius", "Fahrenheit", "Kelvin"],
        "values": None,
    },
    "Speed 🏃": {
        "units": ["Meters per second", "Kilometers per hour", "Miles per hour", "Knots"],
        "values": {"Meters per second": 1, "Kilometers per hour": 0.277778, "Miles per hour": 0.44704, "Knots": 0.514444},
    },
    "Time ⏰": {
        "units": ["Second", "Minute", "Hour", "Day", "Week", "Month", "Year"],
        "values": {"Second": 1, "Minute": 60, "Hour": 3600, "Day": 86400, "Week": 604800, "Month": 2592000, "Year": 31536000},
    }
}

# Sidebar Selection
st.sidebar.markdown("### 🔍 Select Conversion Type")
conversion_type = st.sidebar.selectbox("", list(conversion_types.keys()))

units = conversion_types[conversion_type]["units"]

st.markdown("---")

# User Input
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### Enter Value")
    value = st.number_input("", min_value=0.0, value=1.0)
    
with col2:
    st.markdown("### From Unit")
    from_unit = st.selectbox("", units, key="from_unit")
    
with col3:
    st.markdown("### To Unit")
    to_unit = st.selectbox("", units, key="to_unit")

st.markdown("")

# Conversion Button
convert_button = st.button("🔄 Convert")

if convert_button:
    if conversion_type == "Temperature 🌡️":
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            elif to_unit == "Kelvin":
                result = value + 273.15
            else:
                result = value
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (value - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
            else:
                result = value
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = value - 273.15
            elif to_unit == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value
    else:
        conversion_values = conversion_types[conversion_type]["values"]
        result = convert_units(value, from_unit, to_unit, conversion_values)
    
    with st.spinner("🔄 Converting..."):
        time.sleep(1)
        st.markdown(f'<div class="result-box">{value} {from_unit} = {result:.4f} {to_unit}</div>', unsafe_allow_html=True)

st.markdown("---")

# 🔗 **Footer with GitHub, Streamlit, and LinkedIn & Your Name**
st.markdown(
    """
    <div style="text-align: center; margin-top: 20px;">
        <p style="font-size: 1.2rem;">🚀 Unit Converter by <strong>SAYYED JALEES</strong></p>
        <a href="https://github.com/syedjalees/unit-converter-py-sirZia" target="_blank" style="margin: 0 10px; text-decoration: none;">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="40px" alt="GitHub">
        </a>
        <a href="https://unit-converter-sirzia.streamlit.app/" target="_blank" style="margin: 0 10px; text-decoration: none;">
            <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" width="40px" alt="Streamlit">
        </a>
        <a href="https://www.linkedin.com/in/sayyed-jalees-a9ba0817b/" target="_blank" style="margin: 0 10px; text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40px" alt="LinkedIn">
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)