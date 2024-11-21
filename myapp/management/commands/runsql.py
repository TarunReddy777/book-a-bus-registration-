from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Run an SQL script to populate the SQLite database'

    def handle(self, *args, **kwargs):
        # Path to your SQL file
        sql_file_path = 'BusReservationSystem.sql'

        # Read the SQL file
        with open(sql_file_path, 'r') as file:
            sql_script = file.read()

        # Execute the SQL script
        with connection.cursor() as cursor:
            cursor.executescript(sql_script)

        self.stdout.write(self.style.SUCCESS('SQL script executed successfully'))
