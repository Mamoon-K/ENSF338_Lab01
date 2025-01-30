import json

# Generated by ChatGPT, modified to fit specifications by Ayden
def update_size(data, new_value):
    """
    Recursively updates all occurrences of the 'size' key in a JSON-like structure.
    """
    if isinstance(data, dict):  # If data is a dictionary, check keys
        return {k: (update_size(v, new_value) if k != 'size' else new_value) for k, v in data.items()}
    elif isinstance(data, list):  # If data is a list, check each element
        return [update_size(item, new_value) for item in data]
    else:
        return data  # If not a dict or list, return as is

# Load the JSON file
with open('large-file.json', 'r', encoding='utf8') as file:
    data = json.load(file)

# Update all occurrences of 'size'
updated_data = update_size(data, 42)

# Reverse the list
updated_data = updated_data[::-1]

# Save the modified JSON to a new file
with open('output.2.3.json', 'w') as file:
    json.dump(updated_data, file, indent=4)