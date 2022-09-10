# import db/manager here.

def showhelp():
    print('usage: python main.py <options>')
    print('===== options =====')
    print('-h or --help to print this menu.')
    print('-l or --list to list all tasks.')
    print('-a or --add <DESCRIPTION> to add a new task')
    print('-p or --priority <NUMBER> to assign a priority to a new task. Must use with -a or -s.')
    print('-r or --remove <ID> remove a task.')
    print('-c or --complete <ID> mark a task as complete.')
    print('-cp or --changepriority <ID> <NUMBER> change an existing task\'s priority.')
    print('-u or --update <ID> <DESCRIPTION> update an existing task\'s description.')
    print('-s or --search <OPTIONS> search a task by options.')
    print('-t or --sort show sorted list of tasks by increasing order of priority.')
    print('-d or --desc decreasing order of priority. Must use with -t.')
    print('-i or --id <ID> task ID. Must use with -s for search task with ID.')
    print('-dp or --description <TEXT> task description. Must use with -s for search task with description.')

# command to list all tasks
def list_all_tasks_cmd():
    pass

# command to add a task
def add_task_cmd(task, priority):
    pass

# command to delete a task
def remove_task_cmd(id):
    pass

# command to complete a task
def complete_task_cmd(id):
    pass

# command to edit task priority
def change_priority_cmd(id, priority):
    pass

# command to edit task description
def update_cmd(id, desc):
    pass

# command to search a task by id, description, or priority
def search_cmd(id, desc, priority):
    pass

# command to sort the tasks in specified order
def sort_cmd(order):
    pass
