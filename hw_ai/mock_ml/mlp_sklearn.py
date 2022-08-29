import pandas as pd
import numpy as np
from hyperopt import fmin, tpe, Trials, hp, STATUS_OK
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('test.csv')
x = data[['meanattitude.roll', 'rangeattitude.roll', 'sdattitude.roll', 'varattitude.roll', 'medianattitude.roll',
          'meanattitude.pitch', 'rangeattitude.pitch', 'sdattitude.pitch', 'varattitude.pitch', 'medianattitude.pitch',
          'meanattitude.yaw', 'rangeattitude.yaw', 'sdattitude.yaw', 'varattitude.yaw', 'medianattitude.yaw',
          'meanrotationRate.x', 'rangerotationRate.x', 'sdrotationRate.x', 'varrotationRate.x', 'medianrotationRate.x',
          'meanrotationRate.y', 'rangerotationRate.y', 'sdrotationRate.y', 'varrotationRate.y', 'medianrotationRate.y',
          'meanrotationRate.z', 'rangerotationRate.z', 'sdrotationRate.z', 'varrotationRate.z', 'medianrotationRate.z',
          'meanuserAcceleration.x', 'rangeuserAcceleration.x', 'sduserAcceleration.x', 'varuserAcceleration.x',
          'medianuserAcceleration.x', 'meanuserAcceleration.y', 'rangeuserAcceleration.y', 'sduserAcceleration.y',
          'varuserAcceleration.y', 'medianuserAcceleration.y', 'meanuserAcceleration.z', 'rangeuserAcceleration.z',
          'sduserAcceleration.z', 'varuserAcceleration.z', 'medianuserAcceleration.z'
          ]]
y = data[['label']]
scaler = StandardScaler()

x = scaler.fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

baseline_classifier = MLPClassifier()
baseline_classifier.fit(x_train, y_train)
y_baseline_pred = baseline_classifier.predict(x_test)
print("baseline accuracy:" + str(accuracy_score(y_test, y_baseline_pred)))

coarse_search_space = \
    {'hidden_layer_size': hp.choice('hidden_layer_sizes', [(50,), (50, 50,), (50,50,50)]),
     'alpha': hp.lognormal('alpha', mu=np.log(1e-4), sigma=1),
     'solver': hp.choice('algorithm', ['sgd', 'adam']),
     'activation': hp.choice('activation', ['logistic', 'tanh', 'relu']),
     'learning_rate_init': hp.loguniform('learning_rate_init', low=np.log(1e-4), high=np.log(1.)),
     }


def objective_fn(args):
    dict = {
        'hidden_layer_sizes': args['hidden_layer_size'],
        'alpha': args['alpha'],
        'activation': args['activation'],
        'solver': args['solver'],
        'learning_rate_init': args['learning_rate_init'],
    }
    classifier = MLPClassifier(**dict)
    classifier.fit(x_train, y_train)
    loss = -classifier.score(x_test, y_test)
    return {'loss': loss, 'status': STATUS_OK, 'model': classifier}


trials = Trials()
best = fmin(objective_fn,
            space=coarse_search_space,
            algo=tpe.suggest,
            trials=trials,
            max_evals=10)

best_model = trials.best_trial['result']['model']
print("Training Accuracy: %f" % best_model.score(x_train, y_train))
print("Testing Accuracy: %f" % best_model.score(x_test, y_test))

print(best)
