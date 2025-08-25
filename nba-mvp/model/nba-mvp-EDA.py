# %%

import pandas as pd
import seaborn as sns

# %%
# Load the data
data = pd.read_csv("data/data.csv")

# %%
sns.set_theme(style="whitegrid")

# %%

sns.histplot(data=data["Share"], x="Share", y="Count  bins=10, binrange = (0.001,1))
# %%
# data for correlation matrix

corrdata = data.drop(columns=["Player", "Team", "Pos", "Season"])
corr = corrdata.corr()
sns.heatmap(corr, fmt=".2f", cmap="coolwarm")

# There is a lot of information we can gain from this 
# correlation matrix. We can see that there are a lot
# of features that are highly correlated with each other.
# But more importantly we can garner an understanding of 
# which features are highly correlated with the target 
# variable, "Share".


# %%
sns.barplot(data=corr["Share"].sort_values(ascending=False).reset_index().head(20), x="index", y="Share", palette="viridis", ) 
# %%
# most MVP votes seem to be given to players between 
# 23 to 33 years of age. We should include age as a 
# predictor

sns.scatterplot(data=data, x="Age", y="Share", alpha=0.7)

# %%
sns.scatterplot(data=data, x="G", y="Share", alpha=0.7)

# %%
sns.scatterplot(data=data, x="GS", y="Share", alpha=0.7)

# %%

# seems that upwards of 65 games played and started 
# is a good predictor of MVP votes. we should include 
# only one of the two as a predictor, since they are
# highly correlated. we will use games started
# as it is more indicative of a player's importance


# %%
sns.scatterplot(data=data, x="FG", y="Share", alpha = 0.7)
# %%
sns.scatterplot(data=data, x="FGA", y="Share", alpha = 0.7)
# %%
sns.scatterplot(data=data, x="FG%", y="Share", alpha = 0.7)

# %%

# This is interesting, it seems that FGA and FG are 
# both very clsoely related to MVP voting share,
# but so if FG%, which is a measure of efficiency.
# however, there are much better measures of efficiency
# that we can use, such as TS% or eFG%. As a result, 
# I will skip metrics like 2P% etc. 

# %%
sns.scatterplot(data=data, x="eFG%", y="Share", alpha = 0.7)

# %%
["Age", "GS"]