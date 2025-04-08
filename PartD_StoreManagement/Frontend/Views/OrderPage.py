from datetime import datetime
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout, QSpinBox
from Models.StoreManagementBackendConnectModel import Store_management_instance
from Controllers.OrderController import OrderController
from Controllers.OrderItemController import OrderItemController
from PySide6.QtCore import Signal

class OrderPage(QWidget):
    order_created = Signal()
    def __init__(self, user):
        super().__init__()
        self.user = user 
        self.selected_quantities = {}
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Create New Order")
        self.resize(800, 600)
        layout = QVBoxLayout(self)

        self.products_table = QTableWidget()
        self.products_table.setColumnCount(7)
        self.products_table.setHorizontalHeaderLabels([
            "ID", "Name", "Price per Item", "Minimum Quantity", 
            "In Stock", "Supplier ID", "Quantity to Order"
        ])
        layout.addWidget(self.products_table)

        self.load_products()

        self.order_button = QPushButton("Place Order")
        self.order_button.clicked.connect(self.place_order)
        layout.addWidget(self.order_button)

    def load_products(self):
        products = Store_management_instance.Products
        self.products_table.setRowCount(0)

        for product in products:
            row = self.products_table.rowCount()
            self.products_table.insertRow(row)

            self.products_table.setItem(row, 0, QTableWidgetItem(str(product.id)))
            self.products_table.setItem(row, 1, QTableWidgetItem(product.product_name))
            self.products_table.setItem(row, 2, QTableWidgetItem(str(product.price_per_item)))
            self.products_table.setItem(row, 3, QTableWidgetItem(str(product.minimum_quantity)))
            self.products_table.setItem(row, 4, QTableWidgetItem(str(product.in_stock)))
            self.products_table.setItem(row, 5, QTableWidgetItem(str(product.supplier_id)))

            spin_box = QSpinBox()
            spin_box.setRange(0, 10000)
            spin_box.valueChanged.connect(lambda value, pid=product.id: self.selected_quantities.__setitem__(pid, value))
            self.products_table.setCellWidget(row, 6, spin_box)

    def place_order(self):
        new_order_data = {
            "id": 0,
            "supplierId": self.user.id,
            "invitedDate": datetime.now().isoformat(),
            "approvalDate": datetime.now().isoformat(),
            "completeDate": datetime.now().isoformat(),
            "status": "Invited"
        }
        new_order = OrderController.postOrder(new_order_data)
        if not new_order or "ERROR" in str(new_order):
            print("Failed to create order.")
            return

        for product_id, quantity in self.selected_quantities.items():
            if quantity > 0:
                order_item_data = {
                    "id": 0,
                    "orderId": new_order["id"],
                    "productId": product_id,
                    "quantity": quantity
                }
                OrderItemController.postOrderItem(order_item_data)

        self.order_created.emit()
        self.close()

