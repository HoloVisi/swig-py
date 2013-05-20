# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_xbmcgui', [dirname(__file__)])
        except ImportError:
            import _xbmcgui
            return _xbmcgui
        if fp is not None:
            try:
                _mod = imp.load_module('_xbmcgui', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _xbmcgui = swig_import_helper()
    del swig_import_helper
else:
    import _xbmcgui
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x



def lock():
  return _xbmcgui.lock()
lock = _xbmcgui.lock

def unlock():
  return _xbmcgui.unlock()
unlock = _xbmcgui.unlock

def getCurrentWindowId():
  return _xbmcgui.getCurrentWindowId()
getCurrentWindowId = _xbmcgui.getCurrentWindowId

def getCurrentWindowDialogId():
  return _xbmcgui.getCurrentWindowDialogId()
getCurrentWindowDialogId = _xbmcgui.getCurrentWindowDialogId
ICON_OVERLAY_NONE = _xbmcgui.ICON_OVERLAY_NONE
ICON_OVERLAY_RAR = _xbmcgui.ICON_OVERLAY_RAR
ICON_OVERLAY_ZIP = _xbmcgui.ICON_OVERLAY_ZIP
ICON_OVERLAY_LOCKED = _xbmcgui.ICON_OVERLAY_LOCKED
ICON_OVERLAY_HAS_TRAINER = _xbmcgui.ICON_OVERLAY_HAS_TRAINER
ICON_OVERLAY_TRAINED = _xbmcgui.ICON_OVERLAY_TRAINED
ICON_OVERLAY_UNWATCHED = _xbmcgui.ICON_OVERLAY_UNWATCHED
ICON_OVERLAY_WATCHED = _xbmcgui.ICON_OVERLAY_WATCHED
ICON_OVERLAY_HD = _xbmcgui.ICON_OVERLAY_HD
class ListItem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ListItem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ListItem, name)
    __repr__ = _swig_repr
    __swig_setmethods__["item"] = _xbmcgui.ListItem_item_set
    __swig_getmethods__["item"] = _xbmcgui.ListItem_item_get
    if _newclass:item = _swig_property(_xbmcgui.ListItem_item_get, _xbmcgui.ListItem_item_set)
    def __init__(self, *args): 
        this = _xbmcgui.new_ListItem(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmcgui.delete_ListItem
    __del__ = lambda self : None;
    def getLabel(self): return _xbmcgui.ListItem_getLabel(self)
    def getLabel2(self): return _xbmcgui.ListItem_getLabel2(self)
    def setLabel(self, *args): return _xbmcgui.ListItem_setLabel(self, *args)
    def setLabel2(self, *args): return _xbmcgui.ListItem_setLabel2(self, *args)
    def setIconImage(self, *args): return _xbmcgui.ListItem_setIconImage(self, *args)
    def setThumbnailImage(self, *args): return _xbmcgui.ListItem_setThumbnailImage(self, *args)
    def select(self, *args): return _xbmcgui.ListItem_select(self, *args)
    def isSelected(self): return _xbmcgui.ListItem_isSelected(self)
    def setInfo(self, *args): return _xbmcgui.ListItem_setInfo(self, *args)
    def addStreamInfo(self, *args): return _xbmcgui.ListItem_addStreamInfo(self, *args)
    def addContextMenuItems(self, *args): return _xbmcgui.ListItem_addContextMenuItems(self, *args)
    def setProperty(self, *args): return _xbmcgui.ListItem_setProperty(self, *args)
    def getProperty(self, *args): return _xbmcgui.ListItem_getProperty(self, *args)
    def setPath(self, *args): return _xbmcgui.ListItem_setPath(self, *args)
    def setMimeType(self, *args): return _xbmcgui.ListItem_setMimeType(self, *args)
    def getdescription(self): return _xbmcgui.ListItem_getdescription(self)
    def getduration(self): return _xbmcgui.ListItem_getduration(self)
    def getfilename(self): return _xbmcgui.ListItem_getfilename(self)
ListItem_swigregister = _xbmcgui.ListItem_swigregister
ListItem_swigregister(ListItem)
cvar = _xbmcgui.cvar

CONTROL_TEXT_OFFSET_X = _xbmcgui.CONTROL_TEXT_OFFSET_X
CONTROL_TEXT_OFFSET_Y = _xbmcgui.CONTROL_TEXT_OFFSET_Y
class Control(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Control, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Control, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xbmcgui.new_Control(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmcgui.delete_Control
    __del__ = lambda self : None;
    def canAcceptMessages(self, *args): return _xbmcgui.Control_canAcceptMessages(self, *args)
    def setLabel(self, *args): return _xbmcgui.Control_setLabel(self, *args)
    def reset(self): return _xbmcgui.Control_reset(self)
    def setSelected(self, *args): return _xbmcgui.Control_setSelected(self, *args)
    def setPercent(self, *args): return _xbmcgui.Control_setPercent(self, *args)
    def setDisabledColor(self, *args): return _xbmcgui.Control_setDisabledColor(self, *args)
    def getPercent(self): return _xbmcgui.Control_getPercent(self)
    def getLabel(self): return _xbmcgui.Control_getLabel(self)
    def getText(self): return _xbmcgui.Control_getText(self)
    def size(self): return _xbmcgui.Control_size(self)
    def setTextures(self, *args): return _xbmcgui.Control_setTextures(self, *args)
    def setText(self, *args): return _xbmcgui.Control_setText(self, *args)
    def setStaticContent(self, *args): return _xbmcgui.Control_setStaticContent(self, *args)
    def setSpace(self, *args): return _xbmcgui.Control_setSpace(self, *args)
    def setRadioDimension(self, *args): return _xbmcgui.Control_setRadioDimension(self, *args)
    def setPageControlVisible(self, *args): return _xbmcgui.Control_setPageControlVisible(self, *args)
    def setItemHeight(self, *args): return _xbmcgui.Control_setItemHeight(self, *args)
    def setImageDimensions(self, *args): return _xbmcgui.Control_setImageDimensions(self, *args)
    def setImage(self, *args): return _xbmcgui.Control_setImage(self, *args)
    def setColorDiffuse(self, *args): return _xbmcgui.Control_setColorDiffuse(self, *args)
    def selectItem(self, *args): return _xbmcgui.Control_selectItem(self, *args)
    def scroll(self, *args): return _xbmcgui.Control_scroll(self, *args)
    def isSelected(self): return _xbmcgui.Control_isSelected(self)
    def getSpinControl(self): return _xbmcgui.Control_getSpinControl(self)
    def getSpace(self): return _xbmcgui.Control_getSpace(self)
    def getSelectedPosition(self): return _xbmcgui.Control_getSelectedPosition(self)
    def getSelectedItem(self): return _xbmcgui.Control_getSelectedItem(self)
    def getSelected(self): return _xbmcgui.Control_getSelected(self)
    def getListItem(self, *args): return _xbmcgui.Control_getListItem(self, *args)
    def getLabel2(self): return _xbmcgui.Control_getLabel2(self)
    def getItemHeight(self): return _xbmcgui.Control_getItemHeight(self)
    def addLabel(self, *args): return _xbmcgui.Control_addLabel(self, *args)
    def addItemStream(self, *args): return _xbmcgui.Control_addItemStream(self, *args)
    def addListItem(self, *args): return _xbmcgui.Control_addListItem(self, *args)
    def getId(self): return _xbmcgui.Control_getId(self)
    def __eq__(self, *args): return _xbmcgui.Control___eq__(self, *args)
    def __gt__(self, *args): return _xbmcgui.Control___gt__(self, *args)
    def __lt__(self, *args): return _xbmcgui.Control___lt__(self, *args)
    def getPosition(self): return _xbmcgui.Control_getPosition(self)
    def getX(self): return _xbmcgui.Control_getX(self)
    def getY(self): return _xbmcgui.Control_getY(self)
    def getHeight(self): return _xbmcgui.Control_getHeight(self)
    def getWidth(self): return _xbmcgui.Control_getWidth(self)
    def setEnabled(self, *args): return _xbmcgui.Control_setEnabled(self, *args)
    def setVisible(self, *args): return _xbmcgui.Control_setVisible(self, *args)
    def setVisibleCondition(self, *args): return _xbmcgui.Control_setVisibleCondition(self, *args)
    def setEnableCondition(self, *args): return _xbmcgui.Control_setEnableCondition(self, *args)
    def setAnimations(self, *args): return _xbmcgui.Control_setAnimations(self, *args)
    def setPosition(self, *args): return _xbmcgui.Control_setPosition(self, *args)
    def setWidth(self, *args): return _xbmcgui.Control_setWidth(self, *args)
    def setHeight(self, *args): return _xbmcgui.Control_setHeight(self, *args)
    def setNavigation(self, *args): return _xbmcgui.Control_setNavigation(self, *args)
    def controlUp(self, *args): return _xbmcgui.Control_controlUp(self, *args)
    def controlDown(self, *args): return _xbmcgui.Control_controlDown(self, *args)
    def controlLeft(self, *args): return _xbmcgui.Control_controlLeft(self, *args)
    def controlRight(self, *args): return _xbmcgui.Control_controlRight(self, *args)
Control_swigregister = _xbmcgui.Control_swigregister
Control_swigregister(Control)

class ControlSpin(Control):
    __swig_setmethods__ = {}
    for _s in [Control]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ControlSpin, name, value)
    __swig_getmethods__ = {}
    for _s in [Control]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ControlSpin, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _xbmcgui.delete_ControlSpin
    __del__ = lambda self : None;
    def setTextures(self, *args): return _xbmcgui.ControlSpin_setTextures(self, *args)
ControlSpin_swigregister = _xbmcgui.ControlSpin_swigregister
ControlSpin_swigregister(ControlSpin)

class ControlLabel(Control):
    __swig_setmethods__ = {}
    for _s in [Control]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ControlLabel, name, value)
    __swig_getmethods__ = {}
    for _s in [Control]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ControlLabel, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xbmcgui.new_ControlLabel(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmcgui.delete_ControlLabel
    __del__ = lambda self : None;
    def getLabel(self): return _xbmcgui.ControlLabel_getLabel(self)
    def setLabel(self, *args): return _xbmcgui.ControlLabel_setLabel(self, *args)
ControlLabel_swigregister = _xbmcgui.ControlLabel_swigregister
ControlLabel_swigregister(ControlLabel)

class ControlEdit(Control):
    __swig_setmethods__ = {}
    for _s in [Control]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ControlEdit, name, value)
    __swig_getmethods__ = {}
    for _s in [Control]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ControlEdit, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xbmcgui.new_ControlEdit(*args)
        try: self.this.append(this)
        except: self.this = this
    def setLabel(self, *args): return _xbmcgui.ControlEdit_setLabel(self, *args)
    def getLabel(self): return _xbmcgui.ControlEdit_getLabel(self)
    def setText(self, *args): return _xbmcgui.ControlEdit_setText(self, *args)
    def getText(self): return _xbmcgui.ControlEdit_getText(self)
    __swig_destroy__ = _xbmcgui.delete_ControlEdit
    __del__ = lambda self : None;
ControlEdit_swigregister = _xbmcgui.ControlEdit_swigregister
ControlEdit_swigregister(ControlEdit)

class ControlList(Control):
    __swig_setmethods__ = {}
    for _s in [Control]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ControlList, name, value)
    __swig_getmethods__ = {}
    for _s in [Control]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ControlList, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xbmcgui.new_ControlList(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmcgui.delete_ControlList
    __del__ = lambda self : None;
    def addItemStream(self, *args): return _xbmcgui.ControlList_addItemStream(self, *args)
    def addListItem(self, *args): return _xbmcgui.ControlList_addListItem(self, *args)
    def selectItem(self, *args): return _xbmcgui.ControlList_selectItem(self, *args)
    def reset(self): return _xbmcgui.ControlList_reset(self)
    def getSpinControl(self): return _xbmcgui.ControlList_getSpinControl(self)
    def getSelectedPosition(self): return _xbmcgui.ControlList_getSelectedPosition(self)
    def getSelectedItem(self): return _xbmcgui.ControlList_getSelectedItem(self)
    def setImageDimensions(self, *args): return _xbmcgui.ControlList_setImageDimensions(self, *args)
    def setItemHeight(self, *args): return _xbmcgui.ControlList_setItemHeight(self, *args)
    def setSpace(self, *args): return _xbmcgui.ControlList_setSpace(self, *args)
    def setPageControlVisible(self, *args): return _xbmcgui.ControlList_setPageControlVisible(self, *args)
    def size(self): return _xbmcgui.ControlList_size(self)
    def getItemHeight(self): return _xbmcgui.ControlList_getItemHeight(self)
    def getSpace(self): return _xbmcgui.ControlList_getSpace(self)
    def getListItem(self, *args): return _xbmcgui.ControlList_getListItem(self, *args)
    def setStaticContent(self, *args): return _xbmcgui.ControlList_setStaticContent(self, *args)
ControlList_swigregister = _xbmcgui.ControlList_swigregister
ControlList_swigregister(ControlList)

class ControlFadeLabel(Control):
    __swig_setmethods__ = {}
    for _s in [Control]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ControlFadeLabel, name, value)
    __swig_getmethods__ = {}
    for _s in [Control]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ControlFadeLabel, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xbmcgui.new_ControlFadeLabel(*args)
        try: self.this.append(this)
        except: self.this = this
    def addLabel(self, *args): return _xbmcgui.ControlFadeLabel_addLabel(self, *args)
    def reset(self): return _xbmcgui.ControlFadeLabel_reset(self)
    __swig_destroy__ = _xbmcgui.delete_ControlFadeLabel
    __del__ = lambda self : None;
