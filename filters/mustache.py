#!/usr/bin/env python
from pandocfilters import toJSONFilter, Str, stringify
import pystache, yaml

"""
Pandoc filter to apply mustache templates on regular text.
"""

mustache_files = None
mustache_hashes = None
mhash = None

def mustache(key, value, format, meta):
    global mustache_files
    global mustache_hashes
    global mhash

    if mustache_files is None:
        mustache_files = list_mustache_files(meta)
        if mustache_files is not None:
            mustache_hashes = [yaml.load(open(file, 'r').read()) for file in mustache_files]
            mhash = { k: v for mdict in mustache_hashes for k, v in mdict.items() }

    # with open('debug.txt', 'a') as the_file:
    #     the_file.write(str(mustache_files))
    #     the_file.write('\n')

    if key == 'Str' and mhash is not None:
        return Str(pystache.render(value, mhash))


def list_mustache_files(meta):
    mustache_metadata = meta.get("mustache", {})

    if not mustache_metadata:  ## no mustache specified
        return None
    else:
        if mustache_metadata['t'] == 'MetaInlines':
            mustache_files = [stringify(mustache_metadata['c'])]
        elif mustache_metadata['t'] == 'MetaList':
            mustache_files = [stringify(item['c']) for item in mustache_metadata['c']]

        return mustache_files

if __name__ == "__main__":
    toJSONFilter(mustache)
