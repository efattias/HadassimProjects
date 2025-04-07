from typing import Dict, Any, Optional, TYPE_CHECKING
from dataclasses import dataclass
if TYPE_CHECKING:
    from Models.OrderModel import OrderModel
    from Models.ProductModel import ProductModel

@dataclass
class OrderItemModel:
    id: int
    order_id: int
    product_id: int
    quantity: int
    order: Optional['OrderModel'] = None  
    product: Optional['ProductModel'] = None  

    @classmethod
    def from_json(cls, jsonData: Dict[str, Any]) -> 'OrderItemModel':
        return cls(
            id=jsonData.get('id'),
            order_id=jsonData.get('orderId'),
            product_id=jsonData.get('productId'),
            quantity=jsonData.get('quantity'),
            order=jsonData.get('order'),  
            product=jsonData.get('product'),  
        )
    
    def to_json(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'orderId': self.order_id,
            'productId': self.product_id,
            'quantity': self.quantity,
            'order': self.order,  
            'product': self.product, 
        }
