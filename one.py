from cgi import print_arguments
from config import drivers_config
import json
import yaml
import configparser


def Python_Configuration_Files():
    '''create config.py & store required vals in dict import it & use dic key to accesss required val'''
    print(drivers_config)

    print(drivers_config['URL'])
    print(drivers_config['FileName'])


# Python_Configuration_Files()

def JSON_method():

    # reading config file

    with open('config.json') as file:
        data = json.load(file)
        print(data['drivers_config']['URL'])


# JSON_method()


def YML_data():

    with open('config.yml', 'r') as file:
        prime_service = yaml.safe_load(file)
        print(prime_service, type(prime_service))
        print(prime_service['URL'])
        print(prime_service['rest']['url'])


# YML_data()


def INI():
    file = open("config.ini", "r")

    config = configparser.RawConfigParser(allow_no_value=True)
    config.read_file(file)

    print(config.get("drivers_config", "URL"))


# INI()
