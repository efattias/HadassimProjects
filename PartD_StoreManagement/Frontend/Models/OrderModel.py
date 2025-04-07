from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from datetime import datetime
from UserModel import UserModel
from OrderItemModel import OrderItemModel

@dataclass
class OrderModel:
    id: int
    supplier_id: int
    supplier: Optional['UserModel'] = None  
    invited_date: datetime = datetime.now()
    approval_date: Optional[datetime] = None
    complete_date: Optional[datetime] = None
    status: str  
    order_items: Optional[List['OrderItemModel']] = None  

    @classmethod
    def from_json(cls, jsonData: Dict[str, Any]) -> 'OrderModel':
        return cls(
            id=jsonData.get('id'),
            supplier_id=jsonData.get('supplierId'),
            supplier=jsonData.get('supplier'),  
            invited_date=datetime.fromisoformat(jsonData.get('invitedDate')) if jsonData.get('invitedDate') else datetime.now(),
            approval_date=datetime.fromisoformat(jsonData.get('approvalDate')) if jsonData.get('approvalDate') else None,
            complete_date=datetime.fromisoformat(jsonData.get('completeDate')) if jsonData.get('completeDate') else None,
            status=jsonData.get('status'),  
            order_items=jsonData.get('orderItems', []),  
        )
    
    def to_json(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'supplierId': self.supplier_id,
            'supplier': self.supplier,  
            'invitedDate': self.invited_date.isoformat(),
            'approvalDate': self.approval_date.isoformat() if self.approval_date else None,
            'completeDate': self.complete_date.isoformat() if self.complete_date else None,
            'status': self.status,  
            'orderItems': self.order_items,  
        }
