import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataframe = pd.read_csv("Salary_dataset.csv")
dataframe = dataframe.drop("Unnamed: 0" , axis=1)
x = dataframe["YearsExperience"].values.reshape(-1, 1)
y = dataframe["Salary"].values.reshape(-1, 1)

class CustomerLinearRegression():
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None
    
    def ssr_gradient(self, x, y, coef):
        res = x * coef[1] + coef[0] - y
        return res.mean(), (res*x).mean()
    
    def gradient_descent(self, gradient, start, n_iter, learn_rate=0.1, tolerance=1e-06):
        vector = start
        for _ in range(n_iter):
            diff = -learn_rate * np.array(gradient(x, y, vector))
            if np.all(np.abs(diff) <= tolerance):
                break
            vector += diff
        return vector
    
    def predict(self, x, y, start=[0.5, 0.5], n_iter=100_000, learn_rate=0.0008):
        self.coef_ = self.gradient_descent(self.ssr_gradient, start=[0.5, 0.5], n_iter=n_iter, learn_rate=learn_rate)
        self.intercept_ = self.coef_[0]
        self.coef_ = self.coef_[1]          
        return x*self.coef_ + self.intercept_

    def mse(self, x, pred):
        return np.mean((x - pred) ** 2)


c = CustomerLinearRegression()
prediction = c.predict(x, y)
def user_input_test(year: int):
    year_for_machine = [[year]]
    return prediction[year_for_machine][0]

def display_plot():
    plt.scatter(x, y)
    plt.plot([min(x), max(x)], [min(prediction), max(prediction)], color="black")
    plt.show()
