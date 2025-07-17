# %%

# Imports
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split

# %%

# Importing the train data
data = pd.read_csv("train.csv")
data
# %%

# Exploring the columns in the data
data.info()
# %%
print(data.isnull().sum())
# %%
# Exploring what values are missing and where.
sns.heatmap(data.isnull())
# %%
light_colors = ["#FF7F7F", "#98FB98"]
sns.countplot(
    data,
    x="Pclass",
    hue="Survived",
    palette=light_colors,
)
# It is clear that bing in class one leads to a slightly higher chance of surviving,
# while being in class 2 is essentially a coin flip and 3 is very unlikely to survive.

# Included

# %%
sns.violinplot(data, y="Age", x="Survived", hue="Survived", palette=light_colors)

# The violin plot shows that for the most part, people around and over 20
# were equally likely to survive or perish but for those under 20, there
# was a slightly higher chance of surivival.

# Included

# %%
sns.countplot(data, x="Sex", hue="Survived", palette=light_colors)

# Being a female led to a great chance of survival compared to being a male

# Included
# %%

sns.violinplot(data, y="SibSp", x="Survived", hue="Survived", palette=light_colors)

# A small chance that having siblings may lead to a slightly higher chance of survival.

# Included

# %%
sns.violinplot(data, y="Parch", x="Survived", hue="Survived", palette=light_colors)

# Again having a bigger family leads to a marginaly better chnace of being saved.

# Included

# %%
sns.violinplot(data, y="Fare", x="Survived", hue="Survived", palette=light_colors)

# People that paid a higher fare than others seem to ahve had a slightly better chance at surviving.

# Included
# %%

# Analysing the cabin a person was in can be slightly difficult because there are many different values.
# A new column "Deck" can be created that extracts the Letter of the deck and remains unknown if the
# Cabin is unknown

data["Deck"] = data["Cabin"].str[0]
data["Deck"] = data["Deck"].fillna("N")
sns.countplot(data, x="Deck", hue="Survived", palette=light_colors)

# If a passenger was given a cabin they had a much better chance of survivng than those not in cabins.

# Included

# %%
data["Embarked"] = data["Embarked"].fillna("N")
sns.countplot(data, x="Embarked", hue="Survived", palette=light_colors)

# Those embarking at port-S tend to have a poor chance of surviving.
# Included
