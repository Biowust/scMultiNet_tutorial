project = "scMultiNet Tutorial"
author = "Cheng Guo"
copyright = "Cheng Guo"
extensions = [
    "myst_nb",
    "sphinx_copybutton",
    "sphinx_design",
]

# 不在 RTD 上执行 notebook，只展示已有输出
nb_execution_mode = "off"

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_theme_options = {
    "navigation_depth": 3,
}
