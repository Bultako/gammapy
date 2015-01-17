# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import sys

__all__ = ['find_runs']


def main(args=None):
    from gammapy.utils.scripts import argparse, GammapyFormatter
    description = find_runs.__doc__.split('\n')[0]
    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=GammapyFormatter)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        help='Input run list file name')
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='Output run list file name (default: stdout)')
    parser.add_argument('x', type=float,
                        help='x coordinate (deg)')
    parser.add_argument('y', type=float,
                        help='y coordinate (deg)')
    parser.add_argument('--pix', action='store_true',
                        help='Input coordinates are pixels '
                        '(default is world coordinates)')
    parser.add_argument('--overwrite', action='store_true',
                        help='Overwrite existing output file?')
    args = parser.parse_args(args)
    find_runs(**vars(args))


def find_runs(infile,
              outfile,
              x,
              y,
              pix,
              overwrite):
    """Select a subset of runs from a given run list.

    TODO: explain.
    """
    import logging
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
    # from gammapy.obs import RunList

    # TODO: implement
    raise NotImplementedError