ControlFadeLabel_swigregister = _xbmcgui.ControlFadeLabel_swigregister
ControlFadeLabel_swigregister(ControlFadeLabel)

class ControlTextBox(Control):
    __swig_setmethods__ = {}
    for _s in [Control]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ControlTextBox, name, value)
    __swig_getmethods__ = {}
    for _s in [Control]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ControlTextBox, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xbmcgui.new_ControlTextBox(*args)
        try: self.this.append(this)
        except: self.this = this
    def setText(self, *args): return _xbmcgui.ControlTextBox_setText(self, *args)
    def reset(self): return _xbmcgui.ControlTextBox_reset(self)
    def scroll(self, *args): return _xbmcgui.ControlTextBox_scroll(self, *args)
    __swig_destroy__ = _xbmcgui.delete_ControlTextBox
    __del__ = lambda self : None;
ControlTextBox_swigregister = _xbmcgui.ControlTextBox_swigregister
ControlTextBox_swigregister(ControlTextBox)

class ControlImage(Control):
    __swig_setmethods__ = {}
    for _s in [Control]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ControlImage, name, value)
    __swig_getmethods__ = {}
    for _s in [Control]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ControlImage, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xbmcgui.new_ControlImage(*args)
        try: self.this.append(this)
        except: self.this = this
    def setImage(self, *args): return _xbmcgui.ControlImage_setImage(self, *args)
    def setColorDiffuse(self, *args): return _xbmcgui.ControlImage_setColorDiffuse(self, *args)
    __swig_destroy__ = _xbmcgui.delete_ControlImage
    __del__ = lambda self : None;
