from setuptools import setup, find_packages
import os
import io

with open("README.md", "r") as fh:
    long_description = fh.read()

here = os.path.abspath(os.path.dirname(__file__))

version_contents = {}
with io.open(os.path.join(here, "gameball", "version.py"), encoding="utf-8") as f:
    exec(f.read(), version_contents)

setup(name= 'gb-alpha',
    version = "3.0.0",
    packages = find_packages(),
    author = "Gameball",
    author_email = "support@gameball.co",
    description = "Gameball Python SDK provides convinient access to the Gameball API frpm applications written in the Python langauage",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/gameballers/gameball-python",
    python_requires = '>=3.4',)
    