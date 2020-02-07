# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""IDA Plugin SDK API wrapper: range"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_range
else:
    import _ida_range

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref


import ida_idaapi


import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        ida_idaapi._BC695.replace_fun(func)
        return func

class rangevec_base_t(object):
    r"""Proxy of C++ qvector< range_t > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> rangevec_base_t
        __init__(self, x) -> rangevec_base_t
        """
        _ida_range.rangevec_base_t_swiginit(self, _ida_range.new_rangevec_base_t(*args))
    __swig_destroy__ = _ida_range.delete_rangevec_base_t

    def push_back(self, *args):
        r"""
        push_back(self, x)
        push_back(self) -> range_t
        """
        return _ida_range.rangevec_base_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""pop_back(self)"""
        return _ida_range.rangevec_base_t_pop_back(self, *args)

    def size(self, *args):
        r"""size(self) -> size_t"""
        return _ida_range.rangevec_base_t_size(self, *args)

    def empty(self, *args):
        r"""empty(self) -> bool"""
        return _ida_range.rangevec_base_t_empty(self, *args)

    def at(self, *args):
        r"""at(self, _idx) -> range_t"""
        return _ida_range.rangevec_base_t_at(self, *args)

    def qclear(self, *args):
        r"""qclear(self)"""
        return _ida_range.rangevec_base_t_qclear(self, *args)

    def clear(self, *args):
        r"""clear(self)"""
        return _ida_range.rangevec_base_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)
        resize(self, _newsize)
        """
        return _ida_range.rangevec_base_t_resize(self, *args)

    def grow(self, *args):
        r"""grow(self, x=range_t())"""
        return _ida_range.rangevec_base_t_grow(self, *args)

    def capacity(self, *args):
        r"""capacity(self) -> size_t"""
        return _ida_range.rangevec_base_t_capacity(self, *args)

    def reserve(self, *args):
        r"""reserve(self, cnt)"""
        return _ida_range.rangevec_base_t_reserve(self, *args)

    def truncate(self, *args):
        r"""truncate(self)"""
        return _ida_range.rangevec_base_t_truncate(self, *args)

    def swap(self, *args):
        r"""swap(self, r)"""
        return _ida_range.rangevec_base_t_swap(self, *args)

    def extract(self, *args):
        r"""extract(self) -> range_t"""
        return _ida_range.rangevec_base_t_extract(self, *args)

    def inject(self, *args):
        r"""inject(self, s, len)"""
        return _ida_range.rangevec_base_t_inject(self, *args)

    def __eq__(self, *args):
        r"""__eq__(self, r) -> bool"""
        return _ida_range.rangevec_base_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""__ne__(self, r) -> bool"""
        return _ida_range.rangevec_base_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> range_t
        begin(self) -> range_t
        """
        return _ida_range.rangevec_base_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> range_t
        end(self) -> range_t
        """
        return _ida_range.rangevec_base_t_end(self, *args)

    def insert(self, *args):
        r"""insert(self, it, x) -> range_t"""
        return _ida_range.rangevec_base_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> range_t
        erase(self, first, last) -> range_t
        """
        return _ida_range.rangevec_base_t_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> range_t
        find(self, x) -> range_t
        """
        return _ida_range.rangevec_base_t_find(self, *args)

    def has(self, *args):
        r"""has(self, x) -> bool"""
        return _ida_range.rangevec_base_t_has(self, *args)

    def add_unique(self, *args):
        r"""add_unique(self, x) -> bool"""
        return _ida_range.rangevec_base_t_add_unique(self, *args)

    def _del(self, *args):
        r"""_del(self, x) -> bool"""
        return _ida_range.rangevec_base_t__del(self, *args)

    def __len__(self, *args):
        r"""__len__(self) -> size_t"""
        return _ida_range.rangevec_base_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""__getitem__(self, i) -> range_t"""
        return _ida_range.rangevec_base_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""__setitem__(self, i, v)"""
        return _ida_range.rangevec_base_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register rangevec_base_t in _ida_range:
_ida_range.rangevec_base_t_swigregister(rangevec_base_t)

class array_of_rangesets(object):
    r"""Proxy of C++ qvector< rangeset_t > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> array_of_rangesets
        __init__(self, x) -> array_of_rangesets
        """
        _ida_range.array_of_rangesets_swiginit(self, _ida_range.new_array_of_rangesets(*args))
    __swig_destroy__ = _ida_range.delete_array_of_rangesets

    def push_back(self, *args):
        r"""
        push_back(self, x)
        push_back(self) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_push_back(self, *args)

    def pop_back(self, *args):
        r"""pop_back(self)"""
        return _ida_range.array_of_rangesets_pop_back(self, *args)

    def size(self, *args):
        r"""size(self) -> size_t"""
        return _ida_range.array_of_rangesets_size(self, *args)

    def empty(self, *args):
        r"""empty(self) -> bool"""
        return _ida_range.array_of_rangesets_empty(self, *args)

    def at(self, *args):
        r"""at(self, _idx) -> rangeset_t"""
        return _ida_range.array_of_rangesets_at(self, *args)

    def qclear(self, *args):
        r"""qclear(self)"""
        return _ida_range.array_of_rangesets_qclear(self, *args)

    def clear(self, *args):
        r"""clear(self)"""
        return _ida_range.array_of_rangesets_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)
        resize(self, _newsize)
        """
        return _ida_range.array_of_rangesets_resize(self, *args)

    def grow(self, *args):
        r"""grow(self, x=rangeset_t())"""
        return _ida_range.array_of_rangesets_grow(self, *args)

    def capacity(self, *args):
        r"""capacity(self) -> size_t"""
        return _ida_range.array_of_rangesets_capacity(self, *args)

    def reserve(self, *args):
        r"""reserve(self, cnt)"""
        return _ida_range.array_of_rangesets_reserve(self, *args)

    def truncate(self, *args):
        r"""truncate(self)"""
        return _ida_range.array_of_rangesets_truncate(self, *args)

    def swap(self, *args):
        r"""swap(self, r)"""
        return _ida_range.array_of_rangesets_swap(self, *args)

    def extract(self, *args):
        r"""extract(self) -> rangeset_t"""
        return _ida_range.array_of_rangesets_extract(self, *args)

    def inject(self, *args):
        r"""inject(self, s, len)"""
        return _ida_range.array_of_rangesets_inject(self, *args)

    def __eq__(self, *args):
        r"""__eq__(self, r) -> bool"""
        return _ida_range.array_of_rangesets___eq__(self, *args)

    def __ne__(self, *args):
        r"""__ne__(self, r) -> bool"""
        return _ida_range.array_of_rangesets___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> rangeset_t
        begin(self) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> rangeset_t
        end(self) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_end(self, *args)

    def insert(self, *args):
        r"""insert(self, it, x) -> rangeset_t"""
        return _ida_range.array_of_rangesets_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> rangeset_t
        erase(self, first, last) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> rangeset_t
        find(self, x) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_find(self, *args)

    def has(self, *args):
        r"""has(self, x) -> bool"""
        return _ida_range.array_of_rangesets_has(self, *args)

    def add_unique(self, *args):
        r"""add_unique(self, x) -> bool"""
        return _ida_range.array_of_rangesets_add_unique(self, *args)

    def _del(self, *args):
        r"""_del(self, x) -> bool"""
        return _ida_range.array_of_rangesets__del(self, *args)

    def __len__(self, *args):
        r"""__len__(self) -> size_t"""
        return _ida_range.array_of_rangesets___len__(self, *args)

    def __getitem__(self, *args):
        r"""__getitem__(self, i) -> rangeset_t"""
        return _ida_range.array_of_rangesets___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""__setitem__(self, i, v)"""
        return _ida_range.array_of_rangesets___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register array_of_rangesets in _ida_range:
