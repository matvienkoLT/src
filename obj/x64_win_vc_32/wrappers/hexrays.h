/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 4.0.1
 *
 * This file is not intended to be easily readable and contains a number of
 * coding conventions designed to improve portability and efficiency. Do not make
 * changes to this file unless you know what you are doing--modify the SWIG
 * interface file instead.
 * ----------------------------------------------------------------------------- */

#ifndef SWIG_ida_hexrays_WRAP_H_
#define SWIG_ida_hexrays_WRAP_H_

#include <map>
#include <string>


class SwigDirector_Hexrays_Hooks : public Hexrays_Hooks, public Swig::Director {

public:
    SwigDirector_Hexrays_Hooks(PyObject *self);
    virtual ~SwigDirector_Hexrays_Hooks();
    virtual int flowchart(qflow_chart_t *fc);
    virtual int stkpnts(mbl_array_t *mba, stkpnts_t *stkpnts);
    virtual int prolog(mbl_array_t *mba, qflow_chart_t *fc, bitset_t *reachable_blocks);
    virtual int microcode(mbl_array_t *mba);
    virtual int preoptimized(mbl_array_t *mba);
    virtual int locopt(mbl_array_t *mba);
    virtual int prealloc(mbl_array_t *mba);
    virtual int glbopt(mbl_array_t *mba);
    virtual int structural(control_graph_t *ct);
    virtual int maturity(cfunc_t *cfunc, ctree_maturity_t new_maturity);
    virtual int interr(int errcode);
    virtual int combine(mblock_t *blk, minsn_t *insn);
    virtual int idaapi print_func(cfunc_t *cfunc, vc_printer_t *vp);
    virtual int func_printed(cfunc_t *cfunc);
    virtual int resolve_stkaddrs(mbl_array_t *mba);
    virtual int open_pseudocode(vdui_t *vu);
    virtual int switch_pseudocode(vdui_t *vu);
    virtual int refresh_pseudocode(vdui_t *vu);
    virtual int close_pseudocode(vdui_t *vu);
    virtual int keyboard(vdui_t *vu, int key_code, int shift_state);
    virtual int right_click(vdui_t *vu);
    virtual int double_click(vdui_t *vu, int shift_state);
    virtual int curpos(vdui_t *vu);
    virtual PyObject *create_hint(vdui_t *vu);
    virtual int text_ready(vdui_t *vu);
    virtual int populating_popup(TWidget *widget, TPopupMenu *popup_handle, vdui_t *vu);
    virtual int lvar_name_changed(vdui_t *vu, lvar_t *v, char const *name, bool is_user_name);
    virtual int lvar_type_changed(vdui_t *vu, lvar_t *v, tinfo_t const *tinfo);
    virtual int lvar_cmt_changed(vdui_t *vu, lvar_t *v, char const *cmt);
    virtual int lvar_mapping_changed(vdui_t *vu, lvar_t *from, lvar_t *to);
    virtual int cmt_changed(cfunc_t *cfunc, treeloc_t const *loc, char const *cmt);

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class Hexrays_Hooks doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[31];
#endif

};


struct SwigDirector_user_lvar_modifier_t : public user_lvar_modifier_t, public Swig::Director {

public:
    SwigDirector_user_lvar_modifier_t(PyObject *self);
    virtual bool idaapi modify_lvars(lvar_uservec_t *lvinf);

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class user_lvar_modifier_t doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[1];
#endif

};


struct SwigDirector_microcode_filter_t : public microcode_filter_t, public Swig::Director {

public:
    SwigDirector_microcode_filter_t(PyObject *self);
    virtual bool match(codegen_t &cdg);
    virtual merror_t apply(codegen_t &cdg);

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class microcode_filter_t doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[2];
#endif

};


class SwigDirector_udc_filter_t : public udc_filter_t, public Swig::Director {

public:
    SwigDirector_udc_filter_t(PyObject *self);
    virtual bool match(codegen_t &cdg);

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class udc_filter_t doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[1];
#endif

};


class SwigDirector_codegen_t : public codegen_t, public Swig::Director {

public:
    SwigDirector_codegen_t(PyObject *self, mbl_array_t *m);
    virtual ~SwigDirector_codegen_t();
    virtual merror_t idaapi analyze_prolog(qflow_chart_t const &fc, bitset_t const &reachable);
    virtual merror_t idaapi gen_micro();
    virtual mreg_t idaapi load_operand(int opnum);
    virtual minsn_t *idaapi emit_micro_mvm(mcode_t code, op_dtype_t dtype, uval_t l, uval_t r, uval_t d, int offsize);

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class codegen_t doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[4];
#endif

};


struct SwigDirector_ctree_visitor_t : public ctree_visitor_t, public Swig::Director {

public:
    SwigDirector_ctree_visitor_t(PyObject *self, int _flags);
    virtual int idaapi visit_insn(cinsn_t *arg0);
    virtual int idaapi visit_expr(cexpr_t *arg0);
    virtual int idaapi leave_insn(cinsn_t *arg0);
    virtual int idaapi leave_expr(cexpr_t *arg0);

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class ctree_visitor_t doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[4];
#endif

};


struct SwigDirector_ctree_parentee_t : public ctree_parentee_t, public Swig::Director {

public:
    SwigDirector_ctree_parentee_t(PyObject *self, bool post = false);
    virtual int idaapi visit_insn(cinsn_t *arg0);
    virtual int idaapi visit_expr(cexpr_t *arg0);
    virtual int idaapi leave_insn(cinsn_t *arg0);
    virtual int idaapi leave_expr(cexpr_t *arg0);

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class ctree_parentee_t doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[4];
#endif

};


struct SwigDirector_cfunc_parentee_t : public cfunc_parentee_t, public Swig::Director {

public:
    SwigDirector_cfunc_parentee_t(PyObject *self, cfunc_t *f, bool post = false);
    virtual int idaapi visit_insn(cinsn_t *arg0);
    virtual int idaapi visit_expr(cexpr_t *arg0);
    virtual int idaapi leave_insn(cinsn_t *arg0);
    virtual int idaapi leave_expr(cexpr_t *arg0);

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class cfunc_parentee_t doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[4];
#endif

};


#endif