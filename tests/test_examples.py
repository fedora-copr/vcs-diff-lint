"""
Run vcs-diff-lint tests against the bundled git repo.
"""

import subprocess
from tests import GITROOTDIR


def run_vcs_diff_lint(old, new, expected_output):
    """ Run vcs-diff-lint in the datadir """
    subprocess.check_call(["git", "checkout", new], cwd=GITROOTDIR)
    out = subprocess.run(["vcs-diff-lint", "--compare-against",
                          old], cwd=GITROOTDIR, stdout=subprocess.PIPE,
                         check=False, encoding="utf-8")
    assert out.stdout == expected_output


def test_basic():
    """
    Test added issues.
    """
    old = '1059de39'
    new = '51806b39'
    data="""\
Error: PYLINT_WARNING:
python/hello-world-python:1: C0114[missing-module-docstring]: Missing module docstring

Error: PYLINT_WARNING:
python/hello-world-python:4: C0116[missing-function-docstring]: api_method: Missing function or method docstring
"""
    run_vcs_diff_lint(old, new, data)
