#include <stdio.h>
#include <stdlib.h>
#include "search_algos.h"
/**
  * bin_search - binary search function
  * @low: the lower boundary of array segment to search
  * @high: the upper boundary of array segment to search
  * @array: pointer to array to search
  * @target: value to find
  * Return: index if found, else -1
  */
int bin_search(int low, int high, int *array, int target)
{
	int mid = 0;

	mid = (high + low) / 2;

	if (target == array[mid])
		return (mid);

	if (high >= low)
	{
		if (mid < target)
			return (bin_search(mid + 1, high, array, target));
		else
			return (bin_search(low, mid - 1, array, target));
	}
	return (-1);
}



/**
  * binary_search - Calls binary search function
  * @array: pointer to first element of array to sort
  * @size: number of elements to sort
  * @value: target value to search for
  * Return: array index of target value on match, or -1
  */

int binary_search(int *array, size_t size, int value)
{
	int high = size - 1;
	int low = 0;

	if (!array)
		return (-1);


	return (bin_search(low, high, array, value));

}
