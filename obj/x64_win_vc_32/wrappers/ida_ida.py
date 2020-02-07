# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""IDA Plugin SDK API wrapper: ida"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_ida
else:
    import _ida_ida

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

f_EXE_old = _ida_ida.f_EXE_old

f_COM_old = _ida_ida.f_COM_old

f_BIN = _ida_ida.f_BIN

f_DRV = _ida_ida.f_DRV

f_WIN = _ida_ida.f_WIN

f_HEX = _ida_ida.f_HEX

f_MEX = _ida_ida.f_MEX

f_LX = _ida_ida.f_LX

f_LE = _ida_ida.f_LE

f_NLM = _ida_ida.f_NLM

f_COFF = _ida_ida.f_COFF

f_PE = _ida_ida.f_PE

f_OMF = _ida_ida.f_OMF

f_SREC = _ida_ida.f_SREC

f_ZIP = _ida_ida.f_ZIP

f_OMFLIB = _ida_ida.f_OMFLIB

f_AR = _ida_ida.f_AR

f_LOADER = _ida_ida.f_LOADER

f_ELF = _ida_ida.f_ELF

f_W32RUN = _ida_ida.f_W32RUN

f_AOUT = _ida_ida.f_AOUT

f_PRC = _ida_ida.f_PRC

f_EXE = _ida_ida.f_EXE

f_COM = _ida_ida.f_COM

f_AIXAR = _ida_ida.f_AIXAR

f_MACHO = _ida_ida.f_MACHO

