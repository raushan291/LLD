from models import Booking

from abc import ABC, abstractmethod

class RequestProcessor(ABC):
    @abstractmethod
    def process_request(self, request):
        pass

class SearchRequestProcessor(RequestProcessor):
    def __init__(self, train_mgr):
        self.train_mgr = train_mgr

    def process_request(self, request):
        print(f"\nSearching trains from {request.src} to {request.dest} on {request.date}...")
        print("\n---- SEARCH RESULTS ----")
        results = []
        for train in self.train_mgr.trains.values():
            if request.src in train.stops and request.dest in train.stops:
                print(f"Train: {train.train_name} | Train ID: {train.train_id} | Number: {train.train_number} | Departure: {train.departure_time} | Stops: {', '.join(train.stops)}")
                results.append(train)
        return results


class BookingRequestProcessor(RequestProcessor):
    def __init__(self, booking_mgr, journey_mgr):
        self.booking_mgr = booking_mgr
        self.journey_mgr = journey_mgr

    def process_request(self, request):
        journey = self.journey_mgr.journeys.get(request.train_id)
        if not journey:
            print("Invalid Train Journey")
            return None

        # find compartment
        compartment = None
        for comp in journey.train.compartments:
            if comp.compartment_type == request.compartment_type:
                compartment = comp
                break

        if not compartment:
            print("Compartment not found")
            return None

        seat_allocations = []

        # allocate seats across coaches
        for passenger in request.users:
            allocated = False
            for coach in compartment.coaches:
                for seat in coach.seats:
                    if seat.is_available:
                        seat.is_available = False

                        seat_allocations.append({
                            "passenger": passenger,
                            "coach": coach.coach_name,
                            "seat_no": seat.seat_id,
                            "seat_type": seat.seat_type.value
                        })

                        allocated = True
                        break

                if allocated:
                    break

            if not allocated:
                print("Not enough seats available, rolling back...")

                # rollback
                for s in seat_allocations:
                    for coach in compartment.coaches:
                        if coach.coach_name == s["coach"]:
                            for seat in coach.seats:
                                if seat.seat_id == s["seat_no"]:
                                    seat.is_available = True

                return None

        booking_id = f"B{len(self.booking_mgr.bookings)+1:03d}"

        booking = Booking(
            booking_id,
            request.train_id,
            journey.train.train_name,
            journey.train.train_number,
            request.users,
            request.src,
            request.dest,
            request.date,
            seat_allocations,
            request.compartment_type.value,
            journey.train.departure_time
        )

        self.booking_mgr.create_booking(booking)

        self._print_booking(booking)

        return booking

    def _print_booking(self, booking):
        print("\n---- BOOKING CONFIRMED ----")
        print(f"Booking ID: {booking.booking_id}")
        print(f"Train: {booking.train_name} | Train ID: {booking.train_id} | Train Number: {booking.train_number}")
        print(f"Departure Time: {booking.departure_time}")
        print(f"From: {booking.src_station} To: {booking.dest_station}")
        print(f"Date: {booking.date}")
        print(f"Compartment: {booking.compartment_type}")

        for s in booking.seat_allocations:
            print(
                f"Passenger: {s['passenger']} | "
                f"Coach: {s['coach']} | "
                f"Seat: {s['seat_no']} | "
                f"Type: {s['seat_type']}"
            )


class CancelRequestProcessor(RequestProcessor):
    def __init__(self, booking_mgr, journey_mgr):
        self.booking_mgr = booking_mgr
        self.journey_mgr = journey_mgr

    def process_request(self, request):
        booking = self.booking_mgr.bookings.get(request.booking_id)
        
        if not booking:
            print("Invalid booking ID")
            return False

        journey = self.journey_mgr.journeys.get(booking.train_id)

        if not journey:
            print("Journey not found")
            return False

        # find compartment
        compartment = None
        for comp in journey.train.compartments:
            if comp.compartment_type.value == booking.compartment_type:
                compartment = comp
                break

        if not compartment:
            print("Compartment not found for cancellation")
            return False

        # release seats
        for s in booking.seat_allocations:
            for coach in compartment.coaches:
                if coach.coach_name == s["coach"]:
                    for seat in coach.seats:
                        if seat.seat_id == s["seat_no"]:
                            seat.is_available = True

        # delete booking
        del self.booking_mgr.bookings[request.booking_id]

        # print cancellation details
        self._print_cancellation(request, booking)

        return True

    def _print_cancellation(self, request, booking):
        # print result
        print("\n---- BOOKING CANCELLED ----")
        print(f"Booking ID: {request.booking_id} cancelled successfully")

        for s in booking.seat_allocations:
            print(
                f"Released -> Passenger: {s['passenger']} | "
                f"Coach: {s['coach']} | "
                f"Seat: {s['seat_no']}"
            )
