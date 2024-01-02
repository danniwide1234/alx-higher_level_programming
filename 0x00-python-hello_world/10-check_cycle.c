#include "lists.h"

/**
 * check_cycle - function that checks if a singly
 * linked list contain cycle
 * @list: list pointer
 * Return: 0 for no cycle,1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *menu;
	listint_t *former;

	menu = list;
	former = list;
	while (list && menu && menu->next)
	{
		list = list->next;
		menu = menu->next->next;

		if (list == menu)
		{
			list = former;
			former = menu;
			while (1)
			{
				menu = former;
				while (menu->next != list && menu->next != former)
				{
					menu = menu->next;
				}
				if (menu->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
