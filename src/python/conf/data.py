class Data:
    """
        Data class to store the input data for the problem
    """
    def __init__(self, vehicle, visits, distance_matrix, time_matrix):
        self.vehicle = vehicle
        self.visits = visits
        self.distance_matrix = distance_matrix
        self.time_matrix = time_matrix