import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Membaca data yang telah dibersihkan
df_day_clean = pd.read_csv('day_clean.csv')
df_hour_clean = pd.read_csv('hour_clean.csv')

# Title of the Dashboard
st.title("Bike Sharing Data Dashboard")

# Sidebar for Navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select a dataset to view", ("Daily Data", "Hourly Data"))

if option == "Daily Data":
    st.header("Daily Data Analysis")

    # Visualisasi Bar Chart Rata-rata Penggunaan Sepeda per Musim
    st.subheader("Average Bike Rentals per Season")
    season_avg_cnt_day = df_day_clean.groupby('season')['cnt'].mean()
    fig, ax = plt.subplots()
    season_avg_cnt_day.plot(kind='bar', color=['springgreen', 'gold', 'orangered', 'skyblue'], ax=ax)
    ax.set_xlabel('Season')
    ax.set_ylabel('Average Count of Bike Rentals')
    ax.set_title('Average Bike Rentals per Season (Day Data)')
    ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'], rotation=0)
    st.pyplot(fig)

elif option == "Hourly Data":
    st.header("Hourly Data Analysis")

    # Visualisasi Box Plot Pengaruh Cuaca terhadap Penggunaan Sepeda
    st.subheader("Distribution of Bike Rentals by Weather Situation")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='weathersit', y='cnt', data=df_hour_clean, ax=ax)
    ax.set_xlabel('Weather Situation')
    ax.set_ylabel('Count of Bike Rentals')
    ax.set_title('Distribution of Bike Rentals by Weather Situation (Hour Data)')
    ax.set_xticklabels(['Clear', 'Mist + Cloudy', 'Light Snow/Rain', 'Heavy Rain/Fog'])
    st.pyplot(fig)

# Menerapkan RFM Analysis pada Hourly Data
if st.sidebar.checkbox("Perform RFM Analysis"):
    st.header("RFM Analysis on Hourly Data")
    rfm_data = df_hour_clean.groupby('registered').agg({
        'dteday': 'max',
        'hr': 'count',
        'cnt': 'sum'
    }).rename(columns={
        'dteday': 'Recency',
        'hr': 'Frequency',
        'cnt': 'Monetary'
    })
    st.write(rfm_data)

# Menampilkan data yang telah dibersihkan
if st.sidebar.checkbox("Show Cleaned Data"):
    if option == "Daily Data":
        st.subheader("Cleaned Daily Data")
        st.write(df_day_clean)
    elif option == "Hourly Data":
        st.subheader("Cleaned Hourly Data")
        st.write(df_hour_clean)