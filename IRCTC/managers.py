from models import Train, TrainJourney, Booking

class TrainManager:
    def __init__(self):
        self.trains = {}

    def create_train(self, train: Train):
        self.trains[train.train_id] = train

class TrainJourneyManager:
    def __init__(self):
        self.journeys = {}

    def create_journey(self, jid, journey: TrainJourney):
        self.journeys[jid] = journey

class BookingManager:
    def __init__(self):
        self.bookings = {}

    def create_booking(self, booking: Booking):
        self.bookings[booking.booking_id] = booking
