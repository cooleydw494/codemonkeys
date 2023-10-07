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
release = '0.3.0'

sys.path.insert(0, os.path.abspath('../codemonkeys'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_rtd_theme',
]
autosummary_generate = True
templates_path = ['templates']
exclude_patterns = ['codemonkeys.config.imports.env', 'codemonkeys.config.imports.theme', 'codemonkeys.config.imports.monkey']
autodoc_mock_imports = [
    'codemonkeys.defs', 'config.monkeys', 'codemonkeys.config.imports.env', 'codemonkeys.config.imports.theme', 'codemonkeys.config.imports.monkey'
]
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'undoc-members': True,
    'private-members': True,
    'show-inheritance': True,

}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
