import csv
import datetime
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.DictReader(csvfile, delimiter=';')
            for phone in phone_reader:
                release_date = datetime.datetime.strptime(phone['release_date'],
                                                        '%Y-%m-%d')
                if phone['lte_exists'] == 'True':
                    lte_exists = True
                else:
                    lte_exists = False

                db_phone = Phone(id=int(phone['id']),
                                 name=phone['name'],
                                 image=phone['image'],
                                 price=int(phone['price']),
                                 release_date=release_date,
                                 lte_exists=lte_exists)
                db_phone.save()
