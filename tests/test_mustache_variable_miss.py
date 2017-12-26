"""
Test that error is thrown if the document contains a mustache {{variable}} that does not exist
in the template.
"""
import os, subprocess, sys, platform

def test_yaml_mapping(tmpdir):

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
    template['content'] = "planet: 'world'"

    # Write contents to files
    with open(doc['path'].strpath, "a") as myfile:
        myfile.write(doc['metadata'].format(**doc['mfiles']))
        myfile.write(doc['text'])
    template['path'].write(template['content'])

    # Run pandoc, assert error
    try:
        output = subprocess.check_output(["pandoc", doc['path'].strpath, "--filter", "pandoc-mustache"], universal_newlines=True, stderr=subprocess.STDOUT)
        assert 0  # expecting an exception when calling pandoc
    except subprocess.CalledProcessError as e:
        assert e.returncode == 83
        if platform.python_implementation()=='CPython':
            assert "pystache.context.KeyNotFoundError" in e.output
        if (sys.version_info > (3, 0)):  # Python 3
            assert "Key 'place' not found" in e.output
        else:
            assert "Key u'place' not found" in e.output
