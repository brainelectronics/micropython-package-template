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
## [0.14.0] - 2026-04-14T18:22:20+02:00
<!-- meta = {'type': 'feature', 'scope': ['all'], 'affected': ['all']} -->

This change updates the manual package installation instructions to use `mpremote` over `rshell`.

In the PyPI section the usage of `twine check` before `twine upload` is recommended.

An example instruction on how to install a specific version with `upip` was added.

The package usage example and the corresponding `main.py` example files are extended to set the LED pin based on the board extracted from `os.uname()`.

This closes [#34](https://github.com/brainelectronics/micropython-package-template/issues/34)

[0.14.0]: https://github.com/brainelectronics/snippets2changelog/tree//0.14.0

## [0.13.1] - 2026-04-11T21:15:55+02:00
<!-- meta = {'type': 'bugfix', 'scope': ['all'], 'affected': ['all']} -->

This change creates the correct release candidate number based on the action run of a pull request workflow run `test-release` instead of the total number of this workflow run. By this fix, the `-rcX` metadata starts at `1` and is incremented with every push, no matter if the push is a force push or a classic new commit on top in a ongoing pull request.

This closes [#33](https://github.com/brainelectronics/micropython-package-template/issues/33)

[0.13.1]: https://github.com/brainelectronics/snippets2changelog/tree//0.13.1

## [0.13.0] - 2026-04-06T22:12:09+02:00
<!-- meta = {'type': 'feature', 'scope': ['all'], 'affected': ['all']} -->

This change creates a new release branch `release/<VERSION>` after a merge and adds the following files to it:
- `changelog.md`
- `package.json`
- `<PACKAGE>/version.py`

This closes [#28](https://github.com/brainelectronics/micropython-package-template/issues/28)

[0.13.0]: https://github.com/brainelectronics/snippets2changelog/tree//0.13.0

## [0.12.0] - 2026-04-06T19:55:15+02:00
<!-- meta = {'type': 'feature', 'scope': ['all'], 'affected': ['all']} -->

This change creates the latest changelog from all submitted snippets before building and deploying the [ReadTheDocs](https://micropython-package-template.readthedocs.io/en/latest/index.html) files

This closes [#26](https://github.com/brainelectronics/micropython-package-template/issues/26)

[0.12.0]: https://github.com/brainelectronics/snippets2changelog/tree//0.12.0

## [0.11.0] - 2026-04-06T19:49:35+02:00
<!-- meta = {'type': 'feature', 'scope': ['all'], 'affected': ['all']} -->

This change updates all tools, python packages and GitHub actions to their latest version.

The `sdist_upip.py` script does no longer remove the `PKG-INFO` and `LICENSE.txt` files from the root of the created `tar.gz` file to meet the [requirements of PyPI](https://packaging.python.org/en/latest/discussions/package-formats/)

This closes [#24](https://github.com/brainelectronics/micropython-package-template/issues/24)

[0.11.0]: https://github.com/brainelectronics/snippets2changelog/tree//0.11.0

## [0.10.0] - 2024-10-01T00:37:03+02:00
<!-- meta = {'type': 'feature', 'scope': ['all'], 'affected': ['all']} -->

This change replaces the modifications and extensions of a changelog by
generating the changelog with all its entries and versions based on changelog
snippets like this one.

This closes [#22](https://github.com/brainelectronics/micropython-package-template/issues/22)

[0.10.0]: https://github.com/brainelectronics/snippets2changelog/tree//0.10.0

## [0.9.0] - 2023-07-11
### Added
- Precommit hooks for `package.json` and package version file validation, yaml style, flake8 and trailing whitespace checks
- Contribution guideline
- Package version file validation step in test workflow

### Fixed
- Added missing empty line in several files

## [0.8.1] - 2023-06-12
### Fixed
- Usage documentation with more comments and WiFi instructions in root README
- Installation of latest available package version with `upip` mentioned in root README
- Available package validation options added as comment to test workflow

## [0.8.0] - 2023-03-29
### Added
- Add `MicoPython` as `Implementation` in setup `classifiers`, see [#16](https://github.com/brainelectronics/micropython-package-template/issues/16)
- Verify `package.json` against latest changelog and setup in test workflow, see [#17](https://github.com/brainelectronics/micropython-package-template/issues/17)

## [0.7.0] - 2023-03-17
### Added
- Set settings for JSON files to use an indentation of 4 in `.editorconfig`
- `package.json` for `mip` installation with MicroPython v1.19.1 or newer
- Instructions for installation with `mip` on  MicroPython v1.19.1 or newer in `README`
- Instructions to be performed after using this template package in `README`
- Example files for `boot` and `main`

### Changed
- Omit package version file from coverage calculation in `.coveragerc`
- Run test workflow also on pull requests
- Update date of license to 2023

### Removed
- No longer used `update_version.py` file removed from flake8 exclude list

### Fixed
- Path to documentation build output folder is only highlighted to avoid broken links errors
- Mock commonly used MicroPython specific modules in docs config file

## [0.6.0] - 2023-02-22
### Added
- `.editorconfig` for common editor settings, see #12
- `.yamllint` to lint all used YAML files, see #12
- `codecov.yaml` to specify further settings and limits for the coverage
- `yamllint` package to the `requirements-test.txt` file
- Run YAML linter on test workflow

### Changed
- Fixed uncovered YAML syntax issues in all workflow files
- Removed unused files from `.gitignore` file

## [0.5.0] - 2023-02-20
### Added
- `.readthedocs.yaml` definition file for ReadTheDocs, see #10
- `docs` folder containing example files and configurations, see #10

## [0.4.0] - 2023-02-20
### Added
- `test-release` and `release` workflows create changelog based (pre-)releases, see #2
- Documentation for manually creating a package and uploading it to PyPi in root README

### Fixed
- All workflows use checkout v3 instead of v2

## [0.3.0] - 2022-11-03
### Added
- Lint package with `flake8` with [test workflow](.github/workflows/test.yaml)
- CI upload status badge added to [`README`](README.md)

### Fixed
- Remove not required packages `setuptools`, `wheel` and `build` from release
  and test-release workflow files
- Show download of this package on badge instead of `be-modbus-wrapper`
- Show `MicroPython Ok` badge instead of `Python3 Ok` in [`README`](README.md)

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
[Unreleased]: https://github.com/brainelectronics/micropython-package-template/compare/0.9.0...main

[0.9.0]: https://github.com/brainelectronics/micropython-package-template/tree/0.9.0
[0.8.1]: https://github.com/brainelectronics/micropython-package-template/tree/0.8.1
[0.8.0]: https://github.com/brainelectronics/micropython-package-template/tree/0.8.0
[0.7.0]: https://github.com/brainelectronics/micropython-package-template/tree/0.7.0
[0.6.0]: https://github.com/brainelectronics/micropython-package-template/tree/0.6.0
[0.5.0]: https://github.com/brainelectronics/micropython-package-template/tree/0.5.0
[0.4.0]: https://github.com/brainelectronics/micropython-package-template/tree/0.4.0
[0.3.0]: https://github.com/brainelectronics/micropython-package-template/tree/0.3.0
[0.2.0]: https://github.com/brainelectronics/micropython-package-template/tree/0.2.0
[0.1.1]: https://github.com/brainelectronics/micropython-package-template/tree/0.1.1
[0.1.0]: https://github.com/brainelectronics/micropython-package-template/tree/0.1.0

[ref-issue-5]: https://github.com/brainelectronics/micropython-package-template/issues/5
[ref-issue-3]: https://github.com/brainelectronics/micropython-package-template/issues/3

[ref-pep440]: https://peps.python.org/pep-0440/
[ref-python-gitignore-template]: https://github.com/github/gitignore/blob/e5323759e387ba347a9d50f8b0ddd16502eb71d4/Python.gitignore
