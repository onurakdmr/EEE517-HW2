# -*- coding: utf-8 -*-
"""EEE517-DeepLearningMethods&Applications

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GUKaNrp-8x66jhWI2TIqUwZvEkmdmvqi

Onur Akdemir

20223516007

EEE 517 - Deep Learning Methods and Applications

Homework
"""

#Dataset selection and adding that dataset to Google Colab. (Breast Cancer Dataset)

from sklearn.datasets import load_breast_cancer

# Load the Breast Cancer dataset (load_breast_cancer() loads the Breast Cancer dataset from scikit-learn.)
data = load_breast_cancer()

# Access features and target variable (data.data contains the features, data.target contains the target variable.)
X, y = data.data, data.target

# Import necessary libraries
import pandas as pd
from sklearn.datasets import load_breast_cancer

# Load the Breast Cancer dataset
data = load_breast_cancer()
X, y = data.data, data.target

# Create a DataFrame with features and target variable
df = pd.DataFrame(X, columns=data.feature_names)
df['target'] = y

# Display the entire DataFrame
pd.set_option('display.max_rows', None)  # Set option to display all rows
pd.set_option('display.max_columns', None)  # Set option to display all columns
print(df)

pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')

# Display the first few rows of the features
import pandas as pd
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
df.head()

print(df.tail())  # Print the last few rows

"""Inputs (Features) like mean radius, mean texture, mean smoothness, etc.

Outputs (Targets) are Binary classification: Malignant or Benign tumor (1 or 0).
"""

# Partb

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix, classification_report

data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

input_size = X_train.shape[1]
output_size = 1

configurations = [
    {'hidden_size': 5, 'batch_size': 32},
    {'hidden_size': 10, 'batch_size': 64},
    {'hidden_size': 15, 'batch_size': 128},
]

# Learning rate and other Adam optimizer parameters
learning_rate = 0.001
beta_1 = 0.9
beta_2 = 0.999
epsilon = 1e-8

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix, accuracy_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Training and Testing for each configuration
for config in configurations:
    model = Sequential()
    model.add(Dense(config['hidden_size'], activation='sigmoid', input_dim=input_size))
    model.add(Dense(output_size, activation='sigmoid'))

    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate, beta_1=beta_1, beta_2=beta_2, epsilon=epsilon)
    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

    history = model.fit(X_train, y_train, epochs=50, batch_size=config['batch_size'], verbose=0)

    # Testing the Neural Network
    predicted_labels = (model.predict(X_test) > 0.5).astype(int)

    # Calculate confusion matrix and related metrics
    conf_matrix = confusion_matrix(y_test, predicted_labels)
    accuracy = np.mean(predicted_labels == y_test)
    precision = conf_matrix[1, 1] / (conf_matrix[1, 1] + conf_matrix[0, 1])
    recall = conf_matrix[1, 1] / (conf_matrix[1, 1] + conf_matrix[1, 0])
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(f'\nConfiguration: {config}')
    print(f'Training Epochs: {len(history.history["loss"])}')  # Print the number of training epochs
    print(f'Confusion Matrix:\n{conf_matrix}')
    print(f'Accuracy: {accuracy}')
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')
    print(f'F1 Score: {f1_score}\n')

# Partc

# Library Imports: The code adds imports for TensorFlow and Keras modules:
import tensorflow as tf
from tensorflow.keras.models import Sequential  # Import Sequential module
from tensorflow.keras.layers import Dense

# Load Breast Cancer dataset
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Neural Network Architecture
input_size = X_train.shape[1]
output_size = 1

configurations = [
    {'hidden_size': 5, 'batch_size': 32},
    {'hidden_size': 10, 'batch_size': 64},
    {'hidden_size': 15, 'batch_size': 128},
]

# Learning rate and other Adam optimizer parameters
learning_rate = 0.001
beta_1 = 0.9
beta_2 = 0.999
epsilon = 1e-8

