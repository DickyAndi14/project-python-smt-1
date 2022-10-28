import streamlit as st
from math import *

st.write("""
# Website Penghitung Luas dan Keliling
penghitung Luas dan keliling suatu benda
""")

r = st.number_input("masukkan nilai", 0)
hitung = st.button("hitung nilai")

if hitung :
    luas = 3.14 * r ** 2
    kel = 2.0 * 3.14 * r
    st.write("nilai radiusnya adalah", r)
    st.write("luasnya adalah", luas)
    st.write("kelilingnya adalah", kel)