# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
## [x.y.z] - yyyy-mm-dd
### Added
### Changed
### Removed
### Fixed
-->
<!--
RegEx for release version from file
r"^\#\# \[\d{1,}[.]\d{1,}[.]\d{1,}\] \- \d{4}\-\d{2}-\d{2}$"
-->

## Released
## [0.1.1] - 2022-10-16
### Fixed
- Move `src/be_upy_blink` to `be_upy_blink` to avoid installations into `/lib/src/be_upy_blink` on a uPy board via `upip`, see [#3][ref-issue-3]
- Adjust all paths to `be_upy_blink` folder and contained files

## [0.1.0] - 2022-10-16
### Added
- This changelog file
- [`.coveragerc`](.coveragerc) file
- [`.flake8`](.flake8) file
- [`.gitignore`](.gitignore) file bases on latest
  [Python gitignore template][ref-python-gitignore-template]
- Default [workflows](.github/workflows)
- Script to [create report directories](create_report_dirs.py)
- [`unittest.cfg`](tests/unittest.cfg) file
- [`requirements.txt`](requirements.txt) file to interact with the uPy board
- [`requirements-test.txt`](requirements-test.txt) file to install packages for unittests
- [`requirements-deploy.txt`](requirements-deploy.txt) file to install packages to deploy
- Initial [`be_upy_blink`](src/be_upy_blink) package
- Basic [`unittests`](tests) for package source code
- Initial root [`README`](README.md)
- [`setup.py`](setup.py) and [`sdist_upip.py`](sdist_upip.py) file

<!-- Links -->
[Unreleased]: https://github.com/brainelectronics/micropython-package-template/compare/0.1.1...develop

[0.1.1]: https://github.com/brainelectronics/micropython-package-template/tree/0.1.1
[0.1.0]: https://github.com/brainelectronics/micropython-package-template/tree/0.1.0

[ref-issue-3]: https://github.com/brainelectronics/micropython-package-template/issues/3

[ref-python-gitignore-template]: https://github.com/github/gitignore/blob/e5323759e387ba347a9d50f8b0ddd16502eb71d4/Python.gitignore
