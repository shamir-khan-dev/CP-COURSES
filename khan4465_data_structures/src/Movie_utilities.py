"""
-------------------------------------------------------
Movie class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 B
__updated__ = "2021-01-12"
-------------------------------------------------------
"""
from Movie import Movie
from pickle import FALSE



def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """
    print("Enter the details for a new movie:")

    # Title
    title = input("Title: ").strip()

    # Year of Release
    while True:
        try:
            year = int(input("Year of release: ").strip())
            if year < Movie.FIRST_YEAR:
                print(f"Error: Year must be >= {Movie.FIRST_YEAR}")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid year.")

    # Director
    director = input("Director: ").strip()

    # Rating
    while True:
        try:
            rating = float(input("Rating (0 to 10): ").strip())
            if rating < Movie.MIN_RATING or rating > Movie.MAX_RATING:
                print(f"Error: Rating must be between {Movie.MIN_RATING} and {Movie.MAX_RATING}.")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid rating.")

    # Genres
    genres = []
    print(f"\nGenres:\n{Movie.genres_menu()}")
    while True:
        user_input = input("Enter a genre number (ENTER to quit): ").strip()

        if user_input == "":
            if len(genres) == 0:
                print("Error: At least one genre must be selected.")
            else:
                break
        elif not user_input.isdigit():
            print("Error: Please enter a valid number.")
        else:
            genre_number = int(user_input)
            if genre_number < 0 or genre_number >= len(Movie.GENRES):
                print(f"Error: Please select a number between 0 and {len(Movie.GENRES) - 1}.")
            elif genre_number in genres:
                print("Error: Genre already selected.")
            else:
                genres.append(genre_number)

    genres.sort()

    # Create the Movie object
    movie = Movie(title, year, director, rating, genres)
    return movie



def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """
    # Split the line into components using the delimiter '|'
    parts = line.strip().split('|')
    
    # Extract components
    title = parts[0]
    year = int(parts[1])
    director = parts[2]
    rating = float(parts[3])
    
    genre_codes = parts[4].split(',')  # Assuming genres are comma-separated

    # Create and return a Movie object
    movie = (title, year, director, rating, genre_codes)
    return movie



def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """

    # Your code here

    return movies


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """
    genres = []
    max_genre_number = len(Movie.GENRES)  # Dynamically determine the max genre index

    print(f"Genres:\n{Movie.genres_menu()}")  # Display the genres menu

    while True:
        user_choice = input("Enter a genre number (ENTER to quit): ").strip()

        if user_choice == "":
            if len(genres) == 0:
                print("Error: must have at least one genre")
            else:
                break  # Quit if the user has selected at least one genre

        elif not user_choice.isdigit():
            print("Error: not a positive number")

        else:
            user_choice = int(user_choice)  # Convert input to an integer

            if user_choice < 0 or user_choice >= max_genre_number:
                print(f"Error: input must be between 0 and {max_genre_number - 1}")
            elif user_choice in genres:
                print("Error: genre already chosen")
            else:
                genres.append(user_choice)

    genres.sort()  # Sort genres before returning
    return genres


def write_movies( movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    The original list of movies must be unchanged.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is
            year (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    
    ymovies = []
    
    for x in range(len(movies)):
        if(movies[x].year == year):
            ymovies.append(movies[x])
    

    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    The original list of movies must be unchanged.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    
    rmovies = []
    
    for x in range(len(movies)):
        if(movies[x].rating >= rating):
            rmovies.append(movies[x])
    

    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    The original list of movies must be unchanged.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes
            genre (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    gmovies = []
    
    for x in range(len(movies)):
        for y in range(len(movies[x].genres)):
            if(movies[x].genres[y] == genre):
                gmovies.append(movies[x]) 

    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    The original list of movies must be unchanged.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """
    gmovies = []  
    for x in range(len(movies)):
        li = []  
        for y in range(len(genres)):
            for z in range(len(movies[x].genres)):
                if genres[y] == movies[x].genres[z]:
                    li.append(genres[y])  
        
        if len(li) == len(genres):
            gmovies.append(movies[x])
    
    return gmovies

def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    The original list of movies must be unchanged.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """

    # Your code here
    
    count = []
    
    for x in range(len(movies)):
        for y in range(len(movies[x].genres)):
            if(Movie.GENRES[movies[x].genres[y]] in Movie.GENRES):
                count.append(movies[x].genres[y])
    return count
