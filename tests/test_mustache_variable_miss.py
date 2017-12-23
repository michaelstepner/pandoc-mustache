"""
Test that error is thrown if the document contains a mustache {{variable}} that does not exist
in the template.
"""
import os, subprocess, pytest

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
    with open(doc['path'], "a") as myfile:
        myfile.write(doc['metadata'].format(**doc['mfiles']))
        myfile.write(doc['text'])
    template['path'].write(template['content'])

    # Run pandoc
    with pytest.raises(subprocess.CalledProcessError):
        output = subprocess.check_output(["pandoc", doc['path'], "--filter", "./filters/mustache.py"], universal_newlines=True)

    # Test output
    #assert output == "<p>Hello world</p>\n"
