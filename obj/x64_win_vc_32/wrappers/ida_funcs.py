# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""IDA Plugin SDK API wrapper: funcs"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_funcs
else:
    import _ida_funcs

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

import ida_range
class stkpnt_array(object):
    r"""Proxy of C++ dynamic_wrapped_array_t< stkpnt_t > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    data = property(_ida_funcs.stkpnt_array_data_get, doc=r"""data""")
    count = property(_ida_funcs.stkpnt_array_count_get, doc=r"""count""")

    def __init__(self, *args):
        r"""__init__(self, _data, _count) -> stkpnt_array"""
        _ida_funcs.stkpnt_array_swiginit(self, _ida_funcs.new_stkpnt_array(*args))

    def __len__(self, *args):
        r"""__len__(self) -> size_t"""
        return _ida_funcs.stkpnt_array___len__(self, *args)

    def __getitem__(self, *args):
        r"""__getitem__(self, i) -> stkpnt_t const &"""
        return _ida_funcs.stkpnt_array___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""__setitem__(self, i, v)"""
        return _ida_funcs.stkpnt_array___setitem__(self, *args)

    __iter__ = ida_idaapi._bounded_getitem_iterator

    __swig_destroy__ = _ida_funcs.delete_stkpnt_array

# Register stkpnt_array in _ida_funcs:
_ida_funcs.stkpnt_array_swigregister(stkpnt_array)

class regvar_array(object):
    r"""Proxy of C++ dynamic_wrapped_array_t< regvar_t > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    data = property(_ida_funcs.regvar_array_data_get, doc=r"""data""")
    count = property(_ida_funcs.regvar_array_count_get, doc=r"""count""")

    def __init__(self, *args):
        r"""__init__(self, _data, _count) -> regvar_array"""
        _ida_funcs.regvar_array_swiginit(self, _ida_funcs.new_regvar_array(*args))

    def __len__(self, *args):
        r"""__len__(self) -> size_t"""
        return _ida_funcs.regvar_array___len__(self, *args)

    def __getitem__(self, *args):
        r"""__getitem__(self, i) -> regvar_t const &"""
        return _ida_funcs.regvar_array___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""__setitem__(self, i, v)"""
        return _ida_funcs.regvar_array___setitem__(self, *args)

    __iter__ = ida_idaapi._bounded_getitem_iterator

    __swig_destroy__ = _ida_funcs.delete_regvar_array

# Register regvar_array in _ida_funcs:
_ida_funcs.regvar_array_swigregister(regvar_array)

class range_array(object):
    r"""Proxy of C++ dynamic_wrapped_array_t< range_t > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    data = property(_ida_funcs.range_array_data_get, doc=r"""data""")
    count = property(_ida_funcs.range_array_count_get, doc=r"""count""")

    def __init__(self, *args):
        r"""__init__(self, _data, _count) -> range_array"""
        _ida_funcs.range_array_swiginit(self, _ida_funcs.new_range_array(*args))

    def __len__(self, *args):
        r"""__len__(self) -> size_t"""
        return _ida_funcs.range_array___len__(self, *args)

    def __getitem__(self, *args):
        r"""__getitem__(self, i) -> range_t"""
        return _ida_funcs.range_array___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""__setitem__(self, i, v)"""
        return _ida_funcs.range_array___setitem__(self, *args)

    __iter__ = ida_idaapi._bounded_getitem_iterator

    __swig_destroy__ = _ida_funcs.delete_range_array

# Register range_array in _ida_funcs:
_ida_funcs.range_array_swigregister(range_array)

