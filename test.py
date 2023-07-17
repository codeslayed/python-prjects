#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the data set
data = pd.read_csv('Position_Salaries.csv')
x = data.iloc[:, 1:-1].values
y = data.iloc[:, -1].values

#training decision tree regression model on the whole dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(x,y)


#predicting a new result
print(regressor.predict([[6.5]]))

#visualising the result
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color='red')
plt.plot(x_grid, regressor.predict(x_grid), color = 'blue')
plt.title('Salary (Decision Tree Regression)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show() #showing the graph 















