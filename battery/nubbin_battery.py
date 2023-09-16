from datetime import datetime, timedelta

from battery.battery import Battery


class NubbinBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        two_years_ago = datetime.today().date() - timedelta(days=2 * 365)  # Approximating 3 years as 365 days each
        return self.last_service_date < two_years_ago
