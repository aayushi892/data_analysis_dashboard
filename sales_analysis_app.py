# Import required libraries
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Function to generate sample data
def generate_sample_data():
    data = {
        'Date': pd.date_range(start='2024-01-01', periods=15),
        'Product': ['A', 'B', 'C', 'D', 'E'] * 3,
        'Category': ['Electronics', 'Clothing', 'Grocery', 'Electronics', 'Clothing'] * 3,
        'Units_Sold': [10, 20, 15, 40, 35, 25, 30, 45, 50, 20, 15, 10, 25, 40, 30],
        'Unit_Price': [100, 50, 20, 200, 80, 110, 55, 25, 210, 85, 105, 60, 30, 220, 90]
    }
    df = pd.DataFrame(data)
    df['Total_Sales'] = df['Units_Sold'] * df['Unit_Price']
    return df

# Load data
df = generate_sample_data()

# Streamlit App
st.title("Sales Analysis and Visualization")
st.write("Explore and analyze sales data interactively!")

# Sidebar for filtering
st.sidebar.header("Filter Options")
product_filter = st.sidebar.multiselect("Select Products:", options=df['Product'].unique(), default=df['Product'].unique())
category_filter = st.sidebar.multiselect("Select Categories:", options=df['Category'].unique(), default=df['Category'].unique())

# Filter data
filtered_df = df[(df['Product'].isin(product_filter)) & (df['Category'].isin(category_filter))]

# Display data
st.subheader("Filtered Sales Data")
st.dataframe(filtered_df)

# Analysis and Visualizations
st.subheader("Visualizations")

# Bar Plot: Total Sales by Product
st.write("### Total Sales by Product")
sales_by_product = filtered_df.groupby('Product')['Total_Sales'].sum().reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='Product', y='Total_Sales', data=sales_by_product, palette='viridis', ax=ax)
st.pyplot(fig)

# Pie Chart: Total Sales by Category
st.write("### Sales Distribution by Category")
sales_by_category = filtered_df.groupby('Category')['Total_Sales'].sum().reset_index()
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(sales_by_category['Total_Sales'], labels=sales_by_category['Category'], autopct='%1.1f%%', startangle=140)
ax.set_title('Sales Distribution by Category')
st.pyplot(fig)

# Line Plot: Units Sold Over Time
st.write("### Units Sold Over Time")
units_by_date = filtered_df.groupby('Date')['Units_Sold'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='Date', y='Units_Sold', data=units_by_date, marker='o', color='green', ax=ax)
ax.set_title('Units Sold Over Time')
plt.xticks(rotation=45)
st.pyplot(fig)

# Summary Section
st.subheader("Summary of Analysis")
st.write("- **Total Sales by Product**:")
st.dataframe(sales_by_product)
st.write("- **Total Sales by Category**:")
st.dataframe(sales_by_category)
st.write("- **Units Sold Over Time**:")
st.dataframe(units_by_date)
