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
## [0.3.0] - 2022-11-03
### Added
- Lint package with `flake8` with [test workflow](.github/workflows/test.yaml)

### Fixed
- Remove not required packages `setuptools`, `wheel` and `build` from release
  and test-release workflow files

## [0.2.0] - 2022-10-22
### Added
- Deploy to [Test Python Package Index](https://test.pypi.org/) on every PR
  build with a [PEP440][ref-pep440] compliant `-rc<BUILDNUMBER>.dev<PR_NUMBER>`
  meta data extension, see [#5][ref-issue-5]
- [Test release workflow](.github/workflows/test-release.yaml) running only on
  PRs is archiving and uploading built artifacts to
  [Test Python Package Index](https://test.pypi.org/)

### Changed
- Built artifacts are no longer archived by the always running
  [test workflow](.github/workflows/test.yaml)

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
[Unreleased]: https://github.com/brainelectronics/micropython-package-template/compare/0.3.0...main

[0.3.0]: https://github.com/brainelectronics/micropython-package-template/tree/0.3.0
[0.2.0]: https://github.com/brainelectronics/micropython-package-template/tree/0.2.0
[0.1.1]: https://github.com/brainelectronics/micropython-package-template/tree/0.1.1
[0.1.0]: https://github.com/brainelectronics/micropython-package-template/tree/0.1.0

[ref-issue-5]: https://github.com/brainelectronics/micropython-package-template/issues/5
[ref-issue-3]: https://github.com/brainelectronics/micropython-package-template/issues/3

[ref-pep440]: https://peps.python.org/pep-0440/
[ref-python-gitignore-template]: https://github.com/github/gitignore/blob/e5323759e387ba347a9d50f8b0ddd16502eb71d4/Python.gitignore
