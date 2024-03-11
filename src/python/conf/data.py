class Data:
    """
        Data class to store the input data for the problem
    """
    def __init__(self, vehicle, visits, distance_matrix, time_matrix):
        self.vehicle = vehicle
        self.visits = visits
        self.distance_matrix = distance_matrix
        self.time_matrix = time_matrix


"""
    Loading the data from the selected folder
    :param folder_path: path to the folder
    :return: Data object
"""
def load_data(folder_path):
    vehicle = read_ini_to_object(folder_path + '/vehicle.ini')
    visits = read_csv_to_objects(folder_path + '/visits.csv')
    distance_matrix = load_matrix(folder_path + '/distance.txt')
    time_matrix = load_matrix(folder_path + '/time.txt')
    return Data(vehicle, visits, distance_matrix, time_matrix)