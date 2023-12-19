import numpy as np
import time
import matplotlib.pyplot as plt

def block_multiply(A, B, block_size):
    m, n = A.shape
    n, p = B.shape
    C = np.zeros((m, p))
    for i in range(0, m, block_size):
        for j in range(0, p, block_size):
            for k in range(0, n, block_size):
                # Compute block C[i:i+block_size, j:j+block_size] 
                # as a product of blocks of A and B
                C_block = np.dot(A[i:i+block_size, k:k+block_size], 
                                 B[k:k+block_size, j:j+block_size])
                # Add block C_block to the corresponding block of C
                C[i:i+block_size, j:j+block_size] += C_block
    return C

# Define matrix sizes and block sizes to test

matrix_sizes = [50, 100, ]
block_sizes = [5, 10, ]

# Measure time taken for each combination of matrix size and block size

for n in matrix_sizes:
    for p in matrix_sizes:
            # Initialize lists for storing times and block sizes
        times = []
        block_sizes_list = []

        for block_size in block_sizes:
                # Generate random matrices A and B
            A = np.random.rand(n, n)
            B = np.random.rand(n, p)

                # Measure time taken for matrix multiplication using blocking
            start_time = time.time()
            C = block_multiply(A, B, block_size)
            end_time = time.time()

                # Append time taken and block size to the lists
            times.append(end_time - start_time)
            block_sizes_list.append(block_size)

            # Plot the results for this matrix size
            plt.plot(block_sizes_list, times, label=f"Matrix size ( {n}, {p})")

# Set the x-axis and y-axis labels and title
plt.xlabel("Blocking size")
plt.ylabel("Time taken (seconds)")
plt.title("Relationship between blocking size and time taken")

# Display the legend and show the plot
plt.legend()
plt.show()




