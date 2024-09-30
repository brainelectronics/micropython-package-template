# Contributing

Guideline to contribute to this package

---------------

## General

You're welcome to contribute to this package with or without raising an issue
before creating a PR.

Please follow the following guideline covering all necessary steps and hints
for a smooth review and contribution process.

## Code

To test and verify your changes it is recommended to run all checks locally in
a virtual environment. Use the following command to setup and install all
tools.

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements-test.txt
```

For very old systems it might be necessary to use an older version of
`pre-commit`, an "always" working version is `1.18.3` with the drawback of not
having `flake8` and maybe other checks in place.

### Format

The Python code format is checked by `flake8` with the default line length
limit of 79. Further configuration can be found in the `.flake8` file in the
repo root.

The YAML code format is checked by `yamllint` with some small adjustments as
defined in the `.yamllint` file in the repo root.

Use the following commands (inside the virtual environment) to run the Python
and YAML checks

```bash
# check Python
flake8 .

# check YAML
yamllint .
```

### Tests

Every code should be covered by a unittest. This can be achieved for
MicroPython up to some degree, as hardware specific stuff can't be always
tested by a unittest.

For now `nose2` is used as tool of choice. The configuration is defined in the
`tests/unittest.cfg` file.

All reports are placed inside the `reports` folder or a subfolder of it. It
can be created with

```bash
python create_report_dirs.py
```

After this either all or a specific unittest can be executed, see the following
commands as an example

```bash
# run all tests
nose2 --config tests/unittest.cfg

# run only one specific tests
nose2 tests.test_blink.TestBlink.test_flash_led
```

As last step the coverage report can be generated. There might be a minimum
coverage limit set up for the project. Check the value of `target` in the
`codecov.yaml` file, located in the repo root.

```bash
coverage html
```

The coverage report is placed at `reports/coverage/html/index.html`

### Precommit hooks

This repo is equipped with a `.pre-commit-config.yaml` file to combine most of
the previously mentioned checks plus the changelog validation, see next
section, into one handy command. It additionally allows to automatically run
the checks on every commit.

In order to run this repo's pre commit hooks, perform the following steps

```bash
# install pre-commit to run before each commit, optionally
pre-commit install

pre-commit run --all-files
```

## Changelog

The changelog format is based on [Keep a Changelog][ref-keep-a-changelog], and
this project adheres to [Semantic Versioning][ref-semantic-versioning].

### General

Please add a changelog snippet for every PR you contribute. The changes are
categorised into:

- `bugfixes` fix an issue which can be used out of the box without any further
changes required by the user. Be aware that in some cases bugfixes can be
breaking changes.
- `features` is used to indicate a backwards compatible change providing
improved or extended functionalitiy. This does, as `bugfixes`, in any case
not require any changes by the user to keep the system running after upgrading.
- `breaking` creates a breaking, non backwards compatible change which
requires the user to perform additional tasks, adopt his currently running
code or in general can't be used as is anymore.

The changelog entry shall be short but meaningful and can of course contain
links and references to other issues or PRs. New lines are only allowed for a
new bulletpoint entry. Usage examples or other code snippets should be placed
in the code documentation, README or the docs folder.

### Creation

To create a new changelog snippet use the CLI tool with its simple interface.
Use the issue number, in this example `22.md`, as the snippet name. The
extension shall always be `.md`.

```bash
changelog-generator create .snippets/22.md
```

The tool will create a basic snippet which can and should be extended with a
detailed description of the change after the file creation.

### Generation

Commit the changes and the snippet file and run the following command to create
a changelog with the latest snippet included

```bash
changelog-generator changelog changelog.md --snippets=.snippets --in-place
```

*Be aware to restore the changelog before another run as it might generate
version entries and version bumps multiple times otherwise.*

### Version file

The package version file, located at `<PACKAGE_NAME>/version.py` contains the
latest changelog version.

To avoid a manual sync of the changelog version and the package version file
content, the `changelog2version` package is used. It parses the changelog,
extracts the latest version and updates the version file.

The package version file can be generated with the following command consuming
the latest changelog entry

```bash
changelog2version \
	--changelog_file changelog.md \
	--version_file <PACKAGE_NAME>/version.py \
	--version_file_type py \
	--debug
```

To validate the existing package version file against the latest changelog
entry use this command

```bash
changelog2version \
	--changelog_file=changelog.md \
	--version_file=<PACKAGE_NAME>/version.py \
	--validate
```

### MicroPython

On MicroPython the `mip` package is used to install packages instead of `pip`
at MicroPython version 1.20.0 and newer. This utilizes a `package.json` file
in the repo root to define all files and dependencies of a package to be
downloaded by [`mip`][ref-mip-docs].

To avoid a manual sync of the changelog version and the MicroPython package
file content, the `setup2upypackage` package is used. It parses the changelog,
extracts the latest version and updates the package file version entry. It
additionally parses the `setup.py` file and adds entries for all files
contained in the package to the `urls` section and all other external
dependencies to the `deps` section.

The MicroPython package file can be generated with the following command based
on the latest changelog entry and `setup` file.

```bash
upy-package \
	--setup_file setup.py \
	--package_changelog_file changelog.md \
	--package_file package.json
```

To validate the existing package file against the latest changelog entry and
setup file content use this command

```bash
upy-package \
	--setup_file setup.py \
	--package_changelog_file changelog.md \
	--package_file package.json \
	--validate
```

## Documentation

Please check the `docs/DOCUMENTATION.md` file for further details.

<!-- Links -->
[ref-keep-a-changelog]: https://keepachangelog.com/en/1.0.0/
[ref-semantic-versioning]: https://semver.org/spec/v2.0.0.html
[ref-mip-docs]: https://docs.micropython.org/en/v1.20.0/reference/packages.html
