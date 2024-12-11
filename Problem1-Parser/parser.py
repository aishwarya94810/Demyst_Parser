import csv
import json
import os

def read_input_file(SPEC):
    """ Reads the input specification JSON file. 
    Parameters: SPEC (str): Path to the specification JSON file. 
    Returns: tuple: A tuple containing the file contents, column names, offsets, fixed width encoding, header inclusion flag, and delimited encoding. 
    """
    with open(SPEC,"r") as input_file:
        file_contents = json.load(input_file)
    print("file_contents:",file_contents)
    print("file_contents:",type(file_contents))
    column_names = file_contents["ColumnNames"]
    print("column_names:",column_names)
    offsets = [int(offset) for offset in file_contents["Offsets"]] 
    fixed_width_encoding = file_contents["FixedWidthEncoding"] 
    include_header = file_contents["IncludeHeader"] == "True" 
    delimited_encoding = file_contents["DelimitedEncoding"] 
    return file_contents,column_names, offsets, fixed_width_encoding,include_header, delimited_encoding

def generate_fixed_width_file(data, filename, column_names, offsets, encoding, include_header):
    """ Generates a fixed width file based on the provided specification. 

    Parameters: 
    data (dict): The data to be written into the fixed width file. 
    filename (str): The name of the fixed width file. 
    column_names (list): List of column names. 
    offsets (list): List of field lengths (offsets). 
    encoding (str): Encoding for the fixed width file. 
    include_header (bool): Flag to include the header in the fixed width file. 

    Returns: str: The filename of the generated fixed width file. """
    print("\ndata:",data)
    try:
        if not os.path.exists(filename):
            with open(filename, "a", encoding=encoding) as f:
                if include_header:
                    header = ''.join(name.ljust(width) for name, width in zip(column_names, offsets))
                    print("\nheader:",header)
                    f.write(header + "\n")
            print(f"Fixed width file '{filename}' generated successfully.")
        else:
            print(f"Fixed width file '{filename}' already exists.")
        return filename
    except FileNotFoundError:
        print("File not found")
    except UnicodeDecodeError:
        print("Encoding error")

def read_fixed_width_file(json_file, offsets, encoding):
    """ Reads the fixed width file and parses it. 
    
    Parameters: 
    json_file (str): The name of the fixed width file. 
    offsets (list):List of field lengths (offsets). 
    encoding (str): Encoding of the fixed width file. 

    Returns: list: Parsed data from the fixed width file. 
    """
    print("\njson_file:",json_file)
    try:
        with open(json_file, "r", encoding=encoding) as f:
            lines = f.readlines()
        print("lines:",lines)
        parsed_data = []
        for line in lines:
            start = 0
            row = []
            for width in offsets:
                field = line[start:start + width].strip()
                row.append(field)
                start += width
            parsed_data.append(row)
        print("parsed_data:",parsed_data)
        return parsed_data
    except FileNotFoundError:
        print("File not found")
    except UnicodeDecodeError:
        print("Encoding error")

def write_csv_file(data, output_file, encoding):
    """ Writes the parsed data to a CSV file. 
    Parameters: 
    data (list): The data to be written into the CSV file. 
    output_file (str): The name of the CSV file. 
    encoding (str): Encoding for the CSV file. 
    
    Returns: None """
    try:
        with open(output_file, "w", newline="", encoding=encoding) as f:
            writer = csv.writer(f)
            writer.writerows(data)
        print(f"CSV file '{output_file}' generated successfully.")
    except FileNotFoundError:
        print("File not found")
    except UnicodeDecodeError:
        print("Encoding error")

SPEC = "~spec.json"
filename = "~fixed_width.txt"
output_file = "~output.csv"

# Load specification
file_contents,column_names, offsets, fixed_width_encoding, include_header, delimited_encoding = read_input_file(SPEC)
json_file = generate_fixed_width_file(file_contents,filename, column_names, offsets, fixed_width_encoding, include_header)

# Parse fixed width file and write to CSV
parsed_data = read_fixed_width_file(json_file, offsets, fixed_width_encoding)
write_csv_file(parsed_data, output_file, delimited_encoding)

