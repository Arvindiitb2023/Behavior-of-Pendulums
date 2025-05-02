import numpy as np
from scipy.integrate import solve_ivp

class PendulamMotion:
    def __init__(self):
        self.m1 = 1
        self.m2 = 2
        self.t = 0
        self.dt = 0.01  # Time step
        self.l1 = 1
        self.l2 = 1
        # l1 , l2 = 1
    def ODE(self,t,state):
        t1 , w1 , t2 ,w2 = state # t = theta ,w=omega
        delta = t2-t1
        m1,m2 = self.m1 ,self.m2
        g = 9.81
        denom1 = (2*m1 +m2 - m2*np.cos(2*delta))
        denom2 = (2*m1 + m2 - m2*np.cos(2*delta)) 

        dw1 = (
        -g * (2*m1 + m2) * np.sin(t1)
        - m2 * g * np.sin(t1 - 2*t2)
        - 2 * np.sin(delta) * m2 * (w2**2 * self.l2 + w1**2 * self.l1 * np.cos(delta))
        ) / (self.l1 * denom1)

        dw2 = (
        2 * np.sin(delta)
        *(w1**2 * self.l1 * (m1 + m2)
           + g * (m1 + m2) * np.cos(t1)
           + w2**2 * self.l2 * m2 * np.cos(delta))
        ) / (self.l2 * denom2)
        damping = 0 # tweak this value
        dw1 -= damping * w1
        dw2 -= damping * w2

        return [w1, dw1, w2, dw2]
    
    def solver(self,state):
        sol = solve_ivp(self.ODE,(self.t, self.t + self.dt),state, t_eval=[self.t + self.dt])
        output = sol.y[:, -1]  # Update to latest state
        self.t += self.dt
        return output

