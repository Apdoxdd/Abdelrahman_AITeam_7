import numpy as np

class logisticRegression:
    def __init__(self, iterations, lr): #lr is learing rate
        self.iterations = iterations
        self.lr = lr
        self.weights = None
        self.bias    = None
    def sigmoid(self, z):
        return 1/(1 + np.exp(-z))

    def fit(self, x_train, y_train):
        #train the logisitic model using gradient descent
        n_samples, n_features = x_train.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.iterations):
            linear_model = np.dot(x_train, self.weights) + self.bias
            y_predicted = self.sigmoid(linear_model)

            dw = (1 / n_samples) * np.dot(x_train.T, (y_predicted - y_train))
            db = ( 1 / n_samples) * np.sum(y_predicted - y_train)
            self.weights -= self.lr * dw
            self.bias    -= self.lr * db


    def predict(self, x_test):

        linear_model = np.dot(x_test,self.weights) + self.bias
        y_predicted = self.sigmoid(linear_model)

        y_predicted_cls = [1 if i > 0.5 else 0 for i in y_predicted]
        return np.array(y_predicted_cls)
    
    

    