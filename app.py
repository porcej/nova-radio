
#!/usr/bin/env python
# -*- coding: ascii -*-

"""
NOVA Public Safety Radio Website

Changelog:
    - 2019-10-04 - Initial Commit
"""

__author__ = "Joseph Porcelli (joe@kt3i.com)"
__version__ = "0.0.1"
__copyright__ = "Copyright (c) 2019 Joseph Porcelli"

from app import create_app

app = create_app()
