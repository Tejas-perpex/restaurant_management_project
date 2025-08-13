# Simple Task Queue Simulation using Python Lists

import time

# Queue to store tasks
task_queue = []

# Enqueue function (add task)
def enqueue(task):
    task_queue.append(task)
    print(f"Task added: {task}")

# Dequeue function (process and remove task)
def dequeue():
    if task_queue:
        task = task_queue.pop(0)  # FIFO: remove first task
        print(f"Processing task: {task}")
        time.sleep(1)  # Simulate task processing time
        print(f"Task completed: {task}")
    else:
        print("No tasks in the queue.")

# Peek function (view next task without removing)
def peek():
    if task_queue:
        print(f"Next task to process: {task_queue[0]}")
    else:
        print("No tasks in the queue.")

# Simulation
enqueue("Send Welcome Email")
enqueue("Generate Report")
enqueue("Backup Database")

peek()

dequeue()
dequeue()
dequeue()
dequeue()  # Trying to dequeue from empty queue