ControlImage_swigregister = _xbmcgui.ControlImage_swigregister
ControlImage_swigregister(ControlImage)

class ControlProgress(Control):
    __swig_setmethods__ = {}
    for _s in [Control]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ControlProgress, name, value)
    __swig_getmethods__ = {}
    for _s in [Control]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ControlProgress, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xbmcgui.new_ControlProgress(*args)
        try: self.this.append(this)
        except: self.this = this
    def setPercent(self, *args): return _xbmcgui.ControlProgress_setPercent(self, *args)
    def getPercent(self): return _xbmcgui.ControlProgress_getPercent(self)
    __swig_destroy__ = _xbmcgui.delete_ControlProgress
    __del__ = lambda self : None;
ControlProgress_swigregister = _xbmcgui.ControlProgress_swigregister
ControlProgress_swigregister(ControlProgress)

class ControlButton(Control):
    __swig_setmethods__ = {}
    for _s in [Control]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ControlButton, name, value)
    __swig_getmethods__ = {}
    for _s in [Control]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ControlButton, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xbmcgui.new_ControlButton(*args)
        try: self.this.append(this)
        except: self.this = this
    def setLabel(self, *args): return _xbmcgui.ControlButton_setLabel(self, *args)
    def setDisabledColor(self, *args): return _xbmcgui.ControlButton_setDisabledColor(self, *args)
    def getLabel(self): return _xbmcgui.ControlButton_getLabel(self)
    def getLabel2(self): return _xbmcgui.ControlButton_getLabel2(self)
    __swig_destroy__ = _xbmcgui.delete_ControlButton
    __del__ = lambda self : None;
