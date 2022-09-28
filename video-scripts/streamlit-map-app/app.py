import streamlit as st
import pandas as pd
# removed np as it was never used here

st.title("My sexy title")
url = (
    "https://s3-us-west-2.amazonaws.com/"
    "streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)

date_column = "date/time"

@st.cache
def get_data():
    data = pd.read_csv(url, nrows=10000)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[date_column]=pd.to_datetime(data[date_column])
    return data

data = get_data()

st.subheader(
    "Places where tiktok videos disappointed me"
)

hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[date_column].dt.hour == hour_to_filter]

st.subheader(f"Map of all disappointments at {hour_to_filter}:00")
st.map(filtered_data)