_ida_range.array_of_rangesets_swigregister(array_of_rangesets)

class range_t(object):
    r"""Proxy of C++ range_t class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    start_ea = property(_ida_range.range_t_start_ea_get, _ida_range.range_t_start_ea_set, doc=r"""start_ea""")
    end_ea = property(_ida_range.range_t_end_ea_get, _ida_range.range_t_end_ea_set, doc=r"""end_ea""")

    def __init__(self, *args):
        r"""
        __init__(self) -> range_t
        __init__(self, ea1, ea2) -> range_t
        """
        _ida_range.range_t_swiginit(self, _ida_range.new_range_t(*args))

    def compare(self, *args):
        r"""compare(self, r) -> int"""
        return _ida_range.range_t_compare(self, *args)

    def __eq__(self, *args):
        r"""__eq__(self, r) -> bool"""
        return _ida_range.range_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""__ne__(self, r) -> bool"""
        return _ida_range.range_t___ne__(self, *args)

    def __gt__(self, *args):
        r"""__gt__(self, r) -> bool"""
        return _ida_range.range_t___gt__(self, *args)

    def __lt__(self, *args):
        r"""__lt__(self, r) -> bool"""
        return _ida_range.range_t___lt__(self, *args)

    def contains(self, *args):
        r"""
        contains(self, ea) -> bool
        contains(self, r) -> bool
        """
        return _ida_range.range_t_contains(self, *args)

    def overlaps(self, *args):
        r"""overlaps(self, r) -> bool"""
        return _ida_range.range_t_overlaps(self, *args)

    def clear(self, *args):
        r"""clear(self)"""
        return _ida_range.range_t_clear(self, *args)

    def empty(self, *args):
        r"""empty(self) -> bool"""
        return _ida_range.range_t_empty(self, *args)

    def size(self, *args):
        r"""size(self) -> asize_t"""
        return _ida_range.range_t_size(self, *args)

    def intersect(self, *args):
        r"""intersect(self, r)"""
        return _ida_range.range_t_intersect(self, *args)

    def extend(self, *args):
        r"""extend(self, ea)"""
        return _ida_range.range_t_extend(self, *args)

    def _print(self, *args):
        r"""_print(self) -> size_t"""
        return _ida_range.range_t__print(self, *args)
    __swig_destroy__ = _ida_range.delete_range_t

