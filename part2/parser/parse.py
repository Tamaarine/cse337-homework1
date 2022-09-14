# import utils.commands here
from utils import commands

# parse the command line arguments and execute the appropriate commands.
def parseArgs(args):
    if len(args) == 1:
        return "Missing Required argument. Type -h to seek help"
    
    i = 1 # Skip the file name    
    while i < len(args):
        arg = args[i]
        
        if arg == "-h" or arg == "--help":
            commands.showhelp()
            break
        elif arg == "-l" or arg == "--list":
            # Why is this one just not commands.manager.get_all_tasks()???
            tasks = commands.manager.get_all_tasks()
            dict_task = commands.manager.parse_tasks_file(tasks)
            
            ret = ""
            for key, val in dict_task.items(): 
                desc = val['DESCRIPTION']
                priority = val['PRIORITY']
                status = val['STATUS']
                ret += f"{key},{desc},{priority},{status}\n"
            
            return ret            
        elif arg == "-a" or arg == "--add":
            # adding task, the next couple arguments
            # there should be at least 3 arguments after
            # the description, -p/--priority, PRIORITY
            # Otherwise print error
            if i + 4 < len(args):
                return "Error: Found extraneous options"
                
            if i + 1 < len(args):    
                desc = args[i + 1]
            else:
                return "Error: Description not provided"
            
            if i + 2 >= len(args):
                # The -p flag doesn't exist
                return "Error: Incorrect priority option"
            
            if args[i + 2] != "-p" and args[i + 2] != "--priority":
                return "Error: Incorrect priority option"
            
            # -p/--priority exist, now checking the parameter
            if i + 3 >= len(args):
                return "Error: Cannot add a task with empty priority"
            
            # Try to parse it if it doesn't work return error
            try:
                priority = int(args[i + 3])
            except ValueError:
                return "Priority must be integer"

            # Reach here means everything is good
            # desc is "" or more, priority is an integer call it 
            # no extraneous options           
            return commands.add_task_cmd(desc, priority)
        elif arg == "-r" or arg == "--remove":
            # If task exists, remove it. print "Removed task ID"
            # otherwise print "Failed to remove task ID"
            # The parameter that this argument takes in must be 
            # an integer. Print "Task ID missing" if it isn't present
            # if additional argument print "Found extraneous options"
            if i + 2 < len(args):
                return "Error: Found extraneous options"
                
            if i + 1 >= len(args):
                return "Task ID missing"
            
            try:
                id = int(args[i + 1])
            except ValueError:
                return "Task ID must be a number"
            
            # If we reach here, id is a number
            # no extraneous options, everything gucci
            return commands.remove_task_cmd(id)
        elif arg == "-c" or arg == "--complete":
            # Sets the task to be complete and print
            # 'Task <Number> completed' if not found still print
            # 'Task <Number> completed'
            # Takes in one integer parameter that is required
            if i + 2 < len(args):
                return "Error: Found extraneous options"
                
            if i + 1 >= len(args):
                return "Task ID missing"
            
            try:
                id = int(args[i + 1])
            except ValueError:
                return "Task ID must be a number"
            
            # Reached here everything gucci
            return commands.complete_task_cmd(id)
        elif arg == "-cp" or arg == "--changepriority":
            # Takes in two parameter 
            # TNUM is the task ID
            # PNUM is the priority
            # 'Priority of task <TNUM> could not be changed' if priority ! > 0 or task not found
            # 'Changed priority of task <TNUM> to <PNUM>' otherwise
            if i + 3 < len(args):
                return "Error: Found extraneous options"
           
            if i + 1 >= len(args):
                # TNUM
                return "Task ID or priority missing"
            
            try:
                id = int(args[i + 1])
            except ValueError:
                return "Task ID must be a number"
            
            if i + 2 >= len(args):
                # PNUM
                return "Task ID or priority missing"
            
            try:
                priority = int(args[i + 2])
            except ValueError:
                return "Task ID must be a number"
            
            return commands.change_priority_cmd(id, priority)
        elif arg == "-u" or arg == "--update":
            # Takes in two parameter
            # NUMBER which is the task ID
            # DESCRIPTION is the string
            # 'Task <NUMBER> updated' if updated and description is not empty
            # 'Failed to update task <NUMBER>'  otherwise
            if i + 3 < len(args):
                return "Error: Found extraneous options"
            
            if i + 1 >= len(args):
                return "Task ID or description missing"
            
            try:
                id = int(args[i + 1])
            except ValueError:
                return "Task ID must be a number"
                
            if i + 2 >= len(args):
                return "Task ID or description missing"
            
            desc = args[i + 2]
            
            return commands.update_cmd(id, desc)
        elif arg == "-s" or arg == "--search":
            # Takes in one parameter 
            # CRITERA must either be ID or DESCRIPTION or PRIORITY
            # At least one search criteria must be present
            # Combination is allowed. 
            # DESCRIPTION search should be case-insensitive
            # Ignore additional arguments after
            id = None
            desc = None
            priority = None
            
            if i + 1 >= len(args):
                return "Search Criteria Missing"
            
            # Look at only subset, maximum of             
            temp_i = 0
            rel_args = args[i + 1: i + 7]
            len_rel_args = len(rel_args)
            
            while temp_i < len_rel_args:
                temp_arg = rel_args[temp_i]
                
                if temp_arg == "-i" or temp_arg == "--id":
                    if temp_i + 1 < len_rel_args:
                        id = rel_args[temp_i + 1]
                        temp_i += 1 
                    else:
                        return "Error: Empty id to search"                
                elif temp_arg == "-dp" or temp_arg == "--description":
                    if temp_i + 1 < len_rel_args:
                        desc = rel_args[temp_i + 1]
                        temp_i += 1
                    else:
                        return "Error: Empty description to search"
                elif temp_arg == "-p" or temp_arg == "--priority":
                    if temp_i + 1 < len_rel_args:
                        priority = rel_args[temp_i + 1]
                        temp_i += 1
                    else:
                        return "Error: Empty priority to search"
                else:
                    # Encounter an invalid arg done going through it 
                    break
                temp_i += 1
            
            try:
                if id is not None:
                    id = int(id)
                if priority is not None:
                    priority = int(priority)
            except ValueError:
                return "search ID and priority must be integer."    
            
            return commands.search_cmd(id, desc, priority)
        elif arg == "-t" or arg == "--sort":
            # Show the sorted list by increasing order of priority
            # The task shown must be in the form of 
            # ID,DESCRIPTION,PRIORITY,STATUS
            # Print 'Error: Found extraneous options' if more than 2
            # arguments are added
            if i + 2 < len(args):
                return "Error: Found extraneous options"
            
            order = ""
            if i + 1 < len(args):
                # Check if -d exists
                if args[i + 1] == "-d" or args[i + 1] == "--desc":
                    order = "-d"
            
            return commands.sort_cmd(order)
        
        i += 1