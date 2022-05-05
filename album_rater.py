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

    # Loops through while loop until a mode is chosen
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
    albums = {1:{"Title":"Be More Chill", "Artist":"Original Cast of Be More Chill", "Genre":"Musical", "Rating":"No Rating"},
                      2:{"Title":"Happy", "Artist":"Original Cast of Be More Chill", "Genre":"Pop", "Rating":"No Rating"},
                      3:{"Title":"Mastermind", "Artist":"Original Cast of Be More Chill", "Genre":"R&B", "Rating":"No Rating"}}
    return albums


def print_dictionary_basic(dictionary):
    """ Accepts a Dictionary and loops through it.
         Prints the keys and values (Album and its differnet values).
    """
    for ID, album in dictionary.items():
        print("Album: {} \nArtist: {} \nGenre: {} \nRating: {}\n".format(album["Title"], album["Artist"],
                                                                                                                album["Genre"], album["Rating"]))


def choose_album(album_dict):
    """ Prints the number needed to choose an album.
         Checks if the ID number is valid and returns it.
    """
    for ID, album in album_dict.items():
        print("Enter {} to choose the album {}".format(ID, album["Title"]))


    # For loop to check the chosen ID is an actual one
    chosen_id = int(input(""))
    for ID in album_dict:
        if chosen_id == ID:
            return chosen_id


def add_album():
    """ Gets user input for each value.
         Returns the different strings and count.
    """
    title = input("What is the title of the album?: ").title()
    artist = input("What is the artist of the album? ").title()
    genre = input("What is the genre of the album? ").title()

    return title, artist, genre


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
    # Uses choose album function to choose an album to rate
    for ID, album in album_dictionary.items():
        album_name = album["Title"]

    # Asks user to rate album from 1-5
    rating = int(input("Rate the album '{}' from 1 - 5: ".format(album_name)))
    
    # Checks if rating is expected
    if rating > 5 or rating < 1:
        print("Your rating must be from 1 - 5, try again")

    else:
        # Returns rating
        return rating


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
                print("  - Since you liked", album["Title"], "listen to", rec_album, "\n")
            else:
               matching_genre = False



# Main routine
if __name__ == "__main__":
    album_dict = album_dictionary()     # Accesses the album dictionary

    # Defines constants
    count = 0

    # Creates while loop
    running =  True
    while running:

        chosen_mode = menu()     # Gets a chosen mode

        # Adds an album using add album function
        # Appends the string input to dictionary
        if chosen_mode == 1:
            title, artist, genre = add_album()
            album_dict[count] = {"Title":title, "Artist":artist, "Genre":genre, "Rating":"No rating"}
            count = count + 1

        # Gets a chosen album
        # Goes to edit album function
        elif chosen_mode == 2:
            chosen_album = choose_album(album_dict)
            edit_album(album_dict, chosen_album)

        # Gets a chosen album
        # Calls delete_album function
        elif chosen_mode == 3:
            chosen_album = choose_album(album_dict)
            delete_album(album_dict, chosen_album)

        # Gets a chosen album
        # Calls rate_albums function
        # Adds rating to dictionary
        elif chosen_mode == 4:
            chosen_album = choose_album(album_dict)
            album_rating = rate_albums(album_dict, chosen_album)

            for ID, album in album_dict.items():
                if ID == chosen_album:
                    album["Rating"] = album_rating
                else:
                    rated_album = False
            

        elif chosen_mode == 5:
            album_recs = album_reccomendations()
            reccomend_albums(album_dict, album_recs)

        else:
            # Uses basic dictionary print to print the albums
            print_dictionary_basic(album_dict)


