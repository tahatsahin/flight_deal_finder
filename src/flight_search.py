import os
import requests
import datetime
from flight_data import FlightData

SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
FLY_FROM = "IST"
TODAY = datetime.datetime.now()
SIX_MONTHS_LATER = datetime.datetime.now() + datetime.timedelta(weeks=+8)
RETURN_MIN = datetime.datetime.now() + datetime.timedelta(days=+3)
RETURN_MAX = datetime.datetime.now() + datetime.timedelta(days=+6)

HEADER = {
    "apikey": os.environ.get("KIWI_API_KEY"),
}

SEARCH_PARAMS = {
    "fly_from": FLY_FROM,
    "fly_to": "",
    "dateFrom": "",
    "dateTo": "",
    "nights_in_dst_from": 3,
    "nights_in_dst_to": 6,
    "curr": "USD",
    "price_to": None,
    "sort": "price",
    "limit": 1,
}


class FlightSearch:
    """ FlightSearch finds if there is a cheaper flight than defined price with using Kiwi - Tequila API. """
    def __init__(self, destination, max_price):
        SEARCH_PARAMS["fly_to"] = destination
        SEARCH_PARAMS["dateFrom"] = TODAY.strftime("%d/%m/%Y")
        SEARCH_PARAMS["dateTo"] = SIX_MONTHS_LATER.strftime("%d/%m/%Y")
        SEARCH_PARAMS["price_to"] = max_price

        search_response = requests.get(SEARCH_ENDPOINT, params=SEARCH_PARAMS, headers=HEADER)
        self.data = search_response.json()["data"]
        self.get_data()

    def get_data(self):
        if self.data:
            parsed_data = []
            for item in self.data:
                parsed_data.append(FlightData(item).get_flight_data())
            return parsed_data
