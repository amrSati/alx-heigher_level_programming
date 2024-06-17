#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to head of list
 * @number: number to be inserted
 *
 * Return: address of new node (on success)
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *prev, *forw;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;
	node->next = NULL;

	prev = *head;
	if (prev == NULL)
		*head = node;
	else if (prev->n > number)
	{
		node->next = *head;
		*head = node;
	}
	else
	{
		forw = prev->next;
		for (; prev->n < number && forw != NULL && forw->n < number;)
		{
			prev = prev->next;
			forw = forw->next;
		}

		prev->next = node;
		node->next = forw;
	}

	return (node);
}
