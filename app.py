import streamlit as st
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(page_title="My First Streamlit App", page_icon="📊")

# Title
st.title("My First Streamlit App")
st.write("Welcome to this awesome app!")

# Add a sidebar
st.sidebar.header("Settings")
user_name = st.sidebar.text_input("Enter your name", "User")
st.sidebar.write(f"Welcome {user_name}!")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Data", "Charts", "About"])

with tab1:
    st.header("Data Section")
    
    # Create sample data
    data = pd.DataFrame({
        'Name': ['Javeria', 'Amna', 'Ayan', 'Zain'],
        'Age': [25, 30, 35, 40],
        'City': ['Multan', 'Kracahi', 'Lahore', 'Pindi']
    })
    
    # Display the data
    st.write("### Sample DataFrame")
    st.dataframe(data)
    
    # Add file uploader
    st.write("### Upload your own CSV")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)

with tab2:
    st.header("Charts Section")
    
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
        scatter_fig = {
            'data': [
                {
                    'x': chart_data['A'],
                    'y': chart_data['B'],
                    'mode': 'markers',
                    'name': 'Points'
                }
            ]
        }
        st.plotly_chart(scatter_fig)

with tab3:
    st.header("About Section")
    
    # Add columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Features")
        st.write("""
        - Interactive Data Display
        - Multiple Chart Types
        - File Upload Capability
        - Real-time Updates
        """)
    
    with col2:
        st.write("### How to Use")
        st.write("""
        1. Enter your name in the sidebar
        2. Explore different tabs
        3. Upload your own data
        4. Interact with charts
        """)
    
    # Add expander
    with st.expander("Show more details"):
        st.write("""
        This is a demo app showing various Streamlit features.
        You can use it as a template for your own applications!
        """)

# Add interactive widgets at the bottom
st.markdown("---")
st.subheader("Interactive Widgets Demo")

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
st.markdown("Built with Streamlit ❤️")