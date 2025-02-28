import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set page config
st.set_page_config(
    page_title="📊 My Enhanced Streamlit App",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stTextInput input, .stNumberInput input {
        border-radius: 5px;
        padding: 10px;
    }
    .stSelectbox div {
        border-radius: 5px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("📊 My Enhanced Streamlit App")
st.write("Welcome to this awesome app! Explore data, visualize charts, and interact with widgets.")

# Add a sidebar
st.sidebar.header("Settings")
user_name = st.sidebar.text_input("Enter your name", "User")
st.sidebar.write(f"Welcome, {user_name}! 👋")

# Create tabs
tab1, tab2, tab3 = st.tabs(["📂 Data", "📈 Charts", "ℹ️ About"])

with tab1:
    st.header("📂 Data Section")
    
    # Create sample data
    data = pd.DataFrame({
        'Name': ['sara', 'Aisha', 'Ayan', 'Zain'],
        'Age': [30, 37, 17, 12],
        'City': ['Narowal', 'Pindi', 'Lahore', 'Karachi']
    })
    
    # Display the data
    st.write("### Sample DataFrame")
    st.dataframe(data, use_container_width=True)
    
    # Add file uploader
    st.write("### Upload your own CSV")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)

with tab2:
    st.header("📈 Charts Section")
    
    # Create sample data for charts
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    # Display different types of charts
    st.write("### Line Chart")
    st.line_chart(chart_data)
    
    st.write("### Area Chart")
    st.area_chart(chart_data)
    
    st.write("### Bar Chart")
    st.bar_chart(chart_data)
    
    # Add interactive elements
    show_scatter = st.checkbox("Show Scatter Plot")
    if show_scatter:
        st.write("### Scatter Plot")
        fig = px.scatter(chart_data, x='A', y='B', title="Scatter Plot")
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("ℹ️ About Section")
    
    # Add columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Features")
        st.write("""
        - Interactive Data Display
        - Multiple Chart Types
        - File Upload Capability
        - Real-time Updates
        - Modern UI with Custom Styling
        """)
    
    with col2:
        st.write("### How to Use")
        st.write("""
        1. Enter your name in the sidebar
        2. Explore different tabs
        3. Upload your own data
        4. Interact with charts and widgets
        """)
    
    # Add expander
    with st.expander("Show more details"):
        st.write("""
        This is a demo app showing various Streamlit features.
        You can use it as a template for your own applications!
        """)

# Add interactive widgets at the bottom
st.markdown("---")
st.subheader("🎛️ Interactive Widgets Demo")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    # Add a slider
    number = st.slider("Select a number", 0, 100, 50)
    st.write(f"Selected number: {number}")
    
    # Add a selectbox
    option = st.selectbox(
        'Choose your favorite color',
        ['Red', 'Green', 'Blue', 'Yellow']
    )
    st.write(f'Your favorite color is {option}')

with col2:
    # Add a text input
    text_input = st.text_input("Type something")
    if text_input:
        st.write(f"You typed: {text_input}")
    
    # Add a button
    if st.button("Click me!"):
        st.balloons()
        st.success("Thanks for clicking!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")