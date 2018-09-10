#include "lists.h"

/**
 * check_cycle - checks if linked list has a cycle
 * @list: node in linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *cycle = list;

	for (list = list->next; list != NULL; list = list->next)
		if (cycle == list)
			return (1);
	return (0);
}
