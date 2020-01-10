import json

from random import choice

from locust import (
    HttpLocust,
    TaskSequence,
    TaskSet,
    seq_task,
    task,
)


HOST = "http://localhost:8000"
VOTING = 3


class DefVisualizer(TaskSet):

    @task
    def index(self):
        self.client.get("/visualizer/{0}/".format(VOTING))


class Visualizer(HttpLocust):
    host = HOST
    task_set = DefVisualizer
