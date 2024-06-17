#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of list
 *
 * Return: 1 if it is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast_ptr = *head;
	listint_t *second_half, *prev_slow = *head;
	listint_t *midnode = NULL;
	int flag = 1;

	if (*head == NULL)
		return (flag);

	while (fast_ptr && fast_ptr->next)
	{
		fast_ptr = fast_ptr->next->next;

		prev_slow = slow_ptr;
		slow_ptr = slow_ptr->next;
	}

	if (fast_ptr != NULL)
	{
		midnode = slow_ptr;
		slow_ptr = slow_ptr->next;
	}

	second_half = slow_ptr;
	prev_slow->next = NULL;
	reverse(&second_half);

	flag = compare(*head, second_half);

	reverse(&second_half);

	if (midnode != NULL)
	{
		prev_slow->next = midnode;
		midnode->next = second_half;
	}
	else
		prev_slow->next = second_half;

	return (flag);
}

/**
 * reverse - reverses a linked list
 * @head: head of list
 *
 * Return: new head of list
 */
listint_t *reverse(listint_t **head)
{
	listint_t *prev = NULL, *cursor = *head, *next;

	while (cursor)
	{
		next = cursor->next;
		cursor->next = prev;
		prev = cursor;
		cursor = next;
	}

	*head = prev;
	return (*head);
}

/**
 * compare - compares equality between two singly linked lists
 * @head1: list 1
 * @head2: list 2
 *
 * Return: 1 if they are equal
 */
int compare(listint_t *head1, listint_t *head2)
{
	listint_t *cursor1 = head1, *cursor2 = head2;

	while (cursor1 && cursor2)
	{
		if (cursor1->n != cursor2->n)
			return (0);

		cursor1 = cursor1->next;
		cursor2 = cursor2->next;
	}

	return (1);
}
