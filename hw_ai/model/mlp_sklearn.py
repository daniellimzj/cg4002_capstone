import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from hyperopt import fmin, tpe, Trials, hp, STATUS_OK
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler
import joblib

# config
np.set_printoptions(threshold=np.inf)
np.set_printoptions(formatter={'float_kind': '{:.12f}'.format})
scaler = StandardScaler()
data = pd.read_csv('main.csv')
# Replace this line with your test csv
# validate_data = pd.read_csv('main_test.csv')

x = data[['meanaccX', 'maxaccX', 'minaccX', 'varaccX', 'medianaccX', '25thpaccX', '75thpaccX',
          'meanaccY', 'maxaccY', 'minaccY', 'varaccY', 'medianaccY', '25thpaccY', '75thpaccY',
          'meanaccZ', 'maxaccZ', 'minaccZ', 'varaccZ', 'medianaccZ', '25thpaccZ', '75thpaccZ',
          'meangyroX', 'maxgyroX', 'mingyroX', 'vargyroX', 'mediangyroX', '25thpgyroX', '75thpgyroX',
          'meangyroY', 'maxgyroY', 'mingyroY', 'vargyroY', 'mediangyroY', '25thpgyroY', '75thpgyroY',
          'meangyroZ', 'maxgyroZ', 'mingyroZ', 'vargyroZ', 'mediangyroZ', '25thpgyroZ', '75thpgyroZ']]

y = data[['label']]
x_scaled = scaler.fit_transform(x)
joblib.dump(scaler, 'scaler.joblib')
# This is the testbench
# x_validate = validate_data[['meanaccX', 'maxaccX', 'minaccX', 'varaccX', 'medianaccX', '25thpaccX', '75thpaccX',
#                             'meanaccY', 'maxaccY', 'minaccY', 'varaccY', 'medianaccY', '25thpaccY', '75thpaccY',
#                             'meanaccZ', 'maxaccZ', 'minaccZ', 'varaccZ', 'medianaccZ', '25thpaccZ', '75thpaccZ',
#                             'meangyroX', 'maxgyroX', 'mingyroX', 'vargyroX', 'mediangyroX', '25thpgyroX', '75thpgyroX',
#                             'meangyroY', 'maxgyroY', 'mingyroY', 'vargyroY', 'mediangyroY', '25thpgyroY', '75thpgyroY',
#                             'meangyroZ', 'maxgyroZ', 'mingyroZ', 'vargyroZ', 'mediangyroZ', '25thpgyroZ', '75thpgyroZ']]

# y_validate = validate_data[['label']]
y = y.values.reshape(-1, )
# y_validate = y_validate.values.reshape(-1, )

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.3, random_state=42)
print("train size:" + str(len(x_train)))
print("test size:" + str(len(x_test)))
baseline_classifier = MLPClassifier()
baseline_classifier.fit(x_train, y_train)
print("baseline accuracy: %f" % baseline_classifier.score(x_test, y_test))
y_p = baseline_classifier.predict(x_test)
cm = confusion_matrix(y_test, y_p)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()
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
        'max_iter': 3000,
    }
    classifier = MLPClassifier(**dict)
    loss = cross_val_score(classifier, x_train, y_train, cv=10, n_jobs=-1).mean()
    return {'loss': -loss, 'status': STATUS_OK, 'model': classifier}


trials = Trials()
best = fmin(objective_fn,
            space=coarse_search_space,
            algo=tpe.suggest,
            trials=trials,
            max_evals=12)
solver = {0: 'sgd', 1: 'adam'}
best_model = MLPClassifier(hidden_layer_sizes=best['hidden_layer_sizes'],
                           alpha=best['alpha'],
                           activation='relu',
                           solver=solver[best['algorithm']],
                           learning_rate_init=best['learning_rate_init']).fit(x_train, y_train)

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

