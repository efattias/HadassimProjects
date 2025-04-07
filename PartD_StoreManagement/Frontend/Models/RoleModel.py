from enum import Enum

class RoleModel(Enum):
    Admin = "Admin"
    Supplier = "Supplier"

    @classmethod
    def from_json(cls, jsonData: str) -> 'RoleModel':
        return cls(jsonData)

    def to_json(self) -> str:
        return self.value