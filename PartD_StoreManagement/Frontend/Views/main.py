import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Models import StoreManagementBackendConnectModel
from Models.StoreManagementBackendConnectModel import Store_management_instance

def main():
    print("haaaaaaaa")
    return 0

if __name__ == '__main__':
    StoreManagementApp = StoreManagementBackendConnectModel.StoreManagementBackendConnectModel()        
    main()