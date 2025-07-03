# %%
import pandas as pd
import plotly.express as px

# %%
data = pd.read_csv("train.csv")
data.head()

# %%
data.columns

# %%
fig = px.histogram(
    data,
    x="Occupation",
    labels={"Credit_Score": "Credit Score"},
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)
fig
# Seems that Occupation has very minimal influence on the credit score of an individual.

# Current list Empty

# %%
# Plotting relationship between age and Credit score
fig = px.box(
    data,
    x="Age",
    y="Credit_Score",
    labels={"Credit_Score": "Credit Score"},
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)
fig
# Plot shows that older people tend to have better credit scores.

# Current list: Age

# %%
fig = px.box(
    data,
    x="Annual_Income",
    y="Credit_Score",
    labels={"Credit_Score": "Credit Score", "Annual_Income": "Annual Income"},
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)
fig
# Despite the large number outliers, we see a correlation between Annual Income and Credit Score, clearly, higher income tends to lead to a better credit score.

# Current list: Age, Annual_Income

# %%
fig = px.box(
    data,
    x="Monthly_Inhand_Salary",
    y="Credit_Score",
    labels={
        "Credit_Score": "Credit Score",
        "Monthly_Inhand_Salary": "Monthly Inhand Income",
    },
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)
fig

# This much like annual income, shows a great correlation between income and credit score, however, the variables are redundant so only annual income will be chosen.

# Current list: Age, Annual_Income

# %%
fig = px.box(
    data,
    x="Num_Bank_Accounts",
    y="Credit_Score",
    labels={
        "Credit_Score": "Credit Score",
        "Num_Bank_Accounts": "Number of Bank Accounts",
    },
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)
fig
# Very clear negative correlation between Number of bacnk accounts and credit score

# Current list: Age, Annual_Income, Nu_Bank_Accounts

# %%
fig = px.box(
    data,
    x="Num_Credit_Card",
    y="Credit_Score",
    labels={
        "Credit_Score": "Credit Score",
        "Num_Credit_Card": "Number of Credit Cards",
    },
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)
fig
# Similarly, a greater number of credit cards also leads to a worse credit score

# Current list: Age, Annual_Income, Num_Bank_Accounts, Num_Credit_Card

# %%
fig = px.box(
    data,
    x="Interest_Rate",
    y="Credit_Score",
    labels={"Credit_Score": "Credit Score", "Interest_Rate": "Interest Rate"},
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)
fig

# Higher interest rate is indicative of a worse credit score on average

# Current list: Age, Annual_Income, Num_Bank_Accounts, Num_Credit_Card, Interest_Rate

# %%
fig = px.box(
    data,
    x="Num_of_Loan",
    y="Credit_Score",
    labels={"Credit_Score": "Credit Score", "Num_of_Loan": "Number of Loans"},
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)
fig

# We see that having a higher number of loans tends to imply a worse Credit Score

# Current list: Age, Annual_Income, Num_Bank_Accounts, Num_Credit_Card, Interest_Rate

# %%
fig = px.box(
    data,
    x="Delay_from_due_date",
    y="Credit_Score",
    labels={"Delay_from_due_date": "Delay", "Credit_Score": "Credit_Score"},
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)
fig

# Clearly, greater delays lead to lower credit rating.

# Current list: Age, Annual_Income, Num_Bank_Accounts, Num_Credit_Card, Interest_Rate, Delay_from_due_date

# %%
fig = px.box(
    data,
    x="Delay_from_due_date",
    y="Credit_Score",
    labels={"Delay_from_due_date": "Delay", "Credit_Score": "Credit Score"},
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)
fig

# %%
fig = px.box(
    data,
    x="Num_of_Delayed_Payment",
    y="Credit_Score",
    labels={
        "Num_of_Delayed_Payment": "Number of Delays",
        "Credit_Score": "Credit Score",
    },
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)
fig

# Both, number and length of delay seems to have the same relationship
# with Credit rating. So Number of Delays may be better as it has a
# smaller number of outliers

# Current list: Age, Annual_Income, Num_Bank_Accounts, Num_Credit_Card, Interest_Rate, Delay_from_due_date, Num_of_Delayed_Payment


# %%
fig = px.box(
    data,
    x="Changed_Credit_Limit",
    y="Credit_Score",
    labels={
        "Changed_Credit_Limit": "Num changes made to Credit limit",
        "Credit_Score": "Credit Score",
    },
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)

fig

# While there is a clear correlation between credit limit changes
# and Credit_Score, It is not a very accurate differentiator between
# standard and poor credit ratings. This metric should be skipped.

# %%
fig = px.box(
    data,
    x="Num_Credit_Inquiries",
    y="Credit_Score",
    labels={
        "Num_Credit_Inquiries": "Num credit inquiries",
        "Credit_Score": "Credit Score",
    },
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)

fig

# Compared tot he changes made in credit limit, Num credit inquiries tends
# to  be a better classifier with respect to Credit Score, lower,
# credit inquiries tend to lead to better gredit ratings.

