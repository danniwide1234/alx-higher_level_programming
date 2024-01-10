#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - function that Prints bytes information
 *
 * @p: Object in python
 * Return: (void)
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int measure, y, boundary;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	measure = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", measure);
	printf("  trying string: %s\n", str);

	if (measure >= 10)
		boundary = 10;
	else
		boundary = measure + 1;

	printf("  first %ld bytes:", boundary);

	for (y = 0; y < boundary; y++)
		if (str[y] >= 0)
			printf(" %02x", str[y]);
		else
			printf(" %02x", 256 + str[y]);

	printf("\n");
}

/**
 * print_python_list - function that Prints list information
 *
 * @p: Object in python
 * Return: (void)
 */
void print_python_list(PyObject *p)
{
	long int measure, y;
	PyListObject *list;
	PyObject *obj;

	measure = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (y = 0; y < measure; y++)
	{
		obj = ((PyListObject *)p)->ob_item[y];
		printf("Element %ld: %s\n", y, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
