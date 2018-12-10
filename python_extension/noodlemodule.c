#include <Python.h>
#include <time.h>
#include <stdbool.h>

struct timespec first;
struct timespec second;
bool isTik=false;

static PyObject* tik(PyObject* self){
	clock_gettime(CLOCK_MONOTONIC,&first);
	isTik=true;
	Py_RETURN_NONE;
}

static PyObject* tok(PyObject* self){
	PyObject* result;
	long timeinterval_ns;
	clock_gettime(CLOCK_MONOTONIC,&second);
	if(!isTik){
		timeinterval_ns=-1;
	}
	else{
		timeinterval_ns=(second.tv_sec-first.tv_sec)*1e9+(second.tv_nsec-first.tv_nsec);
	}
	result=Py_BuildValue("l",timeinterval_ns);
	return result;
}

static PyMethodDef module_methods[]={
	{"tik",(PyCFunction)tik,METH_NOARGS,NULL},
	{"tok",(PyCFunction)tok,METH_NOARGS,NULL}
};

static struct PyModuleDef Noodle={
	PyModuleDef_HEAD_INIT,
	"Noodle",
	NULL,
	-1,
	module_methods
};

PyMODINIT_FUNC PyInit_noodle(){
	return PyModule_Create(&Noodle);
}
