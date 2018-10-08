#!/usr/bin/python3
"""
Queries external API for user todo task information
"""
import json
import requests
import sys

if __name__ == '__main__':

    users = requests.get('https://jsonplaceholder.typicode.com/users')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')

    tasklist = tasks.json()

    newdict = {}

    userlist = users.json()

    for user in userlist:
        task_array = []
        for task in tasklist:
            if task.get('userId') == user.get('id'):
                task_array.append(
                    {"username": user.get('username'),
                     "task": task.get('title'),
                     "completed": task.get('completed')})
        newdict[user.get('id')] = task_array
    print(json.dumps(newdict))

    # tasks = response.json()
    # employee = user.json()[0].get('username')

    # total = 0
    # completed = 0
    # task_list = []

    # for task in tasks:
    #     if task.get('completed'):
    #         completed += 1
    #         task_list.append(task.get('title'))
    #     total += 1

    # print("Employee {} is done with tasks({}/{}):".
    #       format(employee, completed, total))
    # for task in task_list:
    #     print("\t {}".format(task))
