"""
Test that a mustache variable in the abstract will be replaced.
"""
import os, subprocess

def test_mustache_abstract(tmpdir):

    # Define empty dictionaries
    doc = {}
    template = {}

    # Prepare file names
    doc['path'] = tmpdir.join("document.md")
    template['path'] = tmpdir.join("template.yaml")

    # Prepare file contents
    doc['metadata'] = '''---
abstract: Hello {{{{place}}}}.
mustache: {mustachefile}
---
'''  # quadruple curly brace will be printed as double curly brace, doubling is escaping from .format
    doc['mfiles'] = { "mustachefile": template['path'] }
    doc['text'] = "It's {{who}}."
    template['content'] = """place: 'world'
who: 'me'
"""

    # Write contents to files
    with open(doc['path'], "a") as myfile:
        myfile.write(doc['metadata'].format(**doc['mfiles']))
        myfile.write(doc['text'])
    template['path'].write(template['content'])

    # Run pandoc
    output = subprocess.check_output(["pandoc", doc['path'], "--filter", "./src/pandoc-mustache.py", "--to=asciidoc", "--standalone"], universal_newlines=True)

    # Test output
    print (output)
    assert output == """[abstract]
== Abstract
Hello world.

It's me.
"""