class compiler_info_t(object):
    r"""Proxy of C++ compiler_info_t class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    id = property(_ida_ida.compiler_info_t_id_get, _ida_ida.compiler_info_t_id_set, doc=r"""id""")
    cm = property(_ida_ida.compiler_info_t_cm_get, _ida_ida.compiler_info_t_cm_set, doc=r"""cm""")
    size_i = property(_ida_ida.compiler_info_t_size_i_get, _ida_ida.compiler_info_t_size_i_set, doc=r"""size_i""")
    size_b = property(_ida_ida.compiler_info_t_size_b_get, _ida_ida.compiler_info_t_size_b_set, doc=r"""size_b""")
    size_e = property(_ida_ida.compiler_info_t_size_e_get, _ida_ida.compiler_info_t_size_e_set, doc=r"""size_e""")
    defalign = property(_ida_ida.compiler_info_t_defalign_get, _ida_ida.compiler_info_t_defalign_set, doc=r"""defalign""")
    size_s = property(_ida_ida.compiler_info_t_size_s_get, _ida_ida.compiler_info_t_size_s_set, doc=r"""size_s""")
    size_l = property(_ida_ida.compiler_info_t_size_l_get, _ida_ida.compiler_info_t_size_l_set, doc=r"""size_l""")
    size_ll = property(_ida_ida.compiler_info_t_size_ll_get, _ida_ida.compiler_info_t_size_ll_set, doc=r"""size_ll""")
    size_ldbl = property(_ida_ida.compiler_info_t_size_ldbl_get, _ida_ida.compiler_info_t_size_ldbl_set, doc=r"""size_ldbl""")

    def set_64bit_pointer_size(self, *args):
        r"""set_64bit_pointer_size(self)"""
        return _ida_ida.compiler_info_t_set_64bit_pointer_size(self, *args)

    def __init__(self, *args):
        r"""__init__(self) -> compiler_info_t"""
        _ida_ida.compiler_info_t_swiginit(self, _ida_ida.new_compiler_info_t(*args))
    __swig_destroy__ = _ida_ida.delete_compiler_info_t

# Register compiler_info_t in _ida_ida:
_ida_ida.compiler_info_t_swigregister(compiler_info_t)

STT_CUR = _ida_ida.STT_CUR

STT_VA = _ida_ida.STT_VA

STT_MM = _ida_ida.STT_MM

STT_DBG = _ida_ida.STT_DBG

class idainfo(object):
    r"""Proxy of C++ idainfo class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    tag = property(_ida_ida.idainfo_tag_get, _ida_ida.idainfo_tag_set, doc=r"""tag""")
    version = property(_ida_ida.idainfo_version_get, _ida_ida.idainfo_version_set, doc=r"""version""")
    procname = property(_ida_ida.idainfo_procname_get, _ida_ida.idainfo_procname_set, doc=r"""procname""")
    s_genflags = property(_ida_ida.idainfo_s_genflags_get, _ida_ida.idainfo_s_genflags_set, doc=r"""s_genflags""")

    def use_allasm(self, *args):
        r"""use_allasm(self) -> bool"""
        return _ida_ida.idainfo_use_allasm(self, *args)

    def loading_idc(self, *args):
        r"""loading_idc(self) -> bool"""
        return _ida_ida.idainfo_loading_idc(self, *args)

    def readonly_idb(self, *args):
        r"""readonly_idb(self) -> bool"""
        return _ida_ida.idainfo_readonly_idb(self, *args)

    def is_graph_view(self, *args):
        r"""is_graph_view(self) -> bool"""
        return _ida_ida.idainfo_is_graph_view(self, *args)

    def set_graph_view(self, *args):
        r"""set_graph_view(self, value)"""
        return _ida_ida.idainfo_set_graph_view(self, *args)
    lflags = property(_ida_ida.idainfo_lflags_get, _ida_ida.idainfo_lflags_set, doc=r"""lflags""")

    def is_32bit(self, *args):
        r"""is_32bit(self) -> bool"""
        return _ida_ida.idainfo_is_32bit(self, *args)

    def is_64bit(self, *args):
        r"""is_64bit(self) -> bool"""
        return _ida_ida.idainfo_is_64bit(self, *args)

    def is_snapshot(self, *args):
        r"""is_snapshot(self) -> bool"""
        return _ida_ida.idainfo_is_snapshot(self, *args)

    def is_dll(self, *args):
        r"""is_dll(self) -> bool"""
        return _ida_ida.idainfo_is_dll(self, *args)

    def is_flat_off32(self, *args):
        r"""is_flat_off32(self) -> bool"""
        return _ida_ida.idainfo_is_flat_off32(self, *args)

    def is_be(self, *args):
        r"""is_be(self) -> bool"""
        return _ida_ida.idainfo_is_be(self, *args)

    def set_be(self, *args):
        r"""set_be(self, value) -> bool"""
        return _ida_ida.idainfo_set_be(self, *args)

    def is_wide_high_byte_first(self, *args):
        r"""is_wide_high_byte_first(self) -> bool"""
        return _ida_ida.idainfo_is_wide_high_byte_first(self, *args)

    def set_wide_high_byte_first(self, *args):
        r"""set_wide_high_byte_first(self, value)"""
        return _ida_ida.idainfo_set_wide_high_byte_first(self, *args)

    def set_64bit(self, *args):
        r"""set_64bit(self)"""
        return _ida_ida.idainfo_set_64bit(self, *args)

    def is_kernel_mode(self, *args):
        r"""is_kernel_mode(self) -> bool"""
        return _ida_ida.idainfo_is_kernel_mode(self, *args)

    def get_pack_mode(self, *args):
        r"""get_pack_mode(self) -> int"""
        return _ida_ida.idainfo_get_pack_mode(self, *args)

    def set_pack_mode(self, *args):
        r"""set_pack_mode(self, pack_mode) -> int"""
        return _ida_ida.idainfo_set_pack_mode(self, *args)
    database_change_count = property(_ida_ida.idainfo_database_change_count_get, _ida_ida.idainfo_database_change_count_set, doc=r"""database_change_count""")
    filetype = property(_ida_ida.idainfo_filetype_get, _ida_ida.idainfo_filetype_set, doc=r"""filetype""")

    def like_binary(self, *args):
        r"""like_binary(self) -> bool"""
        return _ida_ida.idainfo_like_binary(self, *args)
    ostype = property(_ida_ida.idainfo_ostype_get, _ida_ida.idainfo_ostype_set, doc=r"""ostype""")
    apptype = property(_ida_ida.idainfo_apptype_get, _ida_ida.idainfo_apptype_set, doc=r"""apptype""")
    asmtype = property(_ida_ida.idainfo_asmtype_get, _ida_ida.idainfo_asmtype_set, doc=r"""asmtype""")
    specsegs = property(_ida_ida.idainfo_specsegs_get, _ida_ida.idainfo_specsegs_set, doc=r"""specsegs""")
    af = property(_ida_ida.idainfo_af_get, _ida_ida.idainfo_af_set, doc=r"""af""")
    af2 = property(_ida_ida.idainfo_af2_get, _ida_ida.idainfo_af2_set, doc=r"""af2""")
    baseaddr = property(_ida_ida.idainfo_baseaddr_get, _ida_ida.idainfo_baseaddr_set, doc=r"""baseaddr""")
    start_ss = property(_ida_ida.idainfo_start_ss_get, _ida_ida.idainfo_start_ss_set, doc=r"""start_ss""")
    start_cs = property(_ida_ida.idainfo_start_cs_get, _ida_ida.idainfo_start_cs_set, doc=r"""start_cs""")
    start_ip = property(_ida_ida.idainfo_start_ip_get, _ida_ida.idainfo_start_ip_set, doc=r"""start_ip""")
    start_ea = property(_ida_ida.idainfo_start_ea_get, _ida_ida.idainfo_start_ea_set, doc=r"""start_ea""")
    start_sp = property(_ida_ida.idainfo_start_sp_get, _ida_ida.idainfo_start_sp_set, doc=r"""start_sp""")
    main = property(_ida_ida.idainfo_main_get, _ida_ida.idainfo_main_set, doc=r"""main""")
    min_ea = property(_ida_ida.idainfo_min_ea_get, _ida_ida.idainfo_min_ea_set, doc=r"""min_ea""")
    max_ea = property(_ida_ida.idainfo_max_ea_get, _ida_ida.idainfo_max_ea_set, doc=r"""max_ea""")
    omin_ea = property(_ida_ida.idainfo_omin_ea_get, _ida_ida.idainfo_omin_ea_set, doc=r"""omin_ea""")
    omax_ea = property(_ida_ida.idainfo_omax_ea_get, _ida_ida.idainfo_omax_ea_set, doc=r"""omax_ea""")
    lowoff = property(_ida_ida.idainfo_lowoff_get, _ida_ida.idainfo_lowoff_set, doc=r"""lowoff""")
    highoff = property(_ida_ida.idainfo_highoff_get, _ida_ida.idainfo_highoff_set, doc=r"""highoff""")
    maxref = property(_ida_ida.idainfo_maxref_get, _ida_ida.idainfo_maxref_set, doc=r"""maxref""")
    xrefnum = property(_ida_ida.idainfo_xrefnum_get, _ida_ida.idainfo_xrefnum_set, doc=r"""xrefnum""")
    type_xrefnum = property(_ida_ida.idainfo_type_xrefnum_get, _ida_ida.idainfo_type_xrefnum_set, doc=r"""type_xrefnum""")
    refcmtnum = property(_ida_ida.idainfo_refcmtnum_get, _ida_ida.idainfo_refcmtnum_set, doc=r"""refcmtnum""")
    s_xrefflag = property(_ida_ida.idainfo_s_xrefflag_get, _ida_ida.idainfo_s_xrefflag_set, doc=r"""s_xrefflag""")
    max_autoname_len = property(_ida_ida.idainfo_max_autoname_len_get, _ida_ida.idainfo_max_autoname_len_set, doc=r"""max_autoname_len""")
    nametype = property(_ida_ida.idainfo_nametype_get, _ida_ida.idainfo_nametype_set, doc=r"""nametype""")
    short_demnames = property(_ida_ida.idainfo_short_demnames_get, _ida_ida.idainfo_short_demnames_set, doc=r"""short_demnames""")
    long_demnames = property(_ida_ida.idainfo_long_demnames_get, _ida_ida.idainfo_long_demnames_set, doc=r"""long_demnames""")
    demnames = property(_ida_ida.idainfo_demnames_get, _ida_ida.idainfo_demnames_set, doc=r"""demnames""")

    def get_demname_form(self, *args):
        r"""get_demname_form(self) -> uchar"""
        return _ida_ida.idainfo_get_demname_form(self, *args)
    listnames = property(_ida_ida.idainfo_listnames_get, _ida_ida.idainfo_listnames_set, doc=r"""listnames""")
    indent = property(_ida_ida.idainfo_indent_get, _ida_ida.idainfo_indent_set, doc=r"""indent""")
    comment = property(_ida_ida.idainfo_comment_get, _ida_ida.idainfo_comment_set, doc=r"""comment""")
    margin = property(_ida_ida.idainfo_margin_get, _ida_ida.idainfo_margin_set, doc=r"""margin""")
    lenxref = property(_ida_ida.idainfo_lenxref_get, _ida_ida.idainfo_lenxref_set, doc=r"""lenxref""")
    outflags = property(_ida_ida.idainfo_outflags_get, _ida_ida.idainfo_outflags_set, doc=r"""outflags""")
    s_cmtflg = property(_ida_ida.idainfo_s_cmtflg_get, _ida_ida.idainfo_s_cmtflg_set, doc=r"""s_cmtflg""")
    s_limiter = property(_ida_ida.idainfo_s_limiter_get, _ida_ida.idainfo_s_limiter_set, doc=r"""s_limiter""")
    bin_prefix_size = property(_ida_ida.idainfo_bin_prefix_size_get, _ida_ida.idainfo_bin_prefix_size_set, doc=r"""bin_prefix_size""")
    s_prefflag = property(_ida_ida.idainfo_s_prefflag_get, _ida_ida.idainfo_s_prefflag_set, doc=r"""s_prefflag""")
    strlit_flags = property(_ida_ida.idainfo_strlit_flags_get, _ida_ida.idainfo_strlit_flags_set, doc=r"""strlit_flags""")
    strlit_break = property(_ida_ida.idainfo_strlit_break_get, _ida_ida.idainfo_strlit_break_set, doc=r"""strlit_break""")
    strlit_zeroes = property(_ida_ida.idainfo_strlit_zeroes_get, _ida_ida.idainfo_strlit_zeroes_set, doc=r"""strlit_zeroes""")
    strtype = property(_ida_ida.idainfo_strtype_get, _ida_ida.idainfo_strtype_set, doc=r"""strtype""")
    strlit_pref = property(_ida_ida.idainfo_strlit_pref_get, _ida_ida.idainfo_strlit_pref_set, doc=r"""strlit_pref""")
    strlit_sernum = property(_ida_ida.idainfo_strlit_sernum_get, _ida_ida.idainfo_strlit_sernum_set, doc=r"""strlit_sernum""")
    datatypes = property(_ida_ida.idainfo_datatypes_get, _ida_ida.idainfo_datatypes_set, doc=r"""datatypes""")
    cc = property(_ida_ida.idainfo_cc_get, _ida_ida.idainfo_cc_set, doc=r"""cc""")
    abibits = property(_ida_ida.idainfo_abibits_get, _ida_ida.idainfo_abibits_set, doc=r"""abibits""")

    def is_mem_aligned4(self, *args):
        r"""is_mem_aligned4(self) -> bool"""
        return _ida_ida.idainfo_is_mem_aligned4(self, *args)

    def pack_stkargs(self, *args):
        r"""pack_stkargs(self) -> bool"""
        return _ida_ida.idainfo_pack_stkargs(self, *args)

    def big_arg_align(self, *args):
        r"""big_arg_align(self) -> bool"""
        return _ida_ida.idainfo_big_arg_align(self, *args)

    def stack_ldbl(self, *args):
        r"""stack_ldbl(self) -> bool"""
        return _ida_ida.idainfo_stack_ldbl(self, *args)

    def stack_varargs(self, *args):
        r"""stack_varargs(self) -> bool"""
        return _ida_ida.idainfo_stack_varargs(self, *args)

    def is_hard_float(self, *args):
        r"""is_hard_float(self) -> bool"""
        return _ida_ida.idainfo_is_hard_float(self, *args)

    def use_gcc_layout(self, *args):
        r"""use_gcc_layout(self) -> bool"""
        return _ida_ida.idainfo_use_gcc_layout(self, *args)
    appcall_options = property(_ida_ida.idainfo_appcall_options_get, _ida_ida.idainfo_appcall_options_set, doc=r"""appcall_options""")

    def is_auto_enabled(self, *args):
        r"""is_auto_enabled(self) -> bool"""
        return _ida_ida.idainfo_is_auto_enabled(self, *args)

    def set_auto_enabled(self, *args):
        r"""set_auto_enabled(self, value)"""
        return _ida_ida.idainfo_set_auto_enabled(self, *args)

    def show_void(self, *args):
        r"""show_void(self) -> bool"""
        return _ida_ida.idainfo_show_void(self, *args)

    def set_show_void(self, *args):
        r"""set_show_void(self, value)"""
        return _ida_ida.idainfo_set_show_void(self, *args)

    def show_auto(self, *args):
        r"""show_auto(self) -> bool"""
        return _ida_ida.idainfo_show_auto(self, *args)

    def set_show_auto(self, *args):
        r"""set_show_auto(self, value)"""
        return _ida_ida.idainfo_set_show_auto(self, *args)

    def gen_null(self, *args):
        r"""gen_null(self) -> bool"""
        return _ida_ida.idainfo_gen_null(self, *args)

    def set_gen_null(self, *args):
        r"""set_gen_null(self, value)"""
        return _ida_ida.idainfo_set_gen_null(self, *args)

    def show_line_pref(self, *args):
        r"""show_line_pref(self) -> bool"""
        return _ida_ida.idainfo_show_line_pref(self, *args)

    def set_show_line_pref(self, *args):
        r"""set_show_line_pref(self, value)"""
        return _ida_ida.idainfo_set_show_line_pref(self, *args)

    def line_pref_with_seg(self, *args):
        r"""line_pref_with_seg(self) -> bool"""
        return _ida_ida.idainfo_line_pref_with_seg(self, *args)

    def set_line_pref_with_seg(self, *args):
        r"""set_line_pref_with_seg(self, value)"""
        return _ida_ida.idainfo_set_line_pref_with_seg(self, *args)

    def gen_lzero(self, *args):
        r"""gen_lzero(self) -> bool"""
        return _ida_ida.idainfo_gen_lzero(self, *args)

    def set_gen_lzero(self, *args):
        r"""set_gen_lzero(self, value)"""
        return _ida_ida.idainfo_set_gen_lzero(self, *args)

    def gen_tryblks(self, *args):
        r"""gen_tryblks(self) -> bool"""
        return _ida_ida.idainfo_gen_tryblks(self, *args)

    def set_gen_tryblks(self, *args):
        r"""set_gen_tryblks(self, value)"""
        return _ida_ida.idainfo_set_gen_tryblks(self, *args)

    def get_abiname(self, *args):
        r"""get_abiname(self) -> qstring"""
        return _ida_ida.idainfo_get_abiname(self, *args)

    def get_minEA(self, *args):
        r"""get_minEA(self) -> ea_t"""
        return _ida_ida.idainfo_get_minEA(self, *args)

    def set_minEA(self, *args):
        r"""set_minEA(self, ea)"""
        return _ida_ida.idainfo_set_minEA(self, *args)

    def get_maxEA(self, *args):
        r"""get_maxEA(self) -> ea_t"""
        return _ida_ida.idainfo_get_maxEA(self, *args)

    def set_maxEA(self, *args):
        r"""set_maxEA(self, ea)"""
        return _ida_ida.idainfo_set_maxEA(self, *args)

    def get_procName(self, *args):
        r"""get_procName(self) -> qstring"""
        return _ida_ida.idainfo_get_procName(self, *args)

    abiname = property(get_abiname)

    minEA = property(get_minEA, set_minEA)
    maxEA = property(get_maxEA, set_maxEA)
    procName = property(get_procName)



