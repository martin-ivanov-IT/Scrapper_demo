"""
Configuration for pytest.

NOTE: This file is automatically included when running pytest.
      There is no need to import it explicitly in the test files.
"""

import os
import sys
import pytest


# allow the contents to be found automatically as if we were in that directory
sys.path.append(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
)

from module import example_function as example_function


@pytest.fixture
def some_fixture():
    return example_function()

def get_html():
    with open("firstArticle.txt", "r", encoding="utf-8") as myfile:
        data = myfile.read()
        return data

def get_content():
    with open("content.txt", "r", encoding="utf-8") as myfile:
        data = myfile.read()
        return data