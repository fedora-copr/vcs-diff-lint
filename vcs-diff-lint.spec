Name:    vcs-diff-lint
Version: 1
Release: 1%{?dist}
Summary: VCS Differential Code Analysis Tool
BuildArch: noarch

License: GPLv2+
URL:     https://pagure.io/copr/copr
# Source is created by:
# git clone %%url && cd copr
# tito build --tgz --tag %%name-%%version-%%release
Source0: %name-%version.tar.gz

Requires: csdiff

%description
From within a VCS directory (only Git is supported for now), first run code
analyzers (e.g. PyLint) against the old code (before changes), then run
analyzers against the actual code (not yet pushed changes), perform a diff and
finally print a set of added (or even fixed, as opt-in) analyzers' warnings.


%prep
%autosetup


%install
install -d %buildroot%_bindir
install -p vcs-diff-lint %buildroot%_bindir
install -p vcs-diff-lint-csdiff-pylint %buildroot%_bindir


%files
%license LICENSE
%_bindir/vcs-diff-lint*


%changelog
* Thu Sep 29 2022 Pavel Raiskup <praiskup@redhat.com> 1-1
- new package built with tito