# Register idainfo in _ida_ida:
_ida_ida.idainfo_swigregister(idainfo)
INFFL_AUTO = _ida_ida.INFFL_AUTO

INFFL_ALLASM = _ida_ida.INFFL_ALLASM

INFFL_LOADIDC = _ida_ida.INFFL_LOADIDC

INFFL_NOUSER = _ida_ida.INFFL_NOUSER

INFFL_READONLY = _ida_ida.INFFL_READONLY

INFFL_CHKOPS = _ida_ida.INFFL_CHKOPS

INFFL_NMOPS = _ida_ida.INFFL_NMOPS

INFFL_GRAPH_VIEW = _ida_ida.INFFL_GRAPH_VIEW

LFLG_PC_FPP = _ida_ida.LFLG_PC_FPP

LFLG_PC_FLAT = _ida_ida.LFLG_PC_FLAT

LFLG_64BIT = _ida_ida.LFLG_64BIT

LFLG_IS_DLL = _ida_ida.LFLG_IS_DLL

LFLG_FLAT_OFF32 = _ida_ida.LFLG_FLAT_OFF32

LFLG_MSF = _ida_ida.LFLG_MSF

LFLG_WIDE_HBF = _ida_ida.LFLG_WIDE_HBF

LFLG_DBG_NOPATH = _ida_ida.LFLG_DBG_NOPATH

