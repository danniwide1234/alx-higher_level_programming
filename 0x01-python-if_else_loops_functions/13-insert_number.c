#include "lists.h"

/**
 * insert_node - functon that Inserts a number into
 * a sorted singly-linked list.
 * @head: head of the linked list pointer.
 * @number: The number to insert.
 * Return: NULL if function fail.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *fresh;

	fresh = malloc(sizeof(listint_t));
	if (fresh == NULL)
		return (NULL);
	fresh->n = number;

	if (node == NULL || node->n >= number)
	{
		fresh->next = node;
		*head = fresh;
		return (fresh);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	fresh->next = node->next;
	node->next = fresh;

	return (fresh);
}
