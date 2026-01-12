package cp213;

/**
 * Implements an AVL (Adelson-Velsky Landis) tree. Extends BST.
 *
 * @author Shamir Khan, 4465, khan4465@mylaurier.ca
 * @author Shamir Khan
 * @version 2025-09-07
 * @param <T> the data structure data type
 */
public class AVL<T extends Comparable<T>> extends BST<T> {

    /**
     * Returns the balance data of node. If greater than 1, then left heavy, if less
     * than -1, then right heavy. If in the range -1 to 1 inclusive, the node is
     * balanced. Used to determine whether to rotate a node upon insertion.
     *
     * @param node The TreeNode to analyze for balance.
     * @return A balance number.
     */
    private int balance(final TreeNode<T> node) {
	if (node == null) {
	    return 0;
	}
	return this.nodeHeight(node.getLeft()) - this.nodeHeight(node.getRight());
    }

    /**
     * Rebalances the current node if its children are not balanced.
     *
     * @param node the node to rebalance
     * @return replacement for the rebalanced node
     */
    private TreeNode<T> rebalance(TreeNode<T> node) {
	final int balanceFactor = this.balance(node);
	// Left heavy
	if (balanceFactor > 1) {
	    // Left-Right case
	    if (this.balance(node.getLeft()) < 0) {
		node.setLeft(this.rotateLeft(node.getLeft()));
	    }
	    // Left-Left case
	    return this.rotateRight(node);
	}
	// Right heavy
	if (balanceFactor < -1) {
	    // Right-Left case
	    if (this.balance(node.getRight()) > 0) {
		node.setRight(this.rotateRight(node.getRight()));
	    }
	    // Right-Right case
	    return this.rotateLeft(node);
	}
	return node;
    }

    /**
     * Performs a left rotation around node.
     *
     * @param node The subtree to rotate.
     * @return The new root of the subtree.
     */
    private TreeNode<T> rotateLeft(final TreeNode<T> node) {
	final TreeNode<T> rightChild = node.getRight();
	node.setRight(rightChild.getLeft());
	rightChild.setLeft(node);
	node.updateHeight();
	rightChild.updateHeight();
	return rightChild;
    }

    /**
     * Performs a right rotation around node.
     *
     * @param node The subtree to rotate.
     * @return The new root of the subtree.
     */
    private TreeNode<T> rotateRight(final TreeNode<T> node) {
	final TreeNode<T> leftChild = node.getLeft();
	node.setLeft(leftChild.getRight());
	leftChild.setRight(node);
	node.updateHeight();
	leftChild.updateHeight();
	return leftChild;
    }

    /**
     * Auxiliary method for insert. Inserts data into this AVL. Same as BST
     * insertion with addition of rebalance of nodes.
     *
     * @param node        The current node (TreeNode).
     * @param countedItem Data to be inserted into the node.
     * @return The inserted node.
     */
    @Override
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
	// Rebalance the tree
	return this.rebalance(node);
    }

    /**
     * Auxiliary method for valid. Determines if a subtree based on node is a valid
     * subtree. An AVL must meet the BST validation conditions, and additionally be
     * balanced in all its subtrees - i.e. the difference in height between any two
     * children must be no greater than 1.
     *
     * @param node The root of the subtree to test for validity.
     * @return true if the subtree base on node is valid, false otherwise.
     */
    @Override
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
	// Check AVL property: balance factor must be between -1 and 1
	final int balanceFactor = this.balance(node);
	if (balanceFactor < -1 || balanceFactor > 1) {
	    return false;
	}
	// Recursively check left and right subtrees
	return this.isValidAux(node.getLeft(), minNode, node)
		&& this.isValidAux(node.getRight(), node, maxNode);
    }

    /**
     * Determines whether two AVLs are identical.
     *
     * @param target The AVL to compare this AVL against.
     * @return true if this AVL and target contain nodes that match in position,
     *         data, count, and height, false otherwise.
     */
    public boolean equals(final AVL<T> target) {
	return super.equals(target);
    }

    /**
     * Auxiliary method for remove. Removes data from this BST. Same as BST removal
     * with addition of rebalance of nodes.
     *
     * @param node        The current node (TreeNode).
     * @param countedItem Data removed from the tree.
     * @return The replacement node.
     */
    @Override
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
		    node = successor;
		}
	    }
	}
	node.updateHeight();
	// Rebalance the tree
	return this.rebalance(node);
    }

}
