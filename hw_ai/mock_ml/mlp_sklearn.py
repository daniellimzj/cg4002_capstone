import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from hyperopt import fmin, tpe, Trials, hp, STATUS_OK
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

# config
np.set_printoptions(threshold=np.inf)
np.set_printoptions(formatter={'float_kind':'{:.12f}'.format})

data = pd.read_csv('test.csv')
x = data[['Mean-attitude.roll', 'Range-attitude.roll', 'Var-attitude.roll', 'Median-attitude.roll',
          'Mean-attitude.pitch', 'Range-attitude.pitch', 'Var-attitude.pitch', 'Median-attitude.pitch',
          'Mean-attitude.yaw', 'Range-attitude.yaw', 'Var-attitude.yaw', 'Median-attitude.yaw',
          'Mean-rotationRate.x', 'Range-rotationRate.x', 'Var-rotationRate.x', 'Median-rotationRate.x',
          'Mean-rotationRate.y', 'Range-rotationRate.y', 'Var-rotationRate.y', 'Median-rotationRate.y',
          'Mean-rotationRate.z', 'Range-rotationRate.z', 'Var-rotationRate.z', 'Median-rotationRate.z',
          'Mean-userAcceleration.x', 'Range-userAcceleration.x', 'Var-userAcceleration.x', 'Median-userAcceleration.x',
          'Mean-userAcceleration.y', 'Range-userAcceleration.y', 'Var-userAcceleration.y', 'Median-userAcceleration.y',
          'Mean-userAcceleration.z', 'Range-userAcceleration.z', 'Var-userAcceleration.z', 'Median-userAcceleration.z',
          ]]
y = data[['label']]
y = y.values.reshape(-1, )
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)


baseline_classifier = MLPClassifier(hidden_layer_sizes=(5,),
                                    activation='tanh',)
baseline_classifier.fit(x_train, y_train)
y_baseline_pred = baseline_classifier.predict(x_test)
print("baseline accuracy:" + str(accuracy_score(y_test, y_baseline_pred)))

# Hyperparameter Optimization
coarse_search_space = \
    {'hidden_layer_size': hp.choice('hidden_layer_sizes', [(5,), (50,), (50,50)]),
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
        'max_iter': 2000,
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
y_pred = best_model.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()
print(classification_report(y_pred, y_test))

# Get weights
for i in range(len(best_model.coefs_)):
    weights_file = open('weights' + str(i) + '.txt', "w")
    weights_file.write(repr(best_model.coefs_[i]))
    weights_file.close()


# Get bias
for i in range(len(best_model.intercepts_)):
    bias_file = open('bias' + str(i) + '.txt', "w")
    bias_file.write(repr(best_model.intercepts_[i]))
    bias_file.close()
