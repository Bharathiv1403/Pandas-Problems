"""In the above example :
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}: This line creates a Python dictionary 'd1' with five key-value pairs. Each key is a string ('a', 'b', 'c', 'd', 'e') and each value is an integer.
new_series = pd.Series(d1): This line creates a new Pandas Series object 'new_series' from the dictionary 'd1' using the pd.Series() constructor. The resulting Series object will have the same keys as the dictionary and the corresponding values as its elements."""

import pandas as pd
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
print("Orginal Dictionary")
print(d1)

new_series=pd.Series(d1)
print("Convert Disctionary")
print(new_series)