# Current list: Age, Annual_Income, Num_Bank_Accounts, Num_Credit_Card, Interest_Rate, Delay_from_due_date, Num_of_Delayed_Payment

# %%

fig = px.density_heatmap(
    data,
    x="Credit_Mix",
    y="Credit_Score",
    color_continuous_scale="Blues",
    labels={"Credit_Mix": "Credit Mix", "Credit_Score": "Credit Score"},
)

fig

# Seems to have an expected correlation between credit mix and score.
# Good-Good, Standard-Standard, Bad-Poor. It is important to note
# that the Standard-Standard cell of the heatmap is significantly darker
# (More dense) than the rest, as 46% of data has a standard credit mix
# and 53% has a standard credit score.
#
# Current list: Age, Annual_Income, Num_Bank_Accounts, Num_Credit_Card, Interest_Rate, Delay_from_due_date, Num_of_Delayed_Payment, Credit_Mix
# %%
fig = px.box(
    data,
    x="Outstanding_Debt",
    y="Credit_Score",
    labels={"Outstanding_Debt": "Outstanding Debt", "Credit_Score": "Credit Score"},
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)

fig
# As expected, higher outstanding debt leads to worse credit score.


# %%
fig = px.box(
    data,
    x="Credit_Utilization_Ratio",
    y="Credit_Score",
    labels={
        "Credit_Utilization_Ratio": "Credit Utilization Ratio",
        "Credit_Score": "Credit Score",
    },
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)

fig
# It seems theres not much of a heavy correlation between Credit Utilisation
# and credit rating. So this parameter can be skipped.

# %%
fig = px.box(
    data,
    x="Credit_History_Age",
    y="Credit_Score",
    labels={"Credit_History_Age": "Credit History Age", "Credit_Score": "Credit Score"},
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)

fig
# The Credit History Age clearly has a positive correlation with credit rating
# a higher age leads to a higher score. This feature should be included.

# Current list: Age, Annual_Income, Num_Bank_Accounts, Num_Credit_Card, Interest_Rate, Delay_from_due_date, Num_of_Delayed_Payment, Credit_Mix, Outstanding_Debt, Credit_History_Age

# %%

filtered_data = data[data["Payment_of_Min_Amount"].isin(["Yes", "No"])]
filtered_data
# %%

fig = px.density_heatmap(
    filtered_data,
    x="Payment_of_Min_Amount",
    y="Credit_Score",
    labels={
        "Payment_of_Min_Amount": "Minimum Amount Payments",
        "Credit_Score": "Credit Score",
    },
    color_continuous_scale="Blues",
)

fig

# It seems that there is atleast light correlation between making minimum
# amount payments and credit score. Again, since most people have standard
# ratings, the middle row of the heatmap is very dark, however, the yes
# column has a darker "Poor" cell while the no column has a darker "Good"
# cell. This is a good feature to include in the model

# Current list: Age, Annual_Income, Num_Bank_Accounts, Num_Credit_Card,
# Interest_Rate, Delay_from_due_date, Num_of_Delayed_Payment, Credit_Mix,
# Outstanding_Debt, Credit_History_Age, Payment_of_Min_Amount

# %%
fig = px.box(
    data,
    x="Total_EMI_per_month",
    y="Credit_Score",
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)

fig

# Does not seem to be a very useful indicator visually so this feature can be skipped

# %%
fig = px.box(
    data,
    x="Amount_invested_monthly",
    y="Credit_Score",
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)

fig

# Seems to be a decent indicator of credit rating. The correlation is not the heaviest.
# This feature can be included

# Current list: Age, Annual_Income, Num_Bank_Accounts, Num_Credit_Card,
# Interest_Rate, Delay_from_due_date, Num_of_Delayed_Payment, Credit_Mix,
# Outstanding_Debt, Credit_History_Age, Payment_of_Min_Amount, Amount_invested_monthly
# %%

fig = px.density_heatmap(
    data, x="Payment_Behaviour", y="Credit_Score", color_continuous_scale="Blues"
)

fig

# Much like before, the standard row is very dark due to the heavy frequency of standard
# credit scores. the column with Low spnd small payments also seems to be darker as most
# of the data seems to have that characteistic. This does not seem to be a very great predictor
# %%

fig = px.box(
    data,
    x="Monthly_Balance",
    y="Credit_Score",
    color="Credit_Score",
    color_discrete_map={"Good": "Green", "Standard": "Yellow", "Poor": "Red"},
)

fig

# It seems that a higher monthly balance is a decent indicator of a better credit score
# (And vice-versa). This feature can be the included in the model

# Final list: Age, Annual_Income, Num_Bank_Accounts, Num_Credit_Card,
# Interest_Rate, Delay_from_due_date, Num_of_Delayed_Payment, Credit_Mix,
# Outstanding_Debt, Credit_History_Age, Payment_of_Min_Amount,
# Amount_invested_monthly, Monthly_Balance
