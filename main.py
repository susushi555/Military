import numpy as np
from scipy.integrate import solve_ivp


def lanchester(t ,y, a, b):
    B, R = y
    return [-a*R, -b*B]

a,b = 0.003, 0.002 #　殲滅効率
y0 = [800, 1000] #　初期兵力　B、R
sol = solve_ivp(lanchester, [0,48], y0, args=(a,b), dense_output=True)
t = np.linspace(0,48,200)
B, R = sol.sol(t)