class regarg_t(object):
    r"""Proxy of C++ regarg_t class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    reg = property(_ida_funcs.regarg_t_reg_get, _ida_funcs.regarg_t_reg_set, doc=r"""reg""")
    type = property(_ida_funcs.regarg_t_type_get, _ida_funcs.regarg_t_type_set, doc=r"""type""")
    name = property(_ida_funcs.regarg_t_name_get, _ida_funcs.regarg_t_name_set, doc=r"""name""")

    def __init__(self, *args):
        r"""__init__(self) -> regarg_t"""
        _ida_funcs.regarg_t_swiginit(self, _ida_funcs.new_regarg_t(*args))
    __swig_destroy__ = _ida_funcs.delete_regarg_t

# Register regarg_t in _ida_funcs:
_ida_funcs.regarg_t_swigregister(regarg_t)

class func_t(ida_range.range_t):
    r"""Proxy of C++ func_t class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    flags = property(_ida_funcs.func_t_flags_get, _ida_funcs.func_t_flags_set, doc=r"""flags""")

    def is_far(self, *args):
        r"""is_far(self) -> bool"""
        return _ida_funcs.func_t_is_far(self, *args)

    def does_return(self, *args):
        r"""does_return(self) -> bool"""
        return _ida_funcs.func_t_does_return(self, *args)

    def analyzed_sp(self, *args):
        r"""analyzed_sp(self) -> bool"""
        return _ida_funcs.func_t_analyzed_sp(self, *args)

    def need_prolog_analysis(self, *args):
        r"""need_prolog_analysis(self) -> bool"""
        return _ida_funcs.func_t_need_prolog_analysis(self, *args)
    frame = property(_ida_funcs.func_t_frame_get, _ida_funcs.func_t_frame_set, doc=r"""frame""")
    frsize = property(_ida_funcs.func_t_frsize_get, _ida_funcs.func_t_frsize_set, doc=r"""frsize""")
    frregs = property(_ida_funcs.func_t_frregs_get, _ida_funcs.func_t_frregs_set, doc=r"""frregs""")
    argsize = property(_ida_funcs.func_t_argsize_get, _ida_funcs.func_t_argsize_set, doc=r"""argsize""")
    fpd = property(_ida_funcs.func_t_fpd_get, _ida_funcs.func_t_fpd_set, doc=r"""fpd""")
    color = property(_ida_funcs.func_t_color_get, _ida_funcs.func_t_color_set, doc=r"""color""")
    pntqty = property(_ida_funcs.func_t_pntqty_get, _ida_funcs.func_t_pntqty_set, doc=r"""pntqty""")
    points = property(_ida_funcs.func_t_points_get, _ida_funcs.func_t_points_set, doc=r"""points""")
    regvarqty = property(_ida_funcs.func_t_regvarqty_get, _ida_funcs.func_t_regvarqty_set, doc=r"""regvarqty""")
    regvars = property(_ida_funcs.func_t_regvars_get, _ida_funcs.func_t_regvars_set, doc=r"""regvars""")
    llabelqty = property(_ida_funcs.func_t_llabelqty_get, _ida_funcs.func_t_llabelqty_set, doc=r"""llabelqty""")
    llabels = property(_ida_funcs.func_t_llabels_get, _ida_funcs.func_t_llabels_set, doc=r"""llabels""")
    regargqty = property(_ida_funcs.func_t_regargqty_get, _ida_funcs.func_t_regargqty_set, doc=r"""regargqty""")
    regargs = property(_ida_funcs.func_t_regargs_get, _ida_funcs.func_t_regargs_set, doc=r"""regargs""")
    tailqty = property(_ida_funcs.func_t_tailqty_get, _ida_funcs.func_t_tailqty_set, doc=r"""tailqty""")
    tails = property(_ida_funcs.func_t_tails_get, _ida_funcs.func_t_tails_set, doc=r"""tails""")
    owner = property(_ida_funcs.func_t_owner_get, _ida_funcs.func_t_owner_set, doc=r"""owner""")
    refqty = property(_ida_funcs.func_t_refqty_get, _ida_funcs.func_t_refqty_set, doc=r"""refqty""")
    referers = property(_ida_funcs.func_t_referers_get, _ida_funcs.func_t_referers_set, doc=r"""referers""")

    def __init__(self, *args):
        r"""__init__(self, start=0, end=0, f=0) -> func_t"""
        _ida_funcs.func_t_swiginit(self, _ida_funcs.new_func_t(*args))

    def __get_points__(self, *args):
        r"""__get_points__(self) -> stkpnt_array"""
        return _ida_funcs.func_t___get_points__(self, *args)

    def __get_regvars__(self, *args):
        r"""__get_regvars__(self) -> regvar_array"""
        return _ida_funcs.func_t___get_regvars__(self, *args)

    def __get_tails__(self, *args):
        r"""__get_tails__(self) -> range_array"""
        return _ida_funcs.func_t___get_tails__(self, *args)

    points = property(__get_points__)
    regvars = property(__get_regvars__)
    tails = property(__get_tails__)

    __swig_destroy__ = _ida_funcs.delete_func_t

