Differential code linting for VCS repositories
==============================================

Automatic code analysis has become a natural maintainer's need to improve
the software quality.  We need to run the analysis as soon as possible,
ideally before a new code change is integrated.

Modern analysers are very powerful, increasingly more powerful.  As they
evolve, the same analysers over time raise new warnings.  Powerful
analyzers also need a reasonable context — it is not just enough to take a
look at the patch file (changed code lines) itself to perform the complex
analysis.  A whole changed file needs to be analyzed, or even files that
are used as dependencies (imports, includes, ...).

So before the change is done (change request) we want to run a set of
powerful code analysers, but we aren't typically interested to see all the
warnings (related even to the old code).  We typically want to concentrate
on the changed stuff, new code — to **avoid creating new bugs**.

So there's often a dilemma maintainers have:  What analyser to enable, and
in what verbosity level, to not have unnecessary clutter in the CI workflow
output (so the CI is actually useful)?  Without fixing all the code problems
that cause reports first?

This project aims to help here.  With vcs-diff-lint, you can trivially
enable even very complex and verbose code analysers in even old projects.
And still, thanks to the [csdiff tool](https://github.com/csutils/csdiff)
you'll be informed only about the **new errors** that are related to the
change.

How it works
------------

From within a VCS directory (only Git is supported for now) we first
- analyze set of changed files against given changeset (the `origin/main`
  branch by default), so we know what files need to be analyzed
- run code analyzers against the old file variants (before the change is
  done), then
- run analyzers against the proposed file versions (not yet pushed
  changes),
- perform a diff on the error sets (using csdiff), and finally
- report the set of added (or optionally even fixed) analyzers' warnings.


Features
--------

- PyLint and Mypy is supported
- monorepo support (multiple sub-projects in repo sub-directories)
- file renames supported (if a file was just renamed, the old errors are
  not reported as new)

Usage
-----

Use the https://github.com/marketplace/actions/vcs-diff-lint GitHub Action.

Alternatively, in a local git clone directory, run:

    $ cd my_project && vcs-diff-lint --print-fixed-errors
    # ================
    #  Added warnings
    # ================

    Error: PYLINT_WARNING:
    coprs_frontend/manage.py:105:4: C0104[disallowed-name]: Disallowed name "foo"

    # ================
    #  Fixed warnings
    # ================

    Error: PYLINT_WARNING:
    coprs_frontend/manage.py:9: W0611[unused-import]: Unused import importlib
