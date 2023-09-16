from datetime import datetime, timedelta

from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        four_years_ago = datetime.today().date() - timedelta(days=4 * 365)  # Approximating 3 years as 365 days each
        return self.last_service_date < four_years_ago
