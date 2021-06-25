from locust import HttpUser , task , between

class MyUser(HttpUser):
    wait_time = between(1, 2.5)
    host = "https://the-internet.herokuapp.com/"

    @task
    def launch_url(self):
        response = self.client.get("/abtest")
        print(response.text)