import pandas as pd
from django.core.management.base import BaseCommand
from contracts.models import Contract

class Command(BaseCommand):
    help = 'Imports contracts from an Excel file'

    def handle(self, *args, **kwargs):
        df = pd.read_excel('contracts_data.xlsx')
        for _, row in df.iterrows():
            Contract.objects.create(
                title=row['Title'],
                start_date=row['Start Date'],
                end_date=row['End Date'],
                amount=row['Amount']
            )
        self.stdout.write(self.style.SUCCESS('Contracts imported successfully'))