while True:
    try:
        cast_size = int(input("Cast size: "))
        break
    except ValueError:
        print("Cast size must be in integers")
while True:
    try:
        district_size = int(input("District size: "))
        break
    except ValueError:
        print("District size must be in integers")
        
print(f"There's a total amount of {cast_size*district_size} participants with {cast_size} members for each"
      f" {district_size} districts") 

with open("HG cast.txt.txt", "w") as hunger_games:
    hunger_games.write("The Hunger Games\nhttps://brantsteele.com/extras/hungergames/01/logo.png\n\n")
    
district = 1
while district <= district_size:
    with open("HG cast.txt", "a") as hunger_games:
        hunger_games.write(f"\nDistrict {district}\n#ffffff 0 0\n\n")
        district += 1
    for cast in range(cast_size):
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
