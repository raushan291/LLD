from enum import Enum

class SeatType(Enum):
    LOWER = "LOWER"
    MIDDLE = "MIDDLE"
    UPPER = "UPPER"
    SIDE_LOWER = "SIDE_LOWER"
    SIDE_UPPER = "SIDE_UPPER"
    WINDOW = "WINDOW"
    AISLE = "AISLE"

class CompartmentType(Enum):
    SL = "SLEEPER"     # S1, S2
    AC1 = "AC1"        # H1, H2
    AC2 = "AC2"        # A1, A2
    AC3 = "AC3"        # B1, B2
    CC = "CC"          # C1, C2
