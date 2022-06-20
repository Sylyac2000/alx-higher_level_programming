#include "lists.h"
#define MAX_SIZE  10000

/**
 * is_palindrome - determine if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int  i = 0;
	int length = 0;
	int tablo[MAX_SIZE];

	if (head == NULL)
		return (0);

	if (*head == NULL) /* empty list is palindrome */
		return (1);

	while (tmp) /* length of linked list */
	{
		tmp = tmp->next;
		length += 1;
	}
	if (length == 1) /* single node list is palindrome */
		return (1);

	tmp = *head;
	while (tmp) /* pull node tablo into array to compare */
	{
		tablo[i++] = tmp->n;
		tmp = tmp->next;
	}

	for (i = 0; i <= (length / 2); i++)
	{
		if (tablo[i] != tablo[length - i - 1])
			return (0);
	}
	return (1);
}
