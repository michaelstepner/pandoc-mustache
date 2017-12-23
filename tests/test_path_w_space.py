import os
import subprocess

def test_yaml_header_styles(tmpdir):

    # Prepare file names
    doc = tmpdir.join("document.md")
    template = tmpdir.mkdir("template folder").join("template.yaml")

    # Prepare file contents
    doc_metadata = '''---
mustache: {mustachefile}
---
'''
    doc_text = 'Hello {{place}}'
    template_content = "place: 'world'"
    mfiles = { "mustachefile": template }

    # Write contents to files
    with open(doc, "a") as myfile:
        myfile.write(doc_metadata.format(**mfiles))
        myfile.write(doc_text)
    template.write(template_content)

    # Run pandoc
    output = subprocess.check_output(["pandoc", doc, "--filter", "./filters/mustache.py"], universal_newlines=True)

    # Test output
    assert output == "<p>Hello world</p>\n"
