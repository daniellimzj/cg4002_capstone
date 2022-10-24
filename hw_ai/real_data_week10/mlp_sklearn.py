import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from hyperopt import fmin, tpe, Trials, hp, STATUS_OK
from hyperopt.early_stop import no_progress_loss
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler

# config
np.set_printoptions(threshold=np.inf)
np.set_printoptions(formatter={'float_kind':'{:.12f}'.format})
scaler = StandardScaler()

data = pd.read_csv('main.csv')
# Replace this line with your test csv
# validate_data = pd.read_csv('test_main.csv')

x = data[['meanaccX','maxaccX','minaccX','varaccX','medianaccX','25thpaccX','75thpaccX',
          'meanaccY','maxaccY','minaccY','varaccY','medianaccY','25thpaccY','75thpaccY',
          'meanaccZ','maxaccZ','minaccZ','varaccZ','medianaccZ','25thpaccZ','75thpaccZ',
          'meangyroX','maxgyroX','mingyroX','vargyroX','mediangyroX','25thpgyroX','75thpgyroX',
          'meangyroY','maxgyroY','mingyroY','vargyroY','mediangyroY','25thpgyroY','75thpgyroY',
          'meangyroZ','maxgyroZ','mingyroZ','vargyroZ','mediangyroZ','25thpgyroZ','75thpgyroZ']]

y = data[['label']]
scaler.fit_transform(x)

# This is the testbench
# x_validate = validate_data[['Mean-accX','Range-accX','Var-accX', 'Median-accX',
#           'Mean-accY', 'Range-accY', 'Var-accY', 'Median-accY',
#           'Mean-accZ', 'Range-accZ', 'Var-accZ', 'Median-accZ',
#           'Mean-gyroX', 'Range-gyroX', 'Var-gyroX', 'Median-gyroX',
#           'Mean-gyroY', 'Range-gyroY', 'Var-gyroY', 'Median-gyroY',
#           'Mean-gyroZ', 'Range-gyroZ', 'Var-gyroZ', 'Median-gyroZ',
#           ]]
# y_validate = validate_data[['label']]
y = y.values.reshape(-1, )
# y_validate = y_validate.values.reshape(-1, )

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

baseline_classifier = MLPClassifier(hidden_layer_sizes=(100,100),
                                    activation='relu',)
baseline_classifier.fit(x_train, y_train)
y_baseline_pred = baseline_classifier.predict(x_test)
# y_validate_pred = baseline_classifier.predict(x_validate)
# print(y_validate_pred)
# print("accuracy:" + str(accuracy_score(y_validate, y_validate_pred)))
print("baseline accuracy:" + str(accuracy_score(y_test, y_baseline_pred)))
#
# # Hyperparameter Optimization
coarse_search_space = \
    {'hidden_layer_size': hp.choice('hidden_layer_sizes', range(1, 256)),
     'alpha': hp.lognormal('alpha', mu=np.log(1e-4), sigma=1),
     'solver': hp.choice('algorithm', ['sgd', 'adam']),
     'activation': hp.choice('activation', ['relu']),
     'learning_rate_init': hp.loguniform('learning_rate_init', low=np.log(1e-4), high=np.log(1.)),
     }


def objective_fn(args):
    dict = {
        'hidden_layer_sizes': args['hidden_layer_size'],
        'alpha': args['alpha'],
        'activation': args['activation'],
        'solver': args['solver'],
        'learning_rate_init': args['learning_rate_init'],
        'max_iter': 5000,
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
            max_evals=5000)

best_model = trials.best_trial['result']['model']
plt.plot(best_model.loss_curve_)
print("Training Accuracy: %f" % best_model.score(x_train, y_train))
print("Testing Accuracy: %f" % best_model.score(x_test, y_test))
y_pred = best_model.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()
print(classification_report(y_pred, y_test))
print(best_model)

# Get weights
for i in range(len(best_model.coefs_)):
    weights_file = open('weights' + str(i) + '.txt', "w")
    weight_str = repr(best_model.coefs_[i]).replace("[", "{")
    weight_str = weight_str.replace("]", "}")
    weights_file.write(weight_str)
    weights_file.close()

# Get bias
for i in range(len(best_model.intercepts_)):
    bias_file = open('bias' + str(i) + '.txt', "w")
    bias_str = repr(best_model.intercepts_[i]).replace("[", "{")
    bias_str = bias_str.replace("]", "}")
    bias_file.write(bias_str)
    bias_file.close()

