import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Models import StoreManagementBackendConnectModel
from Models.StoreManagementBackendConnectModel import Store_management_instance
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QColor, QPalette
from LoginWindow import LoginWindow

def main():
    app = QApplication(sys.argv)
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor('#FFFFFF')) 
    palette.setColor(QPalette.WindowText, QColor('#000000'))
    palette.setColor(QPalette.Button, QColor('#D0E4F5')) 
    palette.setColor(QPalette.ButtonText, QColor('#000000')) 
    app.setPalette(palette)
    app.setStyleSheet("""
    QTableWidget::horizontalHeader {
        color: black;
        background-color: #D0E4F5; 
        font-weight: bold;
    }
    QHeaderView::section {
        padding: 4px;
        border: 1px solid #A0A0A0;
    }
""")
    login_window = LoginWindow()
    login_window.showMaximized()

    sys.exit(app.exec())


if __name__ == '__main__':
    StoreManagementApp = StoreManagementBackendConnectModel.StoreManagementBackendConnectModel()        
    main()