# Training and Testing for each configuration
for config in configurations:
    # Neural Network Model Creation: The code uses the Sequential model from Keras to build the neural network:
    model = Sequential()
    # Layer Addition: The code uses the add method to add layers to the model:
    model.add(Dense(config['hidden_size'], activation='sigmoid', input_dim=input_size))
    model.add(Dense(output_size, activation='sigmoid'))

    # Model Compilation: The code uses the compile method to configure the model with the optimizer, loss function, and metrics:
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate, beta_1=beta_1, beta_2=beta_2, epsilon=epsilon)
    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

    # Training History: The code uses the history object returned by the fit method to access training history:
    history = model.fit(X_train, y_train, epochs=50, batch_size=config['batch_size'], verbose=0)

    # Testing the Neural Network
    # Prediction and Evaluation: The code uses the trained model to make predictions and evaluate the performance:
    predicted_labels = (model.predict(X_test) > 0.5).astype(int)

    # Calculate confusion matrix and related metrics
    conf_matrix = confusion_matrix(y_test, predicted_labels)
    accuracy = np.mean(predicted_labels == y_test)
    precision = conf_matrix[1, 1] / (conf_matrix[1, 1] + conf_matrix[0, 1])
    recall = conf_matrix[1, 1] / (conf_matrix[1, 1] + conf_matrix[1, 0])
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(f'\nConfiguration: {config}')
    print(f'Training Epochs: {len(history.history["loss"])}')
    print(f'Confusion Matrix:\n{conf_matrix}')
    print(f'Accuracy: {accuracy}')
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')
    print(f'F1 Score: {f1_score}\n')

#Part4

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix, accuracy_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load Breast Cancer dataset
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Neural Network Architecture
input_size = X_train.shape[1]
output_size = 1

# Learning rate and other Adam optimizer parameters
learning_rate = 0.001
beta_1 = 0.9
beta_2 = 0.999
epsilon = 1e-8

# Different configurations of hidden layers and neurons
configurations = [
    {'hidden_layers': 1, 'neurons': 5, 'batch_size': 32},
    {'hidden_layers': 2, 'neurons': 10, 'batch_size': 64},
    {'hidden_layers': 3, 'neurons': 15, 'batch_size': 128},
]

# Training and Testing for each configuration
for config in configurations:
    model = Sequential()

    # Add input layer
    model.add(Dense(config['neurons'], activation='sigmoid', input_dim=input_size))

    # Add hidden layers
    for _ in range(config['hidden_layers'] - 1):
        model.add(Dense(config['neurons'], activation='sigmoid'))

    # Add output layer
    model.add(Dense(output_size, activation='sigmoid'))

    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate, beta_1=beta_1, beta_2=beta_2, epsilon=epsilon)
    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

    history = model.fit(X_train, y_train, epochs=50, batch_size=config['batch_size'], verbose=0)

    # Testing the Neural Network
    predicted_labels = (model.predict(X_test) > 0.5).astype(int)

    # Calculate confusion matrix and accuracy
    conf_matrix = confusion_matrix(y_test, predicted_labels)
    accuracy = accuracy_score(y_test, predicted_labels)

    print(f'\nConfiguration: {config}')
    print(f'Training Epochs: {len(history.history["loss"])}')
    print(f'Confusion Matrix:\n{conf_matrix}')
    print(f'Accuracy: {accuracy}\n')

from sklearn.metrics import confusion_matrix, classification_report

# Make predictions on the test set
y_pred = model.predict(X_test)
y_pred_binary = (y_pred > 0.5).astype(int)

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred_binary)
print("Confusion Matrix:")
print(conf_matrix)

# Classification Report
print("Classification Report:")
print(classification_report(y_test, y_pred_binary))



