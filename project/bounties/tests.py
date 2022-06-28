from pydoc import describe
from django.test import Client, TestCase
from .models import Bounty
from django.contrib.auth.models import User

class BountyDeleteViewTestCase(TestCase):

    def setUp(self):
        User.objects.create(username="franco")
        user = User.objects.get(username="franco")
        Bounty.objects.create(title="Test bounty", reward=300, description="something", creator=user)
    
    def test_bounty_delete_view(self):
        u = User.objects.get(username="franco")
        c = Client()
        c.force_login(u)
        bounty = Bounty.objects.get(title="Test bounty")
        r = c.post(f"/bounty/delete/{bounty.id}", {"pk": bounty.id})
        bounty = Bounty.objects.get(title="Test bounty")
        self.assertEquals(bounty.status, Bounty.DELETED)
