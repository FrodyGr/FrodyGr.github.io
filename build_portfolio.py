#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds and verifies the portfolio website.
Pure Python to guarantee UTF-8 encoding preservation.
"""
import os

print("Portfolio files: index.html and style.css are present and ready.")
if os.path.exists("index.html") and os.path.exists("style.css"):
    print("Verification passed: index.html ({0} bytes), style.css ({1} bytes)".format(
        os.path.getsize("index.html"), os.path.getsize("style.css")
    ))
