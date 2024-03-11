import configparser

class Vehicle:
    def __init__(self, max_dist, capacity, charge_fast, charge_medium, charge_slow, start_time, end_time):
        self.max_dist = max_dist
        self.capacity = capacity
        self.charge_fast = charge_fast
        self.charge_medium = charge_medium
        self.charge_slow = charge_slow
        self.start_time = start_time
        self.end_time = end_time


"""
    Reading from ini file using configparser
    :param file_path: path to the file
    :return: Vehicle object
"""
def read_ini_to_object(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return Vehicle(
        config['vehicle']['max_dist'],
        config['vehicle']['capacity'],
        config['vehicle']['charge_fast'],
        config['vehicle']['charge_medium'],
        config['vehicle']['charge_slow'],
        config['vehicle']['start_time'],
        config['vehicle']['end_time']
    )