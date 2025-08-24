# %%

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("data.csv")
# %%
X = data.drop(columns=["Season", "Player", "Age", "Team", "Pos"])
y = data["Share"]
# %%

X["3P%"].fillna(0, inplace=True)

# %%

# %%
