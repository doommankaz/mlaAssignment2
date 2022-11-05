import random
import string
import numpy as np


def create_dataset():
    className = ['category1', 'category2', 'category3']
    data = []
    n_entries = 1500
    for entry in range(n_entries):
        row = [random_seq(),
               entry - (entry * np.random.normal(0, 0.3)),
               entry - (entry * np.random.normal(0, 0.3)),
               entry - (entry * np.random.normal(0, 0.3)),
               random.choice(className),
               entry]
        data.append(row)
        random.shuffle(data)
    _data = ""
    for d in data:
        _data += str(d) + "\n"
    print(_data)


def random_seq(stringLength=15):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(stringLength))


if __name__ == '__main__':
    create_dataset()
