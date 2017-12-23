"""
Test that if a list with an empty value for a mustache file is specified in pandoc YAML metadata,
an error is thrown.
"""
import os, subprocess, pytest

def test_blank_mustache_list(tmpdir):

    # Define empty dictionaries
    doc = {}

    # Prepare file names
    doc['path'] = tmpdir.join("document.md")

    # Prepare file contents
    doc['metadata'] = '''---
mustache:
    -
---
'''
    doc['text'] = 'Hello {{place}}'

    # Write contents to files
    with open(doc['path'], "a") as myfile:
        myfile.write(doc['metadata'])
        myfile.write(doc['text'])

    # Run pandoc
    with pytest.raises(subprocess.CalledProcessError):
        output = subprocess.check_output(["pandoc", doc['path'], "--filter", "./filters/mustache.py"], universal_newlines=True)

def test_2el_mustache_list_wblank(tmpdir):

    # Define empty dictionaries
    doc = {}
    template = {}

    # Prepare file names
    doc['path'] = tmpdir.join("document.md")
    template['path'] = tmpdir.join("template.yaml")

    # Prepare file contents
    doc['metadata'] = '''---
mustache:
    - {mustachefile}
    -
---
'''
    doc['mfiles'] = { "mustachefile": template['path'] }
    doc['text'] = 'Hello {{place}}'
    template['content'] = "place: 'world'"

    # Write contents to files
    with open(doc['path'], "a") as myfile:
        myfile.write(doc['metadata'].format(**doc['mfiles']))
        myfile.write(doc['text'])
    template['path'].write(template['content'])

    # Run pandoc
    with pytest.raises(subprocess.CalledProcessError):
        output = subprocess.check_output(["pandoc", doc['path'], "--filter", "./filters/mustache.py"], universal_newlines=True)
