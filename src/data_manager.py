import requests

SHEETY_URL = "https://api.sheety.co/ce222fcd01faec4e0a2ee371f4550e50/flightDeals/prices"


class DataManager:
    """ DataManager gets the data from Google Sheets with using Sheety API. """
    def __init__(self):
        self.destination_data = {}
        sheety_response = requests.get(SHEETY_URL)
        response_list = sheety_response.json()["prices"]
        self.cities_and_prices = {}
        for item in response_list:
            self.cities_and_prices[f'{item["iataCode"]}'] = item["lowestPrice"]

    def get_cities_and_prices(self):
        return self.cities_and_prices
