"""
vcs-diff-lint tests
"""

import os
import shutil
from subprocess import Popen, PIPE, check_call

SRCDIR = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
GITROOTDIR = os.path.join(SRCDIR, 'test-repo')

bundle = None
with Popen(['spectool', '-S', 'vcs-diff-lint.spec'],
           stdout=PIPE, cwd=SRCDIR) as spectool:
    with Popen(['sed', '-n', 's/^Source1: \\(.*\\)/\\1/p'],
               stdin=spectool.stdout, stdout=PIPE,
               encoding="utf-8") as sed:
        bundle, _ = sed.communicate()
        bundle = os.path.basename(bundle.strip())

try:
    shutil.rmtree(GITROOTDIR)
except FileNotFoundError:
    pass
check_call(['git', 'clone', bundle, GITROOTDIR], cwd=SRCDIR)

os.environ["PATH"] = SRCDIR+":"+os.environ["PATH"]
check_call(["bash", "-c", "env"])
