#!/usr/bin/env python

"""
Pandoc filter to apply mustache templates on regular text.
"""

from pandocfilters import toJSONFilter, Str
import pystache, yaml


def mustache(key, value, format, meta):
    mustache_files = list_mustache_files(meta)
    if key == 'Str' and mustache_files is not None:
        mustache_hashes = [yaml.load(open(file, 'r').read()) for file in mustache_files]
        mhash = { k: v for mdict in mustache_hashes for k, v in mdict.items() }

        # with open('debug.txt', 'a') as the_file:
        #     the_file.write(str(mhash))

        return Str(pystache.render(value, mhash))


def list_mustache_files(meta):
    mustache_metadata = meta.get("mustache", {})

    if not mustache_metadata:  ## no mustache specified
        return None
    else:
        if mustache_metadata['t'] == 'MetaInlines':
            mustache_files = [item['c'] for item in mustache_metadata['c']]
        elif mustache_metadata['t'] == 'MetaList':
            mustache_files = [item.get('c')[0].get('c') for item in mustache_metadata['c']]

        return mustache_files

if __name__ == "__main__":
    toJSONFilter(mustache)
