from locust import User, TaskSet, constant , task

class ForumSection(TaskSet):
    wait_time = constant(1)

    @task(10)
    def view_thread(self):
        print("1")
        pass

    @task
    def create_thread(self):
        print("2")
        pass

    @task
    def stop(self):
        self.interrupt()

class LoggedInUser(User):
    wait_time = constant(5)
    tasks = {ForumSection:2}

    @task
    def my_task(self):
        pass