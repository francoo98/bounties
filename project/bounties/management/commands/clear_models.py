from django.core.management.base import BaseCommand
from bounties.models import Bounty, Solution


class Command(BaseCommand):
    def handle(self, *args, **options):
        Bounty.objects.all().delete()
        Solution.objects.all().delete()
