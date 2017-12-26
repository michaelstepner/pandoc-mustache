"""
Test that if no mustache file is specified in pandoc YAML metadata, the doc is returned unaltered.
If there are mustache variables in the document, no error gets thrown: they appear in the output.
"""
import os, subprocess

def test_no_mustache_file(tmpdir):

    # Define empty dictionaries
    doc = {}

    # Prepare file names
    doc['path'] = tmpdir.join("document.md")

    # Prepare file contents
    doc['metadata'] = ''
    doc['text'] = 'Hello {{place}}'

    # Write contents to files
    with open(doc['path'].strpath, "a") as myfile:
        myfile.write(doc['metadata'])
        myfile.write(doc['text'])

    # Run pandoc
    output = subprocess.check_output(["pandoc", doc['path'].strpath, "--filter", "pandoc-mustache"], universal_newlines=True)

    # Test output
    assert output == "<p>Hello {{place}}</p>\n"

def test_blank_mustache_mapping(tmpdir):

    # Define empty dictionaries
    doc = {}

    # Prepare file names
    doc['path'] = tmpdir.join("document.md")

    # Prepare file contents
    doc['metadata'] = '''---
mustache:
---
'''
    doc['text'] = 'Hello {{place}}'

    # Write contents to files
    with open(doc['path'].strpath, "a") as myfile:
        myfile.write(doc['metadata'])
        myfile.write(doc['text'])

    # Run pandoc
    output = subprocess.check_output(["pandoc", doc['path'].strpath, "--filter", "pandoc-mustache"], universal_newlines=True)

    # Test output
    assert output == "<p>Hello {{place}}</p>\n"
