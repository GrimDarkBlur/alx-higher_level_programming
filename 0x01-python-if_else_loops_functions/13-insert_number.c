#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t)), *_head = *head;
	listint_t *prev = NULL;
	int added = 0;

	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	while (_head)
	{
		if (_head->n < number)
			prev = _head, _head = _head->next;
		else
		{
			new_node->next = _head;
			prev->next = new_node;
			added = 1;
			break;
		}
	}

	if (!added)
		_head->next = new_node;

	return (new_node);
}
