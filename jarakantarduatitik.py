import streamlit as st
from math import sqrt

st.write("""
# Website Penghitung Jarak antara Dua Titik
""")

xl = st.number_input("masukkan nilai xl", )
yl = st.number_input("masukkan nilai yl", )
x2 = st.number_input("masukkan nilai x2", )
y2 = st.number_input("masukkan nilai y2", )
hitung = st.button("hitung")

if hitung:
    st.write("nilai xl dan yl adalah", xl,yl)
    st.write("nilai x2 dan y2 adalah", x2,y2)   