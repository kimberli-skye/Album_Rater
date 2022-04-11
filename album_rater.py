#
# album_rater.py
#
# Allows user to add, delete, and rate albums
# Recommends albums based off of genre
#
# KJ
# 08/04 to


# Functions

# Menu that allows the user to access each function when needed
def menu():
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

        #Try and except else and finally.
        else:
            if mode in [0, 1, 2, 3, 4, 5]:
                return mode
                break
            
            else:
                print("Not valid number, enter another.")

# Function that manages the album dictionary
def album_dictionary():
    """ Dictionary of chosen albums (not user entered).
        Returns the dictionary (with a mix of integers and strings).
    """
    albums = {1:{"Title":"Be More Chill", "Artist":"Original Cast of Be More Chill", "Genre":"Musical", "Rating":""},
                      2:{"Title":"Electra Heart", "Artist":"MARINA", "Genre":"Pop", "Rating":""},
                      3:{"Title":"Eye of the Storm", "Artist":"Watt White", "Genre":"Rock", "Rating":""},
        }

    return albums


# Prints album dictionary (basic)
def print_dictionary_basic(dictionary):
    """ Accepts a Dictionary and loops through it.
        Prints the keys and values (Album and its differnet values).
    """
    for ID, album in dictionary.items():
        print("Album: {} \nArtist: {} \nGenre: {} \nRating: {}\n".format(album["Title"], album["Artist"],
                                                                                                                album["Genre"], album["Rating"]))


# Adds album to dictionary
def add_album():
    # Add album title
    title = input("What is the title of the album? ")
    # Add album Artist
    artist = input("What is the artist of the album? ")
    # Add album Genre
    genre = input("What is the genre of the album? ")

    return title, artist, genre


# Allows user to choose an album
# Prints the number needed to choose an album
# Checks if the ID number is valid
# Returns the integer if it is
def choose_album(album_dict):
    for ID, album in album_dict.items():
        print("Enter {} to choose the album {}".format(ID, album["Title"]))

    chosen_ID = int(input(""))

    for ID in album_dict:
        if chosen_ID == ID:
            return chosen_ID
        


# Edit album in dictionary


# Delete album from dictionary


# Rate album


# Reccomends albums with the same genre



# Main routine
if __name__ == "__main__":
    # Accesses the album dictionary
    album_dict = album_dictionary()

    # Sets the prgram running top True
    running =  True
    while running:

        # Gets a chosen mode
        chosen_mode = menu()

        if chosen_mode == 1:
            # Adds an album using add album function
            # Appends the string input to dictionary
            title, artist, genre = add_album()
            album_dict[4] = {"Title":title, "Artist":artist, "Genre":genre, "Rating":""}

        elif chosen_mode == 2:
            print(choose_album(album_dict))

        elif chosen_mode == 3:
            skip

        elif chosen_mode == 4:
            skip

        elif chosen_mode == 5:
            skip

        else:
            # Uses basic dictionary print to print the albums
            print_dictionary_basic(album_dict)


