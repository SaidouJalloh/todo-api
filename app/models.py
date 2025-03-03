from datetime import datetime

class Task:
    def __init__(self, id, title, description="", completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
    
    def update(self, data):
        if "title" in data:
            self.title = data["title"]
        if "description" in data:
            self.description = data["description"]
        if "completed" in data:
            self.completed = data["completed"]
        self.updated_at = datetime.now()