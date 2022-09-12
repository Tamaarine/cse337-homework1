import os

tasks_file = os.path.join(os.getcwd(), 'part2','db', 'tasks.csv')
header = 'ID,DESCRIPTION,PRIORITY,STATUS\n'

def parse_tasks_file(tasks):
    '''
    This function will parse the given parameter called
    tasks, which is just the return value from
    manager.get_all_tasks() -> It return the raw lines
    from the tasks.csv file and process it line by line.
    
    The headers are skipped when it is passed into tasks.
    The tasks might be an empty array, in that case 
    an empty dictionary is returned.
    
    Dictionary format is
    {
        ID: {'DESCRIPTION': <>, 'PRIORITY': <>, 'STATUS': <>},
        ...
    }
    
    Returns the dictionary parsed.
    '''
    dict_task = {}
    
    # Go through each task line, strip '\n' from the end
    # then split it by ',' and store it into dictionary
    for task in tasks:
        task = task.strip('\n')
        splitted = task.split(',')
        ID = int(splitted[0])
        dict_task[ID] = {
            'DESCRIPTION': splitted[1],
            'PRIORITY': splitted[2],
            'STATUS': splitted[3]
            }
    return dict_task
    
def is_empty_dict(dict):
    return len(dict) == 0

def write_back(dict_task):
    '''
    Function that takes in dict_task and write to the
    file. 
    '''
    with open(tasks_file, 'w') as f:
        f.write(header)
        for id in dict_task:
            current_task = dict_task[id]
            description = current_task['DESCRIPTION']
            priority = current_task['PRIORITY']
            status = current_task['STATUS']
            f.write(f"{id},{description},{priority},{status}\n")

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
    '''
    Add a task with the specified parameter. Create the tasks.csv
    if it doesn't exist already. 
    
    After creating it or exist. Append to the file the specified tasks.
    
    Return the task ID that the task was added. 
    
    '''
    
    # Get the parsed dictionary
    dict_task = parse_tasks_file(get_all_tasks())
    
    if is_empty_dict(dict_task):
        # dict_task is empty, assign 1 as its starting id
        new_id = 1
    else:
        # dict_task is not empty, pick up where we left off
        last_id = sorted(dict_task.keys())[-1]
        new_id = last_id + 1
    
    # Add in the new task with last_id + 1 as id
    with open(tasks_file, 'a') as f:
        f.write(f"{new_id},{desc},{priority},Incomplete\n")
    
    return new_id

# returns list of tasks in the task file.
def get_all_tasks():
    '''
    This function actuallys open up the file.
    Skip the header of the tasks.csv file.
    Read all the rest of the line by calling readlines
    and return the list of lines read.
    
    If the file doesn't exist create it.
    
    Return either [] or list of lines read
    
    '''
    create()
    
    # Read all the lines as list
    with open(tasks_file, 'r') as f:
        f.readline() # Skip the first line header
        return f.readlines()

# remove a task from the task file.
def remove_task(id):
    '''
    Return true if the id was successfully removed from tasks.csv
    
    Return false if the id doesn't exist in tasks.csv
    '''
    
    dict_task = parse_tasks_file(get_all_tasks())
    
    if id in dict_task:
        # Perform the replacement
        # i.e. 
        # {1: {x}, 2: {y}, 3: {z}, 4:{a}}, removing 2
        # start at key 2, the object it points to will be z
        # {1: {x}, 2:{z}, 3:{z}, 4:{a}}. then at key 3, be key 4
        # {1: {x}, 2:{z}, 3:{a}, 4:{a}}. then you stop at last key, remove it
        # {1: {x}, 2:{z}, 3:{a}}. Key 2: {y} is removed everything shifted
        # goes from [id, len(keys))
        for i in range(id, len(dict_task.keys())):
            dict_task[i] = dict_task[i + 1]
        
        # Delete last key
        del dict_task[len(dict_task)]
        
        # Then we perform the writeback to the file
        write_back(dict_task)
        
        return True
    else:
        # id doesn't exist
        return False
        

# complete a task in the task file.
def complete_task(id):
    '''
    Return true if the task <id> is set to complete.
    
    Return false if the task <id> doesn't exist
    '''
    
    dict_task = parse_tasks_file(get_all_tasks())
    
    if id in dict_task:
        dict_task[id]['STATUS'] = 'Complete'
        
        # Do the write back
        write_back(dict_task)
        
        return True
    else:
        # id doesn't exist bro
        return False
    

