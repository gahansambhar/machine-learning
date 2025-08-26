# %%
# imports 
import pandas as pd
import seaborn as sns

# %%
purchase = pd.read_csv("QVI_purchase_behaviour.csv")
transaction = pd.read_csv("QVI_transaction_data.csv")
# %%
purchase.info()
transaction.info()
# %%
purchase.dtypes
transaction.dtypes
# %%
# there seems to be no missing values in both datasets

purchase.isnull().sum()
transaction.isnull().sum()
# %%
transaction["DATE"] = pd.to_datetime(transaction["DATE"], unit="D", origin="1899-12-30")
# %%
# Lets extract more date features to see which day of the week
# brings in the most sales
transaction["DAY"] = transaction["DATE"].dt.day_name()
daily_transactions = pd.merge(transaction, purchase, on="LYLTY_CARD_NBR", how="outer")
daily_transactions = daily_transactions.groupby("DAY", "PREMIUM_CUSTOMER")["TOT_SALES"].sum().reset_index()
# %%
sns.barplot(data=daily_transactions, x="DAY", y="TOT_SALES", hue="PREMIUM_CUSTOMER")

# There is not significant spike in sales on the weekends for any type of customer.
# %%