# Register range_t in _ida_range:
_ida_range.range_t_swigregister(range_t)

def range_t_print(*args):
    r"""range_t_print(cb) -> size_t"""
    return _ida_range.range_t_print(*args)

class rangevec_t(rangevec_base_t):
    r"""Proxy of C++ rangevec_t class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""__init__(self) -> rangevec_t"""
        _ida_range.rangevec_t_swiginit(self, _ida_range.new_rangevec_t(*args))
    __swig_destroy__ = _ida_range.delete_rangevec_t

# Register rangevec_t in _ida_range:
_ida_range.rangevec_t_swigregister(rangevec_t)

RANGE_KIND_UNKNOWN = _ida_range.RANGE_KIND_UNKNOWN

RANGE_KIND_FUNC = _ida_range.RANGE_KIND_FUNC

RANGE_KIND_SEGMENT = _ida_range.RANGE_KIND_SEGMENT

RANGE_KIND_HIDDEN_RANGE = _ida_range.RANGE_KIND_HIDDEN_RANGE

class rangeset_t(object):
    r"""Proxy of C++ rangeset_t class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> rangeset_t
        __init__(self, range) -> rangeset_t
        __init__(self, ivs) -> rangeset_t
        """
        _ida_range.rangeset_t_swiginit(self, _ida_range.new_rangeset_t(*args))

    def swap(self, *args):
        r"""swap(self, r)"""
        return _ida_range.rangeset_t_swap(self, *args)

    def add(self, *args):
        r"""
        add(self, range) -> bool
        add(self, start, _end) -> bool
        add(self, aset) -> bool
        """
        return _ida_range.rangeset_t_add(self, *args)

    def sub(self, *args):
        r"""
        sub(self, range) -> bool
        sub(self, ea) -> bool
        sub(self, aset) -> bool
        """
        return _ida_range.rangeset_t_sub(self, *args)

    def includes(self, *args):
        r"""includes(self, range) -> bool"""
        return _ida_range.rangeset_t_includes(self, *args)

    def _print(self, *args):
        r"""_print(self) -> size_t"""
        return _ida_range.rangeset_t__print(self, *args)

    def getrange(self, *args):
        r"""getrange(self, idx) -> range_t"""
        return _ida_range.rangeset_t_getrange(self, *args)

    def lastrange(self, *args):
        r"""lastrange(self) -> range_t"""
        return _ida_range.rangeset_t_lastrange(self, *args)

    def nranges(self, *args):
        r"""nranges(self) -> size_t"""
        return _ida_range.rangeset_t_nranges(self, *args)

    def empty(self, *args):
        r"""empty(self) -> bool"""
        return _ida_range.rangeset_t_empty(self, *args)

    def clear(self, *args):
        r"""clear(self)"""
        return _ida_range.rangeset_t_clear(self, *args)

    def has_common(self, *args):
        r"""
        has_common(self, range) -> bool
        has_common(self, aset) -> bool
        """
        return _ida_range.rangeset_t_has_common(self, *args)

    def contains(self, *args):
        r"""
        contains(self, ea) -> bool
        contains(self, aset) -> bool
        """
        return _ida_range.rangeset_t_contains(self, *args)

    def intersect(self, *args):
        r"""intersect(self, aset) -> bool"""
        return _ida_range.rangeset_t_intersect(self, *args)

    def is_subset_of(self, *args):
        r"""is_subset_of(self, aset) -> bool"""
        return _ida_range.rangeset_t_is_subset_of(self, *args)

    def is_equal(self, *args):
        r"""is_equal(self, aset) -> bool"""
        return _ida_range.rangeset_t_is_equal(self, *args)

    def __eq__(self, *args):
        r"""__eq__(self, aset) -> bool"""
        return _ida_range.rangeset_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""__ne__(self, aset) -> bool"""
        return _ida_range.rangeset_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> range_t
        begin(self) -> range_t
        """
        return _ida_range.rangeset_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> range_t
        end(self) -> range_t
        """
        return _ida_range.rangeset_t_end(self, *args)

    def find_range(self, *args):
        r"""find_range(self, ea) -> range_t"""
        return _ida_range.rangeset_t_find_range(self, *args)

    def cached_range(self, *args):
        r"""cached_range(self) -> range_t"""
        return _ida_range.rangeset_t_cached_range(self, *args)

    def next_addr(self, *args):
        r"""next_addr(self, ea) -> ea_t"""
        return _ida_range.rangeset_t_next_addr(self, *args)

    def prev_addr(self, *args):
        r"""prev_addr(self, ea) -> ea_t"""
        return _ida_range.rangeset_t_prev_addr(self, *args)

    def next_range(self, *args):
        r"""next_range(self, ea) -> ea_t"""
        return _ida_range.rangeset_t_next_range(self, *args)

    def prev_range(self, *args):
        r"""prev_range(self, ea) -> ea_t"""
        return _ida_range.rangeset_t_prev_range(self, *args)

    def __getitem__(self, idx):
        return self.getrange(idx)

    import ida_idaapi
    __len__ = nranges
    __iter__ = ida_idaapi._bounded_getitem_iterator

    __swig_destroy__ = _ida_range.delete_rangeset_t

# Register rangeset_t in _ida_range:
_ida_range.rangeset_t_swigregister(rangeset_t)


if _BC695:
    import sys
    sys.modules["ida_area"] = sys.modules["ida_range"]
    area_t = range_t
    areaset_t = rangeset_t
    def __set_startEA(inst, v):
        inst.start_ea = v
    range_t.startEA = property(lambda self: self.start_ea, __set_startEA)
    def __set_endEA(inst, v):
        inst.end_ea = v
    range_t.endEA = property(lambda self: self.end_ea, __set_endEA)



