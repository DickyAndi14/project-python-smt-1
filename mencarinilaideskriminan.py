from math import sqrt
from math import *
import streamlit as st

st.write("""
# Website Penghitung deskriminan
""")

a = st.number_input("masukkan nilai a", 0)
b = st.number_input("masukkan nilai b", 0)
c = st.number_input("masukkan nilai c", 0)
hitung = st.button("hitung nilai")

if hitung :
    dis = b **2 - 4.0 * a * c
    st.write("nilai a adalah", a)
    st.write("nilai b adalah", b)
    st.write("nilai c adalah", c)
    st.write("nilai deskriminan adalah", dis)