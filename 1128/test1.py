import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5),index=list('abcde'))
print(s)