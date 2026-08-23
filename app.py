import streamlit as st
import numpy as np
import pandas as pd
import sklearn


st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

h1 {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
}

h2, h3 {
    font-weight: bold;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 45px;
    font-size: 18px;
    font-weight: bold;
}

div[data-testid="stSidebar"] {
    padding-top: 20px;
}

div[data-testid="stSidebar"] h1,
div[data-testid="stSidebar"] h2,
div[data-testid="stSidebar"] h3 {
    font-size: 22px;
}

.prediction-box {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)
pipe = pickle.load(open("pipe.pkl","rb"))
df=pd.read_csv("cleaned-home-data.csv")
st.title("🏠 House Price Prediction App")


locations = sorted(df["Location"].dropna().unique())
transactions = sorted(df["Transaction"].dropna().unique())
furnishings = sorted(df["Furnishing"].dropna().unique())
parking_types = sorted(df["Parking Type"].dropna().unique())
states = sorted(df["state"].dropna().unique())

Location = st.sidebar.selectbox("Select Location", locations)

Carpet_Area = st.sidebar.number_input("Enter Carpet Area",
    min_value=100.0,
    max_value=10000.0,
    value=800.0,
    step=50.0
)

Transaction = st.sidebar.selectbox("Select Transaction",transactions)

Furnishing = st.sidebar.selectbox("Select Furnishing",furnishings)
    

Bathroom = st.sidebar.number_input("Enter Bathroom",min_value=1.0,max_value=10.0,value=2.0,step=1.0
)

Balcony = st.sidebar.number_input("Enter Balcony",min_value=0.0,max_value=10.0,value=1.0,step=1.0)


Area = st.sidebar.number_input("Enter Area (in sqft)",min_value=100.0,max_value=20000.0,value=1000.0,step=50.0)

BHK = st.sidebar.number_input("Enter BHK",min_value=1.0,max_value=10.0,value=2.0,step=1.0)

FlatFloor = st.sidebar.number_input("Enter Flat Floor",min_value=1.0,max_value=100.0,value=3.0,step=1.0)

TotalFloors = st.sidebar.number_input("Enter Total Floors",min_value=1.0,max_value=100.0,value=10.0,step=1.0)

ParkingNumbers = st.sidebar.number_input("Enter Parking Numbers",min_value=0.0,max_value=10.0,value=1.0,step=1.0)

Parking_Type = st.sidebar.selectbox("Select Parking Type",parking_types)

state = st.sidebar.selectbox("Select State",states)

if st.sidebar.button("🔮 Predict Price"):
    st.write("You have selected:")
    st.write(f"Location: {Location}")
    st.write(f"Carpet Area: {Carpet_Area}")
    st.write(f"Transaction: {Transaction}")
    st.write(f"Furnishing: {Furnishing}")
    st.write(f"Bathroom: {Bathroom}")
    st.write(f"Balcony: {Balcony}")
    st.write(f"Area: {Area}")
    st.write(f"BHK: {BHK}")
    st.write(f"Flat Floor: {FlatFloor}")
    st.write(f"Total Floors: {TotalFloors}")
    st.write(f"Parking Numbers: {ParkingNumbers}")
    st.write(f"Parking Type: {Parking_Type}")
    st.write(f"State: {state}")

    # Check for user input

    myinput = [[Location,Carpet_Area,Transaction,Furnishing,Bathroom,Balcony,Area,BHK,
                FlatFloor,TotalFloors,ParkingNumbers,Parking_Type,state]]

    columns = ['Location','Carpet Area','Transaction','Furnishing','Bathroom','Balcony','Area(in sqft)','BHK',
               'FlatFloor','TotalFloors','ParkingNumbers','Parking Type','state']

    myinput = pd.DataFrame(data=myinput, columns=columns)

    result = pipe.predict(myinput)
    
    if result[0] < 0:
        st.write("Sorry! Please check your input values.")
    else:
        st.markdown(
            f"""
            <div class="prediction-box">
                <h2>🏠 Predicted House Price</h2>
                <h1>₹ {result[0]:.2f} Crores</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    
