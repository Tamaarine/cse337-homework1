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
            commands.list_all_tasks_cmd()
        elif arg == "-a" or arg == "--add":
            adding_task = True
            commands.add_task_cmd()
        elif arg == "-p" or arg == "--priority":
            # Must be used with options -a or -s
            # If it is with -a, then it is updating the priority
            # with -s it is searching by priority
            pass
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