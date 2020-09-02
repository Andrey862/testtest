from core.models import Counter
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        x = Counter.objects.filter(pk=1)
        if len(x)>0:
            x[0].value = 0
            x[0].save()
            print("resetting counter")
        else:
            Counter.objects.create(value=0)
            print("creating counter")
            
