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
    palette.setColor(QPalette.Button, QColor('#da0000')) 
    palette.setColor(QPalette.ButtonText, QColor('#FFFFFF')) 
    app.setPalette(palette)
    login_window = LoginWindow()
    login_window.showMaximized()

    sys.exit(app.exec())


if __name__ == '__main__':
    StoreManagementApp = StoreManagementBackendConnectModel.StoreManagementBackendConnectModel()        
    main()