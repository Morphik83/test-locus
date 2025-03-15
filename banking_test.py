from locus import HttpUser, task, between

class BankingApp(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def login(self):
        self.client.post("/login", json={"username": "user", "password": "pass"})

    @task(1)
    def transfer(self):
        self.client.post("/transfer", json={"from": "user", "to": "user2", "amount": 100})

    @task(1)
    def logout(self):
        self.client.post("/logout")

# to run:
# locust -f banking_test.py --host=http://yourbankingapp.com --users 1000 --spawn-rate 100