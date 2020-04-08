"""
cortex.parsers is a submodule responsible for handling all the parsing of snapshots,
storing parser classes and functions and running them as services
"""


from .run_parsers import run_parser, run_parser_service
