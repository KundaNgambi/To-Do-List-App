

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

            headers = reader.fieldnames
            print(" | ".join(headers))
            print("-" * 50)

            with open('To do list.csv','r',newline = "") as file:
                reader = csv.DictReader(file)
                for index, row in enumerate(reader,start = 1):
                    print(f'{index}. {row["Date"]}: {row["Task"]}, {row["Status"]}, {row["Priority"]}:')
        break

view_todo_list()

def add_tasks():

    print("\nAdding tasks...\n")
    writer = csv.writer(open('To do list.csv','a',newline = ""))

    while True:
        task = input('Enter task(or "done to finish"): ')
        if task == 'done':
            break

        date = input('Enter date(mm/dd/yyyy):')
        status = input('Enter status:')
        priority = input('Enter priority:')

        writer.writerow([date, task, status, priority])

add_tasks()

print("\n Task Added Successfully\n")



def display_tasks():

    with open('To do list.csv','r',newline = "") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

display_tasks()