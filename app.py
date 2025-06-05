import streamlit as st
import math

st.title("Stable Softmax Calculator")

# Nhập dữ liệu đầu vào cho Softmax
v1 = st.number_input("Nhập vào giá trị v1:")
v2 = st.number_input("Nhập vào giá trị v2:")
v3 = st.number_input("Nhập vào giá trị v3:")

if st.button("Calculate Stable Softmax"):
    max_value = max(v1, v2, v3)

    e_v1 = math.exp(v1 - max_value)
    e_v2 = math.exp(v2 - max_value)
    e_v3 = math.exp(v3 - max_value)

    total_exp = e_v1 + e_v2 + e_v3

    #Calculate stable softmax
    stable_softmax_v1 = e_v1 / total_exp
    stable_softmax_v2 = e_v2 / total_exp
    stable_softmax_v3 = e_v3 / total_exp

    # Hiển thị kết quả
    st.write(f"Stable softmax for v1: {stable_softmax_v1:.8f}")
    st.write(f"Stable softmax for v2: {stable_softmax_v2:.8f}")
    st.write(f"Stable softmax for v3: {stable_softmax_v3:.8f}")
    st.success(f"Stable softmax: {stable_softmax_v1:.8f} {stable_softmax_v2:.8f} {stable_softmax_v3:.8f}")
