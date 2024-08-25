from enum import Enum

class Response():
    
    def __init__(self, status:lambda:Status = lambda:Status.Error, message: str = "", data: dict = {}):
        self.status = status
        self.message = message
        self.data = data
    
    
    def asdict(self) -> dict:
        return { 'Status': self.status.name, 'Message': self.message, 'Data': self.data}


class Status(Enum):
    Success = 0
    Error = 1