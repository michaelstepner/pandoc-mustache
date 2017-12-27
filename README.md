# pandoc-mustache: Variable Substitution in Pandoc

[![Development Status](https://img.shields.io/pypi/status/pandoc-mustache.svg)](https://pypi.python.org/pypi/pandoc-mustache/)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-mustache.svg)](https://pypi.python.org/pypi/pandoc-mustache/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-mustache.svg)](https://pypi.python.org/pypi/pandoc-mustache/)
[![Build Status](https://travis-ci.org/michaelstepner/pandoc-mustache.svg?branch=master)](https://travis-ci.org/michaelstepner/pandoc-mustache)

The **pandoc-mustache** filter allows you to put variables into your pandoc document text, with their values stored in a separate file. When you run `pandoc` the variables are replaced with their values.

*Technical note:* This pandoc filter is not a complete implementation of the [Mustache template spec](https://mustache.github.io/). Only variable replacement is supported: other [tag types](https://mustache.github.io/mustache.5.html#TAG-TYPES) are not currently supported.

## Example

This document, in `document.md`:

```
---
mustache: ./le_gaps.yaml
---
The richest American men live {{diff_le_richpoor_men}} years longer than the poorest men,
while the richest American women live {{diff_le_richpoor_women}} years longer than the poorest women.
```

Combined with these variable definitions, in `le_gaps.yaml`:

```yaml
diff_le_richpoor_men: "14.6"
diff_le_richpoor_women: "10.1"
```

Will be converted by `pandoc document.md --filter pandoc-mustache` to:

> The richest American men live 14.6 years longer than the poorest men, while the richest American women live 10.1 years longer than the poorest women.

## Installation

Install by opening a terminal and running:

```
pip install -U pandoc-mustache
```

Python 2.7, 3.4+, pypy, and pypy3 are supported.

## Usage

1. Within a pandoc document, variables are referenced by enclosing the variable name in double "mustaches", i.e. curly brackets, like `{{this}}`.

2. The variables are defined in one or more separate files, using YAML formatted key-value pairs. For example:

	```yaml
	place: Montreal
	temperature: '7'
	```

3. The pandoc document containing the mustache variables points to the YAML file (or files) which contain the variable definitions. These files are indicated using the mustache field in a [YAML metadata block](https://pandoc.org/MANUAL.html#metadata-blocks), typically placed at the top of the pandoc document. Absolute paths and relative paths are supported: relative paths are evaluated relative to the working directory where `pandoc` is being run.

    An example:

	```yaml
	---
	title: My Report
	author: Jane Smith
	mustache: ./vars.yaml
	---
	The temperature in {{place}} was {{temperature}} degrees.
	```

	Or, with more than one file:

	```yaml
	---
	title: My Report
	author: Jane Smith
	mustache:
	- ./vars.yaml
	- ./additional_vars.yaml
	---
	The temperature in {{place}} was {{temperature}} degrees.
	The humidity was {{humidity}}%.
	```

4. Run pandoc and replace all variables in the document with their values by adding `--filter pandoc-mustache` to the pandoc command.

### Tips and Tricks

* When defining variables in YAML, there is no need to enclose strings in quotes. But you should enclose numbers in quotes if you want them to appear in the document using the exact same formatting. Some examples:

	```yaml
	unquoted_string: Montreal  # becomes: Montreal
	quoted_string: 'Montreal'  # becomes: Montreal
	trailingzero_num: 7.40  # becomes: 7.4
	trailingzero_string: '7.40'  # becomes: 7.40
	```

* If you're writing a document that reports computed numerical results, you can program your code (in R, Python, Stata, etc.) to write those numbers to a YAML file automatically each time they are generated. By referencing your numerical results using variables instead of hard-coding them into the text, the document can be updated instantly if the results change. And you can be certain that all the numbers in the output document reflect the latest results of your analysis.

## Contributing

[![Project Status: Inactive – The project has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows.](http://www.repostatus.org/badges/latest/inactive.svg)](http://www.repostatus.org/#inactive)

This code is not being actively developed. It was created to fulfill my pandoc writing needs, and the current feature set is adequate for me.

If you have a **bug report**, you can create an issue or file a pull request. I'll look into it, time permitting.

If you have a **feature request**, it is unlikely that I will be able to implement it for you. You can create an issue to generate discussion. If you implement a feature, you can file pull request and I will review it eventually, as time permits. If you're interested in making major additions to the code, I'd be happy to welcome a new maintainer to the project.

## License

All of the files in this repository are released to the public domain under a [CC0 license](https://creativecommons.org/publicdomain/zero/1.0/) to permit the widest possible reuse.

## Acknowledgements

This pandoc filter was created using Sergio Correia's [panflute](https://github.com/sergiocorreia/panflute) package. The [panflute](https://github.com/sergiocorreia/panflute) repository also served as an inspiration for the organization of this repository.

### Related Filters

Scott Koga-Browes' [pandoc-abbreviations](https://github.com/scokobro/pandoc-abbreviations) filter also performs variable replacement in pandoc documents, using a different syntax.
