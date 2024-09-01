import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import random

# Set up the page configuration
st.set_page_config(page_title="Interactive Learning Tools", page_icon="📚")

# Add CSS for styling
st.markdown("""
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
            color: #333;
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: 700;
            color: #4CAF50;
            margin-top: 30px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .footer {
            text-align: center;
            font-size: 18px;
            color: #555;
            margin-top: 50px;
        }
        .footer a {
            color: #1E90FF;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">Interactive Learning Tools</div>', unsafe_allow_html=True)

# Section: Interactive Visualization
st.write("### Interactive Scatter Plot")

# Sample data for interactive visualization
data = pd.DataFrame({
    'x': np.random.randn(200),
    'y': np.random.randn(200)
})

# Create an interactive scatter plot
scatter_plot = alt.Chart(data).mark_circle(size=60).encode(
    x='x',
    y='y',
    tooltip=['x', 'y']
).interactive()

st.altair_chart(scatter_plot, use_container_width=True)

# Section: Educational Math Quiz
st.write("### Educational Math Quiz")

# Generate two random numbers for the quiz
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

# Display the math question
st.write(f"What is {num1} + {num2}?")

# Input for the user's answer
user_answer = st.text_input("Your Answer:")

# Check the answer
if user_answer:
    correct_answer = num1 + num2
    if int(user_answer) == correct_answer:
        st.success("Correct! Well done!")
    else:
        st.error(f"Incorrect. The correct answer was {correct_answer}.")

# Footer
st.markdown("""
    <div class="footer">
        Developed By: Irfan Ullah Khan<br>
        <a href="https://flowcv.me/ikm">https://flowcv.me/ikm</a><br>
        Developed For: Essential Generative AI Training<br>
        Conducted By: PAK ANGELS, iCodeGuru, ASPIRE PAKISTAN
    </div>
""", unsafe_allow_html=True)
