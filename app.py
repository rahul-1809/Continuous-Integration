import streamlit as st

st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube and fifith power: ")

num = st.number_input("Enter an integer:", value=1, step=1)

square = num ** 2
cube = num ** 3
fifth_power = num ** 5

st.write(f"The square of {num} is: {square}")
st.write(f"The cube of {num} is: {cube}")
st.write(f"The fifth power of {num} is: {fifth_power}")