LFLG_SNAPSHOT = _ida_ida.LFLG_SNAPSHOT

LFLG_PACK = _ida_ida.LFLG_PACK

LFLG_COMPRESS = _ida_ida.LFLG_COMPRESS

LFLG_KERNMODE = _ida_ida.LFLG_KERNMODE

IDB_UNPACKED = _ida_ida.IDB_UNPACKED

IDB_PACKED = _ida_ida.IDB_PACKED

IDB_COMPRESSED = _ida_ida.IDB_COMPRESSED

AF_CODE = _ida_ida.AF_CODE

AF_MARKCODE = _ida_ida.AF_MARKCODE

AF_JUMPTBL = _ida_ida.AF_JUMPTBL

AF_PURDAT = _ida_ida.AF_PURDAT

AF_USED = _ida_ida.AF_USED

AF_UNK = _ida_ida.AF_UNK

AF_PROCPTR = _ida_ida.AF_PROCPTR

AF_PROC = _ida_ida.AF_PROC

AF_FTAIL = _ida_ida.AF_FTAIL

AF_LVAR = _ida_ida.AF_LVAR

AF_STKARG = _ida_ida.AF_STKARG

AF_REGARG = _ida_ida.AF_REGARG

AF_TRACE = _ida_ida.AF_TRACE

