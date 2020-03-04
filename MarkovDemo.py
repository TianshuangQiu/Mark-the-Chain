import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times"

P = np.array([[1, 0, 0, 0, 0, 0],
              [0.5, 0, 0.5, 0, 0, 0],
              [0, 0.5, 0, 0.5, 0, 0],
              [0, 0, 0.5, 0, 0.5, 0],
              [0, 0, 0, 0.5, 0, 0.5],
              [0, 0, 0, 0, 0, 1]])
state = np.array([[0, 0, 0, 0, 1, 0]])

stateHist = state
dfStateHist = pd.DataFrame(state)
distr_hist = [[0, 0, 0, 0, 0, 0]]

i = 0
tmp = state.dot(P)
while i < 3:
    tmp = np.dot(tmp,P)
    print(tmp)
    i += 1

for x in range(50):
    state = np.dot(state, P)
    print(state)
    stateHist = np.append(stateHist, state, axis=0)

dfDistrHist = pd.DataFrame(stateHist)
dfDistrHist.plot()
plt.title("Starting with 4 coins")
plt.show()
