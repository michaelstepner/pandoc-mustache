"""
Test that the pandoc metadata block containing mustache templates can be in various formats:

---
mustache: /path/to/file
---

---
mustache:
    - /path/to/file
---

---
mustache:
    - /path/to/file1
    - /path/to/file2
---

"""
import os, subprocess

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
    template['content'] = "place: 'world'"

    # Write contents to files
    with open(doc['path'].strpath, "a") as myfile:
        myfile.write(doc['metadata'].format(**doc['mfiles']))
        myfile.write(doc['text'])
    template['path'].write(template['content'])

    # Run pandoc
    output = subprocess.check_output(["pandoc", doc['path'].strpath, "--filter", "pandoc-mustache"], universal_newlines=True)

    # Test output
    assert output == "<p>Hello world</p>\n"

def test_yaml_list_1el(tmpdir):

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

    # Run pandoc
    output = subprocess.check_output(["pandoc", doc['path'].strpath, "--filter", "pandoc-mustache"], universal_newlines=True)

    # Test output
    assert output == "<p>Hello world</p>\n"

def test_yaml_list_2el(tmpdir):

    # Define empty dictionaries
    doc = {}
    template = {}
    template2 = {}

    # Prepare file names
    doc['path'] = tmpdir.join("document.md")
    template['path'] = tmpdir.join("template.yaml")
    template2['path'] = tmpdir.join("template2.yaml")

    # Prepare file contents
    doc['metadata'] = '''---
mustache:
    - {mustachefile}
    - {mustachefile2}
---
'''
    doc['mfiles'] = { "mustachefile": template['path'], "mustachefile2": template2['path'] }
    doc['text'] = 'Hello {{adj}} {{place}}'
    template['content'] = "place: 'world'"
    template2['content'] = "adj: 'dark'"

    # Write contents to files
    with open(doc['path'].strpath, "a") as myfile:
        myfile.write(doc['metadata'].format(**doc['mfiles']))
        myfile.write(doc['text'])
    template['path'].write(template['content'])
    template2['path'].write(template2['content'])

    # Run pandoc
    output = subprocess.check_output(["pandoc", doc['path'].strpath, "--filter", "pandoc-mustache"], universal_newlines=True)

    # Test output
    assert output == "<p>Hello dark world</p>\n"