AF_VERSP = _ida_ida.AF_VERSP

AF_ANORET = _ida_ida.AF_ANORET

AF_MEMFUNC = _ida_ida.AF_MEMFUNC

AF_TRFUNC = _ida_ida.AF_TRFUNC

AF_STRLIT = _ida_ida.AF_STRLIT

AF_CHKUNI = _ida_ida.AF_CHKUNI

AF_FIXUP = _ida_ida.AF_FIXUP

AF_DREFOFF = _ida_ida.AF_DREFOFF

AF_IMMOFF = _ida_ida.AF_IMMOFF

AF_DATOFF = _ida_ida.AF_DATOFF

AF_FLIRT = _ida_ida.AF_FLIRT

AF_SIGCMT = _ida_ida.AF_SIGCMT

AF_SIGMLT = _ida_ida.AF_SIGMLT

AF_HFLIRT = _ida_ida.AF_HFLIRT

AF_JFUNC = _ida_ida.AF_JFUNC

AF_NULLSUB = _ida_ida.AF_NULLSUB

AF_DODATA = _ida_ida.AF_DODATA

AF_DOCODE = _ida_ida.AF_DOCODE

AF_FINAL = _ida_ida.AF_FINAL

AF2_DOEH = _ida_ida.AF2_DOEH

