import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QSpacerItem, QSizePolicy, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from Home_page_admin import Home_page_admin 
from Home_page_supplier import Home_page_supplier
from Models.StoreManagementBackendConnectModel import Store_management_instance
from Models.RoleModel import RoleModel
from RegisterWindow import RegisterWindow


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Login - Store Management")
        layout = QVBoxLayout()
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        font = QFont()
        font.setPointSize(16)

        username_label = QLabel("Username:")
        username_label.setFont(font)
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setFixedSize(350, 40)

        password_label = QLabel("Password:")
        password_label.setFont(font)
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedSize(350, 40)

        # login Button
        login_button = QPushButton("Login")
        login_button.setFixedSize(350, 50)
        login_button.clicked.connect(self.login_func)

        register_button = QPushButton("Register")
        register_button.setFixedSize(350, 40)
        register_button.clicked.connect(self.open_register_window)

        layout.addWidget(username_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.username_input, alignment=Qt.AlignCenter)
        layout.addWidget(password_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.password_input, alignment=Qt.AlignCenter)
        layout.addWidget(login_button, alignment=Qt.AlignCenter)
        layout.addWidget(register_button, alignment=Qt.AlignCenter)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(layout)
        

    def login_func(self):
        username = self.username_input.text()
        password = self.password_input.text()

        for user in Store_management_instance.Users:
            if user.username == username and user.password == password:
                QMessageBox.information(self, "Login Success", f"Welcome, {username}!")
                if user.role == RoleModel.Admin:
                    self.home_page_admin = Home_page_admin(user)
                    self.home_page_admin.showMaximized()
                    self.close()
                if user.role == RoleModel.Supplier:
                    self.home_page_supplier = Home_page_supplier(user)
                    self.home_page_supplier.showMaximized()
                    self.close()
                return

        QMessageBox.warning(self, "Login Failed", "Username or password is incorrect.")

    def open_register_window(self):
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()
