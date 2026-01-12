package cp213;

/**
 * A single linked list structure of {@code T} objects. Extends the
 * {@code SingleLink} class.
 *
 * @author your name, id, email here
 * @version 2025-09-07
 * @param <T> the {@code SingleNode} data type
 */
public class SingleList<T extends Comparable<T>> extends SingleLink<T> {

    /**
     * Searches for the first occurrence of {@code key} in this SingleList. Private
     * helper methods - used only by other ADT methods.
     *
     * @param key the object to look for
     * @return a pointer to the node previous to the node containing {@code key}
     */
    private SingleNode<T> linearSearch(final T key) {
	SingleNode<T> prev = null;
	SingleNode<T> curr = this.front;

	while (curr != null && curr.getDatum().compareTo(key) != 0) {
	    prev = curr;
	    curr = curr.getNext();
	}
	return prev;
    }

    /**
     * Appends data to the end of {@code this}
     *
     * @param datum the object to append
     */
    public void append(final T datum) {
	SingleNode<T> node = new SingleNode<T>(datum, null);

	if (this.front == null) {
	    this.front = node;
	    this.rear = node;
	} else {
	    this.rear.setNext(node);
	    this.rear = node;
	}
	this.length++;
	return;
    }

    /**
     * Removes duplicates from {@code this}. The list contains one and only one of
     * each object formerly present in {@code this}. The first occurrence of each
     * object is preserved.
     */
    public void clean() {
	SingleNode<T> curr = this.front;

	while (curr != null) {
	    SingleNode<T> prev = curr;
	    SingleNode<T> next = curr.getNext();

	    while (next != null) {
		if (next.getDatum().compareTo(curr.getDatum()) == 0) {
		    prev.setNext(next.getNext());
		    if (next == this.rear) {
			this.rear = prev;
		    }
		    this.length--;
		    next = next.getNext();
		} else {
		    prev = next;
		    next = next.getNext();
		}
	    }
	    curr = curr.getNext();
	}
	return;
    }

    /**
     * Combines the contents of {@code left} and {@code right} into {@code this}.
     * Moves nodes only - does not refer to data in any way, or call the high-level
     * methods {@code insert} or {@code remove}. {@code left} and {@code right} are
     * empty when done. Nodes are moved alternately from {@code left} and
     * {@code right} into {@code this}. {@code this} may be empty. May call any
     * appropriate {@code SingleLink} helper methods available. {@code left} and
     * {@code right} are not necessarily the same length.
     *
     * @param left  the first {@code SingleList} to extract nodes from
     * @param right the second {@code SingleList} to extract nodes from
     */
    public void combine(final SingleList<T> left, final SingleList<T> right) {
	boolean fromLeft = true;

	while (left.front != null || right.front != null) {
	    if (fromLeft && left.front != null) {
		left.moveFrontToRear(this);
		fromLeft = false;
	    } else if (right.front != null) {
		right.moveFrontToRear(this);
		fromLeft = true;
	    } else if (left.front != null) {
		left.moveFrontToRear(this);
	    }
	}
	return;
    }

    /**
     * Determines if {@code this} contains {@code key}.
     *
     * @param key the key object to look for
     * @return {@code true} if {@code key} is in {@code this}, {@code false}
     *         otherwise
     */
    public boolean contains(final T key) {
	SingleNode<T> prev = this.linearSearch(key);
	SingleNode<T> curr = prev == null ? this.front : prev.getNext();

	return curr != null && curr.getDatum().compareTo(key) == 0;
    }

    /**
     * Finds the number of times {@code key} appears in {@code this}.
     *
     * @param key the object to look for
     * @return the number of times {@code key} appears in {@code this}
     */
    public int count(final T key) {
	int count = 0;
	SingleNode<T> curr = this.front;

	while (curr != null) {
	    if (curr.getDatum().compareTo(key) == 0) {
		count++;
	    }
	    curr = curr.getNext();
	}
	return count;
    }

    /**
     * Finds and returns the object in {@code this} that matches {@code key}.
     *
     * @param key the object to search for
     * @return the object that matches {@code key}, {@code null} otherwise
     */
    public T find(final T key) {
	SingleNode<T> prev = this.linearSearch(key);
	SingleNode<T> curr = prev == null ? this.front : prev.getNext();

	if (curr != null && curr.getDatum().compareTo(key) == 0) {
	    return curr.getDatum();
	}
	return null;
    }

    /**
     * Get the {@code n}th object in {@code this}.
     *
     * @param n the index of the object to return
     * @return the nth object in {@code this} if {@code n} is a valid index,
     *         {@code null} otherwise
     */
    public T get(final int n) {
	if (n < 0 || n >= this.length) {
	    return null;
	}
	SingleNode<T> curr = this.front;

	for (int i = 0; i < n; i++) {
	    curr = curr.getNext();
	}
	return curr.getDatum();
    }

