#include "lists.h"

/**
 * is_reverse_listint - function that reverses a linked list
 * @head: first node in the list being pointed to
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - function that checks if a linked list is a palindrome
 * @head: linked list the double pointer to it
 *
 * Return: if linked list is palindrome then , 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *snail = *head, *quick = *head, *storage = *head, *copy = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		quick = quick->next->next;
		if (!quick)
		{
			copy = snail->next;
			break;
		}
		if (!quick->next)
		{
			copy = snail->next->next;
			break;
		}
		snail = snail->next;
	}

	reverse_listint(&copy);

	while (copy && storage)
	{
		if (storage->n == copy->n)
		{
			copy = copy->next;
			storage = storage->next;
		}
		else
			return (0);
	}

	if (!copy)
		return (1);

	return (0);
}
