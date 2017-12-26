"""
Test that escaping characters for HTML is disabled.
"""
import os, subprocess

def test_escape_singlequote(tmpdir):

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
    doc['text'] = 'Hello {{place}}'
    template['content'] = "place: world ' universe"

    # Write contents to files
    with open(doc['path'].strpath, "a") as myfile:
        myfile.write(doc['metadata'].format(**doc['mfiles']))
        myfile.write(doc['text'])
    template['path'].write(template['content'])

    # Run pandoc
    output = subprocess.check_output(["pandoc", doc['path'].strpath, "--filter", "pandoc-mustache", "--to=plain"], universal_newlines=True)

    # Test output
    assert output == "Hello world ' universe\n"

def test_escape_gt(tmpdir):

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
    doc['text'] = 'Hello {{place}}'
    template['content'] = "place: world > universe"

    # Write contents to files
    with open(doc['path'].strpath, "a") as myfile:
        myfile.write(doc['metadata'].format(**doc['mfiles']))
        myfile.write(doc['text'])
    template['path'].write(template['content'])

    # Run pandoc
    output = subprocess.check_output(["pandoc", doc['path'].strpath, "--filter", "pandoc-mustache", "--to=plain"], universal_newlines=True)

    # Test output
    assert output == "Hello world > universe\n"

def test_escape_ampersand(tmpdir):

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
    doc['text'] = 'Hello {{place}}'
    template['content'] = "place: world & universe"

    # Write contents to files
    with open(doc['path'].strpath, "a") as myfile:
        myfile.write(doc['metadata'].format(**doc['mfiles']))
        myfile.write(doc['text'])
    template['path'].write(template['content'])

    # Run pandoc
    output = subprocess.check_output(["pandoc", doc['path'].strpath, "--filter", "pandoc-mustache", "--to=plain"], universal_newlines=True)

    # Test output
    assert output == "Hello world & universe\n"
