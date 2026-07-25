import numpy as np
from classification import logisticRegression

def create_toy_dataset():
    
    np.random.seed(42)
    
    
    X_class0 = np.random.randn(50, 2) - [2, 2]
    y_class0 = np.zeros(50)

    
    X_class1 = np.random.randn(50, 2) + [2, 2]
    y_class1 = np.ones(50)

    
    X = np.vstack((X_class0, X_class1))
    y = np.hstack((y_class0, y_class1))
    
    shuffle_idx = np.random.permutation(len(X))
    return X[shuffle_idx], y[shuffle_idx]

def main():
    
    X, y = create_toy_dataset()

    split_index = int(0.8 * len(X))
    X_train, X_test = X[:split_index], X[split_index:]
    y_train, y_test = y[:split_index], y[split_index:]

   
    model = logisticRegression(iterations=1000, lr=0.1)

   # train the model
    print("Training model...")
    model.fit(X_train, y_train)


    predictions = model.predict(X_test)

   
    accuracy = np.sum(y_test == predictions) / len(y_test)
    print(f"Model Accuracy on Test Set: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    main()

#lmao 100% accurecy talk about overfitting