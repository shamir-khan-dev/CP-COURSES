package cp213;

/**
 * Inherited class in simple example of inheritance / polymorphism.
 *
 * CAS stands for Contract Academic Staff and extends the Professor class,
 * adding a 'term' attribute representing the teaching term (e.g., "202109").
 * 
 * @author
 * @version 2022-02-25
 */
public class CAS extends Professor {

    private String term = null;

    /**
     * CAS constructor
     *
     * @param lastName   Last name of the CAS
     * @param firstName  First name of the CAS
     * @param department Department the CAS is in
     * @param term       Teaching term (e.g., "202109" for Fall 2021)
     */
    public CAS(final String lastName, final String firstName, final String department, final String term) {
	super(lastName, firstName, department);
	this.term = term;
    }

    /**
     * Getter for term.
     *
     * @return The term this CAS is teaching in
     */
    public String getTerm() {
	return this.term;
    }

    /**
     * Returns a formatted string for CAS: LastName, FirstName Department:
     * department Term: term
     */
    @Override
    public String toString() {
	return super.toString() + "\nTerm: " + this.term;
    }
}
