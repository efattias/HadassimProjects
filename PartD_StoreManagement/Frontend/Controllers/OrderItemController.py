import requests

class OrderItemController:
    API_URL = "https://localhost:7049/api/OrderItem"
    @staticmethod
    def getOrderItem():
        try:
            response = requests.get(OrderItemController.API_URL, verify=False)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return f"ERROR: {e}"
        
    @staticmethod
    def postOrderItem(newOrderItem):
        try:
            response = requests.post(OrderItemController.API_URL, json=newOrderItem, verify=False)
            response.raise_for_status()
            print(f"OrderItem added successfully: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to add orderItem: {e}")
            if e.response:
                print(f"Response status code: {e.response.status_code}")
                print(f"Response content: {e.response.text}")
            return f"ERROR: {e}"