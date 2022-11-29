# ChangeLog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- New option `--linter-tag` was added.  By default, `vcs-diff-lint` still runs
  all the preconfigured linters.  But this option allows users to select.
  For example, when just `pylint` run is desirable, use `--linter-tag pylint`.
  This option can be specified multiple times.

- Sub-projects (sub-directories) are detected even by existence of
  `.vcs-diff-lint.yml` file, not just `*.spec` file.
