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
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
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
    'inherited-members': True,  # Added to include inherited members in documentation
}

autodoc_typehints = 'description'
autodoc_class_signature = 'separated'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
