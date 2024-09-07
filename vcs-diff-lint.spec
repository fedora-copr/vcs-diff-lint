Name:    vcs-diff-lint
Version: 6.2
Release: 1%{?dist}
Summary: VCS Differential Code Analysis Tool
BuildArch: noarch

License: GPL-2.0-or-later
URL:     https://github.com/fedora-copr/vcs-diff-lint
# Source is created by:
# git clone %%url && cd vcs-diff-lint
# tito build --tgz --tag %%name-%%version-%%release
Source0: %name-%version.tar.gz

Requires: csdiff
Requires: git
Requires: pylint
Requires: python3-mypy
Requires: python3-types-requests
Requires: ruff

%description
Analyze code, and print only reports related to a particular change.

From within a VCS directory (only Git is supported for now) first analyze set of
changed files against given changeset (origin/main by default) so we know what
files need to be analyzed.  Then run code analyzers (e.g. PyLint) against the
old code (before changes), run analyzers against the actual code (not yet pushed
changes), perform a diff (using csdiff utility), and finally print a set of
added (or even fixed, as opt-in) analyzers' warnings.


%prep
%autosetup


%build
# Intentionally empty — nothing to build in this package.


%install
install -d %buildroot%_bindir
install -p vcs-diff-lint %buildroot%_bindir
install -p vcs-diff-lint-csdiff-pylint %buildroot%_bindir
install -p vcs-diff-lint-csdiff-mypy   %buildroot%_bindir
install -p vcs-diff-lint-csdiff-ruff   %buildroot%_bindir


%files
%license LICENSE
%doc README
%_bindir/vcs-diff-lint*


%changelog
* Sat Sep 07 2024 Pavel Raiskup <praiskup@redhat.com> 6.2-1
- drop unnecessary newline in the output
- ruff: don't prefix the error locations with absolute path
- ruff: don't optimize out the full Ruff run
- print the git sha1 being analyzed
- bugfix: correct matching filenames with endswith()

* Wed Aug 28 2024 Pavel Raiskup <praiskup@redhat.com> 6.1-1
- rpm: use SPDX License format

* Wed Aug 28 2024 Pavel Raiskup <praiskup@redhat.com> 6-1
- bugfix: correctly honor file renames
- bugfix: fix subproject detection for git worktree
- ruff: do full project scans (since Ruff is fast enough)
- check the new (changed) code in a side-directory

* Mon Aug 26 2024 Pavel Raiskup <praiskup@redhat.com> - 5-1
- support for fast "ruff" analyser
- --linter-tag option added
- subproject detection by .vcs-diff-lint.yml

* Fri Nov 18 2022 Pavel Raiskup <praiskup@redhat.com> 4-1
- don't print Mypy errors from files that are not explicitly analyzed

* Thu Nov 10 2022 Pavel Raiskup <praiskup@redhat.com> 3-1
- print the headers back to stdout again
- non-monorepo use-case fixed
- add support for Mypy

* Thu Oct 20 2022 Pavel Raiskup <praiskup@redhat.com> 2-1
- don't pollute stdout so csgrep can read it

* Thu Sep 29 2022 Pavel Raiskup <praiskup@redhat.com> 1-1
- new package built with tito
