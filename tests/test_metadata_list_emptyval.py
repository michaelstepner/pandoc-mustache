"""
Test that if a list with an empty value for a mustache file is specified in pandoc YAML metadata,
an error is thrown.
"""
import os, subprocess, sys

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
    with open(doc['path'].strpath, "a") as myfile:
        myfile.write(doc['metadata'])
        myfile.write(doc['text'])

    # Run pandoc, assert error
    try:
        output = subprocess.check_output(["pandoc", doc['path'].strpath, "--filter", "pandoc-mustache"], universal_newlines=True, stderr=subprocess.STDOUT)
        assert 0  # expecting an exception when calling pandoc
    except subprocess.CalledProcessError as e:
        assert e.returncode == 83
        if (sys.version_info > (3, 0)):  # Python 3
            assert "FileNotFoundError" in e.output
        else:
            assert "IOError" in e.output
        assert "No such file or directory:" in e.output

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
        if (sys.version_info > (3, 0)):  # Python 3
            assert "FileNotFoundError" in e.output
        else:
            assert "IOError" in e.output
        assert "No such file or directory:" in e.output
