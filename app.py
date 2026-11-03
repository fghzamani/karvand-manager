import os
import json


if not os.path.exists("data"):
    os.makedirs("data")

with open("data/karvands.json", "w") as file:
    json.dump({}, file, indent=4)



def add_karvand():
    with open("data/karvands.json", "r") as file:
        karvands = json.load(file)

    karvand_id = int(input("Enter the Karvand's ID: "))
    if karvand_id in karvands:
        print("A Karvand with this ID already exists.")
        return

    name = input("Enter the Karvand's full name: ")
    email = input("Enter the Karvand's email: ")
    city = input("Enter the Karvand's city: ")
    education = input("Enter the Karvand's latest education: ")
    skills = []
    while True:

        skill = input("Enter the Karvand's skill or 'done' to finish: ").strip()
        if skill == "done":
            break
        if skill:
            skill_level = input("Enter the skill level (beginner, intermediate, advanced): ").strip().lower()
            if skill_level not in ["beginner", "intermediate", "advanced"]:
                print("Invalid skill level. Please enter 'beginner', 'intermediate', or 'advanced'.")
                continue
            skill_point = input("Enter the skill point (0-100): ").strip()
            if not skill_point.isdigit() or not (0 <= int(skill_point) <= 100):
                print("Invalid skill point. Please enter a number between 0 and 100.")
                continue
            skill = {"name": skill, "level": skill_level, "point": int(skill_point)}
            skills.append(skill)

    karvands[karvand_id] = {"name": name, "skills": skills, "email": email, "city": city, "education": education}

    with open("data/karvands.json", "w") as file:
        json.dump(karvands, file, indent=4)

    print("Karvand added successfully!")

def show_all_karvands():
    with open("data/karvands.json", "r") as file:
        karvands = json.load(file)

    if not karvands:
        print("No Karvands found.")
        return

    for karvand_id, karvand_info in karvands.items():
        print(f"ID: {karvand_id}")
        print(f"Name: {karvand_info['name']}")
        print(f"Email: {karvand_info['email']}")
        print(f"City: {karvand_info['city']}")
        print(f"Education: {karvand_info['education']}")
        print("Skills:")
        for skill in karvand_info["skills"]:
            print(f"  - {skill['name']} (Level: {skill['level']}, Point: {skill['point']})")
        print()

def search_karvand_by_id(karvand_id):
    with open("data/karvands.json", "r") as file:
        karvands = json.load(file)

    if str(karvand_id) in karvands:
        karvand_info = karvands[str(karvand_id)]
        print(f"ID: {karvand_id}")
        print(f"Name: {karvand_info['name']}")
        print(f"Email: {karvand_info['email']}")
        print(f"City: {karvand_info['city']}")
        print(f"Education: {karvand_info['education']}")
        print("Skills:")
        for skill in karvand_info["skills"]:
            print(f"  - {skill['name']} (Level: {skill['level']}, Point: {skill['point']})")
    else:
        print("Karvand not found.")

RUNNING = True
while RUNNING:
    print("\nWelcome to Karvand Manager!")
    print("1. Add a new Karvand")
    print("2. Show all Karvands")
    print("3. Search for a Karvand with id")
    print("4. Search for a Karvand based on skill")
    print("5.Edit a  karvand's information")
    print("6. Delete a karvand")
    print("7. Report")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        add_karvand()

    elif choice == "2":
        show_all_karvands()

    elif choice == "3":
        search_id = int(input("Enter the Karvand's ID to search: "))
        search_karvand_by_id(search_id)

    elif choice == "4":
        RUNNING = False
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please try again.")