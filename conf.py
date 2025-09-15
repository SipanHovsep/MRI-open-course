# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MR Atlas'
copyright = '2025, Sipan Hovsepian'
author = 'Sipan Hovsepian'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ['_static']
html_css_files = ['nobel.css']

html_theme_options = {
    "repository_url": "https://github.com/SipanHovsep/MRI-open-course",
    "use_repository_button": True,   # shows the GitHub icon button
}


extensions = [
    "sphinx.ext.mathjax",
    # other extensions...
]


extensions = [
    "myst_parser",
    # ...your other extensions
]

# (optional) nicer Markdown behavior
myst_enable_extensions = [
    "linkify",
    "deflist",
    "colon_fence",
]



# --- BEGIN: fetch README from GitHub at build time ---
import os, pathlib, urllib.request

GENERATED_DIR = pathlib.Path(__file__).parent / "_generated"
README_URL = "https://raw.githubusercontent.com/SipanHovsep/Field_mapper_robot/main/README.md"
README_LOCAL = GENERATED_DIR / "field_mapper_readme.md"

def _ensure_readme_downloaded(_app):
    GENERATED_DIR.mkdir(exist_ok=True)
    try:
        with urllib.request.urlopen(README_URL) as r:
            text = r.read().decode("utf-8")
        # Ensure there’s a top-level title so it renders nicely as a full page
        if not text.lstrip().startswith("# "):
            text = "# Field Mapper Robot – README\n\n" + text
        README_LOCAL.write_text(text, encoding="utf-8")
    except Exception as e:
        # Fallback: keep previous file if exists, else create a stub
        if not README_LOCAL.exists():
            README_LOCAL.write_text(
                "# Field Mapper Robot – README\n\n"
                "_Could not fetch README during build._",
                encoding="utf-8"
            )

def setup(app):
    app.connect("builder-inited", _ensure_readme_downloaded)
# --- END: fetch README ---



