from models import Coach, Seat, SeatType, CompartmentType

class BaseCoach(Coach):
    def __init__(self, coach_name, compartment_type, seats_per_coach):
        super().__init__(coach_name, compartment_type)
        self.seats_per_coach = seats_per_coach
        self._create_seats()

    def _seat_pattern(self):
        """To be implemented by subclasses"""
        raise NotImplementedError

    def _create_seats(self):
        pattern = self._seat_pattern()
        for s in range(1, self.seats_per_coach + 1):
            seat_type = pattern[(s - 1) % len(pattern)]
            self.seats.append(Seat(s, seat_type))

class AC1Coach(BaseCoach):
    def _seat_pattern(self):
        return [
            SeatType.LOWER,
            SeatType.UPPER,
            SeatType.LOWER,
            SeatType.UPPER
        ]

class AC2Coach(BaseCoach):
    def _seat_pattern(self):
        return [
            SeatType.LOWER,
            SeatType.UPPER,
            SeatType.LOWER,
            SeatType.UPPER,
            SeatType.SIDE_LOWER,
            SeatType.SIDE_UPPER
        ]

class AC3Coach(BaseCoach):
    def _seat_pattern(self):
        return [
            SeatType.LOWER,
            SeatType.MIDDLE,
            SeatType.UPPER,
            SeatType.LOWER,
            SeatType.MIDDLE,
            SeatType.UPPER,
            SeatType.SIDE_LOWER,
            SeatType.SIDE_UPPER
        ]

class SLCoach(BaseCoach):
    def _seat_pattern(self):
        return [
            SeatType.LOWER,
            SeatType.MIDDLE,
            SeatType.UPPER,
            SeatType.LOWER,
            SeatType.MIDDLE,
            SeatType.UPPER,
            SeatType.SIDE_LOWER,
            SeatType.SIDE_UPPER
        ]

class CCCoach(BaseCoach):
    def _seat_pattern(self):
        return [
            SeatType.WINDOW,
            SeatType.MIDDLE,
            SeatType.AISLE,
            SeatType.AISLE,
            SeatType.MIDDLE,
            SeatType.WINDOW
        ]

class CoachFactory:
    """Factory for creating coaches based on compartment type"""

    coach_map = {
        CompartmentType.AC1: AC1Coach,
        CompartmentType.AC2: AC2Coach,
        CompartmentType.AC3: AC3Coach,
        CompartmentType.SL: SLCoach,
        CompartmentType.CC: CCCoach
    }

    @staticmethod
    def generate_coach_name(compartment_type, index):
        if compartment_type == CompartmentType.SL:
            return f"S{index}"
        if compartment_type == CompartmentType.AC1:
            return f"H{index}"
        if compartment_type == CompartmentType.AC2:
            return f"A{index}"
        if compartment_type == CompartmentType.AC3:
            return f"B{index}"
        if compartment_type == CompartmentType.CC:
            return f"C{index}"
        return f"X{index}"

    @staticmethod
    def create_coaches(compartment, coach_count, seats_per_coach):
        coach_cls = CoachFactory.coach_map[compartment.compartment_type]
        for i in range(1, coach_count + 1):
            coach_name = CoachFactory.generate_coach_name(compartment.compartment_type, i)
            coach = coach_cls(coach_name, compartment.compartment_type, seats_per_coach)
            compartment.coaches.append(coach)
