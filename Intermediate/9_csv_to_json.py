# 9. CSV to JSON Converter

import csv
import json
import os


def csv_to_json(csv_file_path, json_file_path):
    """Reads a CSV file and converts it into a formatted JSON file."""
    data = []

    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"File successfully converted! JSON saved at {json_file_path}")
    except FileNotFoundError:
        print("CSV folder path not found.")
    except Exception as e:
        print(f"Error during conversion: {e}")


def main():
    print("=== CSV to JSON Converter ===")

    # Prompt user for CSV file path
    csv_file_path = input("Enter the path to your CSV file: ")

    # Generate JSON filename by replacing .csv with .json
    if not os.path.exists(csv_file_path):
        print(f"CSV file not found at: {csv_file_path}")
        return

    json_file_path = csv_file_path.rsplit('.', 1)[0] + '.json'

    csv_to_json(csv_file_path, json_file_path)


if __name__ == "__main__":
    main()
