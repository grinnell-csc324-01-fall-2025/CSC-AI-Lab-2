import numpy as np
import matplotlib as plt




gamma = 1
R = -1

k = 0

actions = ["up", "down", "left","right" ]



def random_policy(x,y, S):
    moves = []
    if x>0:
        np.append(moves, "left")
    if y>0:
        np.append(moves, "up")
    if x< len(S) -1:
        np.append(moves, "right")
    if y < len(S[0]) -1:
        np.append(moves, "down")
        
    return moves

def evaluate_cell(S_prev, x, y):
    moves= random_policy(x,y,S_prev)
    v = 0

    for a in moves:
        p = 1/len(moves)
        if a == 'up':
            prev_state = S_prev[x,y+1]
        elif a == 'down':
            prev_state = S_prev[x,y-1]
        elif a == 'left':
            prev_state = S_prev[x-1,y]
        elif a == 'right':
            prev_state = S_prev[x+1,y]
        v += p *(R + (gamma*S_prev)) 
    return (v)

def itterative_evaluation(S, theta):
    theta = 0.0001
    while True:
        delta = 0
        S_prev = S

        for x in len(S):
            for y in len(S[x]): # for each s \in S, indexed by x,y
                v_new = evaluate_cell(S_prev, x,y) 
                delta = S_prev[x,y]-v_new
                S[x,y] = v_new 
                delta = max(delta, d)
        plot_itteration(S)
        ## break condition, no square changed more than a delta of value.    
        if delta < theta:
            break
    return


S0 = np.zeros((4, 4))
itterative_evaulation(S0, 
while 

def plot_itteration():
    return


