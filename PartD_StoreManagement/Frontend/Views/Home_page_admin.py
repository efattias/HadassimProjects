from PySide6.QtWidgets import QWidget, QTableWidget, QHeaderView, QTableWidgetItem, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox
from PySide6.QtCore import Qt
from Controllers.OrderController import OrderController
from Models.StoreManagementBackendConnectModel import Store_management_instance
from Models.StatusModel import StatusModel
from OrderPage import OrderPage

class Home_page_admin(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user 
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Admin Home Page - Store Management")

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.order_button = QPushButton("Order Products")
        self.order_button.clicked.connect(self.open_order_page)
        self.layout.addWidget(self.order_button)

        self.filter_combo = QComboBox()
        self.filter_combo.addItem("in proccess")            # default
        self.filter_combo.addItem("all")
        self.filter_combo.addItem(StatusModel.Invited.value)
        self.filter_combo.addItem(StatusModel.Approval.value)
        self.filter_combo.addItem(StatusModel.Completed.value)
        self.filter_combo.currentIndexChanged.connect(self.create_order_table)

        self.layout.addWidget(self.filter_combo)

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

        selected_filter = self.filter_combo.currentText()
        orders = Store_management_instance.Orders

        for order in orders:
            if order:
                if selected_filter == "in proccess" and order.status == StatusModel.Completed.value:
                    continue

                if selected_filter in [s.value for s in StatusModel] and order.status != selected_filter:
                    continue

                self.add_order_row(order)

    def add_order_row(self, order):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        self.table.setItem(row_position, 0, QTableWidgetItem(str(order.id)))
        self.table.setItem(row_position, 1, QTableWidgetItem(order.invited_date.strftime('%Y-%m-%d %H:%M')))
        self.table.setItem(row_position, 2, QTableWidgetItem(order.approval_date.strftime('%Y-%m-%d %H:%M') if order.approval_date else "Not approved"))
        self.table.setItem(row_position, 3, QTableWidgetItem(order.complete_date.strftime('%Y-%m-%d %H:%M') if order.complete_date else "Not completed"))
        
        status_button = QPushButton(order.status)
        status_button.setEnabled(order.status == StatusModel.Approval.value)
        status_button.clicked.connect(lambda checked=False, o=order, b=status_button: self.update_status(o, b))

        status_widget = QWidget()
        status_layout = QHBoxLayout(status_widget)
        status_layout.addWidget(status_button)
        status_layout.setContentsMargins(0, 0, 0, 0)
        status_layout.setAlignment(Qt.AlignCenter)
        self.table.setCellWidget(row_position, 4, status_widget)

        self.table.resizeRowsToContents()

    def update_status(self, order, button):
        new_status = StatusModel.Completed.value
        result = OrderController.updateOrderStatus(order.id, new_status)
        if "ERROR" not in str(result):  
            order.status = new_status
            button.setText(new_status)
            button.setEnabled(False)
            self.create_order_table() 

    def open_order_page(self):
        self.new_page = OrderPage(self.user)  
        self.new_page.order_created.connect(self.refresh_orders)  
        self.new_page.show()

    def refresh_orders(self):
        print("refresh")