# Register func_t in _ida_funcs:
_ida_funcs.func_t_swigregister(func_t)
FUNC_NORET = _ida_funcs.FUNC_NORET

FUNC_FAR = _ida_funcs.FUNC_FAR

FUNC_LIB = _ida_funcs.FUNC_LIB

FUNC_STATICDEF = _ida_funcs.FUNC_STATICDEF

FUNC_FRAME = _ida_funcs.FUNC_FRAME

FUNC_USERFAR = _ida_funcs.FUNC_USERFAR

FUNC_HIDDEN = _ida_funcs.FUNC_HIDDEN

FUNC_THUNK = _ida_funcs.FUNC_THUNK

FUNC_BOTTOMBP = _ida_funcs.FUNC_BOTTOMBP

FUNC_NORET_PENDING = _ida_funcs.FUNC_NORET_PENDING

FUNC_SP_READY = _ida_funcs.FUNC_SP_READY

FUNC_FUZZY_SP = _ida_funcs.FUNC_FUZZY_SP

FUNC_PROLOG_OK = _ida_funcs.FUNC_PROLOG_OK

FUNC_PURGED_OK = _ida_funcs.FUNC_PURGED_OK

FUNC_TAIL = _ida_funcs.FUNC_TAIL

FUNC_LUMINA = _ida_funcs.FUNC_LUMINA



def is_func_entry(*args):
    r"""is_func_entry(pfn) -> bool"""
    return _ida_funcs.is_func_entry(*args)

def is_func_tail(*args):
    r"""is_func_tail(pfn) -> bool"""
    return _ida_funcs.is_func_tail(*args)

def lock_func_range(*args):
    r"""lock_func_range(pfn, lock)"""
    return _ida_funcs.lock_func_range(*args)
class lock_func(object):
    r"""Proxy of C++ lock_func class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""__init__(self, _pfn) -> lock_func"""
        _ida_funcs.lock_func_swiginit(self, _ida_funcs.new_lock_func(*args))
    __swig_destroy__ = _ida_funcs.delete_lock_func

# Register lock_func in _ida_funcs:
_ida_funcs.lock_func_swigregister(lock_func)


def is_func_locked(*args):
    r"""is_func_locked(pfn) -> bool"""
    return _ida_funcs.is_func_locked(*args)

def get_func(*args):
    r"""get_func(ea) -> func_t"""
    return _ida_funcs.get_func(*args)

def get_func_chunknum(*args):
    r"""get_func_chunknum(pfn, ea) -> int"""
    return _ida_funcs.get_func_chunknum(*args)

def func_contains(*args):
    r"""func_contains(pfn, ea) -> bool"""
    return _ida_funcs.func_contains(*args)

def is_same_func(*args):
    r"""is_same_func(ea1, ea2) -> bool"""
    return _ida_funcs.is_same_func(*args)

def getn_func(*args):
    r"""getn_func(n) -> func_t"""
    return _ida_funcs.getn_func(*args)

def get_func_qty(*args):
    r"""get_func_qty() -> size_t"""
    return _ida_funcs.get_func_qty(*args)

def get_func_num(*args):
    r"""get_func_num(ea) -> int"""
    return _ida_funcs.get_func_num(*args)

