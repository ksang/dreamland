Dreamland
==========

A key value memory cache structure to provide data access functionality.

##Speed analysis:

###class FastFetch

####get():

**1. dict.get()**
    - constant time, based on hash map.

**2. list.index()**
    - O(n) time if need to scan the list

    listindex(
    {
        ...
        for (i = start; i < stop && i < Py_SIZE(self); i++) {
            int cmp = PyObject_RichCompareBool(self->ob_item[i], v, Py_EQ);
            if (cmp > 0)
                return PyInt_FromSsize_t(i);
            else if (cmp < 0)
                return NULL;
        ...
    }

    By setting the gate value, we can limit the complexity of this opertion.
    which means we only scan the elements outside of the gate in list.

**3. list.pop()**
    - constant time

    listpop()
    {
        ...
        list_ass_slice(self, i, i+1, (PyObject *)NULL);
        ...
    }
    list_ass_slice(PyListObject *a, Py_ssize_t ilow, Py_ssize_t ihigh, PyObject *v)
    {
        ...
        memmove(&item[ihigh+d], &item[ihigh],
            (Py_SIZE(a) - ihigh)*sizeof(PyObject *));
        list_resize(a, Py_SIZE(a) + d);
        ...
    }

**4. list.insert()/list.append()**
    - insert is O(n) time if insert position is at front of list.
    - append is constant time

    ins1(PyListObject *self, Py_ssize_t where, PyObject *v)
    {
        n = Py_SIZE(self);
        for (i = n; --i >= where; )
            items[i+1] = items[i];
        Py_INCREF(v);
        items[where] = v;
    }

Concluson:
    To optimize get() speed, we implemented two approaches:
    1. Instead of place the most recent used element to the front of position list, we place it in the end. This is because listappend is far more cheap than listinsert of the insert position is in head.
    2. Introduce 'gate' setting to scan only part of the position list, elements inside gate are safe and we don't care how recent they are visited, outside elements are scanned and place to end of list if visited.


####touch():

**1. len()**
    - constant time, so no need to manage size by fastfetch:

    listobject.c:
    list_length(PyListObject *a)
    {
        return Py_SIZE(a);
    }
    object.h: 
    #define Py_SIZE(ob)     (((PyVarObject*)(ob))->ob_size)

Concluson:
    The time complexity of touch() method depends on if the operation is insert or update.
    update is get() + python dictobject update value time(constant)
    insert is python dictobject new value time + list constant time operations.