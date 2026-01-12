package cp213;

import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Utilities for working with Movie objects.
 *
 * @author your name, id, email here
 * @version 2025-10-18
 */
public class MovieUtilities {

    public static int[] genreCounts(final ArrayList<Movie> movies) {
	int[] counts = new int[Movie.GENRES.length];
	for (Movie m : movies) {
	    int g = m.getGenre();
	    if (g >= 0 && g < Movie.GENRES.length) {
		counts[g]++;
	    }
	}
	return counts;
    }

    public static Movie getMovie(final Scanner keyboard) {
	System.out.print("Title: ");
	String title = keyboard.nextLine();

	System.out.print("Year: ");
	int year = keyboard.nextInt();
	keyboard.nextLine(); // consume newline

	System.out.print("Director: ");
	String director = keyboard.nextLine();

	System.out.print("Rating: ");
	double rating = keyboard.nextDouble();
	keyboard.nextLine(); // consume newline

	System.out.println("Genres:");
	System.out.print(Movie.genresMenu());

	System.out.print("Enter a genre number: ");
	int genre = keyboard.nextInt();
	keyboard.nextLine(); // consume newline

	return new Movie(title, year, director, rating, genre);
    }

    public static ArrayList<Movie> getByGenre(final ArrayList<Movie> movies, final int genre) {
	ArrayList<Movie> result = new ArrayList<>();
	for (Movie m : movies) {
	    if (m.getGenre() == genre) {
		result.add(m);
	    }
	}
	return result;
    }

    public static ArrayList<Movie> getByRating(final ArrayList<Movie> movies, final double rating) {
	ArrayList<Movie> result = new ArrayList<>();
	for (Movie m : movies) {
	    if (m.getRating() >= rating) {
		result.add(m);
	    }
	}
	return result;
    }

    public static ArrayList<Movie> getByYear(final ArrayList<Movie> movies, final int year) {
	ArrayList<Movie> result = new ArrayList<>();
	for (Movie m : movies) {
	    if (m.getYear() == year) {
		result.add(m);
	    }
	}
	return result;
    }

    public static int readGenre(final Scanner keyboard) {
	int genre = -1;
	boolean valid = false;
	while (!valid) {
	    System.out.println("Genres:");
	    System.out.print(Movie.genresMenu());
	    System.out.print("Enter a genre number: ");
	    if (keyboard.hasNextInt()) {
		genre = keyboard.nextInt();
		keyboard.nextLine(); // consume newline
		if (genre >= 0 && genre < Movie.GENRES.length) {
		    valid = true;
		} else {
		    System.out.println("Invalid genre number. Try again.");
		}
	    } else {
		System.out.println("Invalid input. Please enter a number.");
		keyboard.nextLine(); // discard invalid input
	    }
	}
	return genre;
    }

    public static Movie readMovie(final String line) {
	String[] parts = line.split("\\|");
	String title = parts[0];
	int year = Integer.parseInt(parts[1]);
	String director = parts[2];
	double rating = Double.parseDouble(parts[3]);
	int genre = Integer.parseInt(parts[4]);
	return new Movie(title, year, director, rating, genre);
    }

    public static ArrayList<Movie> readMovies(final Scanner fileIn) {
	ArrayList<Movie> movies = new ArrayList<>();
	while (fileIn.hasNextLine()) {
	    String line = fileIn.nextLine();
	    Movie m = readMovie(line);
	    movies.add(m);
	}
	return movies;
    }

    public static void writeMovies(final ArrayList<Movie> movies, PrintStream ps) {
	for (Movie m : movies) {
	    m.write(ps);
	}
    }
}
