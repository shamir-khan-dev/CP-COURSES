package cp213;

import java.time.LocalDate;

/**
 * Student class definition.
 *
 * @author your name here
 * @version 2022-01-17
 */
public class Student implements Comparable<Student> {

    // Attributes
    private LocalDate birthDate = null;
    private String forename = "";
    private int id = 0;
    private String surname = "";

    /**
     * Instantiates a Student object.
     *
     * @param id        student ID number
     * @param surname   student surname
     * @param forename  name of forename
     * @param birthDate birthDate in 'YYYY-MM-DD' format
     */
    public Student( /* parameters here */ int id, String surname, String forename, LocalDate birthDate) {

	// assign attributes here

	this.id = id;
	this.surname = surname;
	this.forename = forename;
	this.birthDate = birthDate;

	return;
    }

    /**
     * Gets the student ID.
     * 
     * @return the student's ID number
     */
    public int getId() {
	return this.id;
    }

    /**
     * Sets the student ID.
     * 
     * @param id the student's ID number
     */
    public void setId(final int id) {
	this.id = id;
    }

    /**
     * Gets the student's surname.
     * 
     * @return the student's surname
     */
    public String getSurname() {
	return this.surname;
    }

    /**
     * Sets the student's surname.
     * 
     * @param surname the student's surname
     */
    public void setSurname(final String surname) {
	this.surname = surname;
    }

    /**
     * Gets the student's forename.
     * 
     * @return the student's forename
     */
    public String getForename() {
	return this.forename;
    }

    /**
     * Sets the student's forename.
     * 
     * @param forename the student's forename
     */
    public void setForename(final String forename) {
	this.forename = forename;
    }

    /**
     * Gets the student's birth date.
     * 
     * @return the student's birth date
     */
    public LocalDate getBirthDate() {
	return this.birthDate;
    }

    /**
     * Sets the student's birth date.
     * 
     * @param birthDate the student's birth date
     */
    public void setBirthDate(final LocalDate birthDate) {
	this.birthDate = birthDate;
    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Object#toString() Creates a formatted string of student data.
     */
    @Override

    public String toString() {
	String string = "";

	// your code here

	return String.format("Name:      %s, %s\nID:        %d\nBirthdate: %s", this.surname, this.forename, this.id,
		this.birthDate);

    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Comparable#compareTo(java.lang.Object)
     */
    @Override
    public int compareTo(final Student target) {

	// your code here

	int result = this.surname.compareTo(target.surname);

	if (result == 0) {
	    result = this.forename.compareTo(target.forename);
	}

	if (result == 0) {
	    result = Integer.compare(this.id, target.id);
	}

	return result;

    }

    // getters and setters defined here

}
