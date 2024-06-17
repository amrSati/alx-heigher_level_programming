#include </usr/include/python3.8/Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints python list info
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *) p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, PyTYPE(item)->tp_name);
	}
}
