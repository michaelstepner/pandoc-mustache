"""
Test that a mustache variable in the code or codeblock will be replaced.
"""
import os, subprocess

def test_mustache_code(tmpdir):

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
'''  # quadruple curly brace will be printed as double curly brace, doubling is escaping from .format
    doc['mfiles'] = { "mustachefile": template['path'] }
    doc['code'] = """`echo 'Hello {{who}}!'`
```
printf 'Hello {{who}}!
```
"""
    template['content'] = "who: 'world'"

    # Write contents to files
    with open(doc['path'].strpath, "a") as myfile:
        myfile.write(doc['metadata'].format(**doc['mfiles']))
        myfile.write(doc['code'])
    template['path'].write(template['content'])

    # Run pandoc
    output = subprocess.check_output(["pandoc", doc['path'].strpath, "--filter", "pandoc-mustache", "--to=markdown", "--standalone"], universal_newlines=True)
    # Remove header
    tested_output = output.split('\n', 4)[4]

    # Test output
    print (tested_output)
    assert tested_output == """`echo 'Hello world!'`

    printf 'Hello world!
"""
