

import json

def txt_to_json(input_filename, output_filename):
    '''takes txt file and turns it into a specific json dict to do parsing on'''
    try:
        # Read text from the input file
        with open(input_filename, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        return
    except PermissionError:
        print(f"Error: Permission denied for file '{input_filename}'.")
        return


    # dictionary with a key "speech" and the value being a list of lines
    json_dict = {
        "speech": text.replace('\n', ' ').strip()
    }


    try:
        # Write the JSON data to the output file
        with open(output_filename, 'w') as json_file:
            json.dump(json_dict, json_file, indent=2)
    except PermissionError:
        print(f"Error: Permission denied to write to '{output_filename}'.")
        return

