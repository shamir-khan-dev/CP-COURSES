package cp213;

import java.util.ArrayList;

/**
 * Implements a Binary Search Tree.
 *
 * @author Shamir Khan, 4465, khan4465@mylaurier.ca
 * @author Shamir Khan
 * @version 2025-09-07
 * @param <T> the data structure data type
 */
public class BST<T extends Comparable<T>> {

    // Attributes.
    /**
     * Count of comparisons performed by tree.
     */
    protected int comparisons = 0;
    /**
     * Root node of the tree.
     */
    protected TreeNode<T> root = null;
    /**
     * Number of nodes in the tree.
     */
    protected int size = 0;

    /**
     * Auxiliary method for {@code equals}. Determines whether two subtrees are
     * identical in node data and height.
     *
     * @param source Node of this BST.
     * @param target Node of that BST.
     * @return true if source and target are identical in node data and height.
     */
    protected boolean equalsAux(final TreeNode<T> source, final TreeNode<T> target) {
	if (source == null && target == null) {
	    return true;
	}
	if (source == null || target == null) {
	    return false;
	}
	// Check if data, count, and height match
	final CountedItem<T> sourceData = source.getCountedItem();
	final CountedItem<T> targetData = target.getCountedItem();
	if (sourceData.compareTo(targetData) != 0 || sourceData.getCount() != targetData.getCount()
		|| source.getHeight() != target.getHeight()) {
	    return false;
	}
	// Recursively check left and right subtrees
	return this.equalsAux(source.getLeft(), target.getLeft())
		&& this.equalsAux(source.getRight(), target.getRight());
    }

    /**
     * Auxiliary method for insert. Inserts data into this BST.
     *
     * @param node        The current node (TreeNode).
     * @param countedItem Data to be inserted into the tree.
     * @return The inserted node.
     */
    protected TreeNode<T> insertAux(TreeNode<T> node, final CountedItem<T> countedItem) {

	if (node == null) {
	    // Base case - add a new node containing the data.
	    node = new TreeNode<T>(countedItem);
	    node.getCountedItem().incrementCount();
	    this.size++;
	} else {
	    // Compare the node data against the insert data.
	    final int result = node.getCountedItem().compareTo(countedItem);

	    if (result > 0) {
		// General case - check the left subtree.
		node.setLeft(this.insertAux(node.getLeft(), countedItem));
	    } else if (result < 0) {
		// General case - check the right subtree.
		node.setRight(this.insertAux(node.getRight(), countedItem));
	    } else {
		// Base case - data is already in the tree, increment its count
		node.getCountedItem().incrementCount();
	    }
	}
	node.updateHeight();
	return node;
    }

    /**
     * Auxiliary method for valid. Determines if a subtree based on node is a valid
     * subtree.
     *
     * @param node    The root of the subtree to test for validity.
     * @param minNode The node of the minimum data in the current subtree.
     * @param maxNode The node of the maximum data in the current subtree.
     * @return true if the subtree base on node is valid, false otherwise.
     */
    protected boolean isValidAux(final TreeNode<T> node, TreeNode<T> minNode, TreeNode<T> maxNode) {
	if (node == null) {
	    return true;
	}
	// Check BST property: node data must be between min and max
	if (minNode != null && node.getCountedItem().compareTo(minNode.getCountedItem()) <= 0) {
	    return false;
	}
	if (maxNode != null && node.getCountedItem().compareTo(maxNode.getCountedItem()) >= 0) {
	    return false;
	}
	// Check height property: node height must be 1 + max of children heights
	final int leftHeight = this.nodeHeight(node.getLeft());
	final int rightHeight = this.nodeHeight(node.getRight());
	if (node.getHeight() != Math.max(leftHeight, rightHeight) + 1) {
	    return false;
	}
	// Recursively check left and right subtrees
	return this.isValidAux(node.getLeft(), minNode, node)
		&& this.isValidAux(node.getRight(), node, maxNode);
    }

    /**
     * Returns the height of a given TreeNode. Required for when TreeNode is null.
     *
     * @param node The TreeNode to determine the height of.
     * @return The height attribute of node, 0 if node is null.
     */
    protected int nodeHeight(final TreeNode<T> node) {
	return node != null ? node.getHeight() : 0;
    }

