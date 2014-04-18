import plistlib


# NOTE: Ignoring code complexity
def parse_catalog(fp): # NOQA
    plist = plistlib.readPlist(fp)

    for item in plist['Tracks'].itervalues():
        ok = True

        kind = item.get('Kind', None)
        artist = item.get('Artist')
        album = item.get('Album')
        track = item.get('Name')

        if kind is None or 'audio file' not in kind \
                or not artist \
                or not album \
                or not track:
            continue

        yield item
