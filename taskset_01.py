from locust import SequentialTaskSet , task , between , HttpUser

class SequenceOfTasks(SequentialTaskSet):
    # host = "https://the-internet.herokuapp.com"
    wait_time = between(1, 3)

    @task
    def first(self):
        print("1")

    @task
    def second(self):
        print("2")

    @task
    def stop(self):
        self.interrupt()

class MyUser(HttpUser):
    # host = "https://the-internet.herokuapp.com"
    wait_time = between(1, 3)
    tasks = { SequentialTaskSet : 2 }

    @task
    def test(self):
        pass