import smtplib
import os


class NotificationManager:
    """ Notification Manager Class sends email with the found data with using SMTPLIB. """
    def __init__(self, cheap_flights, send_to):
        self.my_email = os.environ.get("MY_EMAIL")
        self.my_password = os.environ.get("MY_PASSWORD")
        self.cheap_flights = cheap_flights
        self.message = ""
        self.to_address = send_to
        self.create_message()
        self.send_mail(to_address=self.to_address, message=self.message)

    def create_message(self):
        for item in self.cheap_flights:
            if item:
                self.message += f"Cheap Flights Found! Low Price Alert! Only ${item[0]['price']}" \
                           f" to fly from {item[0]['from_city']} to {item[0]['to_city']}," \
                           f" from {item[0]['from_date']} to {item[0]['to_date']}.\n\n"

    def send_mail(self, to_address, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=to_address,
                msg=self.message
            )



