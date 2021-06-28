from locust import TaskSequence,seq_task,HttpUser

class MyTaskSequence(TaskSequence):
    @seq_task(1)
    def first_task(self):
        pass

    @seq_task(2)
    def second_task(self):
        pass

    @seq_task(3)
    @task(10)
    def third_task(self):
        pass


class WebsiteUser(HttpLocust):
    task_set = MyTaskSequence
    min_wait = 4000
    max_wait = 7000
