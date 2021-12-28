class FlightData:
    """ This class creates a structure for the flight information. """
    def __init__(self, flight):
        self.flight = flight
        self.data = {}
        self.price = self.flight["price"]
        self.from_city = self.flight["routes"][0][0]
        self.to_city = self.flight["routes"][0][1]
        self.from_date = self.flight["route"][0]["local_departure"].split("T")[0]
        self.to_date = self.flight["route"][1]["local_departure"].split("T")[0]
        self.get_flight_data()

    def get_flight_data(self):
        self.data = {
            "from_city": self.from_city,
            "to_city": self.to_city,
            "from_date": self.from_date,
            "to_date": self.to_date,
            "price": self.price,
        }
        return self.data
