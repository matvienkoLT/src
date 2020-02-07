# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""IDA Plugin SDK API wrapper: segregs"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_segregs
else:
    import _ida_segregs

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
R_es = _ida_segregs.R_es

R_cs = _ida_segregs.R_cs

R_ss = _ida_segregs.R_ss

R_ds = _ida_segregs.R_ds

R_fs = _ida_segregs.R_fs

R_gs = _ida_segregs.R_gs

class sreg_range_t(ida_range.range_t):
    r"""Proxy of C++ sreg_range_t class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    val = property(_ida_segregs.sreg_range_t_val_get, _ida_segregs.sreg_range_t_val_set, doc=r"""val""")
    tag = property(_ida_segregs.sreg_range_t_tag_get, _ida_segregs.sreg_range_t_tag_set, doc=r"""tag""")

    def __init__(self, *args):
        r"""__init__(self) -> sreg_range_t"""
        _ida_segregs.sreg_range_t_swiginit(self, _ida_segregs.new_sreg_range_t(*args))
    __swig_destroy__ = _ida_segregs.delete_sreg_range_t

# Register sreg_range_t in _ida_segregs:
_ida_segregs.sreg_range_t_swigregister(sreg_range_t)
SR_inherit = _ida_segregs.SR_inherit

SR_user = _ida_segregs.SR_user

SR_auto = _ida_segregs.SR_auto

SR_autostart = _ida_segregs.SR_autostart



def get_sreg(*args):
    r"""get_sreg(ea, rg) -> sel_t"""
    return _ida_segregs.get_sreg(*args)

def split_sreg_range(*args):
    r"""split_sreg_range(ea, rg, v, tag, silent=False) -> bool"""
    return _ida_segregs.split_sreg_range(*args)

def set_default_sreg_value(*args):
    r"""set_default_sreg_value(sg, rg, value) -> bool"""
    return _ida_segregs.set_default_sreg_value(*args)

def set_sreg_at_next_code(*args):
    r"""set_sreg_at_next_code(ea1, ea2, rg, value)"""
    return _ida_segregs.set_sreg_at_next_code(*args)

def get_sreg_range(*args):
    r"""get_sreg_range(out, ea, rg) -> bool"""
    return _ida_segregs.get_sreg_range(*args)

def get_prev_sreg_range(*args):
    r"""get_prev_sreg_range(out, ea, rg) -> bool"""
    return _ida_segregs.get_prev_sreg_range(*args)

def set_default_dataseg(*args):
    r"""set_default_dataseg(ds_sel)"""
    return _ida_segregs.set_default_dataseg(*args)

def get_sreg_ranges_qty(*args):
    r"""get_sreg_ranges_qty(rg) -> size_t"""
    return _ida_segregs.get_sreg_ranges_qty(*args)

def getn_sreg_range(*args):
    r"""getn_sreg_range(out, rg, n) -> bool"""
    return _ida_segregs.getn_sreg_range(*args)

def get_sreg_range_num(*args):
    r"""get_sreg_range_num(ea, rg) -> int"""
    return _ida_segregs.get_sreg_range_num(*args)

def del_sreg_range(*args):
    r"""del_sreg_range(ea, rg) -> bool"""
    return _ida_segregs.del_sreg_range(*args)

def copy_sreg_ranges(*args):
    r"""copy_sreg_ranges(dst_rg, src_rg, map_selector=False)"""
    return _ida_segregs.copy_sreg_ranges(*args)

if _BC695:
    import sys
    sys.modules["ida_srarea"] = sys.modules["ida_segregs"]
    SetDefaultRegisterValue=set_default_sreg_value
    copy_srareas=copy_sreg_ranges
    def ___looks_like_ea_not_segreg(thing):
# yay heuristics. Not sure how best to do this...
        return (type(thing) == long) or (thing > 0x200)
    def del_sreg_range(*args):
        if ___looks_like_ea_not_segreg(args[1]): # 6.95: rg, ea
            ea, rg = args[1], args[0]
        else:                                    # 7.00: ea, rg
            ea, rg = args
        return _ida_segregs.del_sreg_range(ea, rg)
    del_srarea=del_sreg_range
    getSR=get_sreg
    get_prev_srarea=get_prev_sreg_range
    get_srarea2=get_sreg_range
    def get_sreg_range_num(*args):
        if ___looks_like_ea_not_segreg(args[1]): # 6.95: rg, ea
            ea, rg = args[1], args[0]
        else:                                    # 7.00: ea, rg
            ea, rg = args
        return _ida_segregs.get_sreg_range_num(ea, rg)
    get_srarea_num=get_sreg_range_num
    get_srareas_qty2=get_sreg_ranges_qty
    getn_srarea2=getn_sreg_range
    import ida_idaapi
    is_segreg_locked=ida_idaapi._BC695.false_p
    class lock_segreg:
        def __init__():
            pass
    segreg_area_t=sreg_range_t
    splitSRarea1=split_sreg_range
    split_srarea=split_sreg_range
    get_segreg=get_sreg
    set_default_segreg_value=set_default_sreg_value



