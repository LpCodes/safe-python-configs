import json
import yaml
import configparser
import os
from dotenv import load_dotenv
from config import drivers_config  # Assuming drivers_config is defined in config.py


def python_configuration_files():
    """
    Create config.py and store required values in a dictionary. Import it and use dictionary keys to access required values.
    """
    print(drivers_config)
    print(drivers_config.get('URL'))  # Using .get() to avoid KeyError if 'URL' is not present
    print(drivers_config.get('FileName'))


# Uncomment the following line to use the function
# python_configuration_files()


def json_method():
    """
    Read values from a JSON config file.
    """
    with open('config.json') as file:
        data = json.load(file)
        print(data.get('drivers_config', {}).get('URL'))  # Using .get() to handle missing keys


# Uncomment the following line to use the function
# json_method()


def yml_data():
    """
    Read values from a YAML config file.
    """
    with open('config.yml', 'r') as file:
        prime_service = yaml.safe_load(file)
        print(prime_service, type(prime_service))
        print(prime_service.get('URL'))
        print(prime_service.get('rest', {}).get('url'))  # Using .get() to handle missing keys


# Uncomment the following line to use the function
# yml_data()


def ini():
    """
    Read values from an INI config file.
    """
    file = open("config.ini", "r")

    config = configparser.RawConfigParser(allow_no_value=True)
    config.read_file(file)

    print(config.get("drivers_config", "URL"))


# Uncomment the following line to use the function
# ini()


def env_method():
    """
    Load environment variables from a .env file.
    """
    load_dotenv()
    # Use os.environ.get() with a default value to avoid KeyError
    my_name = os.environ.get("myname", "DefaultName")
    password = os.environ.get("password", "DefaultPassword")
    logs_path = os.environ.get("LOGS_PATH", "DefaultLogsPath")

    print(my_name)
    print(password)
    print(logs_path)


# Uncomment the following line to use the function
# env_method()
