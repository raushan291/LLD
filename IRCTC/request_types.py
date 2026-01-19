from abc import ABC, abstractmethod

class Request(ABC):
    def __init__(self, request_id, request_processor):
        self.request_id = request_id
        self.request_processor = request_processor
    
    @abstractmethod
    def process(self):
        pass

class SearchRequest(Request):
    def __init__(self, rid, request_processor, src, dest, date):
        super().__init__(rid, request_processor)
        self.src = src
        self.dest = dest
        self.date = date
    
    def process(self):
        return self.request_processor.process_request(self)

class BookingRequest(Request):
    def __init__(self, rid, request_processor, train_id, users, src, dest, date, compartment_type):
        super().__init__(rid, request_processor)
        self.train_id = train_id
        self.users = users
        self.src = src
        self.dest = dest
        self.date = date
        self.compartment_type = compartment_type
    
    def process(self):
        return self.request_processor.process_request(self)

class CancelRequest(Request):
    def __init__(self, rid, request_processor, booking_id):
        super().__init__(rid, request_processor)
        self.booking_id = booking_id

    def process(self):
        return self.request_processor.process_request(self)