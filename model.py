import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')

df.columns

df_model = df[['avg_salary','Sector','job_state','python_yn','job_sim','R_yn','tableau','power bi','ml','dl']]

df_dum = pd.get_dummies(df_model) 

from sklearn.model_selection import train_test_split
X = df_dum.drop('avg_salary', axis = 1)
y = df_dum.avg_salary.values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor()

from sklearn.model_selection import cross_val_score

np.mean(cross_val_score(regressor, X_train, y_train, scoring = 'neg_mean_absolute_error', cv= 5))

from sklearn.model_selection import GridSearchCV
parameters = {
    "n_estimators": range(10, 400, 10),
    "criterion": ['mse','mae'],
    "max_features": ['auto','sqrt','log2']
    }

gs = GridSearchCV(regressor, param_grid = parameters, scoring = 'neg_mean_absolute_error', cv = 5)
gs.fit(X_train, y_train)

gs.best_score_
y_pred = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, y_pred)

import pickle
filename = 'models/random_forest1_model.sav'
pickle.dump(gs.best_estimator_, open(filename, 'wb'))

# saving the columns
model_columns = list(X.columns)
with open('models/model_columns.pkl','wb') as file:
    pickle.dump(model_columns, file)
