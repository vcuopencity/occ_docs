# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OpenCyberCity Testbed'
copyright = '2026-%Y, OCC Team' # %Y is a placeholder that returns the current year
author = 'OCC Team'
release = '0.5.1' # Unlke with our ROS packages, please keep this somewhat updated

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme' # deciding between 'sphinx_rtd_theme' and 'furo'
html_static_path = ['_static']

html_logo = '_static/home/CCI_logo.avif' # path to logo from config dir. (if furo, will show this and light/dark)

html_static_path = ["_static"]
html_theme_options = {
    'logo_only': False, # Toggle for the text above logo (sphinx_rtd_theme)
    # "light_logo": "CCI_logo.avif", # Light mode logo (furo), optional btw
    # "dark_logo": "CCI_logo.avif", # Dark mode logo (furo), optional btw
}