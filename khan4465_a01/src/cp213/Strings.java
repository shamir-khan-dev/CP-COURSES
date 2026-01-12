package cp213;

/**
 * @author Your name and id here
 * @version 2025-09-07
 */
public class Strings {
    // Constants
    public static final String VOWELS = "aeiouAEIOU";

    /**
     * Determines if {@code string} is a "palindrome": a word, verse, or sentence
     * (such as "Able was I ere I saw Elba") that reads the same backward or
     * forward. Ignores case, spaces, digits, and punctuation in {@code string}.
     *
     * @param string a string
     * @return {@code true} if {@code string} is a palindrome, {@code false}
     *         otherwise
     */
    public static boolean isPalindrome(final String string) {

	// your code here

	String cleaned = string.replaceAll("[^a-zA-Z]", "").toLowerCase();

	for (int x = 0; x < cleaned.length(); x++) {

	    if (cleaned.charAt(x) != cleaned.charAt((cleaned.length() - 1) - x)) {

		return false;
	    }
	}

	return true;
    }

    /**
     * Determines if {@code name} is a valid Java variable name. Variables names
     * must start with a letter or an underscore, but cannot be an underscore alone.
     * The rest of the variable name may consist of letters, numbers and
     * underscores.
     *
     * @param name a string to test as a Java variable name
     * @return {@code true} if {@code name} is a valid Java variable name,
     *         {@code false} otherwise
     */
    public static boolean isValid(final String name) {

	// your code here

	if (name.substring(0, 1).equals("_") || Character.isLetter(name.charAt(0))) {

	    return true;
	}

	return false;
    }

    /**
     * Converts a word to Pig Latin. The conversion is:
     * <ul>
     * <li>if a word begins with a vowel, add "way" to the end of the word.</li>
     * <li>if the word begins with consonants, move the leading consonants to the
     * end of the word and add "ay" to the end of that. "y" is treated as a
     * consonant if it is the first character in the word, and as a vowel for
     * anywhere else in the word.</li>
     * </ul>
     * Preserve the case of the word - i.e. if the first character of word is
     * upper-case, then the new first character should also be upper case.
     *
     * @param word the string to convert to Pig Latin
     * @return the Pig Latin version of word
     */
    public static String pigLatin(String word) {
	final String VOWELS = "aeiouAEIOU";

	if (word == null || word.isEmpty()) {
	    return word;
	}

	boolean startsWithUpper = Character.isUpperCase(word.charAt(0));
	String lowerWord = word.toLowerCase();

	if (VOWELS.contains(lowerWord.substring(0, 1))) {
	    String result = lowerWord + "way";
	    return startsWithUpper ? result.substring(0, 1).toUpperCase() + result.substring(1) : result;
	}

	// Find index of first vowel (including 'y' if not first char)
	int firstVowel = -1;
	for (int i = 0; i < lowerWord.length(); i++) {
	    char ch = lowerWord.charAt(i);
	    if (VOWELS.contains("" + ch) || (i != 0 && ch == 'y')) {
		firstVowel = i;
		break;
	    }
	}

	if (firstVowel == -1) {
	    firstVowel = 0; // no vowels? treat whole word as consonants
	}

	String stem = lowerWord.substring(firstVowel) + lowerWord.substring(0, firstVowel) + "ay";
	return startsWithUpper ? stem.substring(0, 1).toUpperCase() + stem.substring(1) : stem;
    }

}