ControlButton_swigregister = _xbmcgui.ControlButton_swigregister
ControlButton_swigregister(ControlButton)

class ControlCheckMark(Control):
    __swig_setmethods__ = {}
    for _s in [Control]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ControlCheckMark, name, value)
    __swig_getmethods__ = {}
    for _s in [Control]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ControlCheckMark, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xbmcgui.new_ControlCheckMark(*args)
        try: self.this.append(this)
        except: self.this = this
    def getSelected(self): return _xbmcgui.ControlCheckMark_getSelected(self)
    def setSelected(self, *args): return _xbmcgui.ControlCheckMark_setSelected(self, *args)
    def setLabel(self, *args): return _xbmcgui.ControlCheckMark_setLabel(self, *args)
    def setDisabledColor(self, *args): return _xbmcgui.ControlCheckMark_setDisabledColor(self, *args)
    __swig_destroy__ = _xbmcgui.delete_ControlCheckMark
    __del__ = lambda self : None;
ControlCheckMark_swigregister = _xbmcgui.ControlCheckMark_swigregister
ControlCheckMark_swigregister(ControlCheckMark)

class ControlGroup(Control):
    __swig_setmethods__ = {}
    for _s in [Control]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ControlGroup, name, value)
    __swig_getmethods__ = {}
    for _s in [Control]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ControlGroup, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xbmcgui.new_ControlGroup(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmcgui.delete_ControlGroup
    __del__ = lambda self : None;
ControlGroup_swigregister = _xbmcgui.ControlGroup_swigregister
ControlGroup_swigregister(ControlGroup)

class ControlRadioButton(Control):
    __swig_setmethods__ = {}
    for _s in [Control]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ControlRadioButton, name, value)
    __swig_getmethods__ = {}
    for _s in [Control]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ControlRadioButton, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xbmcgui.new_ControlRadioButton(*args)
        try: self.this.append(this)
        except: self.this = this
    def setSelected(self, *args): return _xbmcgui.ControlRadioButton_setSelected(self, *args)
    def isSelected(self): return _xbmcgui.ControlRadioButton_isSelected(self)
    def setLabel(self, *args): return _xbmcgui.ControlRadioButton_setLabel(self, *args)
    def setRadioDimension(self, *args): return _xbmcgui.ControlRadioButton_setRadioDimension(self, *args)
    __swig_destroy__ = _xbmcgui.delete_ControlRadioButton
    __del__ = lambda self : None;
