# %%
import os
import numpy as np
import tarfile
import urllib
import requests

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


# %%
# Uncomment this when fetching data for the first time
# fetch_housing_data()
# %%
import pandas as pd


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


# %%
housing = load_housing_data()
# %%
housing.head()
housing.info()
housing["ocean_proximity"].value_counts()
housing.describe()
# %%
import matplotlib.pyplot as plt

# %%
housing.hist(bins=50, figsize=(25, 30))
# %%
# Now we must take a stratified sample in order to make sure
# we do not introduce a sampling bias into the model
housing["income_cat"] = pd.cut(
    housing["median_income"], bins=[0, 1.5, 3.0, 4.5, 6, np.inf], labels=[1, 2, 3, 4, 5]
)
counts = [i for i in housing["income_cat"].value_counts(sort=False)]
plt.bar(height=counts, width=0.5, x=[1, 2, 3, 4, 5])
# %%
from sklearn.model_selection import StratifiedShuffleSplit

# %%
stratsplit = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=666)

for trainindex, testindex in stratsplit.split(housing, housing["income_cat"]):
    strat_train = housing.loc[trainindex]
    strat_test = housing.loc[testindex]
# %%
# Let us ensure that the stratified split was successful
counts = [i for i in strat_train["income_cat"].value_counts(sort=False)]
plt.bar(height=counts, width=0.5, x=[1, 2, 3, 4, 5])

# %%
counts = [i for i in strat_test["income_cat"].value_counts(sort=False)]
plt.bar(height=counts, width=0.5, x=[1, 2, 3, 4, 5])
# %%
# Now that we. have ensured that our tetst and train splits are
# reprasentative of the median_income distribution, we can
# continue with our analysis
# %%
for set in (strat_train, strat_test):
    set.drop("income_cat", inplace=True, axis=1)

# %%
# creating an eploration set to ensure the data is not damaged on accident
explore = strat_train.copy()

# %%
plt.scatter(
    data=explore,
    y="latitude",
    x="longitude",
    alpha=0.1,
    s=explore["population"] / 100,
    c="median_house_value",
    cmap=plt.get_cmap("jet"),
    label="population",
)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.colorbar()
# %%
corrmatrix = explore.corr(numeric_only=True)
# %%
from pandas.plotting import scatter_matrix

attributes = [
    "median_house_value",
    "median_income",
    "total_rooms",
    "housing_median_age",
]

scatter_matrix(explore[attributes], figsize=(24, 16))

# %%
explore.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.1)
# %%
explore["rooms_per_household"] = explore["total_rooms"] / explore["households"]
explore["bedrooms_per_room"] = explore["total_bedrooms"] / explore["total_rooms"]
explore["population_per_household"] = explore["population"] / explore["households"]
# %%
corrmatrix = explore.corr(numeric_only=True)
# %%
exploreX = strat_train.drop("median_house_value", axis=1)
explorey = strat_test["median_house_value"].copy()
# %%
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="median")
imputerX = exploreX.drop("ocean_proximity", axis=1)
imputerX = imputer.fit_transform(imputerX)

# %%
exploreX = pd.DataFrame(imputerX, columns=exploreX.columns[:8])
# %%