AF2_DORTTI = _ida_ida.AF2_DORTTI

SW_SEGXRF = _ida_ida.SW_SEGXRF

SW_XRFMRK = _ida_ida.SW_XRFMRK

SW_XRFFNC = _ida_ida.SW_XRFFNC

SW_XRFVAL = _ida_ida.SW_XRFVAL

NM_REL_OFF = _ida_ida.NM_REL_OFF

NM_PTR_OFF = _ida_ida.NM_PTR_OFF

NM_NAM_OFF = _ida_ida.NM_NAM_OFF

NM_REL_EA = _ida_ida.NM_REL_EA

NM_PTR_EA = _ida_ida.NM_PTR_EA

NM_NAM_EA = _ida_ida.NM_NAM_EA

NM_EA = _ida_ida.NM_EA

NM_EA4 = _ida_ida.NM_EA4

NM_EA8 = _ida_ida.NM_EA8

NM_SHORT = _ida_ida.NM_SHORT

NM_SERIAL = _ida_ida.NM_SERIAL

DEMNAM_MASK = _ida_ida.DEMNAM_MASK

DEMNAM_CMNT = _ida_ida.DEMNAM_CMNT

DEMNAM_NAME = _ida_ida.DEMNAM_NAME

DEMNAM_NONE = _ida_ida.DEMNAM_NONE

DEMNAM_GCC3 = _ida_ida.DEMNAM_GCC3

DEMNAM_FIRST = _ida_ida.DEMNAM_FIRST

LN_NORMAL = _ida_ida.LN_NORMAL

LN_PUBLIC = _ida_ida.LN_PUBLIC

LN_AUTO = _ida_ida.LN_AUTO

LN_WEAK = _ida_ida.LN_WEAK

OFLG_SHOW_VOID = _ida_ida.OFLG_SHOW_VOID

