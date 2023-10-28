from collections import Counter
import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.4f} seconds to execute.")
        return execution_time
    return wrapper

@timing_decorator
def count_dict(filename):
    word_count = {}
    with open(filename,'r') as file:
        text = file.read()
        split_text = text.split()

        for word in split_text:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count

@timing_decorator
def count_Counter(filename):
    with open(filename, 'r') as file:
        text = file.read()
        split_text = text.split()
        word_count = Counter(split_text)
    
    return word_count

#%%
from count_functions import count_dict,count_Counter
import matplotlib
import matplotlib.pyplot as plt

filename = "shakespear.txt"
list_dict = []
list_counter = []

for i in range(100):
    list_dict.append(count_dict(filename))
    list_counter.append(count_Counter(filename))
    

plt.hist(list_dict, bins=10, edgecolor='k', alpha=0.7, label="dict")
plt.hist(list_counter, bins=10, edgecolor='k', alpha=0.7,label="counter")
plt.legend()
plt.title("Comparison of execution time distribution")
# %%
