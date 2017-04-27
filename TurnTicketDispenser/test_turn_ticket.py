import unittest
import random
from thread import start_new_thread
from time import sleep
import threading

from turn_ticket import TicketDispenser

class TicketDispenserTest(unittest.TestCase):

    def test_get_one_ticket(self):
        dispenser = TicketDispenser()
        ticket = dispenser.getTurnTicket()
        self.assertIsNotNone(ticket)
        self.assertTrue(ticket.turnNumber>=0)

    def test_should_have_100_different_numbers(self):
        dispenser = TicketDispenser()
        numbers=set()
        for i in xrange(0, 100):
            numbers.add(dispenser.getTurnTicket().turnNumber)

        self.assertEquals(100, len(numbers))

    def test_several_dispensers_should_have_100_different_numbers(self):
        dispenser1 = TicketDispenser()
        dispenser2 = TicketDispenser()
        dispenser3 = TicketDispenser()
        dispensers = [dispenser1, dispenser2, dispenser3]
        numbers=set()
        for i in xrange(0, 100):
            numbers.add(dispensers[i%3].getTurnTicket().turnNumber)
        self.assertEquals(100, len(numbers))

    def test_some_dispensers(self):
        dispensers = [TicketDispenser() for i in xrange(20)]
        numbers = set()
        for i in xrange(100):
            numbers.add(random.choice(dispensers).getTurnTicket().turnNumber)
        self.assertEquals(100, len(numbers))

    def test_multiple_threads(self):
        def single_thread_test(numbers):
            dispenser = TicketDispenser()
            number = dispenser.getTurnTicket().turnNumber
            numbers.add(number)

        numbers=set()
        threads=[]
        runlength=100000
        for i in xrange(runlength):
            t = threading.Thread(target=single_thread_test, args=(numbers,))
            threads.append(t)
            t.start()
        print(len(threads), len(numbers))
        for thread in threads:
            thread.join()
        self.assertEquals(runlength, len(numbers))





