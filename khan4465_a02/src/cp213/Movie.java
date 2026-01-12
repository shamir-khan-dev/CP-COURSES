package cp213;

import java.io.PrintStream;

/**
 * Movie class definition.
 *
 * @author your name, id, email
 * @version 2025-10-18
 */
public class Movie implements Comparable<Movie> {

    // Constants
    public static final int FIRST_YEAR = 1888;
    public static final String[] GENRES = { "science fiction", "fantasy", "drama", "romance", "comedy", "zombie",
	    "action", "historical", "horror", "war", "mystery" };
    public static final double MAX_RATING = 10.0;
    public static final double MIN_RATING = 0.0;

    public static String genresMenu() {
	StringBuilder menu = new StringBuilder();
	for (int i = 0; i < GENRES.length; i++) {
	    menu.append(String.format("%2d: %s%n", i, GENRES[i]));
	}
	return menu.toString();
    }

    // Attributes
    private String director = "";
    private int genre = -1;
    private double rating = 0;
    private String title = "";
    private int year = 0;

    public Movie(final String title, final int year, final String director, final double rating, final int genre) {
	this.title = title;
	this.year = year;
	this.director = director;
	this.rating = rating;
	this.genre = genre;
    }

    public Movie(Movie source) {
	this.title = source.title;
	this.year = source.year;
	this.director = source.director;
	this.rating = source.rating;
	this.genre = source.genre;
    }

    @Override
    public int compareTo(final Movie target) {
	int result = this.title.compareToIgnoreCase(target.title);
	if (result == 0) {
	    result = Integer.compare(this.year, target.year);
	}
	return result;
    }

    public String genreToName() {
	return GENRES[this.genre];
    }

    public String getDirector() {
	return this.director;
    }

    public int getGenre() {
	return this.genre;
    }

    public double getRating() {
	return this.rating;
    }

    public String getTitle() {
	return this.title;
    }

    public int getYear() {
	return this.year;
    }

    public String key() {
	return String.format("%s, %d", this.title, this.year);
    }

    public void setRating(final double rating) {
	this.rating = rating;
    }

    @Override
    public String toString() {
	return String.format("Title:    %s%nYear:     %d%nDirector: %s%nRating:   %.1f%nGenre:    %s", this.title,
		this.year, this.director, this.rating, this.genreToName());
    }

    public void write(final PrintStream ps) {
	ps.printf("%s|%d|%s|%.1f|%d%n", this.title, this.year, this.director, this.rating, this.genre);
    }
}
