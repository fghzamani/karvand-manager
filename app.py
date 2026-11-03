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


def search_karvand_by_skill(skill_name):
    with open("data/karvands.json", "r") as file:
        karvands = json.load(file)

    found_karvands = []
    for karvand_id, karvand_info in karvands.items():
        for skill in karvand_info["skills"]:
            if skill["name"].lower() == skill_name.lower():
                found_karvands.append((karvand_id, karvand_info))
                break

    if not found_karvands:
        print("No Karvands found with the specified skill.")
        return

    for karvand_id, karvand_info in found_karvands:
        print(f"ID: {karvand_id}")
        print(f"Name: {karvand_info['name']}")
        print(f"Email: {karvand_info['email']}")
        print(f"City: {karvand_info['city']}")
        print(f"Education: {karvand_info['education']}")
        print("Skills:")
        for skill in karvand_info["skills"]:
            print(f"  - {skill['name']} (Level: {skill['level']}, Point: {skill['point']})")
        print()


def edit_karvand(karvand_id):
    with open("data/karvands.json", "r") as file:
        karvands = json.load(file)

    if str(karvand_id) not in karvands:
        print("Karvand not found.")
        return

    karvand_info = karvands[str(karvand_id)]

    print("Enter new information (leave blank to keep current value):")
    name = input(f"Name [{karvand_info['name']}]: ").strip() or karvand_info['name']
    email = input(f"Email [{karvand_info['email']}]: ").strip() or karvand_info['email']
    city = input(f"City [{karvand_info['city']}]: ").strip() or karvand_info['city']
    education = input(
        f"Education [{karvand_info['education']}]: "
    ).strip() or karvand_info['education']

    skills = []
    while True:
        skill_name = input("Enter a skill name (or 'done' to finish): ").strip()
        if not skill_name:
            print("Skill name cannot be empty.")
            continue
        if skill_name.lower() == 'done':
            break
        skill_level = input("Enter the skill level (beginner, intermediate, advanced): ").strip().lower()
        skill_point = input("Enter the skill point (0-100): ").strip()
        if not skill_point.isdigit() or not (0 <= int(skill_point) <= 100):
            print("Invalid skill point. Please enter a number between 0 and 100.")
            continue
        skills.append({"name": skill_name, "level": skill_level, "point": int(skill_point)})

    karvands[str(karvand_id)] = {
        "name": name,
        "email": email,
        "city": city,
        "education": education,
        "skills": skills if skills else karvand_info["skills"]
    }

    with open("data/karvands.json", "w") as file:
        json.dump(karvands, file, indent=4)

    print("Karvand information updated successfully!")


def delete_karvand(karvand_id):
    with open("data/karvands.json", "r") as file:
        karvands = json.load(file)

    if str(karvand_id) not in karvands:
        print("Karvand not found.")
        return

    del karvands[str(karvand_id)]

    with open("data/karvands.json", "w") as file:
        json.dump(karvands, file, indent=4)

    print("Karvand deleted successfully!")


def generate_report():
    with open("data/karvands.json", "r") as file:
        karvands = json.load(file)

    if not karvands:
        print("No Karvands found.")
        return

    total_karvands = len(karvands)
    total_skills = sum(len(karvand_info["skills"]) for karvand_info in karvands.values())
    average_skills_points = sum(skill["point"] for karvand_info in karvands.values() for skill in karvand_info["skills"]) / total_skills if total_skills > 0 else 0
    city_distribution = {}
    for karvand_info in karvands.values():
        city = karvand_info["city"]
        city_distribution[city] = city_distribution.get(city, 0) + 1

    skill_karvand_counts = {}
    skill_names = {}
    for karvand_info in karvands.values():
        skills_of_karvand = set()
        for skill in karvand_info["skills"]:
            skill_key = skill["name"].strip().lower()
            if skill_key not in skills_of_karvand:
                skills_of_karvand.add(skill_key)
                skill_karvand_counts[skill_key] = (
                    skill_karvand_counts.get(skill_key, 0) + 1
                )
                skill_names[skill_key] = skill["name"].strip()

    unique_skills = [
        skill_names[skill_key]
        for skill_key, count in skill_karvand_counts.items()
        if count == 1
    ]

    print(f"Total Karvands: {total_karvands}")
    print(f"Total Skills: {total_skills}")
    print(f"Skills belonging to only one Karvand: {unique_skills}")
    print(f"Average Skills Points: {average_skills_points:.2f}")
    print(f"City Distribution: {city_distribution}")
    results = {"total_karvands": total_karvands, "total_skills": total_skills, "unique_skills": unique_skills, "average_skills_points": average_skills_points, "cities": city_distribution}
    with open("data/report.json", "w") as file:
        json.dump(results, file, indent=4)


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
        sarch_skill = input("Enter the skill to search for: ").strip().lower()
        search_karvand_by_skill(sarch_skill)

    elif choice == "5":
        edit_id = int(input("Enter the Karvand's ID to edit: "))
        edit_karvand(edit_id)
    elif choice == "6":
        delete_id = int(input("Enter the Karvand's ID to delete: "))
        delete_karvand(delete_id)
    elif choice == "7":
        generate_report()
    elif choice == "8":
        print("Exiting the program. Goodbye!")
        RUNNING = False
    else:
        print("Invalid choice. Please try again.")