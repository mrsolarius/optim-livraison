import csv


class Visit:

    def __init__(self, visit_id, visit_name, visit_lat, visit_lon, demand):
        self.visit_id = visit_id
        self.visit_name = visit_name
        self.visit_lat = visit_lat
        self.visit_lon = visit_lon
        self.demand = demand


"""
    Reading csv file
    :param file_path: path to the file
    :return: list of objects with the header as attributes
"""


def read_csv_to_objects(file_path):
    visites = []
    with open(file_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            visites.append(
                Visit(
                    row["visit_id"],
                    row["visit_name"],
                    row["visit_lat"],
                    row["visit_lon"],
                    row["demand"]
                )
            )
    return visites
