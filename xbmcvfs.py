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
            fp, pathname, description = imp.find_module('_xbmcvfs', [dirname(__file__)])
        except ImportError:
            import _xbmcvfs
            return _xbmcvfs
        if fp is not None:
            try:
                _mod = imp.load_module('_xbmcvfs', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _xbmcvfs = swig_import_helper()
    del swig_import_helper
else:
    import _xbmcvfs
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


class File(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, File, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, File, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xbmcvfs.new_File(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmcvfs.delete_File
    __del__ = lambda self : None;
    def read(self, numBytes = 0): return _xbmcvfs.File_read(self, numBytes)
    def readBytes(self, numBytes = 0): return _xbmcvfs.File_readBytes(self, numBytes)
    def write(self, *args): return _xbmcvfs.File_write(self, *args)
    def size(self): return _xbmcvfs.File_size(self)
    def seek(self, *args): return _xbmcvfs.File_seek(self, *args)
    def close(self): return _xbmcvfs.File_close(self)
File_swigregister = _xbmcvfs.File_swigregister
File_swigregister(File)

class Stat(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Stat, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Stat, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xbmcvfs.new_Stat(*args)
        try: self.this.append(this)
        except: self.this = this
    def st_mode(self): return _xbmcvfs.Stat_st_mode(self)
    def st_ino(self): return _xbmcvfs.Stat_st_ino(self)
    def st_dev(self): return _xbmcvfs.Stat_st_dev(self)
    def st_nlink(self): return _xbmcvfs.Stat_st_nlink(self)
    def st_uid(self): return _xbmcvfs.Stat_st_uid(self)
    def st_gid(self): return _xbmcvfs.Stat_st_gid(self)
    def st_size(self): return _xbmcvfs.Stat_st_size(self)
    def st_atime(self): return _xbmcvfs.Stat_st_atime(self)
    def st_mtime(self): return _xbmcvfs.Stat_st_mtime(self)
    def st_ctime(self): return _xbmcvfs.Stat_st_ctime(self)
    __swig_destroy__ = _xbmcvfs.delete_Stat
    __del__ = lambda self : None;
Stat_swigregister = _xbmcvfs.Stat_swigregister
Stat_swigregister(Stat)


def copy(*args):
  return _xbmcvfs.copy(*args)
copy = _xbmcvfs.copy

def delete(*args):
  return _xbmcvfs.delete(*args)
delete = _xbmcvfs.delete

def rename(*args):
  return _xbmcvfs.rename(*args)
rename = _xbmcvfs.rename

def exists(*args):
  return _xbmcvfs.exists(*args)
exists = _xbmcvfs.exists

def mkdir(*args):
  return _xbmcvfs.mkdir(*args)
mkdir = _xbmcvfs.mkdir

def mkdirs(*args):
  return _xbmcvfs.mkdirs(*args)
mkdirs = _xbmcvfs.mkdirs

def listdir(*args):
  return _xbmcvfs.listdir(*args)
listdir = _xbmcvfs.listdir
# This file is compatible with both classic and new-style classes.


def rmdir(*args):
  return _xbmcvfs.rmdir(*args)
rmdir = _xbmcvfs.rmdir
