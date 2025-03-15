# test_singleuser.py
from locust import HttpUser, task, between

class SingleUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def basic_flow(self):
        # Login
        self.client.post("/login", json={"username": "test_user", "password": "test_pass"})
        
        # Check balance
        self.client.get("/balance")
        
        # Logout
        self.client.post("/logout")