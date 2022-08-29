import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

data = pd.read_csv('test.csv')
x = data[['meanattitude.roll', 'rangeattitude.roll', 'sdattitude.roll', 'varattitude.roll','medianattitude.roll', 'meanattitude.pitch', 'rangeattitude.pitch', 'sdattitude.pitch', 'varattitude.pitch', 'medianattitude.pitch', 'meanattitude.yaw', 'rangeattitude.yaw', 'sdattitude.yaw', 'varattitude.yaw', 'medianattitude.yaw']]
y = data[['label']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

mlp = MLPClassifier(max_iter=200)
parameter_space = {
    'hidden_layer_sizes': [(30,30,30), (30,30,30,30)],
    'activation': ['tanh', 'relu'],
    'solver': ['sgd', 'adam'],
    'alpha': [0.0001, 0.05],
    'learning_rate': ['constant', 'adaptive'],
}


classifier = GridSearchCV(mlp, parameter_space, n_jobs=4, cv=3, verbose=10)
# classifier = MLPClassifier(hidden_layer_sizes=(100,),
#                            random_state=5,
#                            verbose=True,
#                            learning_rate_init=0.001)

classifier.fit(x_train, y_train)

print('Best parameters found:\n', classifier.best_params_)

y_pred = classifier.predict(x_test)
acc = accuracy_score(y_test, y_pred)
print(acc)
