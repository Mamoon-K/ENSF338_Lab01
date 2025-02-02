from ex3_2 import process
import matplotlib.pyplot as plt
import timeit


repeat_times = timeit.repeat(lambda: process(1000), repeat=1000, number=1)
plt.figure(figsize=(10, 6))
plt.hist(repeat_times, bins=30, edgecolor='black')
plt.xlabel("Execution Time (s)")
plt.ylabel("Frequency")
plt.title("Histogram of Execution Times for 1000 Records")
plt.savefig("output.3.3.png")
plt.show()
