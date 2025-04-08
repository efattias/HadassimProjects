import requests

class UserController:
    API_URL = "https://localhost:7049/api/User"
    @staticmethod
    def getUsers():
        try:
            response = requests.get(UserController.API_URL, verify=False)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return f"ERROR: {e}"
        
    @staticmethod
    def postUser(newUser):
        try:
            response = requests.post(UserController.API_URL, json=newUser.to_dict(), verify=False)
            response.raise_for_status()
            print(f"User added successfully: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to add user: {e}")
            if e.response:
                print(f"Response status code: {e.response.status_code}")
                print(f"Response content: {e.response.text}")
            return f"ERROR: {e}"