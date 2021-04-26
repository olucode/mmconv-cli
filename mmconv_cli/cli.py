#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the entry point for the command-line interface (CLI) application.

It can be used as a handy facility for running the task from a command line.

.. note::

    To learn more about Click visit the
    `project website <http://click.pocoo.org/5/>`_.  There is also a very
    helpful `tutorial video <https://www.youtube.com/watch?v=kNke39OZ2k0>`_.

    To learn more about running Luigi, visit the Luigi project's
    `Read-The-Docs <http://luigi.readthedocs.io/en/stable/>`_ page.

.. currentmodule:: mmconv_cli.cli
.. moduleauthor:: olucode <olucode6379@gmail.com>
"""
import logging
from mmconv_cli.convert import ConvertOpts, convert
import click
from .__init__ import __version__

LOGGING_LEVELS = {
    0: logging.NOTSET,
    1: logging.ERROR,
    2: logging.WARN,
    3: logging.INFO,
    4: logging.DEBUG,
}  #: a mapping of `verbose` option counts to logging levels


class Info(object):
    """An information object to pass data between CLI functions."""

    def __init__(self):  # Note: This object must have an empty constructor.
        """Create a new instance."""
        self.verbose: int = 0


# pass_info is a decorator for functions that pass 'Info' objects.
#: pylint: disable=invalid-name
pass_info = click.make_pass_decorator(Info, ensure=True)


# @click.group(invoke_without_command=True)
@click.command()
@click.argument('input', type=click.Path(
    exists=True, resolve_path=True))
@click.argument('out',  type=click.Path(
    exists=False, resolve_path=True))
@click.option("--bank", "-b", help="Bank Statement")
@click.option("--encoding", "-e", default='xlsx', help="Input file type")
@click.option("--output", "-o", default='unicode', help="Output file type")
@click.option("--verbose", "-vv", count=True, help="Enable verbose output.")
# @click.option("--version", "-v", count=True, help="Get library version")
@pass_info
def cli(info: Info, verbose: int, input: str, out: str, output: str, bank: str, encoding: str):
    """Run mmconv-cli."""
    # Use the verbosity count to determine the logging level...
    if verbose > 0:
        logging.basicConfig(
            level=LOGGING_LEVELS[verbose]
            if verbose in LOGGING_LEVELS
            else logging.DEBUG
        )
        click.echo(
            click.style(
                f"Verbose logging is enabled. "
                f"(LEVEL={logging.getLogger().getEffectiveLevel()})",
                fg="yellow",
            )
        )
    info.verbose = verbose

    # TODO: Validate args

    # Perform Conversion
    opts = ConvertOpts(
        file_path=input,
        output_path=out,
        bank=bank,
        file_type=encoding,
        output_type=output
    )
    result = convert(opts)

    click.echo(result)
