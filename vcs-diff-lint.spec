Name:    vcs-diff-lint
Version: 1
Release: 1%{?dist}
Summary: VCS Differential Code Analysis Tool
BuildArch: noarch

License: GPLv2+
URL:     https://github.com/fedora-copr/vcs-diff-lint
# Source is created by:
# git clone %%url && cd vcs-diff-lint
# tito build --tgz --tag %%name-%%version-%%release
Source0: %name-%version.tar.gz

Requires: csdiff
Requires: git
Requires: pylint

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


%files
%license LICENSE
%doc README
%_bindir/vcs-diff-lint*


%changelog
* Thu Sep 29 2022 Pavel Raiskup <praiskup@redhat.com> 1-1
- new package built with tito
