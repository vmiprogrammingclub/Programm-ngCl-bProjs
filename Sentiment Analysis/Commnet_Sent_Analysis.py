import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import random
import pickle

data_dir = "/Users/zacharris/Desktop/reviews/train"
categories = ["pos", "neg"]


IMG_SIZE = 50
training_data = []
X = []
y = []


def create_training_data():
	for category in categories:
		path = os.path.join(data_dir, category) # path to cats or dogs dir
		class_num = categories.index(category)
		for comment in os.listdir(path):
			try:
				file = open(os.path.join(path,img), "r+")
				# new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
				text = file.read()
				file.close()
				new_array = text.split(' ')
				for i in new_array:
					for j in i:
						if (not j.isalnum()):
							i.replace(j, "")
				training_data.append([new_array, class_num])
			except Exception as e:
				pass
	random.shuffle(training_data)





# print(len(training_data))

for sample in training_data[:10]:
	print(sample[1])

def create_model():
	global X

	for features, label in training_data:
		X.append(features)
		y.append(label)



	# X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1) 

# attempt to make a conv. NN from grayscale to color ^^ change 1 to a 3


def saveFile():
	pickle_out = open("X.pickle", "wb")
	pickle.dump(X, pickle_out)
	pickle_out.close()

	pickle_out = open("y.pickle", "wb")
	pickle.dump(y, pickle_out)
	pickle_out.close()


# to open:
# def openFile():
# 	pickle_in = open("X.pickle", "rb")
# 	X = pickle.load(pickle_in)

def main():
	create_training_data()
	create_model()
	saveFile()

main()







