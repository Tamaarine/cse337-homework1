# import db/manager here.
from db import manager

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
    '''
    This function will return a STRING!
    If the task is empty, or task file isn't initialized
    return the string 'TODO List empty. Add some tasks.'
    
    Otherwise, it parses tasks.csv and generate a
    dictionary keyed by the ID by calling parse_tasks_file.
    The tasks parameter passed into it must contain some
    tasks.
    
    Return a string that's formatted as such
    'ID: <> DESC: <> PRIORITY: <> STATUS: <>\n
     ID: <> DESC: <> PRIORITY: <> STATUS: <>\n 
     ...'
    
    '''
    
    # Get the task from the db
    tasks = manager.get_all_tasks()
    
    # Task file isn't initialized or is empty
    if tasks == [] or tasks == None:
        return "TODO List empty. Add some tasks."
    
    # Call the parse_tasks_file from manager
    dict_task = manager.parse_tasks_file(tasks)
    
    ret = ""
    for id in dict_task:
        current_task = dict_task[id]
        ret += f"ID: {id} " \
               f"DESC: {current_task['DESCRIPTION']} " \
               f"PRIORITY: {current_task['PRIORITY']} " \
               f"STATUS: {current_task['STATUS']}\n"
    return ret
    
# command to add a task
def add_task_cmd(task, priority):
    if task == "" or priority <= 0:
        # Do not take in empty string or priority <= 0
        return "Failed to add task"
        
    # Valid arg add it 
    id = manager.add_task(task, priority)
    return f"Task added and assigned ID {id}"

# command to delete a task
def remove_task_cmd(id):
    ret = manager.remove_task(id)
    
    if ret:
        return f"Removed task ID {id}"
    return f"Failed to remove task ID {id}"    

# command to complete a task
def complete_task_cmd(id):
    ret = manager.complete_task(id)
    
    if ret:
        return f"Task {id} completed"
    return f"Task {id} could not be completed"        

# command to edit task priority
def change_priority_cmd(id, priority):
    if priority <= 0:
        # Priority <= 0 we do not change
        return f"Priority of task {id} could not be changed"
        
    ret = manager.change_priority(id, priority)
    
    if ret:
        return f"Changed priority of task {id} to {priority}"
    return f"Priority of task {id} could not be changed"
        

# command to edit task description
def update_cmd(id, desc):
    pass

# command to search a task by id, description, or priority
def search_cmd(id, desc, priority):
    pass

# command to sort the tasks in specified order
def sort_cmd(order):
    pass
