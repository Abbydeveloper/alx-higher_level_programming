#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info(PyObject *p) - print some basic info about Python lists
 * @p: Python Object
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	long int length;
	long int i = 0;
	PyObject *object;
	PyListObject *list;

	length = Py_SIZE(p);
	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", length);

	printf("[*] Allocated = %ld\n", list->allocated);

	for (; i < length; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
