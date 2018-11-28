from django.test import TestCase
from .models import Ticket, Event

# Create your tests here.


class TestEvent(TestCase):

    @classmethod
    def setUpTestData(cls):
        Event.objects.create(name='Test Event', venue='Lviv', description='abcdefg')

    def test_name_max_length(self):
        event = Event.objects.get(id=1)
        max_length = event._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_srt_name(self):
        event = Event.objects.get(id=1)
        expected_object_name = str(event.name)
        self.assertEquals(expected_object_name, str(event))


class TestTicket(TestCase):

    @classmethod
    def setUpTestData(cls):
        Ticket.objects.create(event=Event.objects.create(name='Test Event', venue='Lviv', description='abcdefg'), seat=4)

    def test_event(self):
        """Test event assigned to ticket"""
        ticketevent = Event.objects.get(ticket__event=Event.objects.get(id=1))
        event = Event.objects.get(id=1)
        self.assertEquals(str(ticketevent), str(event))

    def test_object_name_is_srt_name(self):
        ticket = Ticket.objects.get(event=Event.objects.get(id=1))
        expected_object_name = "%s - %s" % (ticket.seat, ticket.event)
        self.assertEquals(expected_object_name, str(ticket))


class TestURL(TestCase):

    def test_home(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)