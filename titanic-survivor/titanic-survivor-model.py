# %%
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("train.csv")
data
# %%

# Encoding categroical features, Deck and Embarked

data["Deck"] = data["Cabin"].str[0]
data["Deck"] = data["Deck"].fillna("N")
data = pd.get_dummies(data, columns=["Sex", "Deck", "Embarked"], drop_first=True)
data
# %%

X = data[
    [
        "Pclass",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Sex_male",
        "Deck_B",
        "Deck_C",
        "Deck_D",
        "Deck_E",
        "Deck_G",
        "Deck_N",
        "Embarked_Q",
        "Embarked_S",
    ]
]

y = data["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# %%
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

randomForrest = RandomForestClassifier(n_estimators=100)
randomForrest.fit(X_train, y_train)

xGBoost = XGBClassifier(eval_metric="logloss")
xGBoost.fit(X_train, y_train)

# %%

# Comparing the random forrest and XGboost approaches.
forrestPredict = randomForrest.predict(X_test)
xGBPredict = xGBoost.predict(X_test)

print("\nRandom Forrest Report:\n", classification_report(y_test, forrestPredict))
print("\n XGBoost Report:\n", classification_report(y_test, xGBPredict))

# Random Forrest seems marginally better

# %%

# Submission file creation
testData = pd.read_csv("test.csv")
testData["Deck"] = testData["Cabin"].str[0]
testData["Deck"] = testData["Deck"].fillna("N")
testData["Embarked"] = testData["Embarked"].fillna("N")
testData = pd.get_dummies(
    testData, columns=["Sex", "Deck", "Embarked"], drop_first=True
)
testData

X = testData[
    [
        "Pclass",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Sex_male",
        "Deck_B",
        "Deck_C",
        "Deck_D",
        "Deck_E",
        "Deck_G",
        "Deck_N",
        "Embarked_Q",
        "Embarked_S",
    ]
]

y = xGBoost.predict(X)
y

submission = pd.DataFrame()

submission = pd.concat([testData["PassengerId"], y], axis=1)
