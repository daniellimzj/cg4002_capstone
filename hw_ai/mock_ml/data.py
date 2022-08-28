import os
import pandas as pd

data_path = os.path.join(os.getcwd(), 'A_DeviceMotion_data')

# specified in dataset
sampling_rate = 50
window_size = 2
num_of_data_per_window = sampling_rate * window_size

raw_features = ["attitude.roll",
                "attitude.pitch",
                "attitude.yaw",
                "rotationRate.x",
                "rotationRate.y",
                "rotationRate.z",
                "userAcceleration.x",
                "userAcceleration.y",
                "userAcceleration.z",]

extracted_features_list = ["mean", "range", "sd", "var", "median"]
extracted_features_dict = dict.fromkeys(["mean", "range", "sd", "var", "median"])
num_raw_features = len(raw_features)
num_extracted_features = len(extracted_features_dict)
print("num of raw features=" + str(num_raw_features) + '\n')
df3 = pd.DataFrame()


# This function takes in a series of data and an index to denote the operation, and returns
# the processed data
def extract(series, index):
    operations = ["mean", "range", "sd", "var", "median"]
    if index == 0:
        return series.mean()
    elif index == 1:
        return series.max() - series.min()
    elif index == 2:
        return series.std()
    elif index == 3:
        return series.var()
    elif index == 4:
        return series.median()


def transform(string):
    if string == 'dws':
        return 1
    elif string == 'ups':
        return 2
    elif string == 'sit':
        return 3
    elif string == 'std':
        return 4
    elif string == 'wlk':
        return 5
    elif string == 'jog':
        return 6


# This function creates new column names for a given raw feature
# i.e, if raw feature = yaw, then [mean yaw, range yaw... etc] is returned.
def util(raw_feature):
    operations = ["mean", "range", "sd", "var", "median"]
    col_vector = []
    for ii in range(len(operations)):
        col_vector.append(operations[ii] + raw_feature)
    return col_vector


for root, dirs, files in os.walk(data_path):
    for file in files:
        path = os.path.join(root, file)
        label = path.split("\\")[-2].split("_")[0]
        df = pd.read_csv(path)
        total_num_of_points = df.shape[0]
        num_of_windows = int(total_num_of_points / num_of_data_per_window)

        # Iterate through each window
        for i in range(num_of_windows):
            # Aggregate Data from all data points in the window and extract the features
            start = i * num_of_data_per_window
            end = start + num_of_data_per_window
            df2 = pd.DataFrame()
            # Iterate through the raw features
            for j in range(num_raw_features):
                raw_data_series = df.iloc[start:end][raw_features[j]]
                # Iterate through to obtain 5 extracted features from 1 raw feature
                col_v = util(raw_features[j])
                temp_df = pd.DataFrame(columns=col_v)
                for x in range(num_extracted_features):
                    feature = extract(raw_data_series, x)
                    name_extracted_feature = extracted_features_list[x]
                    temp_df.at[0, col_v[x]] = feature
                df2 = pd.concat([df2, temp_df], axis=1)
            df2['label'] = transform(label)
            # Concatenate windows together
            df3 = pd.concat([df3, df2])

df3.to_csv("test.csv")


