import requests

class OrderController:
    API_URL = "https://localhost:7049/api/Order"
    @staticmethod
    def getOrder():
        try:
            response = requests.get(OrderController.API_URL, verify=False)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return f"ERROR: {e}"
        
    @staticmethod
    def postOrder(newOrder):
        try:
            response = requests.post(OrderController.API_URL, json=newOrder, verify=False)
            response.raise_for_status()
            print(f"Order added successfully: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to add order: {e}")
            if e.response:
                print(f"Response status code: {e.response.status_code}")
                print(f"Response content: {e.response.text}")
            return f"ERROR: {e}"
        
    @staticmethod
    def updateOrderStatus(order_id, new_status):
        url = f"{OrderController.API_URL}/UpdateStatus/{order_id}"
        try:
            response = requests.post(url, json=new_status, verify=False)
            response.raise_for_status()
            print(f"Order status updated successfully: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to update order status: {e}")
            if e.response:
                print(f"Response status code: {e.response.status_code}")
                print(f"Response content: {e.response.text}")
            return f"ERROR: {e}"