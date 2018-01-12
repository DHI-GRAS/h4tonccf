import os
import sys

import subprocess


here = os.path.abspath(os.path.dirname(__file__))

BINARY_DIR = os.path.join(here, 'bin')

BINARIES = {
    'win32': os.path.join(BINARY_DIR, 'h4tonccf_nc4.exe')}


def run(infile, outfile=None, platform=sys.platform):
    """Run h4tonccf binary

    Parameters
    ----------
    infile : str
        path to input file
    outfile : str, optional
        path to output file
        default: infile with .nc extension
    platform : str
        platform name

    Returns
    -------
    str
        outfile
    """
    if outfile is None:
        outfile = os.path.splitext(infile)[0] + '.nc'

    cmd = [BINARIES[platform]]
    cmd += [infile, outfile]

    subprocess.run(cmd, check=True)

    if not os.path.isfile(outfile):
        raise RuntimeError('Output file was not generated: {}'.format(outfile))

    return outfile
