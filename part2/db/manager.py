import os

tasks_file = os.path.join(os.getcwd(), 'part2','db', 'tasks.csv')

# creates tasks file is none exists
def create():
    pass

# check if tasks file exists
def is_tasks_file_exists():
    pass

# adds a task to the task file and returns the task id.
def add_task(desc, priority):
    pass

# returns list of tasks in the task file.
def get_all_tasks():
    pass

# remove a task from the task file.
def remove_task(id):
    pass

# complete a task in the task file.
def complete_task(id):
    pass

# change the priority of a task in the task file.
def change_priority(id, priority):
    pass

# update the task description of a task in the task file.
def update_desc(id, desc):
    pass

# search for a task in the task file.
def search(id, desc, priority):
    pass

# sort the tasks in the task file. Default order is 1.
def sort(order):
    pass
