#
# album_rater.py
#
# Allows user to add, delete, and rate albums
# Recommends albums based off of genre
#
# KJ
# 08/04 to

# Functions
def menu():
    """ Prints menu that user can choose function from.
         Checks input is valid.
         Returns mode.
    """
    # Loops through while loop
    # Chooses mode
    # Uses try and except to overwrite value errors
    while True:
        try:
            mode = int(input("""\nChoose a mode:
            1: Enter a new album
            2: Edit albums
            3: Delete an album
            4: Rate an album
            5: Get an album reccomendation
            0: View albums
            """))

        except ValueError:
            print("Not a valid number, enter another.")

        # Try and except else and finally.
        # Checks mode is valid, returns mode
        else:
            if mode in [0, 1, 2, 3, 4, 5]:
                return mode
                break
            else:
                print("Not valid number, enter another.")


def album_dictionary():
    """ Dictionary of chosen albums (not user entered).
         Returns the dictionary (with a mix of integers and strings).
    """
    albums = {}
    return albums


def print_dictionary_basic(dictionary):
    """ Accepts a Dictionary and loops through it.
         Prints the keys and values (Album and its differnet values).
    """
    # For loop for each ID in the dictionary
    # Prints entire album in a simple format
    for ID, album in dictionary.items():
        print("Album: {} \nArtist: {} \nGenre: {} \nRating: {}\n".format(album["Title"], album["Artist"],
                                                                                                                album["Genre"], album["Rating"]))


def choose_album(album_dict):
    """ Prints the number needed to choose an album.
         Checks if the ID number is valid and returns it.
    """
    # For loop for each ID in the dictionary
    # Prints id and album in a simple format
    for ID, album in album_dict.items():
        print("Enter id: {} to choose the album {}".format(ID, album["Title"]))


    # While loop for user to add album id
    # Loops if ID is not valid
    # Uses a boolean value to control while loop
    entering_id = True
    while entering_id == True:
        try:
            chosen_id = int(input("\nEnter an album id: "))
            
        except ValueError:
            print("That is not a valid album id")

        else:
            # For loop to check the chosen ID is valid
            for ID in album_dict:
                if chosen_id == ID:
                    return chosen_id
                    entering_id = False


def add_album():
    """ Gets user input for each value.
         Checks input are valid.
         Returns the different strings and count.
    """
    # List of valid genres
    genre_list = ["Pop", "Musical", "Rock", "Jazz", "EDM", "Dubstep", "R&B",
                     "Country", "Indie Rock"]

    # While loop to check the user added a character
    # Boolean to control
    adding_album = True
    while adding_album == True:
        title = input("What is the title of the album?: ").title().strip()
        artist = input("What is the artist of the album? ").title().strip()
        genre = input("What is the genre of the album? ").title().strip()

        # Checks if any variables is blank
        if title == "" or artist == "" or genre== "":
            print("\nA blank space for either catagory is not valid, "
                      "please re-enter the album.\n")

        # Checks if the genre is valid
        elif genre not in genre_list:
            print("\nThat is not a valid genre, valid genres are: ")

            for genre in genre_list:    # Prints each genre in the genre list
                print(genre)

            print("Please re-enter the album.\n")

        # Else: returns variables and exits loop
        else:
            print("Album added")
            return title, artist, genre
            adding_album == False


def edit_album(album_dictionary, chosen_album):
    """ Calls the add_album function.
         replaces the original album with edited album.
    """
    print("Editing album:", album_dictionary[chosen_album])
    title, artist, genre = add_album()
    album_dict[chosen_album] = {"Title":title, "Artist":artist, "Genre":genre, "Rating":"No Rating"}


def delete_album(album_dictionary, chosen_album):
    """ Takes the user chosen album.
         Deletes it from the dictionary.
    """
    del album_dictionary[chosen_album]


