import numpy as np
import matplotlib as plt




Gamma = 1
R = -1

k = 0

actions = ["u", "d", "l","r" ]

def evaluate_cell(S, x, y):
    v_prev = S_prev[x,y]
    Vs = 

    return (v, delta)

def itterative_evaluation(S, theta, Gamma,):
    S0 = np.zeros((4, 4))
    theta = 0.0001
    while True:
        delta = 0
        S_prev = S

        for x in len(S):
            for y in len(S[x]): # for each s \in S, indexed by x,y
                v_new, d = evaluate_cell(S_prev, x,y) 
                S[x][y] = v_new 
                delta = max(delta, d)
        plot_itteration(S)
        ## break condition, no square changed more than a delta of value.    
        if delta < theta:
            break


    return

while 

def plot_itteration():
    return


