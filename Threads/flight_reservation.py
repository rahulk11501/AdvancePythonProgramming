from threading import *


class FlightReservation:
    lock = Lock()
    # lock = Semaphore()

    def __init__(self, ticket_left):
        self.ticket_left = ticket_left

    lock.acquire()

    def buy(self, ticket_requested):
        if self.ticket_left > ticket_requested:
            print("Your ticket is confirmed")
            print("Please make your payment and choose your seats")
            self.ticket_left -= ticket_requested
        else:
            print("There is not enough tickets remaining")

    lock.release()


ticket = FlightReservation(10)
t1 = Thread(target=ticket.buy, args=[3])
t2 = Thread(target=ticket.buy, args=[4])
t3 = Thread(target=ticket.buy(5))

t1.start()
t2.start()
t3.start()
