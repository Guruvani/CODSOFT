#CodSoft Task 1 - To Do List 
#Code for the command line TO Do List

#Source Code :-
print("To-Do List ")
def show():
    print("--------------")
    print("1. Display To do list")
    print("2. Add task")
    print("3. Delete task")
    print("4. Update task")
    print("5. Exit")
    print()
    
#global removed_task
    
def view_list(tasks):
    if not tasks:
        print("List is empty.")
    else:
        print("\n The To Do List:")
        for sno , tasks in enumerate(tasks,1):
            print(f"{sno}.{tasks}") 

def add_tasks(tasks):
    task=input("Enter the new task : ")
    tasks.append(task)
    print(f'"{task}" has been added to the list')
    

def remove_tasks(tasks):
    if not tasks:
        print("Nothing to delete . The List is empty.")
        return
    view_list(tasks)
    task_num=int(input("Enter the no. of task to remove : "))
    if 1 <= task_num <=len(tasks):
        removed_task = tasks.pop(task_num -1)
        print(removed_task,"has been removed")
    else:
        print("Invalid task number")
        
def update_task(tasks):
    if not tasks:
        print("Nothing to update")
        return
    view_list(tasks)
    task_num=int(input("Enter the no. of task to update : "))
    if 1 <= task_num <= len(tasks):
        updated_task=input("Enter the updation to be done : ")
        tasks[task_num -1]=updated_task
        print(f'Task {task_num} has been updated to "{updated_task}"')
    else:
        print("Invalid task number.")      

          
def main():
    tasks=[]
    while True:
        show()
        choice=input("Choose an option from 1 to 5 : ")
        
        if choice == '1':
            view_list(tasks)
        elif choice == '2':
            add_tasks(tasks)
        elif choice == '3':
            remove_tasks(tasks)
        elif choice == '4':
            update_task(tasks)
        elif choice == '5':
            print("EXIT")
            exit()
        else:
            print("Invalid Number")
            
if __name__ == "__main__":
    main()