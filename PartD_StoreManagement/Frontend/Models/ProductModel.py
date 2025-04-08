from typing import Dict, Any, List, Optional, TYPE_CHECKING
from dataclasses import dataclass
from Models.UserModel import UserModel
if TYPE_CHECKING:
    from Models.OrderItemModel import OrderItemModel

@dataclass
class ProductModel:
    id: int
    product_name: str
    price_per_item: float
    minimum_quantity: int
    in_stock: int
    supplier_id: int
    supplier: Optional['UserModel'] = None  
    order_items: Optional[List['OrderItemModel']] = None  

    @classmethod
    def from_json(cls, jsonData: Dict[str, Any]) -> 'ProductModel':
        return cls(
            id=jsonData.get('id'),
            product_name=jsonData.get('productName'),
            price_per_item=jsonData.get('pricePerItem'),
            minimum_quantity=jsonData.get('minimumQuantity'),
            in_stock=jsonData.get('inStock'),
            supplier_id=jsonData.get('supplierId'),
        )
    
    def to_json(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'productName': self.product_name, 
            'pricePerItem': self.price_per_item,  
            'minimumQuantity': self.minimum_quantity,  
            'inStock': self.in_stock,  
            'supplierId': self.supplier_id, 
        }