# change the priority of a task in the task file.
def change_priority(id, priority):
    '''
    Return true if the priority of the task is changed.
    
    Return false if the task <id> doesn't exist
    '''
    
    dict_task = parse_tasks_file(get_all_tasks())
    
    if id in dict_task:
        dict_task[id]['PRIORITY'] = priority
        
        # write back
        write_back(dict_task)
        
        return True
    else:
        # id doesn't exist man
        return False

# update the task description of a task in the task file.
def update_desc(id, desc):
    '''
    Return true if the description of the task is updated.
    
    Return false if the task <id> doesn't exist
    '''
    
    dict_task = parse_tasks_file(get_all_tasks())
    
    if id in dict_task:
        dict_task[id]['DESCRIPTION'] = desc
        
        # write it back yo
        write_back(dict_task)
        
        return True
    else:
        # id doesn't exist!
        return False

# search for a task in the task file.
def search(id, desc, priority):
    '''
    Return a string.
    
    A string of all the tasks that satisfied requirements in the format
    'id,description,priority,status\nid,description,priority,status\n...'
    
    OR 
    
    '' if no matching task
    '''
    
    dict_task = parse_tasks_file(get_all_tasks())
    
    # If id is specified there can only be max of 1 result
    if id != None:
        # Shorter syntax to find the task in dict_task
        # returns a list of dictionary
        ret_dict = [dict_task[key] for key in dict_task if key == id]
        
        # Make sure there is at least one result in it
        if ret_dict == []:
            return ""
        
        ret_dict = ret_dict[-1]        
        w_desc = ret_dict['DESCRIPTION']
        w_priority = int(ret_dict['PRIORITY']) # The only one that's int
        w_status = ret_dict['STATUS']
        w_formatted = f"{id},{w_desc},{w_priority},{w_status}\n"
        
        # Both search are present, need to check both
        if desc != None and priority != None:
            if w_desc.lower() == desc.lower() and \
                w_priority == priority:
                return w_formatted
            return ""
        elif desc != None:
            if w_desc.lower() == desc.lower():
                return w_formatted
            return ""
        elif priority != None:
            if w_priority == priority:
                return w_formatted
            return ""
        else:
            return w_formatted
    else:
        # id is not specified. Either description or priority
        # Take advantage of '' in 'anything' = True to take
        # care of the case that desc == None
        
        result_dict = {}
        
        # Filter through the original dict_task by desc
        # if desc isn't None. Otherwise, result_dict is the original
        # dictionary
        if desc != None:
            temp = {}
            
            desc = desc.lower()
            for key in dict_task:
                task = dict_task[key]
                if task['DESCRIPTION'].lower() == desc:
                    temp[key] = task    
            result_dict = temp
        else:
            result_dict = dict_task
        
        # Then filter through priority if priority isn't None
        # if desc was None. result_dict will be dict_task
        # meaning all tasks are in result_dict and will
        # be filtered by priority.
        # Doing this way is much more concise
        if priority != None:
            temp = {}
            
            for key in result_dict:
                task = result_dict[key]
                if int(task['PRIORITY']) == priority:
                    temp[key] = task    
            result_dict = temp

        ret = ""
        for key in result_dict:
            result = result_dict[key]
            r_desc = result['DESCRIPTION']
            r_priority = result['PRIORITY']
            r_status = result['STATUS']
            ret += f"{key},{r_desc},{r_priority},{r_status}\n"
        return ret

# sort the tasks in the task file. Default order is 1.
def sort(order=1):
    '''
    Sort the tasks in dict_task. The default order is 1
    which meanas to sort it ascendingly. 
    
    2 means to sort it descendingly 
    '''
    
    dict_task = parse_tasks_file(get_all_tasks())
    
    # The way we are going to do it is flatten out the dictionary
    # into a list basically, and just have to call sorted ez
    
    # The list of lists returned is in the form
    # [[id, desc, priority, status], ...]
    flatten_task = [[key, dict_task[key]['DESCRIPTION'], \
        dict_task[key]['PRIORITY'], dict_task[key]['STATUS']] \
        for key in dict_task]
    
    if order == 1:
        flatten_task.sort(key=lambda x : x[2]) 
    else:
        flatten_task.sort(key=lambda x : x[2], reverse=True) 
    
    ret = ""
    for task in flatten_task:
        ret += f"{task[0]},{task[1]},{task[2]},{task[3]}\n"    
        
    return ret