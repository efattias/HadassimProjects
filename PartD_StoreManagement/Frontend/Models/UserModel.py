from typing import Dict, Any, List, Optional
from RoleModel import Role

class UserModel:
    def __init__(self, 
                 id: int, 
                 username: str, 
                 password: str, 
                 role: Role, 
                 company_name: str, 
                 phone_number: str, 
                 representative_name: str, 
                 products: Optional[List[int]] = None, 
                 orders: Optional[List[int]] = None):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
        self.company_name = company_name
        self.phone_number = phone_number
        self.representative_name = representative_name
        self.products = products if products is not None else []
        self.orders = orders if orders is not None else []

    @classmethod
    def from_json(cls, jsonData: Dict[str, Any]) -> 'UserModel':
        role = Role[jsonData.get('role')]
        return cls(
            id=jsonData.get('id'),
            username=jsonData.get('username'),
            password=jsonData.get('password'),
            role=role,
            company_name=jsonData.get('companyName'),
            phone_number=jsonData.get('phoneNumber'),
            representative_name=jsonData.get('representativeName'),
            products=jsonData.get('products', []), 
            orders=jsonData.get('orders', []), 
        )
    
    def to_json(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'role': self.role.name, 
            'companyName': self.company_name,
            'phoneNumber': self.phone_number,
            'representativeName': self.representative_name,
            'products': self.products,  
            'orders': self.orders,  
        }
