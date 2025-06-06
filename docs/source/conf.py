# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os

# -- Project information -----------------------------------------------------

project = 'QBlade Documentation'
copyright = '2024, David Marten, Joseph Saverin, Robert Behrens de Luna, Sebastian Perez-Becker, licensed under CC BY-NC-ND'
author = 'D. Marten, J. Saverin, R. Behrens de Luna, S. Perez-Becker'

# The full version, including alpha/beta/rc tags
release = '2.0.8'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib.bibtex','sphinx.ext.autosectionlabel','sphinx_copybutton','sphinx_rtd_theme']

# bibliography
bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'unsrt'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Include the option to number the figures
numfig = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_theme_path = ['_themes', ]
html_logo = 'images/q_logo_black.png'

html_theme_options = { 'navigation_depth': 5, }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# custom.css is inside one of the html_static_path folders (e.g. _static)
html_css_files = ['custom.css']

html_js_files = ['custom.js']

#html_theme_options = {
#    'logo_only': False,
#    'display_version': True,
#    'prev_next_buttons_location': 'bottom',
#    'style_external_links': False,
#    'vcs_pageview_mode': '',
#    'style_nav_header_background': 'white',
#    # Toc options
#    'collapse_navigation': True,
#    'sticky_navigation': True,
#    'navigation_depth': 4,
#    'includehidden': True,
#    'titles_only': False
#}

# -- New additions to handle Read the Docs deprecation -----------------------

# Set canonical URL from the Read the Docs Domain
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    html_context = {"READTHEDOCS": True}