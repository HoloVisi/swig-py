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
            fp, pathname, description = imp.find_module('_xbmc', [dirname(__file__)])
        except ImportError:
            import _xbmc
            return _xbmc
        if fp is not None:
            try:
                _mod = imp.load_module('_xbmc', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _xbmc = swig_import_helper()
    del swig_import_helper
else:
    import _xbmc
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



def shutdown():
  return _xbmc.shutdown()
shutdown = _xbmc.shutdown

def restart():
  return _xbmc.restart()
restart = _xbmc.restart

def executescript(*args):
  return _xbmc.executescript(*args)
executescript = _xbmc.executescript

def executehttpapi(*args):
  return _xbmc.executehttpapi(*args)
executehttpapi = _xbmc.executehttpapi

def executeJSONRPC(*args):
  return _xbmc.executeJSONRPC(*args)
executeJSONRPC = _xbmc.executeJSONRPC

def sleep(*args):
  return _xbmc.sleep(*args)
sleep = _xbmc.sleep

def getLocalizedString(*args):
  return _xbmc.getLocalizedString(*args)
getLocalizedString = _xbmc.getLocalizedString

def getSkinDir():
  return _xbmc.getSkinDir()
getSkinDir = _xbmc.getSkinDir

def getLanguage():
  return _xbmc.getLanguage()
getLanguage = _xbmc.getLanguage

def getIPAddress():
  return _xbmc.getIPAddress()
getIPAddress = _xbmc.getIPAddress

def getDVDState():
  return _xbmc.getDVDState()
getDVDState = _xbmc.getDVDState

def getFreeMem():
  return _xbmc.getFreeMem()
getFreeMem = _xbmc.getFreeMem

def getInfoLabel(*args):
  return _xbmc.getInfoLabel(*args)
getInfoLabel = _xbmc.getInfoLabel

def getInfoImage(*args):
  return _xbmc.getInfoImage(*args)
getInfoImage = _xbmc.getInfoImage

def playSFX(*args):
  return _xbmc.playSFX(*args)
playSFX = _xbmc.playSFX

def enableNavSounds(*args):
  return _xbmc.enableNavSounds(*args)
enableNavSounds = _xbmc.enableNavSounds

def getCondVisibility(*args):
  return _xbmc.getCondVisibility(*args)
getCondVisibility = _xbmc.getCondVisibility

def getGlobalIdleTime():
  return _xbmc.getGlobalIdleTime()
getGlobalIdleTime = _xbmc.getGlobalIdleTime

def getCacheThumbName(*args):
  return _xbmc.getCacheThumbName(*args)
getCacheThumbName = _xbmc.getCacheThumbName

def translatePath(*args):
  return _xbmc.translatePath(*args)
translatePath = _xbmc.translatePath

def validatePath(*args):
  return _xbmc.validatePath(*args)
validatePath = _xbmc.validatePath

def getRegion(*args):
  return _xbmc.getRegion(*args)
getRegion = _xbmc.getRegion

def getSupportedMedia(*args):
  return _xbmc.getSupportedMedia(*args)
getSupportedMedia = _xbmc.getSupportedMedia

def skinHasImage(*args):
  return _xbmc.skinHasImage(*args)
skinHasImage = _xbmc.skinHasImage

def audioSuspend():
  return _xbmc.audioSuspend()
audioSuspend = _xbmc.audioSuspend

def audioResume():
  return _xbmc.audioResume()
audioResume = _xbmc.audioResume
SERVER_WEBSERVER = _xbmc.SERVER_WEBSERVER
SERVER_AIRPLAYSERVER = _xbmc.SERVER_AIRPLAYSERVER
SERVER_UPNPSERVER = _xbmc.SERVER_UPNPSERVER
SERVER_UPNPRENDERER = _xbmc.SERVER_UPNPRENDERER
SERVER_EVENTSERVER = _xbmc.SERVER_EVENTSERVER
SERVER_JSONRPCSERVER = _xbmc.SERVER_JSONRPCSERVER
SERVER_ZEROCONF = _xbmc.SERVER_ZEROCONF
PLAYLIST_MUSIC = _xbmc.PLAYLIST_MUSIC
PLAYLIST_VIDEO = _xbmc.PLAYLIST_VIDEO
PLAYER_CORE_AUTO = _xbmc.PLAYER_CORE_AUTO
PLAYER_CORE_DVDPLAYER = _xbmc.PLAYER_CORE_DVDPLAYER
PLAYER_CORE_MPLAYER = _xbmc.PLAYER_CORE_MPLAYER
PLAYER_CORE_PAPLAYER = _xbmc.PLAYER_CORE_PAPLAYER
TRAY_OPEN = _xbmc.TRAY_OPEN
DRIVE_NOT_READY = _xbmc.DRIVE_NOT_READY
TRAY_CLOSED_NO_MEDIA = _xbmc.TRAY_CLOSED_NO_MEDIA
TRAY_CLOSED_MEDIA_PRESENT = _xbmc.TRAY_CLOSED_MEDIA_PRESENT
LOGDEBUG = _xbmc.LOGDEBUG
LOGINFO = _xbmc.LOGINFO
LOGNOTICE = _xbmc.LOGNOTICE
LOGWARNING = _xbmc.LOGWARNING
LOGERROR = _xbmc.LOGERROR
LOGSEVERE = _xbmc.LOGSEVERE
LOGFATAL = _xbmc.LOGFATAL
LOGNONE = _xbmc.LOGNONE
CAPTURE_STATE_WORKING = _xbmc.CAPTURE_STATE_WORKING
CAPTURE_STATE_DONE = _xbmc.CAPTURE_STATE_DONE
CAPTURE_STATE_FAILED = _xbmc.CAPTURE_STATE_FAILED
CAPTURE_FLAG_CONTINUOUS = _xbmc.CAPTURE_FLAG_CONTINUOUS
CAPTURE_FLAG_IMMEDIATELY = _xbmc.CAPTURE_FLAG_IMMEDIATELY
class Player(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Player, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Player, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        if self.__class__ == Player:
            _self = None
        else:
            _self = self
        this = _xbmc.new_Player(_self, *args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmc.delete_Player
    __del__ = lambda self : None;
    def playStream(self, *args): return _xbmc.Player_playStream(self, *args)
    def playPlaylist(self, playlist = None, windowed = False): return _xbmc.Player_playPlaylist(self, playlist, windowed)
    def playCurrent(self, windowed = False): return _xbmc.Player_playCurrent(self, windowed)
    def stop(self): return _xbmc.Player_stop(self)
    def pause(self): return _xbmc.Player_pause(self)
    def playnext(self): return _xbmc.Player_playnext(self)
    def playprevious(self): return _xbmc.Player_playprevious(self)
    def playselected(self, *args): return _xbmc.Player_playselected(self, *args)
    def onPlayBackStarted(self): return _xbmc.Player_onPlayBackStarted(self)
    def onPlayBackEnded(self): return _xbmc.Player_onPlayBackEnded(self)
    def onPlayBackStopped(self): return _xbmc.Player_onPlayBackStopped(self)
    def onPlayBackPaused(self): return _xbmc.Player_onPlayBackPaused(self)
    def onPlayBackResumed(self): return _xbmc.Player_onPlayBackResumed(self)
    def onQueueNextItem(self): return _xbmc.Player_onQueueNextItem(self)
    def onPlayBackSpeedChanged(self, *args): return _xbmc.Player_onPlayBackSpeedChanged(self, *args)
    def onPlayBackSeek(self, *args): return _xbmc.Player_onPlayBackSeek(self, *args)
    def onPlayBackSeekChapter(self, *args): return _xbmc.Player_onPlayBackSeekChapter(self, *args)
    def isPlaying(self): return _xbmc.Player_isPlaying(self)
    def isPlayingAudio(self): return _xbmc.Player_isPlayingAudio(self)
    def isPlayingVideo(self): return _xbmc.Player_isPlayingVideo(self)
    def getPlayingFile(self): return _xbmc.Player_getPlayingFile(self)
    def getTime(self): return _xbmc.Player_getTime(self)
    def seekTime(self, *args): return _xbmc.Player_seekTime(self, *args)
    def setSubtitles(self, *args): return _xbmc.Player_setSubtitles(self, *args)
    def showSubtitles(self, *args): return _xbmc.Player_showSubtitles(self, *args)
    def getSubtitles(self): return _xbmc.Player_getSubtitles(self)
    def disableSubtitles(self): return _xbmc.Player_disableSubtitles(self)
    def getAvailableSubtitleStreams(self): return _xbmc.Player_getAvailableSubtitleStreams(self)
    def setSubtitleStream(self, *args): return _xbmc.Player_setSubtitleStream(self, *args)
    def getVideoInfoTag(self): return _xbmc.Player_getVideoInfoTag(self)
    def getMusicInfoTag(self): return _xbmc.Player_getMusicInfoTag(self)
    def getTotalTime(self): return _xbmc.Player_getTotalTime(self)
    def getAvailableAudioStreams(self): return _xbmc.Player_getAvailableAudioStreams(self)
    def setAudioStream(self, *args): return _xbmc.Player_setAudioStream(self, *args)
    def __disown__(self):
        self.this.disown()
        _xbmc.disown_Player(self)
        return weakref_proxy(self)
Player_swigregister = _xbmc.Player_swigregister
Player_swigregister(Player)

def log(*args):
  return _xbmc.log(*args)
log = _xbmc.log

def executebuiltin(*args):
  return _xbmc.executebuiltin(*args)
executebuiltin = _xbmc.executebuiltin

def makeLegalFilename(*args):
  return _xbmc.makeLegalFilename(*args)
makeLegalFilename = _xbmc.makeLegalFilename

def getCleanMovieTitle(*args):
  return _xbmc.getCleanMovieTitle(*args)
getCleanMovieTitle = _xbmc.getCleanMovieTitle

def startServer(*args):
  return _xbmc.startServer(*args)
startServer = _xbmc.startServer
cvar = _xbmc.cvar

class RenderCapture(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RenderCapture, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RenderCapture, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _xbmc.new_RenderCapture()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmc.delete_RenderCapture
    __del__ = lambda self : None;
    def getWidth(self): return _xbmc.RenderCapture_getWidth(self)
    def getHeight(self): return _xbmc.RenderCapture_getHeight(self)
    def getCaptureState(self): return _xbmc.RenderCapture_getCaptureState(self)
    def getAspectRatio(self): return _xbmc.RenderCapture_getAspectRatio(self)
    def getImageFormat(self): return _xbmc.RenderCapture_getImageFormat(self)
    def getImage(self): return _xbmc.RenderCapture_getImage(self)
    def capture(self, *args): return _xbmc.RenderCapture_capture(self, *args)
    def waitForCaptureStateChangeEvent(self, msecs = 0): return _xbmc.RenderCapture_waitForCaptureStateChangeEvent(self, msecs)
RenderCapture_swigregister = _xbmc.RenderCapture_swigregister
RenderCapture_swigregister(RenderCapture)

class InfoTagMusic(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, InfoTagMusic, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, InfoTagMusic, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _xbmc.new_InfoTagMusic()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmc.delete_InfoTagMusic
    __del__ = lambda self : None;
    def getURL(self): return _xbmc.InfoTagMusic_getURL(self)
    def getTitle(self): return _xbmc.InfoTagMusic_getTitle(self)
    def getArtist(self): return _xbmc.InfoTagMusic_getArtist(self)
    def getAlbum(self): return _xbmc.InfoTagMusic_getAlbum(self)
    def getAlbumArtist(self): return _xbmc.InfoTagMusic_getAlbumArtist(self)
    def getGenre(self): return _xbmc.InfoTagMusic_getGenre(self)
    def getDuration(self): return _xbmc.InfoTagMusic_getDuration(self)
    def getTrack(self): return _xbmc.InfoTagMusic_getTrack(self)
    def getDisc(self): return _xbmc.InfoTagMusic_getDisc(self)
    def getReleaseDate(self): return _xbmc.InfoTagMusic_getReleaseDate(self)
    def getListeners(self): return _xbmc.InfoTagMusic_getListeners(self)
    def getPlayCount(self): return _xbmc.InfoTagMusic_getPlayCount(self)
    def getLastPlayed(self): return _xbmc.InfoTagMusic_getLastPlayed(self)
    def getComment(self): return _xbmc.InfoTagMusic_getComment(self)
    def getLyrics(self): return _xbmc.InfoTagMusic_getLyrics(self)
InfoTagMusic_swigregister = _xbmc.InfoTagMusic_swigregister
InfoTagMusic_swigregister(InfoTagMusic)

class InfoTagVideo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, InfoTagVideo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, InfoTagVideo, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _xbmc.new_InfoTagVideo()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmc.delete_InfoTagVideo
    __del__ = lambda self : None;
    def getDirector(self): return _xbmc.InfoTagVideo_getDirector(self)
    def getWritingCredits(self): return _xbmc.InfoTagVideo_getWritingCredits(self)
    def getGenre(self): return _xbmc.InfoTagVideo_getGenre(self)
    def getTagLine(self): return _xbmc.InfoTagVideo_getTagLine(self)
    def getPlotOutline(self): return _xbmc.InfoTagVideo_getPlotOutline(self)
    def getPlot(self): return _xbmc.InfoTagVideo_getPlot(self)
    def getPictureURL(self): return _xbmc.InfoTagVideo_getPictureURL(self)
    def getTitle(self): return _xbmc.InfoTagVideo_getTitle(self)
    def getVotes(self): return _xbmc.InfoTagVideo_getVotes(self)
    def getCast(self): return _xbmc.InfoTagVideo_getCast(self)
    def getFile(self): return _xbmc.InfoTagVideo_getFile(self)
    def getPath(self): return _xbmc.InfoTagVideo_getPath(self)
    def getIMDBNumber(self): return _xbmc.InfoTagVideo_getIMDBNumber(self)
    def getYear(self): return _xbmc.InfoTagVideo_getYear(self)
    def getRating(self): return _xbmc.InfoTagVideo_getRating(self)
    def getPlayCount(self): return _xbmc.InfoTagVideo_getPlayCount(self)
    def getLastPlayed(self): return _xbmc.InfoTagVideo_getLastPlayed(self)
    def getOriginalTitle(self): return _xbmc.InfoTagVideo_getOriginalTitle(self)
    def getPremiered(self): return _xbmc.InfoTagVideo_getPremiered(self)
    def getFirstAired(self): return _xbmc.InfoTagVideo_getFirstAired(self)
InfoTagVideo_swigregister = _xbmc.InfoTagVideo_swigregister
InfoTagVideo_swigregister(InfoTagVideo)

class Keyboard(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Keyboard, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Keyboard, name)
    __repr__ = _swig_repr
    __swig_setmethods__["strDefault"] = _xbmc.Keyboard_strDefault_set
    __swig_getmethods__["strDefault"] = _xbmc.Keyboard_strDefault_get
    if _newclass:strDefault = _swig_property(_xbmc.Keyboard_strDefault_get, _xbmc.Keyboard_strDefault_set)
    __swig_setmethods__["strHeading"] = _xbmc.Keyboard_strHeading_set
    __swig_getmethods__["strHeading"] = _xbmc.Keyboard_strHeading_get
    if _newclass:strHeading = _swig_property(_xbmc.Keyboard_strHeading_get, _xbmc.Keyboard_strHeading_set)
    __swig_setmethods__["bHidden"] = _xbmc.Keyboard_bHidden_set
    __swig_getmethods__["bHidden"] = _xbmc.Keyboard_bHidden_get
    if _newclass:bHidden = _swig_property(_xbmc.Keyboard_bHidden_get, _xbmc.Keyboard_bHidden_set)
    __swig_setmethods__["dlg"] = _xbmc.Keyboard_dlg_set
    __swig_getmethods__["dlg"] = _xbmc.Keyboard_dlg_get
    if _newclass:dlg = _swig_property(_xbmc.Keyboard_dlg_get, _xbmc.Keyboard_dlg_set)
    def __init__(self, *args): 
        this = _xbmc.new_Keyboard(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmc.delete_Keyboard
    __del__ = lambda self : None;
    def doModal(self, autoclose = 0): return _xbmc.Keyboard_doModal(self, autoclose)
    def setDefault(self, *args): return _xbmc.Keyboard_setDefault(self, *args)
    def setHiddenInput(self, hidden = False): return _xbmc.Keyboard_setHiddenInput(self, hidden)
    def setHeading(self, *args): return _xbmc.Keyboard_setHeading(self, *args)
    def getText(self): return _xbmc.Keyboard_getText(self)
    def isConfirmed(self): return _xbmc.Keyboard_isConfirmed(self)
Keyboard_swigregister = _xbmc.Keyboard_swigregister
Keyboard_swigregister(Keyboard)

class PlayList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PlayList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PlayList, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _xbmc.new_PlayList(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _xbmc.delete_PlayList
    __del__ = lambda self : None;
    def getPlayListId(self): return _xbmc.PlayList_getPlayListId(self)
    def add(self, *args): return _xbmc.PlayList_add(self, *args)
    def load(self, *args): return _xbmc.PlayList_load(self, *args)
    def remove(self, *args): return _xbmc.PlayList_remove(self, *args)
    def clear(self): return _xbmc.PlayList_clear(self)
    def size(self): return _xbmc.PlayList_size(self)
    def shuffle(self): return _xbmc.PlayList_shuffle(self)
    def unshuffle(self): return _xbmc.PlayList_unshuffle(self)
    def getposition(self): return _xbmc.PlayList_getposition(self)
PlayList_swigregister = _xbmc.PlayList_swigregister
PlayList_swigregister(PlayList)

class Monitor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Monitor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Monitor, name)
    __repr__ = _swig_repr
    def __init__(self): 
        if self.__class__ == Monitor:
            _self = None
        else:
            _self = self
        this = _xbmc.new_Monitor(_self, )
        try: self.this.append(this)
        except: self.this = this
    def onSettingsChanged(self): return _xbmc.Monitor_onSettingsChanged(self)
    def onScreensaverActivated(self): return _xbmc.Monitor_onScreensaverActivated(self)
    def onScreensaverDeactivated(self): return _xbmc.Monitor_onScreensaverDeactivated(self)
    def onDatabaseUpdated(self, *args): return _xbmc.Monitor_onDatabaseUpdated(self, *args)
    def onDatabaseScanStarted(self, *args): return _xbmc.Monitor_onDatabaseScanStarted(self, *args)
    def onAbortRequested(self): return _xbmc.Monitor_onAbortRequested(self)
    __swig_destroy__ = _xbmc.delete_Monitor
    __del__ = lambda self : None;
    def GetId(self): return _xbmc.Monitor_GetId(self)
    def __disown__(self):
        self.this.disown()
        _xbmc.disown_Monitor(self)
        return weakref_proxy(self)
Monitor_swigregister = _xbmc.Monitor_swigregister
Monitor_swigregister(Monitor)

# This file is compatible with both classic and new-style classes.
