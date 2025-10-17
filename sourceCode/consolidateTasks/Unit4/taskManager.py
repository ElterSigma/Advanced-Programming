# Create a task management system

# Able to create a new task which contains a name, date of creation, and
# due date

# Able to edit the previously mentioned information of the task

# Able to delete the task

#Variables
currentTasks = [["task1", "11/10", "13/10"]]
newTask = []
taskSelect = 0
editTask = 0
newItem = ""

userSelect = int(input("Please select and option: \n1. Create Task\n2. Edit Task\n3. Delete Task\n4. View Tasks\n"))

# Create a new task    
if userSelect == 1:
    # User enters the name, when the task is created, and when the task is
    # meant to be completed
    # This information is then added to the list 'newTask' 
    newTask.append(input("Enter the task name:\n"))
    newTask.append(input("Enter the date of creation:\n"))
    newTask.append(input("Enter the due date:\n"))
    
    # The newly updated 'newTask' will then be added to 'currentTasks'
    currentTasks.append(newTask)
    print("Task created successfuly!")
    print(currentTasks)

# Edit an existing task
elif userSelect == 2:
    print(currentTasks)
    taskSelect = int(input("Select which task to edit:\n"))
    if taskSelect >= len(currentTasks):
        print("Error!")
        
    else:
        newTask = currentTasks[taskSelect]
        print(newTask)
        editTask = int(input("Select which item to edit:\n"))
        if editTask >= len(newTask):
            print("Error!")
        
        else:
            newItem = input("Enter the new information:\n")
            newTask[editTask] = newItem
            currentTasks[taskSelect] = newTask
            print("Task edited successfuly!")
            print(currentTasks)
    

# Delete a task    
elif userSelect == 3:
    print(currentTasks)
    taskSelect = int(input("Select which task to delete:\n"))
    if taskSelect >= len(currentTasks):
        print("Error!")
    
    else:
        currentTasks.pop(taskSelect)
        print("Task deleted successfuly!")
        print(currentTasks)

# View a task
elif userSelect == 4:
    print(currentTasks)

else:
    print("Error! Invalid option!")