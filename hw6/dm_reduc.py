"""Toy dimension reduction."""
import matplotlib.pyplot as plt
import numpy as np

## vector sparse: many zeros (document-term matrix / term-term matrix)
## take up space
## makes ML task harder
# if a dimension is useful
def generate_data(cls: dict, num: int = 100) -> np.ndarray:
    return np.random.multivariate_normal(
        cls["mu"],
        cls["sigma"],
        size=num,
    )
    

def main():
    classes = [{
        "mu":np.array([0,0]),
        "sigma": np.array([[1,0],[0,0.2]])# covariance matrix
        },
        {
        "mu":np.array([4,4]),
        "sigma": np.array([[1,0],[0,0.2]])# covariance matrix
        },
        ]

    data = np.empty((0,2))
    for cls in classes:
        data0 = generate_data(cls)
        data = np.concatenate((data,generate_data(cls)),axis=0)
        plt.plot(data0[:,0],data0[:,1],"o")
    plt.show()
    Sigma = np.cov(data) #covariance of all data without labeling by class
        #[[a,b]
        # [c,d]]
        # a large: appear a lot / different by a lot in this features
        # d small: does not appear a lot/ does not different a lot in this feature. maybe we can drop it??
        # if a,d similar: not helpful to distinguish
        # off diganoal matrix: same, correlation between the freq of two terms in a document
        # if high: two terms/feature have the same information
        # can we compress the dimension if correlation is high\

    print(Sigma)
    plt.title("original")
    plt.plot(data[:,0],data[:,1],"o")
    plt.show()

    plt.title("original but reducd")
    plt.plot(data[:,0],np.zeros(len(data[:,1])),"o")
    plt.show()

    # perform rotation: 
    u,s,vh = np.linalg.svd(Sigma) #singular decomposition, diagnoalize matrix, u diagoanal(s) vh. 
    # u, vh how to rotate
    # column vec of U the new dim
    # s the covariance of each new dim
    print(u,s,vh)
    
    plt.title("PCA: after transformation")
    rotated = data @ u
    plt.plot(rotated[:,0],rotated[:,1],"o")
    plt.show()

    plt.title("PCA: after transformation and reduced")
    rotated = data @ u #search this: rotate with the rotation matrix
    plt.plot(rotated[:,0],np.zeros(len(rotated[:,1])),"o")
    plt.show()
    # cleaner dividing line

    
    

    # return None



if __name__ == "__main__":
    main()
