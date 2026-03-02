import numpy as np
import matplotlib.pyplot as plt
#you can run the cod directly in this file btw
def reg():
    h_sizes=[50, 60, 80, 100, 120]
    h_prices=[150, 180, 240, 300, 330]
    #Converting the inputs and outputs to np array
    features = np.array(h_sizes)
    outputs = np.array(h_prices)
    plt.figure(1)
    plt.plot(features,outputs,"bo")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("prices/house_size data")
    #############################################
    #reshaping the features array
    print("The features: ",features)
    
    features = features.reshape(-1,1)
    print("The features as column vector",features)
    #adding a bias column for the theta node term
    rows,cols = np.shape(features) #to dynamically asses the bias even if features num change
    bias = np.ones((rows,1),int)
    biased_features=np.hstack((bias,features))#to makebias the first column
    print("The biased features: ",biased_features)
    #implementing normal equation
    theta_sub = np.linalg.inv(biased_features.T@ biased_features)#first term
    theta = theta_sub@(biased_features.T@outputs) #entire equation
    print("The normal function weights: ",theta) 
    # calculate the price for 90m^2 house
    x_test = np.array([[1,90]])
    y_test = x_test@theta
    print("Predicted value for the 90 m^2 house: ",y_test)
    x_graph = np.array([[0],[300]])
    x_graph_1 = np.c_[np.ones((2,1)),x_graph]
    y_graph = x_graph_1 @ theta
    plt.figure(2)
    plt.plot(x_graph_1[:,1],y_graph,"r--",label="Regression Line")
    plt.plot(features,outputs,"bo")
    plt.legend()
    plt.show()














if __name__=="__main__":
 reg()