    /**
     * Determines whether two lists are identical.
     *
     * @param source the list to compare against {@code this}
     * @return {@code true} if {@code this} contains the same objects in the same
     *         order as {@code source}, {@code false} otherwise
     */
    public boolean equals(final SingleList<T> source) {
	if (this.length != source.length) {
	    return false;
	}
	SingleNode<T> curr1 = this.front;
	SingleNode<T> curr2 = source.front;

	while (curr1 != null && curr2 != null) {
	    if (curr1.getDatum().compareTo(curr2.getDatum()) != 0) {
		return false;
	    }
	    curr1 = curr1.getNext();
	    curr2 = curr2.getNext();
	}
	return true;
    }

    /**
     * Finds the first location of {@code key} in {@code this}.
     *
     * @param key the object to search for
     * @return the index of {@code key} in {@code this}, -1 otherwise
     */
    public int index(final T key) {
	int index = 0;
	SingleNode<T> curr = this.front;

	while (curr != null) {
	    if (curr.getDatum().compareTo(key) == 0) {
		return index;
	    }
	    curr = curr.getNext();
	    index++;
	}
	return -1;
    }

    /**
     * Inserts object into {@code this} at index {@code i}. If {@code i} greater
     * than the length of {@code this}, append data to the rear of {@code this}.
     *
     * @param i     The index to insert the new data at.
     * @param datum The new object to insert into this SingleList.
     */
    public void insert(int i, final T datum) {
	if (i <= 0) {
	    this.prepend(datum);
	} else if (i >= this.length) {
	    this.append(datum);
	} else {
	    SingleNode<T> curr = this.front;
	    for (int j = 0; j < i - 1; j++) {
		curr = curr.getNext();
	    }
	    SingleNode<T> node = new SingleNode<T>(datum, curr.getNext());
	    curr.setNext(node);
	    this.length++;
	}
	return;
    }

    /**
     * Creates an intersection of {@code left} and {@code right} into {@code this}.
     * Copies data to {@code this}. {@code left} and {@code right} are unchanged.
     * Values from {@code left} are copied in order first, then objects from
     * {@code right} are copied in order.
     * <p>
     * In an intersection, data copied to {@code this} must appear in both
     * {@code left} and {@code right}.
     *
     * @param left  the first {@code SingleList} to create an intersection from
     * @param right the second {@code SingleList} to create an intersection from
     */
    public void intersection(final SingleList<T> left, final SingleList<T> right) {
	this.front = null;
	this.rear = null;
	this.length = 0;

	SingleNode<T> curr = left.front;
	while (curr != null) {
	    if (right.contains(curr.getDatum()) && !this.contains(curr.getDatum())) {
		this.append(curr.getDatum());
	    }
	    curr = curr.getNext();
	}
	return;
    }

    /**
     * Finds the maximum object in {@code this}.
     *
     * @return the maximum object or {@code null} if {@code this} is empty
     */
    public T max() {
	if (this.front == null) {
	    return null;
	}
	T max = this.front.getDatum();
	SingleNode<T> curr = this.front.getNext();

	while (curr != null) {
	    if (curr.getDatum().compareTo(max) > 0) {
		max = curr.getDatum();
	    }
	    curr = curr.getNext();
	}
	return max;
    }

    /**
     * Finds the minimum object in {@code this}.
     *
     * @return the minimum object or {@code null} if {@code this} is empty
     */
    public T min() {
	if (this.front == null) {
	    return null;
	}
	T min = this.front.getDatum();
	SingleNode<T> curr = this.front.getNext();

	while (curr != null) {
	    if (curr.getDatum().compareTo(min) < 0) {
		min = curr.getDatum();
	    }
	    curr = curr.getNext();
	}
	return min;
    }

    /**
     * Inserts object into the front of {@code this}.
     *
     * @param datum the object to insert into the front of {@code this}
     */
    public void prepend(final T datum) {
	SingleNode<T> node = new SingleNode<T>(datum, this.front);

	if (this.front == null) {
	    this.rear = node;
	}
	this.front = node;
	this.length++;
	return;
    }

