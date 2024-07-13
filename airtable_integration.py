from pyairtable import Table
import os

AIRTABLE_API_KEY = os.getenv('AIRTABLE_API_KEY')
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID')

class AirtableIntegration:
    def __init__(self, table_name):
        self.table = Table(AIRTABLE_API_KEY, AIRTABLE_BASE_ID, table_name)

    def add_record(self, data):
        self.table.create(data)

    def get_all_records(self):
        return self.table.all()