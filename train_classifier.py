import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data from the pickle file
data_dict = pickle.load(open('./data.pickle', 'rb'))
labels = data_dict['labels']
data = data_dict['data']

# Determine the maximum number of landmarks
max_landmarks = max(len(sample) for sample in data)

# Pad each sample in data with zeros to make them all the same length
for sample in data:
    while len(sample) < max_landmarks:
        sample.extend([0, 0])  # Assuming each landmark has an x and y coordinate

# Convert lists to NumPy arrays
labels = np.array(labels)
data = np.array(data)

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Create and train the model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Evaluate the model
y_predict = model.predict(x_test)
score = accuracy_score(y_predict, y_test)
print('{}% of samples were classified correctly!'.format(score * 100))

# Save the trained model
with open('model.p', 'wb') as f:
    pickle.dump({'model': model}, f)
