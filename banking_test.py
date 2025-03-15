from locust import HttpUser, task, between

class BankingApp(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        """Login when user starts"""
        self.login()

    def on_stop(self):
        """Logout when user stops"""
        self.logout()

    def login(self):
        """User login with error handling"""
        with self.client.post("/login", 
            json={"username": "user", "password": "pass"}, 
            catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Login failed")

    @task(3)
    def check_balance(self):
        """Check account balance"""
        with self.client.get("/balance", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Balance check failed")

    @task(2)
    def transfer(self):
        """Transfer money between accounts"""
        with self.client.post("/transfer", 
            json={"from": "user", "to": "user2", "amount": 100},
            catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Transfer failed")

    def logout(self):
        """User logout with error handling"""
        with self.client.post("/logout", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Logout failed")

# to run:
# locust -f banking_test.py --host=http://yourbankingapp.com --users 1000 --spawn-rate 100