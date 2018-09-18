#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to address of the head node of linked list
 *
 * Return: 1 if its a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len, i, j;
	int *num_array;
	listint_t *tmp;

	if (!head)
		return (0);
	if (*head == NULL)
		return (1);
	for (len = 0, tmp = *head; tmp; tmp = tmp->next)
		len++;
	num_array = malloc(sizeof(int) * len);
	if (!num_array)
		return (0);
	for (i = 0, tmp = *head; tmp; tmp = tmp->next, i++)
		num_array[i] = tmp->n;
	for (i = 0, j = len - 1; i < j; i++, j--)
		if (num_array[i] != num_array[j])
			return (0);
	return (1);
}
