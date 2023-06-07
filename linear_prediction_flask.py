import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
dataframe = pd.read_csv("Salary_dataset.csv")
dataframe = dataframe.drop("Unnamed: 0" , axis=1)
x = dataframe["YearsExperience"].values.reshape(-1, 1)
y = dataframe["Salary"].values.reshape(-1, 1)
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.75, random_state=0)
machine = LinearRegression()
machine.fit(xtrain, ytrain)
def user_input_test(year: int):
    year_for_machine = [[year]]
    prediction_data = machine.predict(year_for_machine)
    return prediction_data[0]
