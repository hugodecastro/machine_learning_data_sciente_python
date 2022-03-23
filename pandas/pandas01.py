
import pandas as pd

s = pd.Series(
    [1, 4, 6, 5, 7, 10, 6]
)

print(s)

print(s.describe())
print(f'mean: {s.mean()}')
print(f'median: {s.median()}')
print(s.duplicated())

s2 = pd.Series(
    [11, 5, 8]
)

s = s.append(s2)
print(s)