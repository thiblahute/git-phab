import os

from setuptools import setup

setup(
    name="git-phab",
    version="1.9.0",
    author="Xavier Claessens",
    author_email="xavier.claessens@collabora.com",
    description=("Git subcommand to integrate with phabricator"),
    license="GPL",
    keywords="phabricator tool git",
    url="http://packages.python.org/git-phab",
    long_description_markdown_filename='README.md',
    setup_requires=['setuptools-markdown'],
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License (GPL)"
    ],
    install_requires=['GitPython', 'appdirs', 'argcomplete', 'phabricator',
                      'pre-commit'],
    scripts=['git-phab'],
)

os.system("pre-commit install")
