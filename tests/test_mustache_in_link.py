"""
Test that a mustache variable in a link element's '(url)' will be replaced.
"""
import os, subprocess

def test_mustache_link(tmpdir):

    # Define empty dictionaries
    doc = {}
    template = {}

    # Prepare file names
    doc['path'] = tmpdir.join("document.md")
    template['path'] = tmpdir.join("template.yaml")

    # Prepare file contents
    doc['metadata'] = '''---
mustache: {mustachefile}
---
'''
    doc['mfiles'] = { "mustachefile": template['path'] }
    doc['text'] = "This is [a link]({{url}})"
    template['content'] = """url: http://foo.bar"""

    # Write contents to files
    with open(doc['path'].strpath, "a") as myfile:
        myfile.write(doc['metadata'].format(**doc['mfiles']))
        myfile.write(doc['text'])
    template['path'].write(template['content'])

    # Run pandoc
    output = subprocess.check_output(["pandoc", doc['path'].strpath, "--filter", "pandoc-mustache", "--to=asciidoc", "--standalone"], universal_newlines=True)

    # Test output
    print (output)
    assert output == "This is [a link](http://foo.bar)"
