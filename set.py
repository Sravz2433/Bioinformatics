import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_csv('Lab_A7_iris.data.csv')

# Shuffle and split dataset (80% train, 20% test)
train_set, test_set = train_test_split(data, test_size=0.2, random_state=42, shuffle=True)

print(f"Train set size: {len(train_set)}")
print(f"Test set size: {len(test_set)}")


# Separating features (X) and target (y)
X = train_set.iloc[:, :-1]  # all columns except the last one
y = train_set.iloc[:, -1]   # last column (target)

# Label encode the target (species)
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# K-Fold Cross Validation (K=4)
k = 4
kf = KFold(n_splits=k, random_state=42, shuffle=True)

# Implement KNN with K=5
knn = KNeighborsClassifier(n_neighbors=5)

# Perform cross-validation and calculate accuracy for each fold
cross_val_scores = cross_val_score(knn, X, y, cv=kf)

# Report cross-validation results
print(f"Cross-validation scores: {cross_val_scores}")
print(f"Mean accuracy: {cross_val_scores.mean()}")
print(f"Standard deviation: {cross_val_scores.std()}")

import numpy as np

# Range of K values to test
k_values = range(1, 21)

# Store mean accuracy for each K value
mean_scores = []
std_devs = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=kf)
    mean_scores.append(scores.mean())
    std_devs.append(scores.std())

# Find the best K value
best_k = k_values[np.argmax(mean_scores)]

print(f"Best K value: {best_k}")

# Train KNN with the best K value
best_knn = KNeighborsClassifier(n_neighbors=best_k)
best_knn.fit(X, y)

# Calculate validation accuracy
validation_accuracy = max(mean_scores)
validation_std_dev = std_devs[np.argmax(mean_scores)]

# Evaluate on test set
X_test = test_set.iloc[:, :-1]
y_test = test_set.iloc[:, -1]
y_test = encoder.transform(y_test)

test_accuracy = best_knn.score(X_test, y_test)

print(f"Validation Accuracy: {validation_accuracy} ± {validation_std_dev}")
print(f"Test Accuracy: {test_accuracy}")