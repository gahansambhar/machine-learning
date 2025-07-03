# %%
# all required imports

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

pd.set_option("future.no_silent_downcasting", True)

# %%
# importng the training dataframe
train = pd.read_csv("train.csv")

# %%
# creating a list of the features selected during EDA in credt-score-EDA.py

features = [
    "Age",
    "Annual_Income",
    "Num_Bank_Accounts",
    "Num_Credit_Card",
    "Interest_Rate",
    "Delay_from_due_date",
    "Num_of_Delayed_Payment",
    "Credit_Mix",  # needs to be encoded
    "Outstanding_Debt",
    "Credit_History_Age",
    "Payment_of_Min_Amount",  # needs to be encoded
    "Amount_invested_monthly",
    "Monthly_Balance",
]

target = "Credit_Score"

# %%

X = train[features]
y = train[target]

# creating the training and testing feature matrices and the target vectors
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=666
)

# creating the encoder for the highlighted features
encoder = {
    "Credit_Mix": {"Good": 2, "Standard": 1, "Bad": 0},
    "Payment_of_Min_Amount": {"Yes": 1, "No": 0, "NM": -1},
}

X_train = X_train.replace(encoder)
X_test = X_test.replace(encoder)

# %%
# Logistic Regression model
regression = LogisticRegression(max_iter=1000)
regression.fit(X_train, y_train)

# %%
# Forest model with 100 estimators
forest100 = RandomForestClassifier(n_estimators=100)
forest100.fit(X_train, y_train)

# %%
# Forest model with 500 estimators
forest500 = RandomForestClassifier(n_estimators=500)
forest500.fit(X_train, y_train)

# %%
# KNN model
knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)

# %%

# predictons on the test data
y_prediction_regression = regression.predict(X_test)
y_prediction_forest100 = forest100.predict(X_test)
y_prediction_forest500 = forest500.predict(X_test)
y_prediction_knn = knn.predict(X_test)

# %%
print("1) Regression Accuracy:", accuracy_score(y_test, y_prediction_regression))
print(classification_report(y_test, y_prediction_regression))

print("2) Forest100 Accuracy:", accuracy_score(y_test, y_prediction_forest100))
print(classification_report(y_test, y_prediction_forest100))

print("3) Forest500 Accuracy:", accuracy_score(y_test, y_prediction_forest500))
print(classification_report(y_test, y_prediction_forest500))

print("3) KNN Accuracy:", accuracy_score(y_test, y_prediction_knn))
print(classification_report(y_test, y_prediction_knn))

# The accuracy reports show that Random Forest models work the best on this data set.
