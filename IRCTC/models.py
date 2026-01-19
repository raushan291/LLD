from typing import List
from enums import SeatType, CompartmentType

class Seat:
    def __init__(self, seat_id: int, seat_type: SeatType):
        self.seat_id = seat_id
        self.seat_type = seat_type
        self.is_available = True

class Coach:
    def __init__(self, coach_name: str, compartment_type: CompartmentType):
        self.coach_name = coach_name
        self.compartment_type = compartment_type
        self.seats: List[Seat] = []

class Compartment:
    def __init__(self, cid: int, ctype: CompartmentType):
        self.compartment_id = cid
        self.compartment_type = ctype
        self.coaches: List[Coach] = []


class Train:
    def __init__(self, number: int, tid: str, name: str, departure_time: str, stops: List[str] = []):
        self.train_number = number
        self.train_id = tid
        self.train_name = name
        self.departure_time = departure_time
        self.stops = stops
        self.compartments: List[Compartment] = []

class TrainJourney:
    def __init__(self, train: Train, date: str):
        self.train = train
        self.date = date
    
class Booking:
    def __init__(self, booking_id, train_id, train_name, train_number, users, src, dest, date, seat_allocations, compartment_type, departure_time):

        self.booking_id = booking_id
        self.train_id = train_id
        self.train_name = train_name
        self.train_number = train_number
        self.users = users
        self.src_station = src
        self.dest_station = dest
        self.date = date
        self.seat_allocations = seat_allocations
        self.compartment_type = compartment_type
        self.departure_time = departure_time
