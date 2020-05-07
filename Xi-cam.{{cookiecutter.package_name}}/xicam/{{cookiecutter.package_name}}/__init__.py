# Notes for development:
#
# Xi-CAM documentation: https://xi-cam2.readthedocs.io/
# Documentation for python Qt: https://doc.qt.io/qtforpython/api.html
from qtpy.QtWidgets import QLabel

from xicam.plugins import GUIPlugin, GUILayout


class {{cookiecutter.plugin_name}}(GUIPlugin):
    # Defines the name of the plugin (how it is displayed in Xi-CAM)
    name = "{{cookiecutter.display_name}}"

    def __init__(self, *args, **kwargs):
        # Insert code here

        # Modify stages here
        self.stages = {'Stage 1': GUILayout(QLabel("Stage 1...")),
                       "Stage 2": GUILayout(QLabel("Stage 2..."))}

        # Initialize the parent class, GUIPlugin
        super({{cookiecutter.plugin_name}}, self).__init__(*args, **kwargs)