def get_prev_func(*args):
    r"""get_prev_func(ea) -> func_t"""
    return _ida_funcs.get_prev_func(*args)

def get_next_func(*args):
    r"""get_next_func(ea) -> func_t"""
    return _ida_funcs.get_next_func(*args)

def get_func_ranges(*args):
    r"""get_func_ranges(ranges, pfn) -> ea_t"""
    return _ida_funcs.get_func_ranges(*args)

def get_func_cmt(*args):
    r"""get_func_cmt(pfn, repeatable) -> ssize_t"""
    return _ida_funcs.get_func_cmt(*args)

def set_func_cmt(*args):
    r"""set_func_cmt(pfn, cmt, repeatable) -> bool"""
    return _ida_funcs.set_func_cmt(*args)

def update_func(*args):
    r"""update_func(pfn) -> bool"""
    return _ida_funcs.update_func(*args)

def add_func_ex(*args):
    r"""add_func_ex(pfn) -> bool"""
    return _ida_funcs.add_func_ex(*args)

def add_func(*args):
    r"""add_func(ea1, ea2=BADADDR) -> bool"""
    return _ida_funcs.add_func(*args)

def del_func(*args):
    r"""del_func(ea) -> bool"""
    return _ida_funcs.del_func(*args)

def set_func_start(*args):
    r"""set_func_start(ea, newstart) -> int"""
    return _ida_funcs.set_func_start(*args)
MOVE_FUNC_OK = _ida_funcs.MOVE_FUNC_OK

MOVE_FUNC_NOCODE = _ida_funcs.MOVE_FUNC_NOCODE

MOVE_FUNC_BADSTART = _ida_funcs.MOVE_FUNC_BADSTART

MOVE_FUNC_NOFUNC = _ida_funcs.MOVE_FUNC_NOFUNC

MOVE_FUNC_REFUSED = _ida_funcs.MOVE_FUNC_REFUSED


def set_func_end(*args):
    r"""set_func_end(ea, newend) -> bool"""
    return _ida_funcs.set_func_end(*args)

def reanalyze_function(*args):
    r"""reanalyze_function(pfn, ea1=0, ea2=BADADDR, analyze_parents=False)"""
    return _ida_funcs.reanalyze_function(*args)

def find_func_bounds(*args):
    r"""find_func_bounds(nfn, flags) -> int"""
    return _ida_funcs.find_func_bounds(*args)
FIND_FUNC_NORMAL = _ida_funcs.FIND_FUNC_NORMAL

FIND_FUNC_DEFINE = _ida_funcs.FIND_FUNC_DEFINE

FIND_FUNC_IGNOREFN = _ida_funcs.FIND_FUNC_IGNOREFN

FIND_FUNC_KEEPBD = _ida_funcs.FIND_FUNC_KEEPBD

FIND_FUNC_UNDEF = _ida_funcs.FIND_FUNC_UNDEF

FIND_FUNC_OK = _ida_funcs.FIND_FUNC_OK

FIND_FUNC_EXIST = _ida_funcs.FIND_FUNC_EXIST


def get_func_name(*args):
    r"""get_func_name(ea) -> ssize_t"""
    return _ida_funcs.get_func_name(*args)

def calc_func_size(*args):
    r"""calc_func_size(pfn) -> asize_t"""
    return _ida_funcs.calc_func_size(*args)

def get_func_bitness(*args):
    r"""get_func_bitness(pfn) -> int"""
    return _ida_funcs.get_func_bitness(*args)

def get_func_bits(*args):
    r"""get_func_bits(pfn) -> int"""
    return _ida_funcs.get_func_bits(*args)

def get_func_bytes(*args):
    r"""get_func_bytes(pfn) -> int"""
    return _ida_funcs.get_func_bytes(*args)

def is_visible_func(*args):
    r"""is_visible_func(pfn) -> bool"""
    return _ida_funcs.is_visible_func(*args)

