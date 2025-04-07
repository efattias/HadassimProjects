import requests

class ProductController:
    API_URL = "https://localhost:7049/api/Product"
    @staticmethod
    def getProduct():
        try:
            response = requests.get(ProductController.API_URL, verify=False)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return f"ERROR: {e}"
        
    @staticmethod
    def postProduct(newProduct):
        try:
            response = requests.post(ProductController.API_URL, json=newProduct, verify=False)
            response.raise_for_status()
            print(f"Product added successfully: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to add product: {e}")
            if e.response:
                print(f"Response status code: {e.response.status_code}")
                print(f"Response content: {e.response.text}")
            return f"ERROR: {e}"
        
    @staticmethod
    def updateProductStock(product_id, add_to_stock):
        url = f"{ProductController.API_URL}/UpdateInStock/{product_id}?addToStock={add_to_stock}"
        try:
            response = requests.post(url, verify=False)
            response.raise_for_status()
            print(f"Stock updated successfully: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to update stock: {e}")
            if e.response:
                print(f"Response status code: {e.response.status_code}")
                print(f"Response content: {e.response.text}")
            return f"ERROR: {e}"