from enum import Enum

class StatusModel(Enum):
    Invited = "Invited"
    Approval = "Approval"
    Completed = "Completed"

    @classmethod
    def from_json(cls, jsonData: str) -> 'StatusModel':
        return cls(jsonData)

    def to_json(self) -> str:
        return self.value