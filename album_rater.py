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
# Will create this when each function is working

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


# Edit album in dictionary


# Delete album from dictionary


# Rate album


# Reccomends albums with the same genre



# Main routine
if __name__ == "__main__":
    # Accesses the album dictionary
    album_dict = album_dictionary()


    # Adds an album using add album function
    # Appends the string input to dictionary
    title, artist, genre = add_album()
    album_dict[count] = {"Title":title, "Artist":artist, "Genre":genre, "Rating":""}

    # Uses basic dictionary print to print the albums
    print_dictionary_basic(album_dict)
