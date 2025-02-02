import json
import timeit
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Load JSON
def load(file, n):
    with open(file, 'r', encoding='utf8') as file:
        data = json.load(file)
    return data[:n]

#modify JSON
def modify(data):
    for record in data:
        record['size'] = 42
    return data

def process(n):
    data = load('large-file.json', n)
    data = modify(data)


# Measure execution time
sizes = [1000, 2000, 5000, 10000]
time_results = []


for size in sizes:
    time_taken = timeit.timeit(lambda: process(size), number=100)
    time_results.append(time_taken / 100)
    
sizes_np = np.array(sizes).reshape(-1, 1)
time_results_np = np.array(time_results)
model = LinearRegression()
model.fit(sizes_np, time_results_np)
predicted = model.predict(sizes_np)

plt.figure(figsize=(10, 6))
plt.scatter(sizes, time_results, color='blue', label='Actual')
plt.plot(sizes, predicted, color='red', label='Predicted')
plt.xlabel('Number of Records')
plt.ylabel('Time (s)')
plt.title('Linear Regression of Execution Time')
plt.legend()
plt.savefig('output.3.2.png')
plt.show()