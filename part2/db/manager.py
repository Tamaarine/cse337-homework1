import os

tasks_file = os.path.join(os.getcwd(), 'part2','db', 'tasks.csv')

# creates tasks file is none exists
def create():
    if not is_tasks_file_exists():
        # File doesn't exist, create it with
        # and return truthy value
        with open(tasks_file, "w") as f:
            f.write('ID,DESCRIPTION,PRIORITY,STATUS\n')
        return 1
    # File already exists return 0
    return 0

# check if tasks file exists
def is_tasks_file_exists():
    # tasks_file doesn't exist return false 
    if not os.path.exists(tasks_file):
        return False
    # tasks_file exist return true
    return True

# adds a task to the task file and returns the task id.
def add_task(desc, priority):
    pass

# returns list of tasks in the task file.
def get_all_tasks():
    if is_tasks_file_exists():
        # Only read all the lines as list
        # and return them if it exists
        with open(tasks_file, 'r') as f:
            f.readline() # Skip the first line header
            return f.readlines()
    else:
        return ""

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
