import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report


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
y = y.values.reshape(-1,)
scaler = StandardScaler()

x = scaler.fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

classifier = KNeighborsClassifier(n_neighbors=10)
classifier.fit(x_train, y_train)

acc = classifier.score(x_test, y_test)
print(acc)
y_pred = classifier.predict(x_test)
print(classification_report(y_pred, y_test))