"""Part 2:

Configuration: {'hidden_size': 5, 'batch_size': 32}
Accuracy: 53.44%
Precision: 97.26%
Recall: 100%
F1 Score: 98.61%

Configuration: {'hidden_size': 10, 'batch_size': 64}
Accuracy: 53.23%
Precision: 98.61%
Recall: 100%
F1 Score: 99.30%

Configuration: {'hidden_size': 15, 'batch_size': 128}
Accuracy: 53.02%
Precision: 97.18%
Recall: 97.18%
F1 Score: 97.18%
"""



"""Part 3:

Configuration: {'hidden_size': 5, 'batch_size': 32}
Accuracy: 53.23%
Precision: 98.61%
Recall: 100%
F1 Score: 99.30%

Configuration: {'hidden_size': 10, 'batch_size': 64}
Accuracy: 53.02%
Precision: 98.59%
Recall: 98.59%
F1 Score: 98.59%

Configuration: {'hidden_size': 15, 'batch_size': 128}
Accuracy: 53.88%
Precision: 94.67%
Recall: 100%
F1 Score: 97.26%

Part 4:

Configuration: {'hidden_layers': 1, 'neurons': 5, 'batch_size': 32}
Accuracy: 98.25%

Configuration: {'hidden_layers': 2, 'neurons': 10, 'batch_size': 64}
Accuracy: 98.25%

Configuration: {'hidden_layers': 3, 'neurons': 15, 'batch_size': 128}
Accuracy: 85.96%[link text](https://)
"""



"""Part 5:

Confusion Matrix:
[[27 16]
 [ 0 71]]

Classification Report:
Precision:
Class 0: 100%
Class 1: 82%

ecall:
Class 0: 63%
Class 1: 100%

F1 Score:
Class 0: 77%
Class 1: 90%
"""



"""Overall Summary:

Part 2 and Part 3: Similar performances, slight variations in precision and recall.

Part 4: Configuration with one hidden layer and five neurons achieved the highest accuracy.

Part 5: The model achieved good precision and recall for both classes, but there is room for improvement in class 0's precision and recall.


These results provide insights into how different configurations affect the model's performance. Depending on your specific goals and constraints, you might choose the configuration that best suits your needs.
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Example Line Plot for Training History
plt.figure(figsize=(10, 5))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Value')
plt.title('Training History')
plt.legend()
plt.show()

# Example Bar Plot for Accuracy, Precision, Recall, and F1 Score
metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
values = [accuracy, precision, recall, f1_score]

plt.figure(figsize=(8, 5))
plt.bar(metrics, values, color=['blue', 'green', 'orange', 'red'])
plt.title('Model Metrics')
plt.ylabel('Value')
plt.show()

# Example Confusion Matrix Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='g', xticklabels=['0', '1'], yticklabels=['0', '1'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

import matplotlib.pyplot as plt

# Results from Part 2
configurations_part2 = [
    {'hidden_size': 5, 'batch_size': 32},
    {'hidden_size': 10, 'batch_size': 64},
    {'hidden_size': 15, 'batch_size': 128},
]

# Accuracy, Precision, Recall, F1 Score
accuracy_part2 = [0.534, 0.532, 0.530]
precision_part2 = [0.973, 0.986, 0.972]
recall_part2 = [1.0, 1.0, 0.972]
f1_score_part2 = [0.986, 0.993, 0.972]

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.plot([config['hidden_size'] for config in configurations_part2], accuracy_part2, marker='o')
plt.title('Accuracy')
plt.xlabel('Hidden Size')

plt.subplot(2, 2, 2)
plt.plot([config['hidden_size'] for config in configurations_part2], precision_part2, marker='o')
plt.title('Precision')
plt.xlabel('Hidden Size')

plt.subplot(2, 2, 3)
plt.plot([config['hidden_size'] for config in configurations_part2], recall_part2, marker='o')
plt.title('Recall')
plt.xlabel('Hidden Size')

plt.subplot(2, 2, 4)
plt.plot([config['hidden_size'] for config in configurations_part2], f1_score_part2, marker='o')
plt.title('F1 Score')
plt.xlabel('Hidden Size')

plt.tight_layout()
plt.show()

