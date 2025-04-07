from PySide6.QtWidgets import QWidget

# ---------------Admin Home Page---------------
class HomePage(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user  
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Admin Home Page - Store Management")