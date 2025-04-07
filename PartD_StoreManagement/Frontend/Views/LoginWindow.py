from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QSpacerItem, QSizePolicy, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from HomePage import HomePage 
from Models.StoreManagementBackendConnectModel import Store_management_instance


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

        # סיסמה
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

        layout.addWidget(username_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.username_input, alignment=Qt.AlignCenter)
        layout.addWidget(password_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.password_input, alignment=Qt.AlignCenter)
        layout.addWidget(login_button, alignment=Qt.AlignCenter)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(layout)

    def login_func(self):
        username = self.username_input.text()
        password = self.password_input.text()

        for user in Store_management_instance.Users:
            if user.username == username and user.password == password:
                QMessageBox.information(self, "Login Success", f"Welcome, {username}!")
                self.home_page = HomePage(user)
                self.home_page.showMaximized()
                self.close()
                return

        QMessageBox.warning(self, "Login Failed", "Username or password is incorrect.")
