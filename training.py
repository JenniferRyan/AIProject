from prep_glass import load_glass_training, load_glass_test
from sklearn import svm
from sklearn.metrics import accuracy_score

# Classifier
clf = svm.SVC()

# Training and Test Data Loading
train, test = load_glass_training(), load_glass_test()

X, y = train.data, train.target

# Classifier fitted with training data and training labels
clf.fit(X, y)

# Use the test data on the classifier to predict it's classes
pred = clf.predict(test.data)

# Check how accurate the classifier was at predicting the test data
print accuracy_score(pred, test.target)