from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QHBoxLayout, QGroupBox
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from Models.UserModel import UserModel
from Models.ProductModel import ProductModel
from Models.RoleModel import RoleModel
from Models.StoreManagementBackendConnectModel import Store_management_instance
from Controllers.UserController import UserController
from Controllers.ProductController import ProductController

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.product_inputs = []  
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Register - Supplier")
        layout = QVBoxLayout()
        font = QFont()
        font.setPointSize(14)

        self.username_input = self._create_labeled_input("Username:", layout, font)
        self.password_input = self._create_labeled_input("Password:", layout, font, is_password=True)
        self.company_name_input = self._create_labeled_input("Company Name:", layout, font)
        self.phone_input = self._create_labeled_input("Phone Number:", layout, font)
        self.rep_input = self._create_labeled_input("Representative Name:", layout, font)

        product_area_label = QLabel("Products:")
        product_area_label.setFont(font)
        layout.addWidget(product_area_label, alignment=Qt.AlignCenter)

        self.product_layout = QVBoxLayout()
        self.add_product_fields() 

        add_product_button = QPushButton("Add Product")
        add_product_button.clicked.connect(self.add_product_fields)
        layout.addLayout(self.product_layout)
        layout.addWidget(add_product_button, alignment=Qt.AlignCenter)

        register_button = QPushButton("Register")
        register_button.setFixedSize(200, 40)
        register_button.clicked.connect(self.register_user)
        layout.addWidget(register_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def _create_labeled_input(self, label_text, layout, font, is_password=False):
        label = QLabel(label_text)
        label.setFont(font)
        input_field = QLineEdit()
        input_field.setFixedSize(300, 35)
        if is_password:
            input_field.setEchoMode(QLineEdit.Password)
        layout.addWidget(label, alignment=Qt.AlignCenter)
        layout.addWidget(input_field, alignment=Qt.AlignCenter)
        return input_field

    def add_product_fields(self):
        container = QGroupBox()
        inner_layout = QHBoxLayout()

        product_name = QLineEdit()
        product_name.setPlaceholderText("Product Name")
        price = QLineEdit()
        price.setPlaceholderText("Price")
        min_qty = QLineEdit()
        min_qty.setPlaceholderText("Min Qty")
        stock = QLineEdit()
        stock.setPlaceholderText("In Stock")

        for w in [product_name, price, min_qty, stock]:
            w.setFixedSize(130, 30)
            inner_layout.addWidget(w)

        container.setLayout(inner_layout)
        self.product_layout.addWidget(container)
        self.product_inputs.append((product_name, price, min_qty, stock))

    def register_user(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        company = self.company_name_input.text().strip()
        phone = self.phone_input.text().strip()
        rep = self.rep_input.text().strip()

        if not all([username, password, company, phone, rep]):
            QMessageBox.warning(self, "Missing Info", "Please fill in all supplier details.")
            return

        if any(u.username == username for u in Store_management_instance.Users):
            QMessageBox.warning(self, "Username Taken", "Please choose a different username.")
            return

        new_user = UserModel(
            id=0,
            username=username,
            password=password,
            role=RoleModel.Supplier,
            company_name=company,
            phone_number=phone,
            representative_name=rep,
            products=[]
        )

        saved_user_data = UserController.postUser(new_user)

        if not saved_user_data or "id" not in saved_user_data:
            QMessageBox.critical(self, "Error", "Failed to register supplier.")
            return

        saved_user = UserModel.from_json(saved_user_data)


        for inputs in self.product_inputs:
            name, price, min_qty, stock = [i.text().strip() for i in inputs]
            if not all([name, price, min_qty, stock]):
                continue  

            try:
                product = ProductModel(
                    id=0,
                    product_name=name,
                    price_per_item=float(price),
                    minimum_quantity=int(min_qty),
                    in_stock=int(stock),
                    supplier_id=saved_user.id,
                    supplier=saved_user
                )
                saved_product_data = ProductController.postProduct(product)

                if not saved_product_data or "id" not in saved_product_data:
                    QMessageBox.warning(self, "Product Error", f"Failed to save product: {product.product_name}")
                    continue

                saved_product = ProductModel.from_json(saved_product_data)
                saved_user.products.append(saved_product.id)
            except ValueError:
                QMessageBox.warning(self, "Invalid Input", "Please ensure price and quantities are numbers.")
                return

        QMessageBox.information(self, "Registration Success", "Supplier and products registered successfully!")

        from LoginWindow import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