OFLG_SHOW_AUTO = _ida_ida.OFLG_SHOW_AUTO

OFLG_GEN_NULL = _ida_ida.OFLG_GEN_NULL

OFLG_SHOW_PREF = _ida_ida.OFLG_SHOW_PREF

OFLG_PREF_SEG = _ida_ida.OFLG_PREF_SEG

OFLG_LZERO = _ida_ida.OFLG_LZERO

OFLG_GEN_ORG = _ida_ida.OFLG_GEN_ORG

OFLG_GEN_ASSUME = _ida_ida.OFLG_GEN_ASSUME

OFLG_GEN_TRYBLKS = _ida_ida.OFLG_GEN_TRYBLKS

SW_RPTCMT = _ida_ida.SW_RPTCMT

SW_ALLCMT = _ida_ida.SW_ALLCMT

SW_NOCMT = _ida_ida.SW_NOCMT

SW_LINNUM = _ida_ida.SW_LINNUM

SW_TESTMODE = _ida_ida.SW_TESTMODE

SW_SHHID_ITEM = _ida_ida.SW_SHHID_ITEM

SW_SHHID_FUNC = _ida_ida.SW_SHHID_FUNC

SW_SHHID_SEGM = _ida_ida.SW_SHHID_SEGM

LMT_THIN = _ida_ida.LMT_THIN

LMT_THICK = _ida_ida.LMT_THICK

LMT_EMPTY = _ida_ida.LMT_EMPTY

PREF_SEGADR = _ida_ida.PREF_SEGADR

PREF_FNCOFF = _ida_ida.PREF_FNCOFF

PREF_STACK = _ida_ida.PREF_STACK

STRF_GEN = _ida_ida.STRF_GEN

STRF_AUTO = _ida_ida.STRF_AUTO

STRF_SERIAL = _ida_ida.STRF_SERIAL

STRF_UNICODE = _ida_ida.STRF_UNICODE

STRF_COMMENT = _ida_ida.STRF_COMMENT

STRF_SAVECASE = _ida_ida.STRF_SAVECASE

ABI_8ALIGN4 = _ida_ida.ABI_8ALIGN4

ABI_PACK_STKARGS = _ida_ida.ABI_PACK_STKARGS

ABI_BIGARG_ALIGN = _ida_ida.ABI_BIGARG_ALIGN

ABI_STACK_LDBL = _ida_ida.ABI_STACK_LDBL

ABI_STACK_VARARGS = _ida_ida.ABI_STACK_VARARGS

ABI_HARD_FLOAT = _ida_ida.ABI_HARD_FLOAT

ABI_SET_BY_USER = _ida_ida.ABI_SET_BY_USER

ABI_GCC_LAYOUT = _ida_ida.ABI_GCC_LAYOUT



def show_repeatables(*args):
    r"""show_repeatables() -> bool"""
    return _ida_ida.show_repeatables(*args)

def show_all_comments(*args):
    r"""show_all_comments() -> bool"""
    return _ida_ida.show_all_comments(*args)

def show_comments(*args):
    r"""show_comments() -> bool"""
    return _ida_ida.show_comments(*args)

def should_trace_sp(*args):
    r"""should_trace_sp() -> bool"""
    return _ida_ida.should_trace_sp(*args)

def should_create_stkvars(*args):
    r"""should_create_stkvars() -> bool"""
    return _ida_ida.should_create_stkvars(*args)
UA_MAXOP = _ida_ida.UA_MAXOP


def calc_default_idaplace_flags(*args):
    r"""calc_default_idaplace_flags() -> int"""
    return _ida_ida.calc_default_idaplace_flags(*args)
MAXADDR = _ida_ida.MAXADDR


def to_ea(*args):
    r"""to_ea(reg_cs, reg_ip) -> ea_t"""
    return _ida_ida.to_ea(*args)
IDB_EXT32 = _ida_ida.IDB_EXT32

IDB_EXT64 = _ida_ida.IDB_EXT64

IDB_EXT = _ida_ida.IDB_EXT