def is_finally_visible_func(*args):
    r"""is_finally_visible_func(pfn) -> bool"""
    return _ida_funcs.is_finally_visible_func(*args)

def set_visible_func(*args):
    r"""set_visible_func(pfn, visible)"""
    return _ida_funcs.set_visible_func(*args)

def set_func_name_if_jumpfunc(*args):
    r"""set_func_name_if_jumpfunc(pfn, oldname) -> int"""
    return _ida_funcs.set_func_name_if_jumpfunc(*args)

def calc_thunk_func_target(*args):
    r"""calc_thunk_func_target(pfn) -> ea_t"""
    return _ida_funcs.calc_thunk_func_target(*args)

def func_does_return(*args):
    r"""func_does_return(callee) -> bool"""
    return _ida_funcs.func_does_return(*args)

def reanalyze_noret_flag(*args):
    r"""reanalyze_noret_flag(ea) -> bool"""
    return _ida_funcs.reanalyze_noret_flag(*args)

def set_noret_insn(*args):
    r"""set_noret_insn(insn_ea, noret) -> bool"""
    return _ida_funcs.set_noret_insn(*args)

def get_fchunk(*args):
    r"""get_fchunk(ea) -> func_t"""
    return _ida_funcs.get_fchunk(*args)

def getn_fchunk(*args):
    r"""getn_fchunk(n) -> func_t"""
    return _ida_funcs.getn_fchunk(*args)

def get_fchunk_qty(*args):
    r"""get_fchunk_qty() -> size_t"""
    return _ida_funcs.get_fchunk_qty(*args)

def get_fchunk_num(*args):
    r"""get_fchunk_num(ea) -> int"""
    return _ida_funcs.get_fchunk_num(*args)

def get_prev_fchunk(*args):
    r"""get_prev_fchunk(ea) -> func_t"""
    return _ida_funcs.get_prev_fchunk(*args)

def get_next_fchunk(*args):
    r"""get_next_fchunk(ea) -> func_t"""
    return _ida_funcs.get_next_fchunk(*args)

def append_func_tail(*args):
    r"""append_func_tail(pfn, ea1, ea2) -> bool"""
    return _ida_funcs.append_func_tail(*args)

def remove_func_tail(*args):
    r"""remove_func_tail(pfn, tail_ea) -> bool"""
    return _ida_funcs.remove_func_tail(*args)

def set_tail_owner(*args):
    r"""set_tail_owner(fnt, func_start) -> bool"""
    return _ida_funcs.set_tail_owner(*args)

def func_tail_iterator_set(*args):
    r"""func_tail_iterator_set(fti, pfn, ea) -> bool"""
    return _ida_funcs.func_tail_iterator_set(*args)

def func_tail_iterator_set_ea(*args):
    r"""func_tail_iterator_set_ea(fti, ea) -> bool"""
    return _ida_funcs.func_tail_iterator_set_ea(*args)

def func_parent_iterator_set(*args):
    r"""func_parent_iterator_set(fpi, pfn) -> bool"""
    return _ida_funcs.func_parent_iterator_set(*args)

def func_item_iterator_next(*args):
    r"""func_item_iterator_next(fii, testf, ud) -> bool"""
    return _ida_funcs.func_item_iterator_next(*args)

def func_item_iterator_prev(*args):
    r"""func_item_iterator_prev(fii, testf, ud) -> bool"""
    return _ida_funcs.func_item_iterator_prev(*args)

def func_item_iterator_decode_prev_insn(*args):
    r"""func_item_iterator_decode_prev_insn(fii, out) -> bool"""
    return _ida_funcs.func_item_iterator_decode_prev_insn(*args)

def func_item_iterator_decode_preceding_insn(*args):
    r"""func_item_iterator_decode_preceding_insn(fii, visited, p_farref, out) -> bool"""
    return _ida_funcs.func_item_iterator_decode_preceding_insn(*args)

def f_any(*args):
    r"""f_any(arg1, arg2) -> bool"""
    return _ida_funcs.f_any(*args)
