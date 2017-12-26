"""
Pandoc filter to apply mustache templates on regular text.
"""
from past.builtins import basestring
from panflute import *
import pystache, yaml

def prepare(doc):
    """ Parse metadata to obtain list of mustache templates,
        then load those templates.
    """
    doc.mustache_files = doc.get_metadata('mustache')
    if isinstance(doc.mustache_files, basestring):  # process single YAML value stored as string
        if not doc.mustache_files:
            doc.mustache_files = None  # switch empty string back to None
        else:
            doc.mustache_files = [ doc.mustache_files ]  # put non-empty string in list
    # with open('debug.txt', 'a') as the_file:
    #     the_file.write(str(doc.mustache_files))
    #     the_file.write('\n')
    if doc.mustache_files is not None:
        doc.mustache_hashes = [yaml.load(open(file, 'r').read()) for file in doc.mustache_files]
        doc.mhash = { k: v for mdict in doc.mustache_hashes for k, v in mdict.items() }  # combine list of dicts into a single dict
        doc.mrenderer = pystache.Renderer(escape=lambda u: u, missing_tags='strict')
    else:
        doc.mhash = None

def action(elem, doc):
    """ Apply combined mustache template to all strings in document.
    """
    if type(elem) == Str and doc.mhash is not None:
        elem.text = doc.mrenderer.render(elem.text, doc.mhash)
        return elem

def main(doc=None):
    return run_filter(action, prepare=prepare, doc=doc)

if __name__ == '__main__':
    main()
