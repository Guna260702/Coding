import pandas as pd

data = pd.read_csv('WS.csv')

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
hypothesis = ['0'] * len(X[0])

for i in range(len(X)):
    if y[i] == 'Yes':
        for j in range(len(X[0])):
            if hypothesis[j] == '0':
                hypothesis[j] = X[i][j]
            elif hypothesis[j] != X[i][j]:
                hypothesis[j] = '?'

print('Final Hypothesis:', hypothesis)
