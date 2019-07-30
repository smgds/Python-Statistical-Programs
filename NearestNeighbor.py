# =============================================================================
# 
'''CPSC-51100, Summer II 2019
NAME: Amy Noyes
PROGRAMMING ASSIGNMENT #3
'''
# =============================================================================
print("\n")
print("CPSC-51100, Summer II 2019", "NAME: Amy Noyes", \
      "PROGRAMMING ASSIGNMENT #3", sep="\n")
      
print("\n")

import numpy as np 

# Load training and testing csv files using NumPy
train_attributes = np.loadtxt('iris-training-data.csv', delimiter = ',', dtype=float, usecols=(0,1,2,3))
train_class = np.loadtxt('iris-training-data.csv', delimiter = ',', dtype=str, usecols=[4])
test_attributes = np.loadtxt('iris-testing-data.csv', delimiter = ',', dtype=float, usecols=(0,1,2,3))
test_class = np.loadtxt('iris-testing-data.csv', delimiter = ',', dtype=str, usecols=[4])

# Array for predicted class labels
predicted_label = []

# Distance function of two instances
dist = lambda point1, point2: np.sqrt(((point1-point2)**2).sum())

# Array of distances in data
distance_matrix = np.asarray([[dist(p1, p2) for p2 in train_attributes] for p1 in test_attributes])

# Calculates closest data
predicted_label = [train_class[np.argmin(x)] for x in distance_matrix]

# Calculates accuracy between predicted and actual
accuracy = ((sum(predicted_label == test_class) / float(test_class.shape[0])) * 100)

# Print actual and predicted
print("#, True, Predicted")
for i in range(0, len(test_class)):
    print(str(i+1), str(test_class[i]), str(predicted_label[i]), sep = ',')

# Print accuracy
print("Accuracy: " + str(round(accuracy, 2))+"%")