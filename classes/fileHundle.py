import json

test_data = {
    "status": "ok",
    "message": "Hello, JSON file!",
    "test_passed": True,
}

with open("test_output.json", "w", encoding="utf-8") as file:
  json.dump(test_data, file, indent=4)

print("JSON file created successfully.")