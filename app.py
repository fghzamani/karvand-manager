import json
import os


DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "karvands.json")
REPORT_FILE = os.path.join(DATA_DIR, "report.json")
INITIAL_DATA = {
    "bootcamp": {
        "name": "Karvand Bootcamp"
    },
    "karvands": []
}


def load_data():
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(DATA_FILE):
        save_data(INITIAL_DATA)
        return {"bootcamp": dict(INITIAL_DATA["bootcamp"]), "karvands": []}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        print("The JSON file is empty or invalid. Starting with empty data.")
        save_data(INITIAL_DATA)
        return {"bootcamp": dict(INITIAL_DATA["bootcamp"]), "karvands": []}

    if not isinstance(data, dict) or not isinstance(data.get("karvands"), list):
        print("The JSON structure is invalid. Starting with empty data.")
        save_data(INITIAL_DATA)
        return {"bootcamp": dict(INITIAL_DATA["bootcamp"]), "karvands": []}

    return data


def save_data(data):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def find_karvand(karvands, karvand_id):
    return next(
        (karvand for karvand in karvands if karvand["id"] == karvand_id),
        None
    )


def add_karvand():
    data = load_data()
    karvands = data["karvands"]

    if karvands:
        karvand_id = max(karvand["id"] for karvand in karvands) + 1
    else:
        karvand_id = 1

    name = input("Enter the Karvand's full name: ").strip()
    email = input("Enter the Karvand's email: ").strip()
    city = input("Enter the Karvand's city: ").strip()
    education = input("Enter the Karvand's latest education: ").strip()
    field_of_study = input("Enter the Karvand's field of study: ").strip()
    skills = []

    while True:
        skill_name = input(
            "Enter the Karvand's skill or 'done' to finish: "
        ).strip()
        if skill_name.lower() == "done":
            break
        if not skill_name:
            print("Skill name cannot be empty.")
            continue

        skill_level = input(
            "Enter the skill level (beginner, intermediate, advanced): "
        ).strip().lower()
        if skill_level not in {"beginner", "intermediate", "advanced"}:
            print("Invalid skill level.")
            continue

        skill_point = input("Enter the skill point (0-100): ").strip()
        if not skill_point.isdigit() or not 0 <= int(skill_point) <= 100:
            print("Invalid skill point. Enter a number between 0 and 100.")
            continue

        skills.append({
            "name": skill_name,
            "level": skill_level,
            "point": int(skill_point)
        })

    karvands.append({
        "id": karvand_id,
        "name": name,
        "email": email,
        "city": city,
        "education": education,
        "field_of_study": field_of_study,
        "skills": skills
    })
    save_data(data)
    print("Karvand added successfully!")


def print_karvand(karvand):
    print(f"ID: {karvand['id']}")
    print(f"Name: {karvand['name']}")
    print(f"Email: {karvand['email']}")
    print(f"City: {karvand['city']}")
    print(f"Education: {karvand['education']}")
    print(f"Field of study: {karvand['field_of_study']}")
    print("Skills:")
    for skill in karvand["skills"]:
        print(
            f"  - {skill['name']} "
            f"(Level: {skill['level']}, Point: {skill['point']})"
        )


def show_all_karvands():
    data = load_data()
    if not data["karvands"]:
        print("No Karvands found.")
        return

    for karvand in data["karvands"]:
        print_karvand(karvand)
        print()


def get_id(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("The ID must be a number.")
        return None


def search_karvand_by_id(karvand_id):
    data = load_data()
    karvand = find_karvand(data["karvands"], karvand_id)
    if karvand is None:
        print("Karvand not found.")
        return
    print_karvand(karvand)


def search_karvand_by_skill(skill_name):
    data = load_data()
    skill_name = skill_name.strip().lower()
    found = [
        karvand for karvand in data["karvands"]
        if any(
            skill["name"].strip().lower() == skill_name
            for skill in karvand["skills"]
        )
    ]

    if not found:
        print("No Karvands found with the specified skill.")
        return
    for karvand in found:
        print_karvand(karvand)
        print()


def edit_karvand(karvand_id):
    data = load_data()
    karvand = find_karvand(data["karvands"], karvand_id)
    if karvand is None:
        print("Karvand not found.")
        return

    print("Leave a field blank to keep its current value.")
    for field, label in (
        ("name", "Name"),
        ("email", "Email"),
        ("city", "City"),
        ("education", "Education"),
        ("field_of_study", "Field of study")
    ):
        value = input(f"{label} [{karvand[field]}]: ").strip()
        if value:
            karvand[field] = value

    save_data(data)
    print("Karvand information updated successfully!")


def delete_karvand(karvand_id):
    data = load_data()
    karvand = find_karvand(data["karvands"], karvand_id)
    if karvand is None:
        print("Karvand not found.")
        return

    data["karvands"].remove(karvand)
    save_data(data)
    print("Karvand deleted successfully!")


def generate_report():
    data = load_data()
    karvands = data["karvands"]
    if not karvands:
        print("No Karvands found.")
        return

    skills = [
        skill for karvand in karvands for skill in karvand["skills"]
    ]
    unique_skills = list({
        skill["name"].strip().lower(): skill["name"].strip()
        for skill in skills
    }.values())
    report = {
        "total_karvands": len(karvands),
        "total_skills": len(skills),
        "average_skill_score": (
            sum(skill["point"] for skill in skills) / len(skills)
            if skills else 0
        ),
        "cities": list(dict.fromkeys(karvand["city"] for karvand in karvands)),
        "unique_skills": unique_skills
    }

    print(json.dumps(report, indent=4, ensure_ascii=False))
    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)


while True:
    print("\nWelcome to Karvand Manager!")
    print("1. Add a new Karvand")
    print("2. Show all Karvands")
    print("3. Search for a Karvand with ID")
    print("4. Search for a Karvand based on skill")
    print("5. Edit a Karvand's information")
    print("6. Delete a Karvand")
    print("7. Report")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")
    if choice == "1":
        add_karvand()
    elif choice == "2":
        show_all_karvands()
    elif choice == "3":
        karvand_id = get_id("Enter the Karvand's ID to search: ")
        if karvand_id is not None:
            search_karvand_by_id(karvand_id)
    elif choice == "4":
        search_karvand_by_skill(input("Enter the skill to search for: "))
    elif choice == "5":
        karvand_id = get_id("Enter the Karvand's ID to edit: ")
        if karvand_id is not None:
            edit_karvand(karvand_id)
    elif choice == "6":
        karvand_id = get_id("Enter the Karvand's ID to delete: ")
        if karvand_id is not None:
            delete_karvand(karvand_id)
    elif choice == "7":
        generate_report()
    elif choice == "8":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
