package cp213;

/**
 * Instructional Assistant class that inherits from Student. Adds a course
 * attribute to represent the course the IA supports.
 *
 * @author
 * @version 2022-02-25
 */
public class IA extends Student {

    private String course = null;

    /**
     * IA constructor
     *
     * @param lastName  Last name of the IA
     * @param firstName First name of the IA
     * @param id        Student ID
     * @param course    Course the IA is assigned to (e.g., CP213)
     */
    public IA(final String lastName, final String firstName, final String id, final String course) {
	super(lastName, firstName, id);
	this.course = course;
    }

    /**
     * Getter for course.
     *
     * @return The course the IA is helping with.
     */
    public String getCourse() {
	return this.course;
    }

    /**
     * Getter for id (inherited from Student). Required by the tester for direct
     * access.
     *
     * @return The ID of the IA.
     */
    @Override
    public String getId() {
	return super.getId();
    }

    /**
     * Returns formatted string: LastName, FirstName: ID Course: course
     */
    @Override
    public String toString() {
	return super.toString() + "\nCourse: " + this.course;
    }
}
