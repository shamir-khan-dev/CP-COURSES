package cp213;

/**
 * Implements a Popularity Tree. Extends BST.
 *
 * @author Shamir Khan, 4465, khan4465@mylaurier.ca
 * @author Shamir Khan
 * @version 2025-09-07
 * @param <T> the data structure data type
 */
public class PopularityTree<T extends Comparable<T>> extends BST<T> {

	/**
	 * Auxiliary method for valid. May force node rotation if the retrieval count of
	 * the located node data is incremented.
	 *
	 * @param node The node to examine for key.
	 * @param key  The data to search for. Count is updated to count in matching
	 *             node data if key is found.
	 * @return The updated node.
	 */
	private TreeNode<T> retrieveAux(TreeNode<T> node, final CountedItem<T> key) {
		if (node == null) {
			return null;
		}
		this.comparisons++;
		final int result = node.getCountedItem().compareTo(key);
		if (result == 0) {
			// Found the node - increment its count
			node.getCountedItem().incrementCount();
		} else if (result > 0) {
			// Search left subtree
			node.setLeft(this.retrieveAux(node.getLeft(), key));
		} else {
			// Search right subtree
			node.setRight(this.retrieveAux(node.getRight(), key));
		}
		node.updateHeight();
		// Rebalance at this level (may propagate up the tree)
		node = this.rebalancePopularity(node);
		return node;
	}

	/**
	 * Rebalances the tree based on popularity (count) rather than height.
	 * A node's count must be >= its children's counts.
	 *
	 * @param node the node to rebalance
	 * @return the rebalanced node
	 */
	private TreeNode<T> rebalancePopularity(TreeNode<T> node) {
		if (node == null) {
			return null;
		}
		final int nodeCount = node.getCountedItem().getCount();
		// Check left child
		if (node.getLeft() != null) {
			final int leftCount = node.getLeft().getCountedItem().getCount();
			if (leftCount > nodeCount) {
				// Left child is more popular - need right rotation
				return this.rotateRight(node);
			}
		}
		// Check right child
		if (node.getRight() != null) {
			final int rightCount = node.getRight().getCountedItem().getCount();
			if (rightCount > nodeCount) {
				// Right child is more popular - need left rotation
				return this.rotateLeft(node);
			}
		}
		return node;
	}

	/**
	 * Performs a left rotation around node.
	 *
	 * @param parent The subtree to rotate.
	 * @return The new root of the subtree.
	 */
	private TreeNode<T> rotateLeft(final TreeNode<T> parent) {
		final TreeNode<T> rightChild = parent.getRight();
		parent.setRight(rightChild.getLeft());
		rightChild.setLeft(parent);
		parent.updateHeight();
		rightChild.updateHeight();
		return rightChild;
	}

	/**
	 * Performs a right rotation around {@code node}.
	 *
	 * @param parent The subtree to rotate.
	 * @return The new root of the subtree.
	 */
	private TreeNode<T> rotateRight(final TreeNode<T> parent) {
		final TreeNode<T> leftChild = parent.getLeft();
		parent.setLeft(leftChild.getRight());
		leftChild.setRight(parent);
		parent.updateHeight();
		leftChild.updateHeight();
		return leftChild;
	}

	/**
	 * Replaces BST insertAux - does not increment count on repeated insertion.
	 * Counts are incremented only on retrieve.
	 */
	@Override
	protected TreeNode<T> insertAux(TreeNode<T> node, final CountedItem<T> countedItem) {
		if (node == null) {
			// Base case - add a new node containing the data.
			// Note: count is NOT incremented on insertion for PopularityTree
			node = new TreeNode<T>(countedItem);
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
			}
			// If data already exists, do nothing (don't increment count)
		}
		node.updateHeight();
		return node;
	}

	/**
	 * Auxiliary method for valid. Determines if a subtree based on node is a valid
	 * subtree. An Popularity Tree must meet the BST validation conditions, and
	 * additionally the counts of any node data must be greater than or equal to the
	 * counts of its children.
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
		// Check PopularityTree property: node count must be >= children counts
		final int nodeCount = node.getCountedItem().getCount();
		if (node.getLeft() != null && node.getLeft().getCountedItem().getCount() > nodeCount) {
			return false;
		}
		if (node.getRight() != null && node.getRight().getCountedItem().getCount() > nodeCount) {
			return false;
		}
		// Recursively check left and right subtrees
		return this.isValidAux(node.getLeft(), minNode, node)
				&& this.isValidAux(node.getRight(), node, maxNode);
	}

	/**
	 * Determines whether two PopularityTrees are identical.
	 *
	 * @param target The PopularityTree to compare this PopularityTree against.
	 * @return true if this PopularityTree and target contain nodes that match in
	 *         position, data, count, and height, false otherwise.
	 */
	public boolean equals(final PopularityTree<T> target) {
		return super.equals(target);
	}

	/**
	 * Very similar to the BST retrieve, but increments the data count here instead
	 * of in the insertion.
	 *
	 * @param key The key to search for.
	 */
	@Override
	public CountedItem<T> retrieve(CountedItem<T> key) {
		this.root = this.retrieveAux(this.root, key);
		if (this.root != null) {
			// Find the node with matching key to return
			TreeNode<T> node = this.root;
			while (node != null) {
				final int result = node.getCountedItem().compareTo(key);
				if (result == 0) {
					return node.getCountedItem().copy();
				} else if (result > 0) {
					node = node.getLeft();
				} else {
					node = node.getRight();
				}
			}
		}
		return null;
	}

}
