# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths to sys.path if your modules are outside the root
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Activate U.co.uk Account'
copyright = '2025, U.co.uk'
author = 'U.co.uk Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions (add as needed)
extensions = []

# Allow reStructuredText raw HTML
raw_enabled = True

# Templates and patterns to ignore
templates_path = ['_templates']  # Uncomment if using custom templates
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# HTML theme (uncomment and customize if needed)
# html_theme = 'sphinx_rtd_theme'

# Basic page info
html_title = "How to Activate Your U.co.uk Account – Complete Guide"
html_short_title = "U.co.uk Activation"
html_favicon = 'favicon.ico'  # Ensure this file is in the _static or root folder

# Hide "View page source"
html_show_sourcelink = False

# Allow unsafe raw HTML in .rst files
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static assets (uncomment if using)
# html_static_path = ['_static']
