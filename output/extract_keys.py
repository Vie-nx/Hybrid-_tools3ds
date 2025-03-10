import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_keys_from_file(file_path):
    """
    Reads an AES keys file in text format and returns a dictionary.
    """
    keys = {}
    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    if "=" in line:
                        key_name, key_value = line.split("=", 1)
                        keys[key_name] = key_value
    except FileNotFoundError:
        logging.error(f"File not found {file_path}.")
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")
    return keys

def combine_keys(keys1, keys2):
    """
    Combines two dictionaries of keys, giving priority to the keys in the first dictionary.
    """
    combined_keys = keys1.copy()
    combined_keys.update({k: v for k, v in keys2.items() if k not in combined_keys or combined_keys[k] == "None"})
    return combined_keys

def write_sorted_keys(file_path, keys):
    """
    Writes the keys to a text file, sorted by key name.
    """
    try:
        with open(file_path, "w") as file:
            sections = {
                "# KeyX\n": "KeyX",
                "\n# KeyY\n": "KeyY",
                "\n# KeyN\n": "KeyN",
                "\n# Common Keys\n": "common",
            }
            for section, keyword in sections.items():
                file.write(section)
                section_keys = [k for k in keys if keyword in k.lower() and keys[k] is not None]
                if not section_keys:
                    file.write("# No keys found for this section.\n")
                else:
                    for key in sorted(section_keys):
                        file.write(f"{key}={keys[key]}\n")
        logging.info(f"Sorted keys saved to {file_path}.")
    except IOError:
        logging.error(f"Could not write to file {file_path}.")
    except Exception as e:
        logging.error(f"Error writing to file {file_path}: {e}")

def extract_and_combine_keys(output_path, *key_files):
    """
    Combines keys from multiple files into a single output file.
    """
    try:
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
            logging.info(f"Output directory created: {output_dir}")

        all_keys = {}
        for file_path in key_files:
            if not os.path.exists(file_path):
                logging.error(f"File not found {file_path}.")
                continue
            keys = read_keys_from_file(file_path)
            all_keys = combine_keys(all_keys, keys)

        write_sorted_keys(output_path, all_keys)
        logging.info(f"Combined and sorted keys saved to {output_path}")

    except PermissionError:
        logging.error(f"Permission denied when accessing file or directory.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
def clean_key_file(input_path, output_path):
    """
    Cleans a key file by removing extra spaces, fixing line endings, and ensuring proper formatting.
    """
    with open(input_path, "r") as input_file:
        lines = input_file.readlines()

    cleaned_lines = []
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if line and not line.startswith("#"):  # Skip empty lines and comments
            cleaned_lines.append(line + "\n")  # Add clean line with LF ending

    with open(output_path, "w", newline="\n") as output_file:
        output_file.writelines(cleaned_lines)

# Paths
input_file = r"Z:\ye_Alon\roms\nintendo\3ds\extractor and create aes\aeskeys\aes_keys_amigo.txt"
output_file = r"Z:\ye_Alon\roms\nintendo\3ds\extractor and create aes\aeskeys\aes_keys_cleaned.txt"

# Clean the file
clean_key_file(input_file, output_file)
print(f"Cleaned file saved to {output_file}")

# Paths of input and output files
key_files = [
    r"Z:\ye_Alon\roms\nintendo\3ds\extractor and create aes\aeskeys\aes_keys.txt",
    r"Z:\ye_Alon\roms\nintendo\3ds\extractor and create aes\aeskeys\aes_keys_amigo.txt",
    r"Z:\ye_Alon\roms\nintendo\3ds\extractor and create aes\aeskeys\aes_keys_mias.txt",
    r"Z:\ye_Alon\roms\nintendo\3ds\extractor and create aes\aeskeys\keys_aes.txt",
]
output_path = r"Z:\ye_Alon\roms\nintendo\3ds\extractor and create aes\output\aes_keys_combinado.txt"

# Extract, combine, and sort the keys
extract_and_combine_keys(output_path, *key_files)