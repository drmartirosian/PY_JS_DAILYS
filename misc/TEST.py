tasks = [3,1,2,7]
threads = 2
counter = 0

def my_computer():
    global counter, tasks
    # print(tasks)
    while len(tasks) > 0:
        perform_tasks()
        remove_finished()
        # print(f'{tasks}=>{counter}')
    print(f"Tasks complete: {counter}")

def perform_tasks():
    global counter, tasks
    if len(tasks) > 1:
        counter += 1
        for task in range(threads):
            tasks[task] -= 1
    elif len(tasks) == 1:
        counter += 1
        for task in range(1):
            tasks[task] -= 1

def remove_finished():
    global counter, tasks
    while 0 in tasks:
        for task in tasks:
            if task <= 0:
                tasks.remove(0)

my_computer()