class func_tail_iterator_t(object):
    r"""Proxy of C++ func_tail_iterator_t class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> func_tail_iterator_t
        __init__(self, _pfn, ea=BADADDR) -> func_tail_iterator_t
        """
        _ida_funcs.func_tail_iterator_t_swiginit(self, _ida_funcs.new_func_tail_iterator_t(*args))
    __swig_destroy__ = _ida_funcs.delete_func_tail_iterator_t

    def set(self, *args):
        r"""set(self, _pfn, ea=BADADDR) -> bool"""
        return _ida_funcs.func_tail_iterator_t_set(self, *args)

    def set_ea(self, *args):
        r"""set_ea(self, ea) -> bool"""
        return _ida_funcs.func_tail_iterator_t_set_ea(self, *args)

    def set_range(self, *args):
        r"""set_range(self, ea1, ea2) -> bool"""
        return _ida_funcs.func_tail_iterator_t_set_range(self, *args)

    def chunk(self, *args):
        r"""chunk(self) -> range_t"""
        return _ida_funcs.func_tail_iterator_t_chunk(self, *args)

    def first(self, *args):
        r"""first(self) -> bool"""
        return _ida_funcs.func_tail_iterator_t_first(self, *args)

    def last(self, *args):
        r"""last(self) -> bool"""
        return _ida_funcs.func_tail_iterator_t_last(self, *args)

    def next(self, *args):
        r"""next(self) -> bool"""
        return _ida_funcs.func_tail_iterator_t_next(self, *args)

    def prev(self, *args):
        r"""prev(self) -> bool"""
        return _ida_funcs.func_tail_iterator_t_prev(self, *args)

    def main(self, *args):
        r"""main(self) -> bool"""
        return _ida_funcs.func_tail_iterator_t_main(self, *args)

# Register func_tail_iterator_t in _ida_funcs:
_ida_funcs.func_tail_iterator_t_swigregister(func_tail_iterator_t)

class func_item_iterator_t(object):
    r"""Proxy of C++ func_item_iterator_t class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> func_item_iterator_t
        __init__(self, pfn, _ea=BADADDR) -> func_item_iterator_t
        """
        _ida_funcs.func_item_iterator_t_swiginit(self, _ida_funcs.new_func_item_iterator_t(*args))

    def set(self, *args):
        r"""set(self, pfn, _ea=BADADDR) -> bool"""
        return _ida_funcs.func_item_iterator_t_set(self, *args)

    def set_range(self, *args):
        r"""set_range(self, ea1, ea2) -> bool"""
        return _ida_funcs.func_item_iterator_t_set_range(self, *args)

    def first(self, *args):
        r"""first(self) -> bool"""
        return _ida_funcs.func_item_iterator_t_first(self, *args)

    def last(self, *args):
        r"""last(self) -> bool"""
        return _ida_funcs.func_item_iterator_t_last(self, *args)

    def current(self, *args):
        r"""current(self) -> ea_t"""
        return _ida_funcs.func_item_iterator_t_current(self, *args)

    def chunk(self, *args):
        r"""chunk(self) -> range_t"""
        return _ida_funcs.func_item_iterator_t_chunk(self, *args)

    def next(self, *args):
        r"""next(self, func, ud) -> bool"""
        return _ida_funcs.func_item_iterator_t_next(self, *args)

    def prev(self, *args):
        r"""prev(self, func, ud) -> bool"""
        return _ida_funcs.func_item_iterator_t_prev(self, *args)

    def next_addr(self, *args):
        r"""next_addr(self) -> bool"""
        return _ida_funcs.func_item_iterator_t_next_addr(self, *args)

    def next_head(self, *args):
        r"""next_head(self) -> bool"""
        return _ida_funcs.func_item_iterator_t_next_head(self, *args)

    def next_code(self, *args):
        r"""next_code(self) -> bool"""
        return _ida_funcs.func_item_iterator_t_next_code(self, *args)

    def next_data(self, *args):
        r"""next_data(self) -> bool"""
        return _ida_funcs.func_item_iterator_t_next_data(self, *args)

    def next_not_tail(self, *args):
        r"""next_not_tail(self) -> bool"""
        return _ida_funcs.func_item_iterator_t_next_not_tail(self, *args)

    def prev_addr(self, *args):
        r"""prev_addr(self) -> bool"""
        return _ida_funcs.func_item_iterator_t_prev_addr(self, *args)

    def prev_head(self, *args):
        r"""prev_head(self) -> bool"""
        return _ida_funcs.func_item_iterator_t_prev_head(self, *args)

    def prev_code(self, *args):
        r"""prev_code(self) -> bool"""
        return _ida_funcs.func_item_iterator_t_prev_code(self, *args)

    def prev_data(self, *args):
        r"""prev_data(self) -> bool"""
        return _ida_funcs.func_item_iterator_t_prev_data(self, *args)

    def prev_not_tail(self, *args):
        r"""prev_not_tail(self) -> bool"""
        return _ida_funcs.func_item_iterator_t_prev_not_tail(self, *args)

    def decode_prev_insn(self, *args):
        r"""decode_prev_insn(self, out) -> bool"""
        return _ida_funcs.func_item_iterator_t_decode_prev_insn(self, *args)

    def decode_preceding_insn(self, *args):
        r"""decode_preceding_insn(self, visited, p_farref, out) -> bool"""
        return _ida_funcs.func_item_iterator_t_decode_preceding_insn(self, *args)
    __swig_destroy__ = _ida_funcs.delete_func_item_iterator_t

