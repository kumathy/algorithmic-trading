from datetime import date

from django.core.management.base import BaseCommand
from trading.services.massive_client import MassiveAPIClient


class Command(BaseCommand):
    def handle(self, *args, **options):
        client = MassiveAPIClient()
        result = client.fetch_bulk_momentum_data(["AAPL", "NVDA"], date(2026, 5, 12))
        print(result)
