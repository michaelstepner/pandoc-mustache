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

def test_yaml_mapping_with_var(tmpdir):

    # Define empty dictionaries
    doc = {}
    template = {}

    # Prepare file names
    doc['path'] = tmpdir.join("document.md")
    template['path'] = tmpdir.join("template.yaml")

    # Prepare file contents
    doc['metadata'] = '''---
mustache: {mustachefile}
adj: dark
---
'''
    doc['mfiles'] = { "mustachefile": template['path'] }
    doc['text'] = 'Hello {{adj}} {{place}}'
    template['content'] = "place: 'world'"

    # Write contents to files
    with open(doc['path'].strpath, "a") as myfile:
        myfile.write(doc['metadata'].format(**doc['mfiles']))
        myfile.write(doc['text'])
    template['path'].write(template['content'])

    # Run pandoc
    output = subprocess.check_output(["pandoc", doc['path'].strpath, "--filter", "pandoc-mustache"], universal_newlines=True)

    # Test output
    assert output == "<p>Hello dark world</p>\n"

def test_yaml_list_1el_with_var(tmpdir):

    # Define empty dictionaries
    doc = {}
    template = {}

    # Prepare file names
    doc['path'] = tmpdir.join("document.md")
    template['path'] = tmpdir.join("template.yaml")

    # Prepare file contents
    doc['metadata'] = '''---
adj: dark
mustache:
    - {mustachefile}
---
'''
    doc['mfiles'] = { "mustachefile": template['path'] }
    doc['text'] = 'Hello {{adj}} {{place}}'
    template['content'] = "place: 'world'"

    # Write contents to files
    with open(doc['path'].strpath, "a") as myfile:
        myfile.write(doc['metadata'].format(**doc['mfiles']))
        myfile.write(doc['text'])
    template['path'].write(template['content'])

    # Run pandoc
    output = subprocess.check_output(["pandoc", doc['path'].strpath, "--filter", "pandoc-mustache"], universal_newlines=True)

    # Test output
    assert output == "<p>Hello dark world</p>\n"

def test_yaml_list_2el_with_var(tmpdir):

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
saying: my old friend
---
'''
    doc['mfiles'] = { "mustachefile": template['path'], "mustachefile2": template2['path'] }
    doc['text'] = 'Hello {{adj}} {{place}} {{saying}}'
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
    assert output == "<p>Hello dark world my old friend</p>\n"

def test_yaml_mapping_with_var_override(tmpdir):

    # Define empty dictionaries
    doc = {}
    template = {}

    # Prepare file names
    doc['path'] = tmpdir.join("document.md")
    template['path'] = tmpdir.join("template.yaml")

    # Prepare file contents
    doc['metadata'] = '''---
mustache: {mustachefile}
adj: great
---
'''
    doc['mfiles'] = { "mustachefile": template['path'] }
    doc['text'] = 'Hello {{adj}} {{place}}'
    template['content'] = """place: 'world'
adj: great
"""

    # Write contents to files
    with open(doc['path'].strpath, "a") as myfile:
        myfile.write(doc['metadata'].format(**doc['mfiles']))
        myfile.write(doc['text'])
    template['path'].write(template['content'])

    # Run pandoc
    output = subprocess.check_output(["pandoc", doc['path'].strpath, "--filter", "pandoc-mustache"], universal_newlines=True)

    # Test output
    assert output == "<p>Hello great world</p>\n"
