import streamlit as st

st.write("""
# Website Penghitung Suhu
penghitung suhu dari celcius ke fahrenheit
""")

celcius = st.number_input("masukkan nilai", 0)
hitung = st.button("hitung suhu")

if hitung :
    suhu = celcius * 9.0 / 5.0 + 32.0
    st.write("suhu dalam fahrenheit adalah", suhu)