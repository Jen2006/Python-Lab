
tasks=[]

def add_task(task_no,description,priority):
 task={
  "discription":description,
  "priority":priority,
  "status":"incomplete"
  }
 tasks[task_no]=task

def remove_task():
  index=int(input("Enter the Index of the task to be removed"))
  tasks.pop(index)

def update_desc():
  index=int(input("Enter the index"))
  desc=input("Enter the description")
  
  

