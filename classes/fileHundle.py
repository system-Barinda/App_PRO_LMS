# import json
# test_data = {
#     "status": "ok",
#     "message": "Hello, JSON file!",
#     "test_passed": True,
# }
# with open("test_output.json", "w", encoding="utf-8") as file:
#   json.dump(test_data, file, indent=4)

# print("JSON file created successfully.")



# import json

# file_path = "test_output.json"

# # 1. Write test data
# payload = {"statement": "Testing JSON write and read", "count": 1}
# with open(file_path, "w", encoding="utf-8") as f:
#   json.dump(payload, f, indent=2)

# # 2. Read back and verify
# with open(file_path, "r", encoding="utf-8") as f:
#   loaded_data = json.load(f)

# assert loaded_data == payload, "Mismatch between written and read data!"
# print("Test passed! Loaded content:", loaded_data)


import numpy as np

# Element-wise math without a loop
prices = np.array([10.0, 25.5, 40.0])
discounted = prices * 0.9

print("Discounted:", discounted)  # [ 9.0, 22.95, 36.0 ]
print("Mean price:", np.mean(prices))  # 25.166666666666668

# 2D matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Matrix product:\n", A @ B)