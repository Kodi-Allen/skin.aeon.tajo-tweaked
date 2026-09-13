import xbmc
import xbmcaddon
import xbmcgui


window = xbmcgui.Window(10000)
addon_id = xbmc.getInfoLabel('Container.PluginName')
fanart = ''

if addon_id:
    try:
        fanart = xbmcaddon.Addon(addon_id).getAddonInfo('fanart') or ''
    except Exception:
        fanart = ''

if fanart:
    window.setProperty('AeonTajo.PluginFanart', fanart)
else:
    window.clearProperty('AeonTajo.PluginFanart')