ControlRadioButton_swigregister = _xbmcgui.ControlRadioButton_swigregister
ControlRadioButton_swigregister(ControlRadioButton)

class ControlSlider(Control):
    __swig_setmethods__ = {}
    for _s in [Control]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ControlSlider, name, value)
    __swig_getmethods__ = {}
    for _s in [Control]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ControlSlider, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xbmcgui.new_ControlSlider(*args)
        try: self.this.append(this)
        except: self.this = this
    def getPercent(self): return _xbmcgui.ControlSlider_getPercent(self)
    def setPercent(self, *args): return _xbmcgui.ControlSlider_setPercent(self, *args)
    __swig_destroy__ = _xbmcgui.delete_ControlSlider
    __del__ = lambda self : None;
ControlSlider_swigregister = _xbmcgui.ControlSlider_swigregister
ControlSlider_swigregister(ControlSlider)

class Dialog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Dialog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Dialog, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _xbmcgui.new_Dialog()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmcgui.delete_Dialog
    __del__ = lambda self : None;
    def yesno(self, *args): return _xbmcgui.Dialog_yesno(self, *args)
    def select(self, *args): return _xbmcgui.Dialog_select(self, *args)
    def ok(self, *args): return _xbmcgui.Dialog_ok(self, *args)
    def browse(self, *args): return _xbmcgui.Dialog_browse(self, *args)
    def browseSingle(self, *args): return _xbmcgui.Dialog_browseSingle(self, *args)
    def browseMultiple(self, *args): return _xbmcgui.Dialog_browseMultiple(self, *args)
    def numeric(self, *args): return _xbmcgui.Dialog_numeric(self, *args)
