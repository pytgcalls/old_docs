import os
import sys
from datetime import datetime

from pytgcalls import __version__

sys.path.insert(0, os.path.abspath('../..'))

# DOCS VERSIONED v1.0.1
project = 'PyTgCalls'
copyright = f'2020-{datetime.now().year}, Laky-64'
author = 'Laky-64'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx_copybutton',
    'sphinx_tabs.tabs',
]

master_doc = 'index'
source_suffix = '.rst'
autodoc_member_order = 'bysource'

version = __version__.__version__
release = version

templates_path = ['_templates']

napoleon_use_rtype = False

pygments_style = 'friendly'

html_title = 'PyTgCalls Documentation'
html_theme = 'furo'
html_show_sourcelink = False
html_show_copyright = False

napoleon_use_param = False
