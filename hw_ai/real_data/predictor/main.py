import numpy as np
import pandas as pd
from pynq import allocate 
from pynq import Overlay 
import time as time 


COLUMNS = ['Mean-accX', 'Range-accX', 'Var-accX', 'Median-accX', 'Mean-accY', 'Range-accY', 'Var-accY', 'Median-accY', 'Mean-accZ', 'Range-accZ', 'Var-accZ', 'Median-accZ', 'Mean-gyroX', 'Range-gyroX',
    'Var-gyroX', 'Median-gyroX', 'Mean-gyroY', 'Range-gyroY', 'Var-gyroY', 'Median-gyroY', 'Mean-gyroZ', 'Range-gyroZ', 'Var-gyroZ', 'Median-gyroZ']

INDEX_TO_ACTION_MAP = {1: "grenade", 2: "reload", 3: "shield", 4: "logout", 5: "idle"}

start = time.time_ns()
overlay = Overlay('design_1.bit')
print(overlay.is_loaded())
for i in overlay.ip_dict:
    print(i)
dma = overlay.axi_dma_0
dma_send = overlay.axi_dma_0.sendchannel
dma_recv = overlay.axi_dma_0.recvchannel

input_buffer = allocate(shape=(24,), dtype = np.float32)
output_buffer = allocate(shape=(5,), dtype = np.float32)

# Form test variables
df = pd.read_csv('extracted_features.csv')
x = df[['Mean-accX', 'Range-accX', 'Var-accX', 'Median-accX', 'Mean-accY', 'Range-accY', 'Var-accY', 'Median-accY', 'Mean-accZ', 'Range-accZ', 'Var-accZ', 'Median-accZ', 'Mean-gyroX', 'Range-gyroX',
    'Var-gyroX', 'Median-gyroX', 'Mean-gyroY', 'Range-gyroY', 'Var-gyroY', 'Median-gyroY', 'Mean-gyroZ', 'Range-gyroZ', 'Var-gyroZ', 'Median-gyroZ']]

y = df[['label']]

correct = 0
total = len(df.index)

for index,row in x.iterrows():
    test_data = row.tolist()
    correct_label = y.iloc[index].tolist()
    input_buffer[:] = test_data
    #start_time = time.time_ns()
    dma_send.transfer(input_buffer)
    dma_recv.transfer(output_buffer)

    dma_send.wait()
    dma_recv.wait()
    idx = output_buffer.argmax(axis=0) + 1
    #end_time = time.time_ns()
    if idx == correct_label:
        correct += 1

# Get accuracy score
#print("Total rows: ", total)
print("Accuracy score: ", correct/total * 100 )
#print("Time taken: ", end_time - start_time)


class MoveClassifier:
    def __init__(self):
        self.overlay = Overlay('design_1.bit')
        self.dma = self.overlay.axi_dma_0
        self.dma_send = self.overlay.axi_dma_0.sendchannel
        self.dma_recv = self.overlay.axi_dma_0.recvchannel

        self.input_buffer = allocate(shape=(24,), dtype = np.float32)
        self.output_buffer = allocate(shape=(5,), dtype = np.float32)

    def classifyMove(self, data):
        self.input_buffer[:] = data

        self.dma_send.transfer(self.input_buffer)
        self.dma_recv.transfer(self.output_buffer)

        self.dma_send.wait()
        self.dma_recv.wait()
        idx = output_buffer.argmax(axis=0) + 1

        return INDEX_TO_ACTION_MAP[idx]