from models import Compartment, Train, TrainJourney
from enums import CompartmentType
from managers import TrainManager, TrainJourneyManager, BookingManager
from request_processors import SearchRequestProcessor, BookingRequestProcessor, CancelRequestProcessor
from request_types import SearchRequest, BookingRequest, CancelRequest
from coach_factory import CoachFactory

def setup_trains(train_mgr):
    # ---------------- first train ----------------
    train = Train(12952, "T1", "New Delhi Mumbai Central Rajdhani Express", "16:55", stops=["NDLS", "KOTA", "NAD", "RTM", "BRC", "ST", "BVI", "MMCT"])

    # AC1 Compartment -> H1
    ac1_compartment = Compartment(1, CompartmentType.AC1)
    CoachFactory.create_coaches(ac1_compartment, coach_count=1, seats_per_coach=24)

    # AC2 Compartment -> A1, A2, A3, A4
    ac2_compartment = Compartment(2, CompartmentType.AC2)
    CoachFactory.create_coaches(ac2_compartment, coach_count=4, seats_per_coach=54)

    # AC3 Compartment -> B1, B2, B3, B4, B5, B6
    ac3_compartment = Compartment(3, CompartmentType.AC3)
    CoachFactory.create_coaches(ac3_compartment, coach_count=6, seats_per_coach=72)

    # Sleeper Compartment -> S1, S2, S3, S4, S5, S6, S7, S8, S9, S10
    sl_compartment = Compartment(4, CompartmentType.SL)
    CoachFactory.create_coaches(sl_compartment, coach_count=10, seats_per_coach=72)

    # CC Compartment -> C1, C2, C3
    cc_compartment = Compartment(5, CompartmentType.CC)
    CoachFactory.create_coaches(cc_compartment, coach_count=3, seats_per_coach=78)

    train.compartments.append(ac1_compartment)
    train.compartments.append(ac2_compartment)
    train.compartments.append(sl_compartment)
    train.compartments.append(ac3_compartment)
    train.compartments.append(cc_compartment)

    train_mgr.create_train(train)

    # ---------------- second train ----------------
    train2 = Train(22210, "T2", "Mumbai Central Duronto", "23:25", stops=["NDLS", "KOTA", "RTM", "BRC", "MMCT"])

    # AC1 Compartment -> H1
    ac1_compartment = Compartment(1, CompartmentType.AC1)
    CoachFactory.create_coaches(ac1_compartment, coach_count=1, seats_per_coach=24)

    # AC2 Compartment -> A1, A2, A3, A4
    ac2_compartment = Compartment(2, CompartmentType.AC2)
    CoachFactory.create_coaches(ac2_compartment, coach_count=4, seats_per_coach=54)

    # AC3 Compartment -> B1, B2, B3, B4, B5, B6
    ac3_compartment = Compartment(3, CompartmentType.AC3)
    CoachFactory.create_coaches(ac3_compartment, coach_count=6, seats_per_coach=72)

    # Sleeper Compartment -> S1, S2, S3, S4, S5, S6, S7, S8, S9, S10
    sl_compartment = Compartment(4, CompartmentType.SL)
    CoachFactory.create_coaches(sl_compartment, coach_count=10, seats_per_coach=72)

    # CC Compartment -> C1, C2, C3
    cc_compartment = Compartment(5, CompartmentType.CC)
    CoachFactory.create_coaches(cc_compartment, coach_count=3, seats_per_coach=78)

    train2.compartments.append(ac1_compartment)
    train2.compartments.append(ac2_compartment)
    train2.compartments.append(sl_compartment)
    train2.compartments.append(ac3_compartment)
    train2.compartments.append(cc_compartment)

    train_mgr.create_train(train2)

def setup_journeys(train_mgr, journey_mgr):
    for tid, train in train_mgr.trains.items():
        journey = TrainJourney(train, "2026-01-20")
        journey_mgr.create_journey(train.train_id, journey)
        print(f"Journey created for Train ID: {tid} on 2026-01-20")


# Managers
train_mgr = TrainManager()
journey_mgr = TrainJourneyManager()
booking_mgr = BookingManager()

# ---------------- TRAIN CREATION ----------------
setup_trains(train_mgr)

# ---------------- JOURNEY CREATION ----------------
setup_journeys(train_mgr, journey_mgr)

# ------------------- PROCESSORS -------------------
search_processor = SearchRequestProcessor(train_mgr)
booking_processor = BookingRequestProcessor(booking_mgr, journey_mgr)
cancel_processor = CancelRequestProcessor(booking_mgr, journey_mgr)

# --------------------- SEARCH ---------------------
search_req = SearchRequest("R1", search_processor,"NDLS", "MMCT", "2026-01-20")
search_res = search_req.process()
print(f"\nTotal trains found: {len(search_res)}")

# --------------------- BOOKING ---------------------
booking_req = BookingRequest(
    "R2",
    booking_processor,
    "T1",
    ["Passanger-1", "Passanger-2", "Passanger-3", "Passanger-4", "Passanger-5"],
    "NDLS",
    "MMCT",
    "2026-01-20",
    CompartmentType.AC2
)

booking_req.process()

# --------------------- CANCELLATION -----------------

cancel_req = CancelRequest("R3", cancel_processor, "B001")
cancel_req.process()

# --------- BOOKING AGAIN AFTER CANCELLATION ----------
booking_req.process()
