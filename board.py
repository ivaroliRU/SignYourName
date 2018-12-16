import uuid

def create_id():
    return str(uuid.uuid1())

class Board:
    def __init__(self, name, id, content, about):
        self.board_name = name
        self.board_id = id
        self.board_content = content
        self.board_about = about
    
    def serialize(self):
        ser = {"name": self.board_name, "id": self.board_id, "about": self.board_about, "data": self.board_content}
        return ser