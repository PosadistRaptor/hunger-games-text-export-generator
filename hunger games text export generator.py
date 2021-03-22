while True:
    try:
        team_size = int(input("Team size: "))
        break
    except ValueError:
        print("Cast size must be in integers")
while True:
    try:
        total_district = int(input("Total district : "))
        break
    except ValueError:
        print("Total district must be in integers")

print(f"There's a total amount of {team_size * total_district} participants with {team_size} members for each"
      f" {total_district} districts")

with open("HG cast.txt.txt", "w") as hunger_games:
    hunger_games.write("The Hunger Games\nhttps://brantsteele.com/extras/hungergames/01/logo.png\n\n")

i = 1
while i <= total_district:
    with open("HG cast.txt", "a") as hunger_games:
        hunger_games.write(f"\nDistrict {i}\n#ffffff 0 0\n\n")
        i += 1
    for cast in range(team_size):
        name = input("\nName : ")
        gender = input("Gender (M/F): ").strip()
        while gender.lower() != "m" and gender.lower() != "f":
            print("You have to input M or F")
            gender = input("Gender (M/F): ").strip()
        if gender.lower() == "m":
            gender = 1
        elif gender.lower() == "f":
            gender = 0
        image_link = input("Image link: ").strip()
        with open("HG cast.txt", "a") as hunger_games:
            hunger_games.write(f"""{name}
{name}
{gender}
{image_link}
BW

""")
