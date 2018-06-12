from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

digits = datasets.load_digits()
def display_img(img_no):
    fig, ax = plt.subplots()
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.matshow(digits.images[img_no], cmap=plt.cm.binary);
    plt.show()
display_img(0)
#print(digits.images[0])
#print(digits.data[0].shape)
#print(digits.target[0])