# Register func_item_iterator_t in _ida_funcs:
_ida_funcs.func_item_iterator_t_swigregister(func_item_iterator_t)

class func_parent_iterator_t(object):
    r"""Proxy of C++ func_parent_iterator_t class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> func_parent_iterator_t
        __init__(self, _fnt) -> func_parent_iterator_t
        """
        _ida_funcs.func_parent_iterator_t_swiginit(self, _ida_funcs.new_func_parent_iterator_t(*args))
    __swig_destroy__ = _ida_funcs.delete_func_parent_iterator_t

    def set(self, *args):
        r"""set(self, _fnt) -> bool"""
        return _ida_funcs.func_parent_iterator_t_set(self, *args)

    def parent(self, *args):
        r"""parent(self) -> ea_t"""
        return _ida_funcs.func_parent_iterator_t_parent(self, *args)

    def first(self, *args):
        r"""first(self) -> bool"""
        return _ida_funcs.func_parent_iterator_t_first(self, *args)

    def last(self, *args):
        r"""last(self) -> bool"""
        return _ida_funcs.func_parent_iterator_t_last(self, *args)

    def next(self, *args):
        r"""next(self) -> bool"""
        return _ida_funcs.func_parent_iterator_t_next(self, *args)

    def prev(self, *args):
        r"""prev(self) -> bool"""
        return _ida_funcs.func_parent_iterator_t_prev(self, *args)

    def reset_fnt(self, *args):
        r"""reset_fnt(self, _fnt)"""
        return _ida_funcs.func_parent_iterator_t_reset_fnt(self, *args)

# Register func_parent_iterator_t in _ida_funcs:
_ida_funcs.func_parent_iterator_t_swigregister(func_parent_iterator_t)


def get_prev_func_addr(*args):
    r"""get_prev_func_addr(pfn, ea) -> ea_t"""
    return _ida_funcs.get_prev_func_addr(*args)

def get_next_func_addr(*args):
    r"""get_next_func_addr(pfn, ea) -> ea_t"""
    return _ida_funcs.get_next_func_addr(*args)

def read_regargs(*args):
    r"""read_regargs(pfn)"""
    return _ida_funcs.read_regargs(*args)

def add_regarg(*args):
    r"""add_regarg(pfn, reg, tif, name)"""
    return _ida_funcs.add_regarg(*args)
IDASGN_OK = _ida_funcs.IDASGN_OK

