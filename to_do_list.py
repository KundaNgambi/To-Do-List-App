

import csv
import os

def setup():
    if not os.path.exists('To do list.csv'):
        with open('To do list.csv','w',newline = "") as file:

            fieldnames = ['Date','Task', 'Status', 'Priority']
            writer = csv.DictWriter(file,fieldnames = fieldnames)
            writer.writeheader()
setup()


def view_todo_list():

    while True:
        view = input('Would you like to view the to do list?(y/n):').lower()
        if view == 'n':
            break
        elif view == 'y':
            print("\nTo do list:\n")

            with open('To do list.csv', 'r', newline="") as file:
                reader = csv.DictReader(file)

                print(f"{'No.':<4} {'Date':<12} {'Task':<25} {'Status':<12} {'Priority':<10}")
                print("-" * 70)

                for index, row in enumerate(reader, start=1):
                    print(f"{index:<4} "
                          f"{row['Date']:<12} "
                          f"{row['Task']:<25} "
                          f"{row['Status']:<12} "
                          f"{row['Priority']:<10}")
        break

view_todo_list()

def add_tasks():

    print("\nAdding tasks...\n")
    writer = csv.writer(open('To do list.csv','a',newline = ""))

    while True:
        task = input('Enter task(or "done to finish"): ')
        if task == 'done':
            return

        date = input('Enter date(mm/dd/yyyy):')
        status = input('Enter status:')
        priority = input('Enter priority:')

        writer.writerow([date, task, status, priority])

        print("\n Task Added Successfully\n")

add_tasks()



def delete_task():

    filename = 'To do list.csv'

    with open(filename, 'r', newline="") as file:
        reader = csv.DictReader(file)
        tasks = list(reader)

    if not tasks:
        print("No tasks to delete.")
        return
    while True:
        delete = input("Would you like to delete a task?(y/n): ").lower()

        if delete != 'y':
            return

        print("\nTo do list:\n")
        print(f"{'No.':<4} {'Task':<25} {'Status':<12} {'Priority':<10}")
        print("-" * 60)
        for index, task in enumerate(tasks, start=1):
            print(f"{index:<4} {task['Task']:<25} {task['Status']:<12} {task['Priority']:<10}")

        try:
            choice = int(input("\nEnter task number to delete: "))

            if 1 <= choice <= len(tasks):
                deleted = tasks.pop(choice - 1)
                print(f"Deleted: {deleted['Task']}")
            else:
                print("Invalid number.")
                return

        except ValueError:
            print("Please enter a valid number.")
            return

        with open(filename, 'w', newline="") as file:
            fieldnames = ['Date', 'Task', 'Status', 'Priority']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(tasks)

delete_task()