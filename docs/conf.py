#
# Twisted documentation build configuration file, created by
# sphinx-quickstart on Tue Jan 14 11:31:15 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("./_extensions"))
sys.path.insert(0, os.path.abspath(".."))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = "1.2"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
]

try:
    import rst2pdf.pdfbuilder

    extensions.append("rst2pdf.pdfbuilder")
except ImportError:
    pass

extensions.append("apilinks")
extensions.append("traclinks")
extensions.append("apidocs")

from twisted import version as twisted_version_object


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Twisted"
copyright = "2017, Twisted Matrix Labs"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "{major}.{minor}".format(
    major=twisted_version_object.major, minor=twisted_version_object.minor
)
# The full version, including alpha/beta/rc tags.
release = twisted_version_object.short()

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# See Read The Docs environment variables
# https://docs.readthedocs.io/en/stable/builds.html#build-environment
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

if not on_rtd:
    html_theme = "twistedtrac"

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ["_themes"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Output file base name for HTML help builder.
htmlhelp_basename = "Twisteddoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ("index", "Twisted.tex", "Twisted Documentation", "Twisted Matrix Labs", "manual"),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [("index", "twisted", "Twisted Documentation", ["Twisted Matrix Labs"], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "Twisted",
        "Twisted Documentation",
        "Twisted Matrix Labs",
        "Twisted",
        "One line description of project.",
        "Miscellaneous",
    ),
]


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = "Twisted"
epub_author = "Twisted Matrix Labs"
epub_publisher = "Twisted Matrix Labs"
epub_copyright = "2014, Twisted Matrix Labs"


# -- Extension configuration ----------------------------------------------

# Base url for apilinks extension
apilinks_base_url = "/documents/{}/api/".format(release)
if on_rtd:
    # For a PR the link is like:
    # https://twisted--1422.org.readthedocs.build/en/1422/
    # For a release:
    # https://twisted.readthedocs.io/en/twisted-20.3.0/
    # https://twisted.readthedocs.io/en/latest/
    apilinks_base_url = "/{}/{}/api/".format(
        os.environ["READTHEDOCS_LANGUAGE"],
        os.environ["READTHEDOCS_VERSION"],
    )

traclinks_base_url = "https://twistedmatrix.com/trac"

# A dict mapping unique IDs (which can be used to disambiguate references) to a
# tuple of (<external sphinx documentation URI>, <inventory file location>).
# The inventory file may be None to use the default location at the given URI.
intersphinx_mapping = {
    "py3": ("https://docs.python.org/3", None),
}
# How long to cache remote inventories. Positive is a number of days,
# negative means infinite. The default is 5 days, which should be fine
# for standard library documentation that does not typically change
# significantly after release.
# intersphinx_cache_limit = 5
