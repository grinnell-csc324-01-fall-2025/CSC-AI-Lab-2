import numpy as np

Gamma = 1
R = -1

k = 0

actions = ["u", "d", "l","r" ]
terminalS = [(0,0), (3,3)]

def next_state(x, y, a):
    nx, ny = x, y
    if a == "u": nx -= 1 #
    if a == "d": nx += 1
    if a == "l": ny -= 1
    if a == "r": ny += 1
    if nx < 0 or nx > 3 or ny < 0 or ny > 3:
        return x, y
    return nx, ny


def evaluate_cell(S_prev, x, y):
    v_prev = S_prev[x,y]
    if (x, y) in terminalS:
        return 0.0, 0.0
    
    total = 0.0
    for a in actions:
        nx, ny = next_state(x, y, a)
        total += (R + Gamma * S_prev[nx, ny])
    v_new = total / 4.0

    delta = abs(v_new - v_prev)
    return (v_new, delta)

PRINT_KS = set(range(0, 11))

def itterative_evaluation(S, theta, Gamma):
    S = np.zeros((4, 4))
    print_iteration(S, 0)   
    k=1
    while True:
        delta = 0.0
        S_prev = S.copy()

        for x in range(len(S)):
            for y in range(len(S[x])): # for each s \in S, indexed by x,y
                v_new, d = evaluate_cell(S_prev, x,y) 
                S[x][y] = v_new 
                delta = max(delta, d)
        if k in PRINT_KS:
            print_iteration(S, k)
        k+=1
        ## break condition, no square changed more than a delta of value.    
        if delta < theta:
            print_iteration(S, "∞")
            break

    return S

def print_iteration(S, k):
    print(f"\nV at iteration k = {k}")
    for row in S:
        print(" ".join(f"{float(v):6.1f}" for v in row))

# run the evaluation
theta = 0.0001
S_final = itterative_evaluation(np.zeros((4,4)), theta, Gamma)