    /**
     * Auxiliary method for remove. Removes data from this BST.
     *
     * @param node        The current node (TreeNode).
     * @param countedItem Data to be removed from the tree.
     * @return The replacement node.
     */
    protected TreeNode<T> removeAux(TreeNode<T> node, final CountedItem<T> countedItem) {
	if (node == null) {
	    return null;
	}
	final int result = node.getCountedItem().compareTo(countedItem);
	if (result > 0) {
	    // Search left subtree
	    node.setLeft(this.removeAux(node.getLeft(), countedItem));
	} else if (result < 0) {
	    // Search right subtree
	    node.setRight(this.removeAux(node.getRight(), countedItem));
	} else {
	    // Found the node
	    node.getCountedItem().decrementCount();
	    if (node.getCountedItem().getCount() == 0) {
		// Remove the node entirely
		if (node.getLeft() == null && node.getRight() == null) {
		    // Leaf node
		    this.size--;
		    return null;
		} else if (node.getLeft() == null) {
		    // Only right child
		    this.size--;
		    return node.getRight();
		} else if (node.getRight() == null) {
		    // Only left child
		    this.size--;
		    return node.getLeft();
		} else {
		    // Two children - find inorder successor (smallest in right subtree)
		    TreeNode<T> successorParent = node;
		    TreeNode<T> successor = node.getRight();
		    while (successor.getLeft() != null) {
			successorParent = successor;
			successor = successor.getLeft();
		    }
		    // Detach successor from its current position
		    if (successorParent == node) {
			successorParent.setRight(successor.getRight());
		    } else {
			successorParent.setLeft(successor.getRight());
		    }
		    // Move successor to replace current node
		    successor.setLeft(node.getLeft());
		    if (successor != node.getRight()) {
			successor.setRight(node.getRight());
		    }
		    successor.updateHeight();
		    this.size--;
		    return successor;
		}
	    }
	}
	node.updateHeight();
	return node;
    }

    /**
     * Determines if this BST contains key.
     *
     * @param key The key to search for.
     * @return true if this contains key, false otherwise.
     */
    public boolean contains(final CountedItem<T> key) {
	return this.retrieve(key) != null;
    }

    /**
     * Determines whether two trees are identical.
     *
     * @param target The tree to compare this BST against.
     * @return true if this and target contain nodes that match in position, data,
     *         count, and height, false otherwise.
     */
    public boolean equals(final BST<T> target) {
	boolean isEqual = false;

	if (this.size == target.size) {
	    isEqual = this.equalsAux(this.root, target.root);
	}
	return isEqual;
    }

    /**
     * Get number of comparisons executed by the retrieve method.
     *
     * @return comparisons
     */
    public int getComparisons() {
	return this.comparisons;
    }

    /**
     * Returns the height of the root node of this tree.
     *
     * @return height of root node, 0 if the root node is null.
     */
    public int getHeight() {
	return this.root != null ? this.root.getHeight() : 0;
    }

    /**
     * Returns the number of nodes in the tree.
     *
     * @return number of nodes in this tree.
     */
    public int getSize() {
	return this.size;
    }

    /**
     * Returns a list of the data in the current tree. The list contents are in
     * order from smallest to largest.
     *
     * Not thread safe as it assumes contents of the tree are not changed by an
     * external thread during the loop.
     *
     * @return The contents of this tree as a list of data.
     */
    public ArrayList<CountedItem<T>> inOrder() {
	return this.root.inOrder();
    }

    /**
     * Inserts data into this tree.
     *
     * @param countedItem Data to store.
     */
    public void insert(final CountedItem<T> countedItem) {
	this.root = this.insertAux(this.root, countedItem);
	return;
    }

    /**
     * Determines if this tree is empty.
     *
     * @return true if this tree is empty, false otherwise.
     */
    public boolean isEmpty() {
	return this.size == 0;
    }

    /**
     * Determines if this tree is a valid BST; i.e. a node's left child data is
     * smaller than its data, and its right child data is greater than its data, and
     * a node's height is equal to the maximum of the heights of its two children
     * (empty child nodes have a height of 0), plus 1.
     *
     * @return true if this tree is a valid BST, false otherwise.
     */
    public boolean isValid() {
	return this.isValidAux(this.root, null, null);
    }

    /**
     * Returns a list of the data in the current tree. The list contents are in node
     * level order starting from the root node. Helps determine the structure of the
     * tree.
     *
     * Not thread safe as it assumes contents of the tree are not changed by an
     * external thread during the loop.
     *
     * @return this tree data as a list of data.
     */
    public ArrayList<CountedItem<T>> levelOrder() {
	return this.root.levelOrder();
    }

    /**
     * Returns a list of the data in the current tree. The list contents are in node
     * preorder.
     *
     * Not thread safe as it assumes contents of the tree are not changed by an
     * external thread during the loop.
     *
     * @return The contents of this tree as a list of data.
     */
    public ArrayList<CountedItem<T>> preOrder() {
	return this.root.preOrder();
    }

    /**
     * Removes data from the tree. Decrements the node count, and if the count is 0,
     * removes the node entirely.
     *
     * @param countedItem Data to decrement or remove.
     */
    public void remove(final CountedItem<T> countedItem) {
	this.root = this.removeAux(this.root, countedItem);
	return;
    }

    /**
     * Resets the comparison count to 0.
     */
    public void resetComparisons() {
	this.comparisons = 0;
	return;
    }

    /**
     * Retrieves a copy of data matching key (key should have data count of 0).
     * Returning a complete CountedItem gives access to the data and its count.
     *
     * @param key The key to look for.
     * @return The complete CountedItem that matches key, null otherwise.
     */
    public CountedItem<T> retrieve(final CountedItem<T> key) {
	TreeNode<T> node = this.root;
	while (node != null) {
	    this.comparisons++;
	    final int result = node.getCountedItem().compareTo(key);
	    if (result == 0) {
		return node.getCountedItem().copy();
	    } else if (result > 0) {
		node = node.getLeft();
	    } else {
		node = node.getRight();
	    }
	}
	return null;
    }
}
