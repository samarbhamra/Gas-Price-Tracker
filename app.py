import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from forecast.forecast import make_forecast
from config import DB_URL

st.title("⛽ Gas Price Tracker & Forecaster")

engine = create_engine(DB_URL)

@st.cache_data
def load_data():
    return pd.read_sql("SELECT * FROM gas_prices", engine)

df = load_data()
st.write("### 📊 Raw Data", df)

city = st.selectbox("Select a City", df['city'].unique())
city_df = df[df['city'] == city][['date', 'price']].sort_values('date')

if st.button("Generate Forecast"):
    forecast = make_forecast(city_df)
    st.line_chart(forecast[['ds', 'yhat']].set_index('ds'))
