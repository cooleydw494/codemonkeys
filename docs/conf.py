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
    'sphinx_material',
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

html_theme = 'sphinx_material'
html_static_path = ['_static']

html_theme_options = {
    'nav_title': 'CodeMonkeys Sphinx Docs',
    'base_url': 'https://cooleydw494.github.io/codemonkeys',
    'color_primary': '#16141c',
    'color_accent': '#059fff',

    'repo_url': 'https://github.com/cooleydw494/codemonkeys',
    'repo_name': 'CodeMonkeys Framework Repo',
    'repo_type': 'github',

    'globaltoc_depth': 3,
    'globaltoc_collapse': True,
    'globaltoc_includehidden': True,

    'html_minify': True,
    'css_minify': True,
}
