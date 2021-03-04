threads = 2
tasks = [2,7,4,6,8]

while len(tasks) > 0:
    for idx in range(0,threads):
        if tasks[idx] <= 0:
            tasks.remove(tasks[idx])
        elif tasks[idx] > 0
            temp = tasks[idx]-1
            if temp <= 0:
                print("remove 0...")
            else:
            tasks.remove(tasks[idx])
            tasks.insert(0,temp)







        print(f"{temp}")
