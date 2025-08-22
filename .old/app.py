from array import array
from altair import value
import streamlit as st 
from scipy.integrate import solve_ivp
import numpy as np

def lanchester(t, y, a, b):
    B, R = y
    return [-a * R, -b * B]

st.title('Lanchester Model Simulation')
blue = st.number_input('Initial Blue Army Strength', value=800) #青軍の初期兵力
red = st.number_input('Initial Red Army Strength', value=1000) #赤軍の初期兵力
y0 = [blue, red]  # 初期兵力 B、R
a, b = 0.003, 0.002 #殲滅効率
sol = solve_ivp(lanchester, [0,48], y0, args=(a,b), dense_output=True)
t = np.linspace(0, 48, 200)
B, R = sol.sol(t)
st.write('Blue Army:', B)
st.write('Red Army:', R)
st.line_chart(B, x_label='Blue Army')
st.line_chart(R, x_label='Red Army')