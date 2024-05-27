import json
from typing import List

from loguru import logger


def list_to_string(string_list: List[str], delimiter: str = ", ") -> str:
    """
    Converts a list of strings to a single string with a specified delimiter.

    Args:
        string_list (List[str]): The list of strings to convert.
        delimiter (str): The delimiter to use for separating the strings. Default is ', '.

    Returns:
        str: The resulting string.
    """
    return delimiter.join(string_list)


def read_json_and_extract_keys(file_path: str, key1: str, key2: str) -> dict:
    """
    Reads a JSON file and extracts the values of two specified keys.

    Args:
        file_path (str): The path to the JSON file.
        key1 (str): The first key to extract.
        key2 (str): The second key to extract.

    Returns:
        Optional[Tuple[Any, Any]]: A tuple containing the values of the specified keys.
                                   If a key is not found, the value will be "Key not found".
                                   Returns None if the file cannot be read.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            logger.info("JSON file read successfully.")

        result = {
            key1: data.get(key1, "Key not found"),
            key2: data.get(key2, "Key not found"),
        }

        return result

    except (FileNotFoundError, json.JSONDecodeError):
        return None
