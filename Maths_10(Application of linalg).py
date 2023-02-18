import numpy as np

# Define the message to be encoded as a column vector
message = np.array([[1], [2], [3]])

# Define the encoding matrix (must be non-singular)
encoding_matrix = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])

# Encode the message by multiplying it with the encoding matrix
encoded_message = np.dot(encoding_matrix, message)

# Calculate the inverse of the encoding matrix
inv_encoding_matrix = np.linalg.inv(encoding_matrix)

# Decode the message by multiplying the encoded message with the inverse of the encoding matrix
decoded_message = np.dot(inv_encoding_matrix, encoded_message)

# Print the encoded message
print("Encoded message: \n")
print(encoded_message)

# Print the decoded message
print("\n Decoded message: \n")
print(decoded_message)