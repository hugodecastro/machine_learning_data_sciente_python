import pandas as pd

df = pd.DataFrame(
    [['fchollet/keras', 11302], ['openai/universe', 4350], ['pandas-dev/pandas', 8168]],
    columns=['repository', 'stars']
)

print(df.shape)

print(df)

print(df['stars'])

print(f'média: {df["stars"].mean()}')
print(df['stars'].median())

print(df.iloc[1]['stars'])