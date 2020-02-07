/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 4.0.1
 *
 * This file is not intended to be easily readable and contains a number of
 * coding conventions designed to improve portability and efficiency. Do not make
 * changes to this file unless you know what you are doing--modify the SWIG
 * interface file instead.
 * ----------------------------------------------------------------------------- */

#ifndef SWIG_ida_kernwin_WRAP_H_
#define SWIG_ida_kernwin_WRAP_H_

#include <map>
#include <string>


class SwigDirector_UI_Hooks : public UI_Hooks, public Swig::Director {

public:
    SwigDirector_UI_Hooks(PyObject *self);
    virtual ~SwigDirector_UI_Hooks();
    virtual void range();
    virtual void idcstart();
    virtual void idcstop();
    virtual void suspend();
    virtual void resume();
    virtual void saving();
    virtual void saved();
    virtual void term();
    virtual int debugger_menu_change(bool enable);
    virtual void widget_visible(TWidget *widget);
    virtual void widget_closing(TWidget *widget);
    virtual void widget_invisible(TWidget *widget);
    virtual PyObject *get_ea_hint(ea_t ea);
    virtual PyObject *get_item_hint(ea_t ea, int max_lines);
    virtual PyObject *get_custom_viewer_hint(TWidget *viewer, place_t *place);
    virtual void database_inited(int is_new_database, char const *idc_script);
    virtual void ready_to_run();
    virtual void preprocess_action(char const *name);
    virtual void postprocess_action();
    virtual void get_chooser_item_attrs(chooser_base_t const *chooser, size_t n, chooser_item_attrs_t *attrs);
    virtual void updating_actions(action_update_ctx_t *ctx);
    virtual void updated_actions();
    virtual void populating_widget_popup(TWidget *widget, TPopupMenu *popup_handle, action_activation_ctx_t const *ctx = NULL);
    virtual void finish_populating_widget_popup(TWidget *widget, TPopupMenu *popup_handle, action_activation_ctx_t const *ctx = NULL);
    virtual void plugin_loaded(plugin_info_t const *plugin_info);
    virtual void plugin_unloading(plugin_info_t const *plugin_info);
    virtual void current_widget_changed(TWidget *widget, TWidget *prev_widget);
    virtual void screen_ea_changed(ea_t ea, ea_t prev_ea);
    virtual PyObject *create_desktop_widget(char const *title, jobj_wrapper_t cfg);

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
          std::string msg = "Method in class UI_Hooks doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[29];
#endif

};


class SwigDirector_View_Hooks : public View_Hooks, public Swig::Director {

public:
    SwigDirector_View_Hooks(PyObject *self);
    virtual ~SwigDirector_View_Hooks();
    virtual void view_activated(TWidget *view);
    virtual void view_deactivated(TWidget *view);
    virtual void view_keydown(TWidget *view, int key, view_event_state_t state);
    virtual void view_click(TWidget *view, view_mouse_event_t const *event);
    virtual void view_dblclick(TWidget *view, view_mouse_event_t const *event);
    virtual void view_curpos(TWidget *view);
    virtual void view_created(TWidget *view);
    virtual void view_close(TWidget *view);
    virtual void view_switched(TWidget *view, tcc_renderer_type_t rt);
    virtual void view_mouse_over(TWidget *view, view_mouse_event_t const *event);
    virtual void view_loc_changed(TWidget *view, lochist_entry_t const *now, lochist_entry_t const *was);
    virtual void view_mouse_moved(TWidget *view, view_mouse_event_t const *event);

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
          std::string msg = "Method in class View_Hooks doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[12];
#endif

};


#endif