Dialog_swigregister = _xbmcgui.Dialog_swigregister
Dialog_swigregister(Dialog)

class DialogProgress(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DialogProgress, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DialogProgress, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _xbmcgui.new_DialogProgress()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmcgui.delete_DialogProgress
    __del__ = lambda self : None;
    def create(self, *args): return _xbmcgui.DialogProgress_create(self, *args)
    def update(self, *args): return _xbmcgui.DialogProgress_update(self, *args)
    def close(self): return _xbmcgui.DialogProgress_close(self)
    def iscanceled(self): return _xbmcgui.DialogProgress_iscanceled(self)
DialogProgress_swigregister = _xbmcgui.DialogProgress_swigregister
DialogProgress_swigregister(DialogProgress)

class Action(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Action, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Action, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _xbmcgui.new_Action()
        try: self.this.append(this)
        except: self.this = this
    def getId(self): return _xbmcgui.Action_getId(self)
    def getButtonCode(self): return _xbmcgui.Action_getButtonCode(self)
    def getAmount1(self): return _xbmcgui.Action_getAmount1(self)
    def getAmount2(self): return _xbmcgui.Action_getAmount2(self)
    __swig_destroy__ = _xbmcgui.delete_Action
    __del__ = lambda self : None;
Action_swigregister = _xbmcgui.Action_swigregister
Action_swigregister(Action)

class Window(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Window, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Window, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        if self.__class__ == Window:
            _self = None
        else:
            _self = self
        this = _xbmcgui.new_Window(_self, *args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmcgui.delete_Window
    __del__ = lambda self : None;
    def onAction(self, *args): return _xbmcgui.Window_onAction(self, *args)
    def onControl(self, *args): return _xbmcgui.Window_onControl(self, *args)
    def onClick(self, *args): return _xbmcgui.Window_onClick(self, *args)
    def onFocus(self, *args): return _xbmcgui.Window_onFocus(self, *args)
    def onInit(self): return _xbmcgui.Window_onInit(self)
    def show(self): return _xbmcgui.Window_show(self)
    def setFocus(self, *args): return _xbmcgui.Window_setFocus(self, *args)
    def setFocusId(self, *args): return _xbmcgui.Window_setFocusId(self, *args)
    def getFocus(self): return _xbmcgui.Window_getFocus(self)
    def getFocusId(self): return _xbmcgui.Window_getFocusId(self)
    def removeControl(self, *args): return _xbmcgui.Window_removeControl(self, *args)
    def removeControls(self, *args): return _xbmcgui.Window_removeControls(self, *args)
    def getHeight(self): return _xbmcgui.Window_getHeight(self)
    def getWidth(self): return _xbmcgui.Window_getWidth(self)
    def getResolution(self): return _xbmcgui.Window_getResolution(self)
    def setCoordinateResolution(self, *args): return _xbmcgui.Window_setCoordinateResolution(self, *args)
    def setProperty(self, *args): return _xbmcgui.Window_setProperty(self, *args)
    def getProperty(self, *args): return _xbmcgui.Window_getProperty(self, *args)
    def clearProperty(self, *args): return _xbmcgui.Window_clearProperty(self, *args)
    def clearProperties(self): return _xbmcgui.Window_clearProperties(self)
    def close(self): return _xbmcgui.Window_close(self)
    def doModal(self): return _xbmcgui.Window_doModal(self)
    def addControl(self, *args): return _xbmcgui.Window_addControl(self, *args)
    def addControls(self, *args): return _xbmcgui.Window_addControls(self, *args)
    def getControl(self, *args): return _xbmcgui.Window_getControl(self, *args)
    def __disown__(self):
        self.this.disown()
        _xbmcgui.disown_Window(self)
        return weakref_proxy(self)
Window_swigregister = _xbmcgui.Window_swigregister
Window_swigregister(Window)

class WindowDialog(Window):
    __swig_setmethods__ = {}
    for _s in [Window]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, WindowDialog, name, value)
    __swig_getmethods__ = {}
    for _s in [Window]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, WindowDialog, name)
    __repr__ = _swig_repr
    def __init__(self): 
        if self.__class__ == WindowDialog:
            _self = None
        else:
            _self = self
        this = _xbmcgui.new_WindowDialog(_self, )
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmcgui.delete_WindowDialog
    __del__ = lambda self : None;
    def show(self): return _xbmcgui.WindowDialog_show(self)
    def close(self): return _xbmcgui.WindowDialog_close(self)
    def __disown__(self):
        self.this.disown()
        _xbmcgui.disown_WindowDialog(self)
        return weakref_proxy(self)
WindowDialog_swigregister = _xbmcgui.WindowDialog_swigregister
WindowDialog_swigregister(WindowDialog)

class WindowXML(Window):
    __swig_setmethods__ = {}
    for _s in [Window]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, WindowXML, name, value)
    __swig_getmethods__ = {}
    for _s in [Window]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, WindowXML, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        if self.__class__ == WindowXML:
            _self = None
        else:
            _self = self
        this = _xbmcgui.new_WindowXML(_self, *args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmcgui.delete_WindowXML
    __del__ = lambda self : None;
    def addItemString(self, *args): return _xbmcgui.WindowXML_addItemString(self, *args)
    def addListItem(self, *args): return _xbmcgui.WindowXML_addListItem(self, *args)
    def removeItem(self, *args): return _xbmcgui.WindowXML_removeItem(self, *args)
    def getCurrentListPosition(self): return _xbmcgui.WindowXML_getCurrentListPosition(self)
    def setCurrentListPosition(self, *args): return _xbmcgui.WindowXML_setCurrentListPosition(self, *args)
    def getListItem(self, *args): return _xbmcgui.WindowXML_getListItem(self, *args)
    def getListSize(self): return _xbmcgui.WindowXML_getListSize(self)
    def clearList(self): return _xbmcgui.WindowXML_clearList(self)
    def setProperty(self, *args): return _xbmcgui.WindowXML_setProperty(self, *args)
    def __disown__(self):
        self.this.disown()
        _xbmcgui.disown_WindowXML(self)
        return weakref_proxy(self)
WindowXML_swigregister = _xbmcgui.WindowXML_swigregister
WindowXML_swigregister(WindowXML)

class WindowXMLDialog(WindowXML):
    __swig_setmethods__ = {}
    for _s in [WindowXML]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, WindowXMLDialog, name, value)
    __swig_getmethods__ = {}
    for _s in [WindowXML]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, WindowXMLDialog, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        if self.__class__ == WindowXMLDialog:
            _self = None
        else:
            _self = self
        this = _xbmcgui.new_WindowXMLDialog(_self, *args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmcgui.delete_WindowXMLDialog
    __del__ = lambda self : None;
    def show(self): return _xbmcgui.WindowXMLDialog_show(self)
    def close(self): return _xbmcgui.WindowXMLDialog_close(self)
    def __disown__(self):
        self.this.disown()
        _xbmcgui.disown_WindowXMLDialog(self)
        return weakref_proxy(self)
WindowXMLDialog_swigregister = _xbmcgui.WindowXMLDialog_swigregister
WindowXMLDialog_swigregister(WindowXMLDialog)

# This file is compatible with both classic and new-style classes.