# Rate album
def rate_albums(album_dictionary, chosen_album):
    """ Finds album name.
         Takes user input for rating.
         Loops if value error is encountereed.
         Checks rating is valid and returns integer.
    """
    # Uses choose album function to choose an album to rate
    for ID, album in album_dictionary.items():
        album_name = album["Title"]

    # While loop to check loop through rating
    # Boolean to control
    rating_album = True
    while rating_album:
        try:
            # Asks user to rate album from 1-5
            rating = int(input("Rate the album '{}' from 1 - 5: ".format(album_name)))
        
        except ValueError:
            print("That isn't a number")

        else:
            # Checks if rating is expected
            if rating > 5 or rating < 1:
                print("Your rating must be from 1 - 5, try again")

            else:
                # Returns rating
                return rating
                rating_album = False


# Dictionary of albums with susequent genres
def album_reccomendations():
    album_recs = {"Pop":"Glory Days - Little Mix",
                              "Musical":"The Trail to Oregon! - Team StarKid",
                              "Rock":"Nevermind - Nirvana",
                              "Jazz":"TROLLS soundtrack - Dreamworks Trolls",
                              "EDM":"Bangarang - Skrillex",
                              "Dubstep":"Untrue - Burial",
                              "R&B":"Back of My Mind - H.E.R.",
                              "Country":"Come On Over - Shania Twain",
                              "Indie Rock":"Scaled and Icy - Twenty One Pilot"}

    return album_recs


# Reccomends albums with the same genre
def reccomend_albums(album_dict, album_recs):
    print("Album reccomendations:")

    # Loops through two dictionarys to checks if genres match
    for ID, album in album_dict.items():
        for genre, rec_album in album_recs.items():
            if genre == album["Genre"]:
                print("  - Since you liked", album["Title"], "you should listen to", rec_album, "\n")
            else:
               matching_genre = False


def album_check(album_count, min_albums):
    """ Checks if there are any albums in dict.
         Returns boolean variable.
    """
    if album_count == min_albums:
        no_albums = True
    else:
        no_albums = False

    return no_albums
        


# Main routine
if __name__ == "__main__":
    album_dict = album_dictionary()     # Accesses the album dictionary

    # Defines constants
    album_count = 0
    min_albums = 0

    # Creates while loop
    running =  True
    while running:

        chosen_mode = menu()     # Gets a chosen mode

        if chosen_mode == 1:
            # Adds an album using add album function
            # Appends the string input to dictionary
            title, artist, genre = add_album()
            album_dict[album_count] = {"Title":title, "Artist":artist, "Genre":genre, "Rating":"No rating"}
            album_count = album_count + 1


        elif chosen_mode == 2:
            # Checks if there are any albums
            no_albums_check = album_check(album_count, min_albums)
            
            if no_albums_check == False:
                # Gets a chosen album
                # Goes to edit album function
                chosen_album = choose_album(album_dict)
                edit_album(album_dict, chosen_album)
                
            else:
                print("You have no albums")


        elif chosen_mode == 3:
            # Checks if there are any albums
            no_albums_check = album_check(album_count, min_albums)
            
            if no_albums_check == False:
                # Gets a chosen album
                # Calls delete_album function
                chosen_album = choose_album(album_dict)
                delete_album(album_dict, chosen_album)
                
            else:
                print("You have no albums")


        elif chosen_mode == 4:
            # Checks if there are any albums
            no_albums_check = album_check(album_count, min_albums)
            
            if no_albums_check == False:
                # Gets a chosen album
                # Calls rate_albums function
                # Adds rating to dictionary
                chosen_album = choose_album(album_dict)
                album_rating = rate_albums(album_dict, chosen_album)

                for ID, album in album_dict.items():
                    if ID == chosen_album:
                        album["Rating"] = album_rating
                
            else:
                print("You have no albums")
            

        elif chosen_mode == 5:
            # Checks if there are any albums
            no_albums_check = album_check(album_count, min_albums)
            
            if no_albums_check == False:
                # Reccomends albums with the same genre
                album_recs = album_reccomendations()
                reccomend_albums(album_dict, album_recs)
            else:
                # Uses basic dictionary print to print the albums
                print("You have no albums")
            

        else:
            # Checks if there are any albums
            no_albums_check = album_check(album_count, min_albums)
            if no_albums_check == False:
                print_dictionary_basic(album_dict)
            else:
                # Uses basic dictionary print to print the albums
                print("You have no albums")


