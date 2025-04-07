from PySide6.QtWidgets import QWidget, QTableWidget, QHeaderView, QTableWidgetItem, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from Controllers.OrderController import OrderController
from Models.StoreManagementBackendConnectModel import Store_management_instance

class Home_page_supplier(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user 
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Supplier Home Page - Store Management")

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.create_order_table()

    def create_order_table(self):
        if hasattr(self, 'table'):
            self.table.clearContents()
            self.table.setRowCount(0)
        else:
            self.table = QTableWidget()
            self.table.setColumnCount(5)
            self.table.setHorizontalHeaderLabels(["ID", "invited_date", "approval_date", "complete_date", "status"])
            self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.layout.addWidget(self.table)  

        orders = Store_management_instance.Orders
        for order in orders:
            if(order.supplier_id == self.user.id):
                self.add_order_row(order)
    
    def add_order_row(self, order):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        self.table.setItem(row_position, 0, QTableWidgetItem(str(order.id)))
        self.table.setItem(row_position, 1, QTableWidgetItem(order.invited_date.strftime('%Y-%m-%d %H:%M')))
        self.table.setItem(row_position, 2, QTableWidgetItem(order.approval_date.strftime('%Y-%m-%d %H:%M') if order.approval_date else "Not approved"))
        self.table.setItem(row_position, 3, QTableWidgetItem(order.complete_date.strftime('%Y-%m-%d %H:%M') if order.complete_date else "Not completed"))
        
        status_button = QPushButton(order.status)
        status_button.setEnabled(order.status == "Invited")
        status_button.clicked.connect(lambda checked=False, o=order, b=status_button: self.update_status(o, b))

        status_widget = QWidget()
        status_layout = QHBoxLayout(status_widget)
        status_layout.addWidget(status_button)
        status_layout.setContentsMargins(0, 0, 0, 0)
        status_layout.setAlignment(Qt.AlignCenter)
        self.table.setCellWidget(row_position, 4, status_widget)

        self.table.resizeRowsToContents()

    def update_status(self, order, button):
        new_status = "Approval"
        result = OrderController.updateOrderStatus(order.id, new_status)
        if "ERROR" not in str(result):  
            order.status = new_status
            button.setText(new_status)
            button.setEnabled(False)
