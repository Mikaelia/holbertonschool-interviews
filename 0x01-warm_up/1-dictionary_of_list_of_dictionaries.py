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

    with open("todo_all_employees.json", "w") as f:
        f.write(json.dumps(newdict))
