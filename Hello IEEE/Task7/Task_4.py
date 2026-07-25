import numpy as np
from Task_3.classification import logisticRegression


def main():
    # 1. Define the 4D XOR dataset based on the provided truth table
    X = np.array([
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 0, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ])
    
    y = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0])

    model = logisticRegression(iterations=5000, lr=0.1)

    print("Training model on 4D XOR dataset...")
    model.fit(X, y)

    predictions = model.predict(X)

    
    accuracy = np.sum(y == predictions) / len(y)
    
    print("-" * 30)
    print(f"target outputs: {y}")
    print(f"Model Predicts: {predictions}")
    print("-" * 30)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    main()    


