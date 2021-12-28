from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Instantiating DataManager class to get the data from Google sheets
destination_data = DataManager()
# Saving the destination and prices from Google Sheets
cities_and_prices = destination_data.get_cities_and_prices()

cheap_flights = []
for key, value in cities_and_prices.items():
    """ Finding if there is a better deal than defined and saving it to a list. """
    cheap_flights.append(FlightSearch(destination=key, max_price=value).get_data())

send_to = "tahatsahin@gmail.com"
send_email = NotificationManager(cheap_flights, send_to)
