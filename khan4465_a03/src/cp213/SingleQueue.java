package cp213;

/**
 * A single linked queue structure of {@code T} objects. Only the front
 * {@code T} object contained in the queue is visible through the standard queue
 * methods. Extends the {@code SingleLink} class.
 *
 * @author your name, id, email here
 * @version 2025-09-07
 * @param <T> the {@code SingleNode} data type
 */
public class SingleQueue<T> extends SingleLink<T> {

    /**
     * Combines the contents of {@code left} and {@code right} into {@code this}.
     * Moves nodes only - does not refer to data in any way, or call the high-level
     * methods {@code insert} or {@code remove}. {@code left} and {@code right} are
     * empty when done. Nodes are moved alternately from {@code left} and
     * {@code right} into the rear of {@code this}. {@code this} may be empty. May
     * call any appropriate {@code SingleLink} helper methods available.
     * {@code left} and {@code right} are not necessarily the same length.
     *
     * @param left  the first {@code SingleQueue} to extract nodes from
     * @param right the second {@code SingleQueue} to extract nodes from
     */
    public void combine(final SingleQueue<T> left, final SingleQueue<T> right) {
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
     * Adds data to the rear of {@code this}. Increments the queue length.
     *
     * @param datum the data to add to the rear of the queue
     */
    public void insert(final T datum) {
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
     * Returns and removes the front data of {@code this}. The next node in the
     * queue becomes the new front node. Decrements the queue length.
     *
     * @return the object at the front of the queue or {@code null} if {@code this}
     *         is empty
     */
    public T remove() {
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
     * Splits the contents of {@code this} into {@code left} and {@code right}.
     * Moves nodes only - does not move data or call the high-level methods
     * {@code insert} or {@code remove}. {@code this} is empty when done. Nodes are
     * moved alternately from {@code this} to the rear of {@code left} and
     * {@code right}. {@code left} and {@code right} may already contain data.
     * <p>
     * This is the opposite of the combine method.
     *
     * @param left  the first {@code SingleQueue} to move nodes to
     * @param right the second {@code SingleQueue} to move nodes to
     */
    public void splitAlternate(final SingleQueue<T> left, final SingleQueue<T> right) {
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
}
