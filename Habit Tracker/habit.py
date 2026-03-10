import json
from pathlib import Path
import datetime

habits = []
storage =  Path("habit.json")

def load_habit(storage):

    if not storage.exists():
        return[]
    try:
        with open(storage, 'r') as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError:
        return []

def save_habits(habits):
    with open (storage, 'w') as f:
        json.dump(habits, f, indent=4)

def new_habit(habits):
    
    name = input("Enter Habit Name: ").capitalize()
    description = input("Enter Description: ").capitalize()
    date = str(datetime.date.today().strftime("%d-%m-%Y"))
    habits_no = len(habits) + 1

    habits.append({
        "Habit No" : habits_no,
        "Name" : name,
        "Description" : description,
        "Date" : date,
        "Complete" : "No"
    })

def mark_habit(habits):
    check = input("Habit Name to Mark as Complete: ").capitalize()

    found = False

    for habit in habits:
        if check ==  habit["Name"]:
            habit["Complete"] = "Yes"
            print(f"Habit '{check}' mark as Completed")
            found = True
            break

    if not found:
        print("No habit for this Name")

def view_all_habits():

    with open (storage, 'r') as f:
        content = f.read().strip()

        if not content:
            print("No Habits Yet!")
            return
        
        data = json.loads(content)

        print(json.dumps(data, indent=4))

def view_today_progress(habits):
    total = 0
    complete = 0

    today_date = str(datetime.date.today().strftime("%d-%m-%Y"))

    print("---------------------")
    print("Toady Habits")
    print("---------------------")

    for habit in habits:

        if today_date == habit["Date"]:
            total += 1
            name = habit["Name"]
            status = habit["Complete"]
            print(f"{name} - {status}")
    
            if habit["Complete"] == "Yes":
                complete += 1
                
    print(f"Progress : {complete} / {total} completed")

def view_habit_statistics(habits):

    total = 0
    complete = 0
    imcomplete = 0

    for habit in habits:
        total += 1
        if habit["Complete"] == "Yes":
            complete += 1
        elif habit["Complete"] == "No":
            imcomplete += 1

    print("--------------------")
    print("Total Habits")
    print("--------------------")
    print(f"Total Habits: {total}")
    print(f"Complete Habits: {complete}")
    print(f"Incomplete Habits: {imcomplete}")

def del_habit(habits):
    user = input("Enter Habit Name to Delete: ")

    found = False

    for habit in habits:
        if user == habit["Name"]:
            habits.remove(habit)
            print(f"Habit {user} has been deleted")
            found = True
            break

    if not found:
        print("No Habit Found!")

def reset_journal():

    with open(storage , 'w') as f:
        f.write('[]')
        print("Journal has been Reset")

def main():
    habits = load_habit(storage)

    while True:
        print("---------------------------------")
        print("1: New Habit")
        print("2: Mark Habit")
        print("3: View Today Progress")
        print("4: View All Habits")
        print("5: View Habit Staistics")
        print("6: Delete Habit")
        print("6: Reset Journal")
        print("7: Exit")
        print("---------------------------------")

        try:
            user = int(input("Enter Num(1-7): "))

            if user == 1:
                new_habit(habits)
                save_habits(habits)

            elif user == 2:
                mark_habit(habits)
                save_habits(habits)

            elif user == 3:
                view_today_progress(habits)

            elif user == 4:
                view_all_habits()

            elif user == 5:
                view_habit_statistics(habits)

            elif user == 6:
                del_habit(habits)
                save_habits(habits)

            elif user == 7:
                reset_journal()

            else:
                print("GoodBye!")
                break
        except ValueError:
            print("Enter Number")

main()

