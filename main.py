import users
import sys

def main():
    print("Hello, please select an option below by typing the corresponding number and pressing ENTER\n")
    print("1) Create New User")
    print("2) Load User")
    print("3) Exit")
    user_input = input()

    if user_input == "1":
        name_check = None

        while name_check != "1":
            print("What is your name? (Type your name and press ENTER)")
            user_name = input()
            print(f"Is {user_name} correct? Type 1 for YES and 2 for NO")
            name_check = input()

            if name_check == "1":
                user_profile = users.User(user_name, {}, {}, {}, {}, {}, {}, {})
                profile_menu(user_profile)

    elif user_input == "2":
        pass

    elif user_input == "3":
        exit_program()
        

def profile_menu(user_profile):
    print("Please select an option below by typing the corresponding number and pressing ENTER\n")
    user_input = None
    print("1) Add Book")
    print("2) Add Movie")
    print("3) Add TV Show Season")
    print("4) Add Video Game")
    print("5) Add Event")
    print("6) View Finished Goals")
    print("7) View Card Collection")
    print("8) Edit User")
    print("9) Exit")

    while user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4" and user_input != "5" and user_input != "6" and user_input != "7" and user_input != "8" and user_input != "9":
        user_input = input()

    if user_input == "1":
        add_book_form(user_profile)
    elif user_input == "2":
        add_movie_form(user_profile)
    
def add_book_form(user_profile):
    print("Please select an option below by typing the corresponding number and pressing ENTER\n")
    print("1) Add Book Details")
    print("2) Go Back to Previous Menu")

    user_input = None

    while user_input != "1" and user_input != "2":
        user_input = input()

    if user_input == "1":
        print("Please add the relevant information below next to each field and press ENTER\n")
        title = input("Book Title: ")
        author = input("Author: ")
        int_check = 0
        while int_check == 0:
            try:
                page_count = int(input("Page Count (numbers only): "))
            except:
                print("Integers only please.")

            else:
                int_check = 1
        year = input("Year Published: ")
        date_finished = input("Date Finished (month/day/4-digit year): ")
        hours = int(input("Approximate Hours Read Before Completion (numbers only): "))
        rating = input("Rating (1-5, 5 being best): ")
        user_profile.add_book(title, author, page_count, year, date_finished, hours, rating)
        users.User.add_book()

    elif user_input == "2":
        profile_menu()

def add_movie_form(user_profile):
    print("Please select an option below by typing the corresponding number and pressing ENTER\n")
    print("1) Add Movie Details")
    print("2) Go Back to Previous Menu")

    user_input = None

    while user_input != "1" and user_input != "2":
        user_input = input()

    if user_input == "1":
        print("Please add the relevant information below next to each field and press ENTER\n")
        title = input("Movie Title: ")
        director = input("Director: ")
        year = input("Year Published: ")
        date_finished = input("Date Finished (month/day/4-digit year): ")
        runtime = input("Runtime (mins): ")
        rating = input("Rating (1-5, 5 being best): ")

        user_profile.add_movie(title, director, year, date_finished, runtime, rating)

    elif user_input == "2":
        profile_menu()

    
def exit_program():
    print("Are you sure you want to exit? Type 1 for YES and 2 for NO")
    exit_check = input()

    if exit_check == "1":
        sys.exit()
    else:
        main()


if __name__ == "__main__":
    main()