def marks(avg):
    if avg >= 90:
        return "Grade A"
    elif avg >= 75:
        return "Grade B"
    elif avg >= 50:
        return "Grade C"
    else:
        return "Grade F"

def get_mark(subject):
    while True:
        try:
            score = float(input(f"Enter marks for {subject}: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid response in the marks entered. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("(*_______Student Grade Calculator_______*)\n")
    maths = get_mark("Maths")
    physics = get_mark("Physics")
    chem = get_mark("Chemistry")
    bio = get_mark("Biology")
    german = get_mark("German")
    
    total = maths + physics + chem + bio + german
    avg = total / 5
    grade = marks(avg)
    print("*____________________________________________*\n")
    print("The Total Marks Are:", total)
    print("You Have Aquired:", grade)
    print("The Average Marks are:", avg)
    print("*____________________________________________*")
main()