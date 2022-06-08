#include "lists.h"

/**
 * check_cycle - frees a listint_t list
 * @list: pointer to struct listint_t
 * Return: 0 if no cycle, 1 is yes
 */
int check_cycle(listint_t *list)
{
	listint_t *list_tortue;
	listint_t *list_lievre;

	list_tortue = list;
	list_lievre = list;
	while (list_lievre && list_lievre->next)
	{
		list_tortue = list_tortue->next;
		list_lievre = list_lievre->next->next;
		if (list_tortue == list_lievre)
			return (1);
	}

	return (0);
}
