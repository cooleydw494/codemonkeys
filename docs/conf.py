# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'codemonkeys'
copyright = '2023, David Cooley'
author = 'David Cooley'
release = '1.0.8'

sys.path.insert(0, os.path.abspath('../codemonkeys'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_rtd_theme',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
]
autosummary_generate = True
templates_path = ['templates']
exclude_patterns = []
autodoc_mock_imports = [
    'codemonkeys.defs',
    'monkey.monkeys',
    'codemonkeys.utils.imports.monkey',
    'codemonkeys.utils.imports.env',
    'codemonkeys.utils.imports.theme',
]
autodoc_default_options = {
    'members': True,
    'member-order': 'groupwise',
    'undoc-members': True,
    'private-members': True,
    'show-inheritance': True,
    'inherited-members': True,
}

autodoc_typehints = 'description'
autodoc_class_signature = 'separated'

html_logo = './_static/codemonkeys-sphinx-logo.png'
html_favicon = './_static/favicon.ico'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

html_context = {
    # 'display_github': True,
    'github_user': 'cooleydw494',
    'github_repo': 'codemonkeys',
    'github_version': 'main',
    'conf_py_path': '/docs/',
}

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'github_url': 'https://github.com/cooleydw494/codemonkeys',
    'analytics_id': 'G-DPDC9P9GP6',
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_nav_header_background': '#16141c',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'logo_only': True,
}
