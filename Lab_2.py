import numpy as np
import matplotlib.pyplot as plt


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
    print_arrows(S)  
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
            print_arrows(S)
        k+=1
        ## break condition, no square changed more than a delta of value.    
        if delta < theta:
            print_iteration(S, f"∞({k})")
            print_arrows(S)
            break

    return S

def print_iteration(S, k):
    print(f"\nV at iteration k = {k}")
    for row in S:
        print(" ".join(f"{float(v):6.2f}" for v in row))

def print_arrows(S):
    V = []
    X = np.array([])
    Y = np.array([])
    for row in range(len(S)):
        for col in range(len(S[0])):
            if (row ==0 and col == 0 ) or (row == len(S)-1 and col == len(S)-1):
                continue
            o = [row+0.5, col+0.5]
            values = [0,0,0,0]
            

            values[0] = S[max(0, row-1 )][col] #left
            values[1]  = S[min(3, row+1 )][col] #right
            values[2]  = S[row][min(3, col+1 )] #up
            values[3]  = S[row][max(0, col-1 )] #down note directions flipped to account for negative y origin
            maximum = np.max(values)

            directions = np.array([[-1,0], [1,0], [0,-1], [0,1]])
            for x in range(len(values)):
                if values[x] == maximum:
                    V.append(directions[x])
                    X = np.append(X, o[0] )
                    Y = np.append(Y, o[1])
    V =np.array(V)
    plt.figure(figsize=(5, 5)) 
    plt.quiver(X,Y, V[:,0], V[:,1])
    
    plt.xlim(0,4)
    plt.ylim(0,4)
    plt.gca().invert_yaxis()
    plt.xticks(range(5))
    plt.yticks(range(5))
    plt.grid(True)
    plt.show()
            


# run the evaluation
theta = 0.0001
S_final = itterative_evaluation(np.zeros((4,4)), theta, Gamma)