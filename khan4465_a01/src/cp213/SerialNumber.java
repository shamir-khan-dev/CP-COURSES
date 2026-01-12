package cp213;

import java.io.PrintStream;
import java.util.Scanner;

/**
 * @author Your name and id here
 * @version 2025-09-07
 */
public class SerialNumber {

    /**
     * Determines if a string contains all digits.
     *
     * @param string the string to test
     * @return {@code true} if {@code string} is all digits, {@code false} otherwise
     */
    public static boolean allDigits(final String string) {

	// your code here

	boolean con = true;

	for (int x = 0; x < string.length(); x++) {

	    if (!Character.isDigit(string.charAt(x))) {

		return false;
	    }

	}

	return con;
    }

    /**
     * Determines if a string is a good serial number. Good serial numbers are of
     * the form 'SN/nnnn-nnn', where 'n' is a digit.
     *
     * @param sn the serial number to test
     * @return {@code true} if the serial number is valid in form, {@code false}
     *         otherwise.
     */
    public static boolean validSn(final String sn) {
	// A valid SN should be 11 characters long: SN/1234-567
	if (sn == null || sn.length() != 11) {
	    return false;
	}

	// check the fixed characters
	if (!sn.substring(0, 1).equals("S")) {
	    return false;
	}
	if (!sn.substring(1, 2).equals("N")) {
	    return false;
	}
	if (!sn.substring(2, 3).equals("/")) {
	    return false;
	}
	if (!sn.substring(7, 8).equals("-")) {
	    return false;
	}

	// check the four digits after SN/
	if (!Character.isDigit(sn.charAt(3))) {
	    return false;
	}
	if (!Character.isDigit(sn.charAt(4))) {
	    return false;
	}
	if (!Character.isDigit(sn.charAt(5))) {
	    return false;
	}
	if (!Character.isDigit(sn.charAt(6))) {
	    return false;
	}

	// check the three digits after the dash
	if (!Character.isDigit(sn.charAt(8))) {
	    return false;
	}
	if (!Character.isDigit(sn.charAt(9))) {
	    return false;
	}
	if (!Character.isDigit(sn.charAt(10))) {
	    return false;
	}

	// if all checks passed
	return true;
    }

    /**
     * Evaluates serial numbers from a file. Writes valid serial numbers to
     * {@code goodSns}, and invalid serial numbers to {@code badSns}. Each line of
     * {@code fileIn} contains a (possibly valid) serial number.
     *
     * @param fileIn  a file already open for reading
     * @param goodSns a file already open for writing
     * @param badSns  a file already open for writing
     */
    public static void validSnFile(final Scanner fileIn, final PrintStream goodSns, final PrintStream badSns) {
	while (fileIn.hasNextLine()) {
	    String sn = fileIn.nextLine().trim(); // get a serial number and trim whitespace

	    if (validSn(sn)) {
		goodSns.println(sn);
	    } else {
		badSns.println(sn);
	    }
	}
    }

}
