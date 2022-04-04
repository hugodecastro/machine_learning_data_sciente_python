import pandas as pd
import pydataset

titanic = pydataset.data('titanic')

print(titanic.head())
print(titanic.tail())
print(titanic.describe())