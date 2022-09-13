# import utils.commands here
from utils import commands

# parse the command line arguments and execute the appropriate commands.
def parseArgs(args):
    if len(args) == 1:
        return "Missing Required argument. Type -h to seek help"
    
    adding_task = False
    removing_task = False
    searching = False
    descending = False
    
    i = 1 # Skip the file name    
    while i < len(args):
        arg = args[i]
        
        if arg == "-h" or arg == "--help":
            commands.showhelp()
            break
        elif arg == "-l" or arg == "--list":
            return commands.list_all_tasks_cmd()
        elif arg == "-a" or arg == "--add":
            # adding task, the next couple arguments
            # there should be at least 3 arguments after
            # the description, -p/--priority, PRIORITY
            # Otherwise print error
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

            # At this point if there are any more options
            # print error
            if i + 4 < len(args):
                return "Error: Found extraneous options"

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
            removing_task = True
            pass
        elif arg == "-c" or arg == "--complete":
            # Sets the task to be complete and print
            # 'Task <Number> completed' if not found still print
            # 'Task <Number> completed'
            # Takes in one integer parameter that is required
            pass 
        elif arg == "-cp" or arg == "--changepriority":
            # Takes in two parameter 
            # TNUM is the task ID
            # PNUM is the priority
            # 'Priority of task <TNUM> could not be changed' if priority ! > 0 or task not found
            # 'Changed priority of task <TNUM> to <PNUM>' otherwise
            pass
        elif arg == "-u" or arg == "--update":
            # Takes in two parameter
            # NUMBER which is the task ID
            # DESCRIPTION is the string
            # 'Task <NUMBER> updated' if updated and description is not empty
            # 'Failed to update task <NUMBER>'  otherwise
            pass
        elif arg == "-s" or arg == "--search":
            # Takes in one parameter 
            # CRITERA must either be ID or DESCRIPTION or PRIORITY
            # At least one search criteria must be present
            # Combination is allowed. 
            # DESCRIPTION search should be case-insensitive
            # Ignore additional arguments after
            pass
        elif arg == "-t" or arg == "--sort":
            # Show the sorted list by increasing order of priority
            # The task shown must be in the form of 
            # ID,DESCRIPTION,PRIORITY,STATUS
            # Print 'Error: Found extraneous options' if more than 2
            # arguments are added
            pass
        elif arg == "-d" or arg == "--desc":
            # Must be used with -t to specify descending
            descending = True
        elif arg == "-i" or arg == "--id":
            # Must be used with -s for search task with ID
            pass
        elif arg == "-dp" or arg == "--description":
            # Must be used with -s for search task with description
            pass
        
        i += 1