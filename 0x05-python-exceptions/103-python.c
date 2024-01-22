#include <time.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - function that Prints bytes information
 *
 * @p: Python Object
 * Return: (void)
 */

void print_python_bytes(PyObject *p)
{
	char *string;
	long int measure, k, boundary;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	measure = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  measure: %ld\n", measure);
	printf("  trying string: %s\n", string);

	if (measure >= 10)
		boundary = 10;
	else
		boundary = measure + 1;

	printf("  first %ld bytes:", boundary);

	for (k = 0; k < boundary; k++)
		if (string[k] >= 0)
			printf(" %02x", string[k]);
		else
			printf(" %02x", 256 + string[k]);

	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * print_python_float - function that Prints float information
 *
 * @p: Python Object
 * Return: (void)
 */

void print_python_float(PyObject *p)
{
	double fer;
	char *nf;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	fer = ((PyFloatObject *)(p))->ob_fval;
	nf = PyOS_double_to_string(fer, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  value: %s\n", nf);
	setbuf(stdout, NULL);
}

/**
 * print_python_list - function that Prints list information
 *
 * @p: Python Object
 * Return: (void)
 */

void print_python_list(PyObject *p)
{
	long int measure, k;
	PyListObject *list;
	PyObject *obj;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	measure = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", measure);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (k = 0; k < measure; k++)
	{
		obj = list->ob_item[k];
		printf("Element %ld: %s\n", k, ((obj)->ob_type)->tp_name);

		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		if (PyFloat_Check(obj))
			print_python_float(obj);
	}
	setbuf(stdout, NULL);
}