if _BC695:
    AF2_ANORET=AF_ANORET
    AF2_CHKUNI=AF_CHKUNI
    AF2_DATOFF=AF_DATOFF
    AF2_DOCODE=AF_DOCODE
    AF2_DODATA=AF_DODATA
    AF2_FTAIL=AF_FTAIL
    AF2_HFLIRT=AF_HFLIRT
    AF2_JUMPTBL=AF_JUMPTBL
    AF2_MEMFUNC=AF_MEMFUNC
    AF2_PURDAT=AF_PURDAT
    AF2_REGARG=AF_REGARG
    AF2_SIGCMT=AF_SIGCMT
    AF2_SIGMLT=AF_SIGMLT
    AF2_STKARG=AF_STKARG
    AF2_TRFUNC=AF_TRFUNC
    AF2_VERSP=AF_VERSP
    AF_ASCII=AF_STRLIT
    ASCF_AUTO=STRF_AUTO
    ASCF_COMMENT=STRF_COMMENT
    ASCF_GEN=STRF_GEN
    ASCF_SAVECASE=STRF_SAVECASE
    ASCF_SERIAL=STRF_SERIAL
    ASCF_UNICODE=STRF_UNICODE
    INFFL_LZERO=OFLG_LZERO
    ansi2idb=ida_idaapi._BC695.identity
    idb2scr=ida_idaapi._BC695.identity
    scr2idb=ida_idaapi._BC695.identity
    showAllComments=show_all_comments
    showComments=show_comments
    showRepeatables=show_repeatables
    toEA=to_ea
    def __wrap_hooks_callback(klass, new_name, old_name, do_call):
        bkp_name = "__real_%s" % new_name
        def __wrapper(self, *args):
            rc = getattr(self, bkp_name)(*args)
            cb = getattr(self, old_name, None)
            if cb:
                rc = do_call(cb, *args)
            return rc
        setattr(klass, bkp_name, getattr(klass, new_name))
        setattr(klass, new_name, __wrapper)
    idainfo.ASCIIbreak = idainfo.strlit_break
    idainfo.ASCIIpref = idainfo.strlit_pref
    idainfo.ASCIIsernum = idainfo.strlit_sernum
    idainfo.ASCIIzeroes = idainfo.strlit_zeroes
    idainfo.asciiflags = idainfo.strlit_flags
    idainfo.beginEA = idainfo.start_ea
    idainfo.binSize = idainfo.bin_prefix_size
    def my_get_proc_name(self):
        return [self.procname, self.procname]
    idainfo.get_proc_name = my_get_proc_name
    idainfo.graph_view = property(idainfo.is_graph_view, idainfo.set_graph_view)
    idainfo.mf = property(idainfo.is_be, idainfo.set_be)
    idainfo.namelen = idainfo.max_autoname_len
    idainfo.omaxEA = idainfo.omax_ea
    idainfo.ominEA = idainfo.omin_ea
    def make_outflags_accessors(bit):
        def getter(self):
            return (self.outflags & bit) != 0
        def setter(self, value):
            if value:
                self.outflags |= bit
            else:
                self.outflags &= ~bit
        return getter, setter
    idainfo.s_assume = property(*make_outflags_accessors(OFLG_GEN_ASSUME))
    idainfo.s_auto = property(idainfo.is_auto_enabled, idainfo.set_auto_enabled)
    idainfo.s_null = property(*make_outflags_accessors(OFLG_GEN_NULL))
    idainfo.s_org = property(*make_outflags_accessors(OFLG_GEN_ORG))
    idainfo.s_prefseg = property(*make_outflags_accessors(OFLG_PREF_SEG))
    idainfo.s_showauto = property(*make_outflags_accessors(OFLG_SHOW_AUTO))
    idainfo.s_showpref = property(*make_outflags_accessors(OFLG_SHOW_PREF))
    idainfo.s_void = property(*make_outflags_accessors(OFLG_SHOW_VOID))
    idainfo.startIP = idainfo.start_ip
    idainfo.startSP = idainfo.start_sp
    def make_lflags_accessors(bit):
        def getter(self):
            return (self.lflags & bit) != 0
        def setter(self, value):
            if value:
                self.lflags |= bit
            else:
                self.lflags &= ~bit
        return getter, setter
    idainfo.wide_high_byte_first = property(*make_lflags_accessors(LFLG_WIDE_HBF))
    def make_obsolete_accessors():
        def getter(self):
            return False
        def setter(self, value):
            pass
        return getter, setter
    idainfo.allow_nonmatched_ops = property(*make_obsolete_accessors())
    idainfo.check_manual_ops = property(*make_obsolete_accessors())



cvar = _ida_ida.cvar

