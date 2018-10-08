#include <stdlib.h>
#include <stdio.h>
#include "binary_trees.h"

/**
  * binary_tree_is_full - checks if the binary tree is full
  * @tree: pointer to the tree to check
  * Return: 0 if tree is NULL or not full
  */
int binary_tree_is_full(const binary_tree_t *tree)
{
	int left;
	int right;

	if (!tree)
		return (0);

	if (!(tree->left) && !(tree->right))
		return (1);

	left = binary_tree_is_full(tree->left);
	right =  binary_tree_is_full(tree->right);

	if (left && right)
		return (1);

	return (0);


}
