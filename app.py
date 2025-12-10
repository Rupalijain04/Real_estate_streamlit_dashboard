import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 

# Load cleaned data
df = pd.read_csv("C:/Users/rupal/OneDrive/Desktop/Labmentix Internship/4th project - Real Estate Investment Advisor (12 Dec 2025)/real_estate_project/data/cleaned_data1.csv")


# App title
st.title("Real Estate Investment Dashboard")

# Show full dataset
st.subheader("Dataset Preview")
st.dataframe(df.head())

# City filter
st.subheader("Select City")
city = st.selectbox("Choose a City:", df["City"].unique())

filtered_data = df[df["City"] == city]

st.subheader("Properties in Selected City")
st.dataframe(filtered_data)

# User price input
st.subheader("Enter Property Price")
price = st.number_input("Enter current property price (in lakhs):", min_value=0.0)

# Future price calculation (8% growth for 5 years)
future_price = price * (1.08 ** 5)

st.subheader("Estimated Price After 5 Years")
st.write(f"₹ {round(future_price, 2)} Lakhs")

#  Good / Bad Investment Logic
city_avg_price = filtered_data["Price_in_Lakhs"].mean()

st.subheader("Investment Decision")

if future_price > city_avg_price:
    st.success("✅ This is a GOOD Investment")
else:
    st.error("❌ This is NOT a Good Investment")


# CHART 1 : Price Distribution
st.subheader("Price Distribution")
fig1 = plt.figure()
sns.histplot(df["Price_in_Lakhs"], bins=30)
plt.ylabel("Count")
st.pyplot(fig1)

# CHART 2 : CITY-WISE AVERAGE PRICE
st.subheader("City-wise Average Price")

city_price = df.groupby("City")["Price_in_Lakhs"].mean().sort_values(ascending=False).head(10)

fig2 = plt.figure()
city_price.plot(kind="bar")
plt.xlabel("City")
plt.ylabel("Average Price (Lakhs)")
st.pyplot(fig2)

# CHART 3 : PROPERTY TYPE COUNT
if "Property_Type" in df.columns:
    st.subheader("Property Type Count")

    fig3 = plt.figure()
    sns.countplot(x=df["Property_Type"])
    plt.xticks(rotation=45)
    st.pyplot(fig3)

#-----------------------------------------------------------------------------------------------------------

# App title
#st.title("Real Estate Investment Dashboard")

# ✅ Upload CSV instead of using C: drive
#uploaded_file = st.file_uploader("Upload your cleaned_data.csv file", type=["csv"])

#if uploaded_file is not None:
    #df = pd.read_csv(uploaded_file)

    # Show dataset
    #st.subheader("Dataset Preview")
    #st.dataframe(df.head())

    # City filter
    #if "City" in df.columns:
        #st.subheader("Select City")
        #city = st.selectbox("Choose a City:", df["City"].unique())
        #filtered_data = df[df["City"] == city]

        #st.subheader("Properties in Selected City")
        #st.dataframe(filtered_data)
    #else:
        #st.warning("City column not found")
        #filtered_data = df

    # User price input
    #st.subheader("Enter Property Price")
    #price = st.number_input("Enter current property price (in lakhs):", min_value=0.0)

    # Future price calculation (8% growth for 5 years)
    #future_price = price * (1.08 ** 5)

    #st.subheader("Estimated Price After 5 Years")
    #st.write(f"₹ {round(future_price, 2)} Lakhs")

    # Good / Bad Investment Logic
    #if "Price_in_Lakhs" in filtered_data.columns:
        #city_avg_price = filtered_data["Price_in_Lakhs"].mean()

        #st.subheader("Investment Decision")
        #if future_price > city_avg_price:
            #st.success("✅ This is a GOOD Investment")
        #else:
            #st.error("❌ This is NOT a Good Investment")
    #else:
        #st.warning("Price_in_Lakhs column not found")

    # CHART 1 : Price Distribution
    #if "Price_in_Lakhs" in df.columns:
        #st.subheader("Price Distribution")
        #sns.histplot(df["Price_in_Lakhs"], bins=30)
        #plt.xlabel("Price in Lakhs")
        #plt.ylabel("Count")
        #st.pyplot(fig1)

    # CHART 2 : CITY-WISE AVERAGE PRICE
    #if "City" in df.columns and "Price_in_Lakhs" in df.columns:
        #st.subheader("City-wise Average Price")

        #city_price = df.groupby("City")["Price_in_Lakhs"].mean().sort_values(ascending=False).head(10)

        #fig2 = plt.figure()
        #city_price.plot(kind="bar")
        #plt.xlabel("City")
        #plt.ylabel("Average Price (Lakhs)")
        #st.pyplot(fig2)

    # CHART 3 : PROPERTY TYPE COUNT
    #if "Property_Type" in df.columns:
        #st.subheader("Property Type Count")

        #fig3 = plt.figure()
        #sns.countplot(x=df["Property_Type"])
        #plt.xticks(rotation=45)
        #st.pyplot(fig3)

#else:
    #st.warning("⚠️ Please upload your cleaned_data.csv file to continue.")