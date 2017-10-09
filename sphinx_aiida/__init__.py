"""
Defines reStructuredText directives to simplify documenting AiiDA and its plugins.
"""

from . import workchain


def setup(app):
    """
    Setup function to add the extension classes / nodes to Sphinx.
    """
    workchain.setup_aiida_workchain(app)

    return {'parallel_read_safe': True}
