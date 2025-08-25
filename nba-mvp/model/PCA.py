# %%

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
data = pd.read_csv("data.csv")
# %%
X = data.drop(columns=["Season", "Player", "Age", "Team", "Pos", "GS", "Share"])
X.fillna(0, inplace=True)
y = data["Share"]
# %%
scaler = StandardScaler()
scaledX = scaler.fit_transform(X) 

cols = ["standardised-"+col for col in X.columns]
scaledX = pd.DataFrame(scaledX, columns=cols)
# %%
pca = PCA()
pcaX = pca.fit_transform(scaledX)
# %%
explained_variance = pca.explained_variance_ratio_
# %%
sns.lineplot(data=explained_variance)
# %%
cumulative_explained_variance = explained_variance.cumsum()
# %%
sns.lineplot(data=cumulative_explained_variance)
# %%
num_pc = 20
pca = PCA(n_components=num_pc)
pcaX = pca.fit_transform(scaledX)
# %%

X_train, X_test, y_train, y_test = train_test_split(pcaX, y, test_size=0.3, random_state=666)
# %%
from xgboost import XGBRFRegressor

# %%
rfRegressor = XGBRFRegressor()
# %%
rfRegressor.fit(X_train, y_train)
# %%
from sklearn.metrics import mean_squared_error
# %%
prediction = rfRegressor.predict(X_test)
# %%
# Regression Metrics (Not necessarily the best measures as we are more interested in the rank)
print(mean_squared_error(prediction, y_test)**(1/2))
# %%
from scipy.stats import spearmanr, kendalltau
# %%
spearmanmetric = spearmanr(y_test, prediction)

kendalltaumetric = kendalltau(y_test, prediction)
# %%
# Simply running a PCA on the data and creating predictions is not a very great idea. 