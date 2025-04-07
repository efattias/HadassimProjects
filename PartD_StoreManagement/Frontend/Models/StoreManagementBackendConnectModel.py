from Models import UserModel
from Models import ProductModel
from Models import OrderModel
from Models import OrderItemModel
from Controllers import UserController
from Controllers import ProductController
from Controllers import OrderController
from Controllers import OrderItemController

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class StoreManagementBackendConnectModel:
    
    _instance = None
    _is_initialized = False

    @classmethod
    def new(cls, *args, **kwargs):
        if cls._instance is not None:
            raise Exception("Cannot create another instance of StoreManagementBackendConnectModel")
        cls._instance = super(StoreManagementBackendConnectModel, cls).__new__(cls)
        cls._instance.__init__(*args, **kwargs)
        return cls._instance
    
    def __init__(self):
        if not self._is_initialized:
            self.Users = [UserModel.UserModel.from_json(newUser) for newUser in UserController.UserController.getUsers()]
            self.Products = [ProductModel.ProductModel.from_json(newProduct) for newProduct in ProductController.ProductController.getProduct()]
            self.Orders = [OrderModel.OrderModel.from_json(newOrder) for newOrder in OrderController.OrderController.getOrder()]
            self.OrderItems = [OrderItemModel.OrderItemModel.from_json(newOrderItem) for newOrderItem in OrderItemController.OrderItemController.getOrderItem()]
            self._is_initialized = True

    # def check_initialization_and_print_users(self):
    #     if self._is_initialized:
    #         print("StoreManagementBackendConnectModel is initialized.")
    #         print("User list:")
    #         for user in self.Users:
    #             print(user)  
    #     else:
    #         print("StoreManagementBackendConnectModel is not initialized.")

if StoreManagementBackendConnectModel._instance is None:
    Store_management_instance = StoreManagementBackendConnectModel.new()
    # Store_management_instance.check_initialization_and_print_users()
else:
    print("Instance already exists.")