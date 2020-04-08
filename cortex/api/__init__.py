"""
cortex.api is a submodule that is responsible for serving a REST API, which is consumed by cortex.cli and cortex.gui
By default, it connects to a running MongoDB server, but can be easily extended to different databases
"""


from .api_server import run_api_server
