import hashlib
import sys

import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs


WINDOW = xbmcgui.Window(10000)
DEFAULT_BASE = 'special://profile/addon_data/plugin.video.themoviedb.helper/'


def get_arg(name, default=''):
    prefix = f'{name}='
    for arg in sys.argv[1:]:
        if arg.startswith(prefix):
            return arg[len(prefix):].strip().strip('"').strip("'")
    return default


def get_int_info(label, default):
    try:
        return int(xbmc.getInfoLabel(label) or default)
    except (TypeError, ValueError):
        return default


def join_path(base, *parts):
    value = (base or DEFAULT_BASE).replace('\\', '/')
    if not value.endswith('/'):
        value += '/'
    return value + '/'.join(str(part).strip('/\\') for part in parts)


def get_helper_base():
    try:
        addon = xbmcaddon.Addon('plugin.video.themoviedb.helper')
        return addon.getSettingString('image_location') or DEFAULT_BASE
    except Exception:
        return DEFAULT_BASE


def get_cached_blur(source):
    radius = get_int_info('Skin.String(TMDbHelper.Blur.Radius)', 40)
    size = get_int_info('Skin.String(TMDbHelper.Blur.Size)', 480)
    image_hash = hashlib.md5(str(source).encode(errors='surrogatepass')).hexdigest()
    filename = f'{image_hash}-{radius}-{size}.jpg'
    return join_path(get_helper_base(), 'blur_v2', filename)


def run_tmdbhelper(source, prefix):
    prop = f'{prefix}.BlurSource'
    WINDOW.setProperty(f'TMDbHelper.WinProp.{prop}', source)
    xbmc.executebuiltin(f'RunScript(plugin.video.themoviedb.helper,blur_image=$WINPROP[{prop}],prefix={prefix})')


def main():
    prefix = get_arg('prefix', 'VideoInfo') or 'VideoInfo'
    source_prop = get_arg('source_prop', 'VideoInfo.BlurSource') or 'VideoInfo.BlurSource'
    source = WINDOW.getProperty(source_prop)

    blur_prop = f'TMDbHelper.{prefix}.BlurImage'
    original_prop = f'{blur_prop}.Original'

    if not source:
        WINDOW.clearProperty(blur_prop)
        WINDOW.clearProperty(original_prop)
        return

    cached = get_cached_blur(source)
    if xbmcvfs.exists(cached):
        WINDOW.setProperty(blur_prop, cached)
        WINDOW.setProperty(original_prop, source)
        return

    run_tmdbhelper(source, prefix)


if __name__ == '__main__':
    main()
