from setuptools import setup, find_packages
import io
import os


install_requires = [
    "mailchimp3~=3.0.2",
    "oauth2client~=4.1.2",
    "gspread~=3.0.0",
    "beautifulsoup4~=4.6.3",
    "requests~=2.24.0",
    "geopy~=1.18.1",
    "pandas>=0.25.0",
    "algoliasearch>=2.0,<3.0",
    "spacy~=2.2.4",
]

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="rasa-demo",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        # supported python versions
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(where="demo"),
    version="2.0",
    install_requires=install_requires,
    description="Rasa Demo Bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Rasa Technologies GmbH",
    author_email="hi@rasa.com",
    maintainer="Akela Drissner-Schmid",
    maintainer_email="akela@rasa.com",
    license="GNU General Public License v3.0",
    url="https://github.com/rasahq/rasa-demo",
    download_url="https://github.com/RasaHQ/rasa-demo/archive/main.zip",
    project_urls={
        "Bug Reports": "https://github.com/rasahq/rasa-demo/issues",
        "Source": "https://github.com/rasahq/rasa-demo",
    },
)
