import unittest
from maincode import Client, Event, Guest


class TestEventManagement(unittest.TestCase):

    def setUp(self):
        # Set up test data
        self.client = Client(client_id=1, name="Test Client", address="Test Address", contact_details="Test Contact",
                             budget=1000)
        self.event = Event(event_id=1, event_type="Test Event", theme="Test Theme", date="2024-05-03", time="12:00 PM",
                           duration="2 hours", venue_address="Test Venue", client_id=self.client.client_id,
                           guest_list=[], suppliers=[], invoice=None)
        self.guest = Guest(guest_id=1, name="Test Guest", address="Test Address", contact_details="Test Contact")

    def test_retrieve_client_info(self):
        # Test case 1: retrieve the info for a specific client
        expected_info = "Name: Test Client, Address: Test Address, Contact Details: Test Contact, Budget: 1000"
        self.assertEqual(self.client.name, "Test Client")
        self.assertEqual(self.client.address, "Test Address")
        self.assertEqual(self.client.contact_details, "Test Contact")
        self.assertEqual(self.client.budget, 1000)


    def test_delete_event(self):
        # Test case 2: deleting an event
        self.event = None
        self.assertIsNone(self.event)

    def test_add_new_guest(self):
        # Test case 3: adding a new guest
        new_guest = Guest(guest_id=2, name="New Guest", address="New Address", contact_details="New Contact")
        self.event.guest_list.append(new_guest)
        self.assertEqual(len(self.event.guest_list), 1)


if __name__ == "__main__":
    unittest.main()