    /**
     * Finds, removes, and returns the object in {@code this} that matches
     * {@code key}.
     *
     * @param key the object to search for
     * @return the object matching {@code key}, {@code null} otherwise
     */
    public T remove(final T key) {
	SingleNode<T> prev = this.linearSearch(key);
	SingleNode<T> curr = prev == null ? this.front : prev.getNext();

	if (curr != null && curr.getDatum().compareTo(key) == 0) {
	    T datum = curr.getDatum();
	    if (prev == null) {
		this.front = curr.getNext();
	    } else {
		prev.setNext(curr.getNext());
	    }
	    if (curr == this.rear) {
		this.rear = prev;
	    }
	    this.length--;
	    return datum;
	}
	return null;
    }

    /**
     * Removes and returns the object at the front of {@code this}.
     *
     * @return the object at the front of {@code this}, if empty return {@code null}
     */
    public T removeFront() {
	if (this.front == null) {
	    return null;
	}
	T datum = this.front.getDatum();
	this.front = this.front.getNext();
	this.length--;

	if (this.front == null) {
	    this.rear = null;
	}
	return datum;
    }

    /**
     * Finds and removes all objects in {@code this} that match {@code key}.
     *
     * @param key the object to search for
     */
    public void removeMany(final T key) {
	SingleNode<T> prev = null;
	SingleNode<T> curr = this.front;

	while (curr != null) {
	    if (curr.getDatum().compareTo(key) == 0) {
		if (prev == null) {
		    this.front = curr.getNext();
		} else {
		    prev.setNext(curr.getNext());
		}
		if (curr == this.rear) {
		    this.rear = prev;
		}
		this.length--;
		curr = curr.getNext();
	    } else {
		prev = curr;
		curr = curr.getNext();
	    }
	}
	return;
    }

    /**
     * Reverses the order of the objects in {@code this}.
     */
    public void reverse() {
	SingleNode<T> prev = null;
	SingleNode<T> curr = this.front;
	SingleNode<T> next = null;

	this.rear = this.front;
	while (curr != null) {
	    next = curr.getNext();
	    curr.setNext(prev);
	    prev = curr;
	    curr = next;
	}
	this.front = prev;
	return;
    }

    /**
     * Splits the contents of {@code this} into {@code left} and {@code right}.
     * Moves nodes only - does not move data or call high-level methods.
     * {@code this} is empty when done.The first half of {@code this} is moved to
     * {@code left}, and the last half of {@code this} is moved to {@code right}. If
     * the resulting lengths are not the same, left should have one more object than
     * right. Order is preserved. {@code left} and {@code right} may already contain
     * data.
     *
     * @param left  the first {@code SingleList} to move nodes to
     * @param right the second {@code SingleList} to move nodes to
     */
    public void split(final SingleList<T> left, final SingleList<T> right) {
	int half = (this.length + 1) / 2;
	int count = 0;

	while (this.front != null && count < half) {
	    this.moveFrontToRear(left);
	    count++;
	}
	while (this.front != null) {
	    this.moveFrontToRear(right);
	}
	return;
    }

    /**
     * Splits the contents of {@code this} into {@code left} and {@code right}.
     * Moves nodes only - does not move data or call the high-level methods
     * {@code insert} or {@code remove}. {@code this} is empty when done. Nodes are
     * moved alternately from {@code this} to the rear of {@code left} and
     * {@code right}. {@code left} and {@code right} may already contain data.
     * <p>
     * This is the opposite of the combine method.
     *
     * @param left  the first {@code SingleList} to move nodes to
     * @param right the second {@code SingleList} to move nodes to
     */
    public void splitAlternate(final SingleList<T> left, final SingleList<T> right) {
	boolean toLeft = true;

	while (this.front != null) {
	    if (toLeft) {
		this.moveFrontToRear(left);
		toLeft = false;
	    } else {
		this.moveFrontToRear(right);
		toLeft = true;
	    }
	}
	return;
    }

    /**
     * Creates an union of {@code left} and {@code right} into {@code this}. Copies
     * data to {@code this}. {@code left} and {@code right} are unchanged. Values
     * from {@code left} are copied in order first, then objects from {@code right}
     * are copied in order.
     * <p>
     * In an intersection, data copied to {@code this} must appear in one or both of
     * {@code left} and {@code right}.
     *
     * @param left  the first {@code SingleList} to create an union from
     * @param right the second {@code SingleList} to create an union from
     */
    public void union(final SingleList<T> left, final SingleList<T> right) {
	this.front = null;
	this.rear = null;
	this.length = 0;

	SingleNode<T> curr = left.front;
	while (curr != null) {
	    if (!this.contains(curr.getDatum())) {
		this.append(curr.getDatum());
	    }
	    curr = curr.getNext();
	}
	curr = right.front;
	while (curr != null) {
	    if (!this.contains(curr.getDatum())) {
		this.append(curr.getDatum());
	    }
	    curr = curr.getNext();
	}
	return;
    }
}
