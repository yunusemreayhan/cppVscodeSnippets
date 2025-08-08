import os
import json

def combine_json_files(source_dir, output_file):
    combined_data = {}
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    print(f"Reading and combining: {file_path}")
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        # Assuming each JSON file contains a dictionary
                        # and we want to merge them. If there are key collisions,
                        # the last one read will overwrite previous ones.
                        combined_data.update(data)
                except json.JSONDecodeError:
                    print(f"Warning: Could not decode JSON from {file_path}. Skipping.")
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, indent=4)
    print(f"Successfully combined JSON files into {output_file}")

if __name__ == "__main__":
    vscode_dir = ".vscode"
    output_json_file = os.path.join(vscode_dir, "cpp.json")
    combine_json_files(vscode_dir, output_json_file)
