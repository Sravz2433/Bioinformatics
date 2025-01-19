import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.svm import SVC  # For comparison
import cvxopt

# Step 1: Create a non-linearly separable dataset (two moons dataset)
X, Y = make_moons(n_samples=100, noise=0.15, random_state=42)
Y = np.where(Y == 0, -1, 1)  # Change labels to -1 and 1

# Step 2: Define the Gaussian (RBF) Kernel function
def gaussian_kernel(x1, x2, sigma=0.5):
    return np.exp(-np.linalg.norm(x1 - x2)**2 / (2 * sigma**2))

# Step 3: Construct the Kernel Matrix (Gram matrix)
def kernel_matrix(X, sigma=0.5):
    n_samples = X.shape[0]
    K = np.zeros((n_samples, n_samples))
    for i in range(n_samples):
        for j in range(n_samples):
            K[i, j] = gaussian_kernel(X[i], X[j], sigma)
    return K

# Step 4: SVM Dual Optimization with Gaussian Kernel using cvxopt
def svm_gaussian_kernel(X, Y, C=1, sigma=0.5):
    n_samples, n_features = X.shape
    K = kernel_matrix(X, sigma)

    P = cvxopt.matrix(np.outer(Y, Y) * K)
    q = cvxopt.matrix(-np.ones(n_samples))
    G_std = cvxopt.matrix(np.diag(-np.ones(n_samples)))
    h_std = cvxopt.matrix(np.zeros(n_samples))
    G_slack = cvxopt.matrix(np.vstack((np.diag(-np.ones(n_samples)), np.identity(n_samples))))
    h_slack = cvxopt.matrix(np.hstack((np.zeros(n_samples), np.ones(n_samples) * C)))
    A = cvxopt.matrix(Y, (1, n_samples), 'd')
    b = cvxopt.matrix(0.0)

    solution = cvxopt.solvers.qp(P, q, G_slack, h_slack, A, b)
    alphas = np.ravel(solution['x'])
    
    # Extract support vectors
    support_vector_indices = np.where(alphas > 1e-5)[0]
    support_vectors = X[support_vector_indices]
    alphas_sv = alphas[support_vector_indices]
    Y_sv = Y[support_vector_indices]

    # Bias term
    b = np.mean([Y_sv[i] - np.sum(alphas_sv * Y_sv * K[support_vector_indices[i], support_vector_indices])
                 for i in range(len(support_vector_indices))])
    
    return alphas, b, support_vectors, support_vector_indices

# Step 5: Decision Function for Gaussian Kernel SVM
def decision_function(X, support_vectors, alphas_sv, Y_sv, b, sigma=0.5):
    def kernel_decision(x):
        return np.sum(alphas_sv * Y_sv * np.array([gaussian_kernel(x, sv, sigma) for sv in support_vectors])) + b
    return np.array([kernel_decision(x) for x in X])

# Step 6: Train the custom Gaussian Kernel SVM
alphas, b, support_vectors, support_vector_indices = svm_gaussian_kernel(X, Y, C=1, sigma=0.5)

# Step 7: Compare with scikit-learn's SVM using RBF Kernel
clf = SVC(kernel='rbf', gamma='scale', C=1)
clf.fit(X, Y)

# Step 8: Visualization of decision boundaries
def plot_decision_boundary(X, Y, clf, ax, title):
    xx, yy = np.meshgrid(np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 100),
                         np.linspace(X[:, 1].min() - 1, X[:, 1].max() + 1, 100))
    Z = clf(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.bwr)
    ax.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.bwr, edgecolors='k')
    ax.set_title(title)

# Step 9: Plot both decision boundaries side by side
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Custom Gaussian Kernel SVM decision boundary
plot_decision_boundary(X, Y, lambda x: decision_function(x, support_vectors, alphas[support_vector_indices], Y[support_vector_indices], b, sigma=0.5),
                       axes[0], 'Custom Gaussian Kernel SVM')

# scikit-learn's RBF SVM decision boundary
plot_decision_boundary(X, Y, lambda x: clf.decision_function(x), axes[1], 'scikit-learn RBF Kernel SVM')

plt.tight_layout()
plt.show()
