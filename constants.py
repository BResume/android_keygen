#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard library imports.
import json
import os

# Constant definitions.
_MODULE_PATH = os.path.dirname(os.path.realpath(__file__))
PACKAGE_NAME = "pydlock"
VERSION_FILE = os.path.join(_MODULE_PATH, "version.json")

with open(VERSION_FILE, "r") as file:
    
    # Versioning system: SemVer
    #  - MAJOR: Incremented for incompatible API changes.
    #  - MINOR: Incremented for new backwards compatible functionality.
    #  - PATCH: Incremented for make backwards compatible bug fixes.
    # For more info: https://semver.org/
    AUTHOR  = "Erick Edward Shepherd"
    VERSION = json.load(file)

DEFAULT_ENCODING = "utf-8"

# Module dunder definitions.
__author__  = AUTHOR
__version__ = (
    f"{VERSION['major']}."
    f"{VERSION['minor']}."
    f"{VERSION['patch']}."
)