IDASGN_BADARG = _ida_funcs.IDASGN_BADARG

IDASGN_APPLIED = _ida_funcs.IDASGN_APPLIED

IDASGN_CURRENT = _ida_funcs.IDASGN_CURRENT

IDASGN_PLANNED = _ida_funcs.IDASGN_PLANNED


def plan_to_apply_idasgn(*args):
    r"""plan_to_apply_idasgn(fname) -> int"""
    return _ida_funcs.plan_to_apply_idasgn(*args)

def apply_idasgn_to(*args):
    r"""apply_idasgn_to(signame, ea, is_startup) -> int"""
    return _ida_funcs.apply_idasgn_to(*args)

def get_idasgn_qty(*args):
    r"""get_idasgn_qty() -> int"""
    return _ida_funcs.get_idasgn_qty(*args)

def get_current_idasgn(*args):
    r"""get_current_idasgn() -> int"""
    return _ida_funcs.get_current_idasgn(*args)

def calc_idasgn_state(*args):
    r"""calc_idasgn_state(n) -> int"""
    return _ida_funcs.calc_idasgn_state(*args)

def del_idasgn(*args):
    r"""del_idasgn(n) -> int"""
    return _ida_funcs.del_idasgn(*args)

def get_idasgn_title(*args):
    r"""get_idasgn_title(name) -> ssize_t"""
    return _ida_funcs.get_idasgn_title(*args)

def apply_startup_sig(*args):
    r"""apply_startup_sig(ea, startup) -> bool"""
    return _ida_funcs.apply_startup_sig(*args)

def try_to_add_libfunc(*args):
    r"""try_to_add_libfunc(ea) -> int"""
    return _ida_funcs.try_to_add_libfunc(*args)
LIBFUNC_FOUND = _ida_funcs.LIBFUNC_FOUND

LIBFUNC_NONE = _ida_funcs.LIBFUNC_NONE

LIBFUNC_DELAY = _ida_funcs.LIBFUNC_DELAY


def get_fchunk_referer(*args):
    r"""get_fchunk_referer(ea, idx) -> ea_t"""
    return _ida_funcs.get_fchunk_referer(*args)

def get_idasgn_desc(*args):
    r"""get_idasgn_desc(n) -> PyObject *"""
    return _ida_funcs.get_idasgn_desc(*args)

def get_idasgn_desc_with_matches(*args):
    r"""get_idasgn_desc_with_matches(n) -> PyObject *"""
    return _ida_funcs.get_idasgn_desc_with_matches(*args)

def func_t__from_ptrval__(*args):
    r"""func_t__from_ptrval__(ptrval) -> func_t"""
    return _ida_funcs.func_t__from_ptrval__(*args)

#<pycode(py_funcs)>
import ida_idaapi
@ida_idaapi.replfun
def calc_thunk_func_target(*args):
    if len(args) == 2:
        pfn, rawptr = args
        target, fptr = calc_thunk_func_target.__dict__["orig"](pfn)
        import ida_pro
        ida_pro.ea_pointer.frompointer(rawptr).assign(fptr)
        return target
    else:
        return calc_thunk_func_target.__dict__["orig"](*args)
#</pycode(py_funcs)>


if _BC695:
    FUNC_STATIC=FUNC_STATICDEF
    add_regarg2=add_regarg
    clear_func_struct=lambda *args: True
    def del_func_cmt(pfn, rpt):
        set_func_cmt(pfn, "", rpt)
    func_parent_iterator_set2=func_parent_iterator_set
    func_setend=set_func_end
    func_setstart=set_func_start
    func_tail_iterator_set2=func_tail_iterator_set
    def get_func_limits(pfn, limits):
        import ida_range
        rs = ida_range.rangeset_t()
        if get_func_ranges(rs, pfn) == ida_idaapi.BADADDR:
            return False
        limits.start_ea = rs.begin().start_ea
        limits.end_ea = rs.begin().end_ea
        return True
    get_func_name2=get_func_name




