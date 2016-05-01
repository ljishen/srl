from locust import HttpLocust, TaskSet
from random import randint

import json

headers = {'content-type': 'application/json'}

def landing(l):
    l.client.get("/")

def searchdatasets(l):
    l.client.post("/datasets/search", data=json.dumps({}), headers=headers)

def searchreadgroupsets(l):
    l.client.post("/readgroupsets/search", data=json.dumps({"datasetId": "WyIxa2dlbm9tZXMiXQ"}), headers=headers)

def searchreads(l):
    start = randint(0,123123123)
    end = start + randint(1,123123123)
    l.client.post("/reads/search", data=json.dumps({"readGroupIds": ["WyIxa2dlbm9tZXMiLCJyZ3MiLCJIRzAwMDk3Lm1hcHBlZC5JTExVTUlOQS5id2EuR0JSLmxvd19jb3ZlcmFnZS4yMDEzMDQxNSIsIlNSUjc0MTM4NCJd"], "referenceId": "WyJOQ0JJMzciLCIxIl0", "start": start, "end": end}), headers=headers)

def searchfeaturesets(l):
    l.client.post("/featuresets/search", data=json.dumps({"datasetId": "WyIxa2dlbm9tZXMiXQ"}), headers=headers)

def searchfeatures(l):
    start = randint(0,123123123)
    end = start + randint(1,123123123)
    chrom = "chr" + str(randint(1,22))
    l.client.post("/features/search", data=json.dumps({"featureSetId": "WyIxa2dlbm9tZXMiLCJnZW5jb2RlX3YyNGxpZnQzNyJd",  "start": start, "end": end, "referenceName": chrom, "parentId": "", "featureTypes": []}), headers=headers)
  
def searchvariants(l):
    start = randint(0,123123123)
    end = start + randint(1,123123123)
    chrom = str(randint(1,22))
    l.client.post("/variants/search", data=json.dumps({"variantSetId": "WyIxa2dlbm9tZXMiLCJ2cyIsInJlbGVhc2UiXQ",  "start": start, "end": end, "referenceName": chrom}), headers=headers)

def searchvariantannotations(l):
    start = randint(0,123123123)
    end = start + randint(1,123123123)
    chrom = str(randint(1,22))
    l.client.post("/variantannotations/search", data=json.dumps({"variantAnnotationSetId": "WyIxa2dlbm9tZXMiLCJ2cyIsImZ1bmN0aW9uYWxfYW5ub3RhdGlvbiIsInZhcmlhbnRhbm5vdGF0aW9ucyJd",  "start": start, "end": end, "referenceName": chrom}), headers=headers)

class UserBehavior(TaskSet):
    tasks = {
      searchdatasets: 1,
      searchreads: 100,
      searchreadgroupsets: 100,
      searchfeaturesets: 100,
      searchfeatures: 100,
      searchvariants: 1000,
      searchvariantannotations: 100}

    def on_start(self):
        landing(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=5000
    max_wait=9000