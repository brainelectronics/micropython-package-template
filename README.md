# MicroPython package template

[![Downloads](https://pepy.tech/badge/be-modbus-wrapper)](https://pepy.tech/project/micropython-package-template)
![Release](https://img.shields.io/github/v/release/brainelectronics/micropython-package-template?include_prereleases&color=success)
![Python](https://img.shields.io/badge/python3-Ok-green.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/github/brainelectronics/micropython-package-template/branch/main/graph/badge.svg)](https://app.codecov.io/github/brainelectronics/micropython-package-template)

MicroPython PyPi package template project with auto deploy

---------------

## General

MicroPython PyPi package template with GitHub Action based testing and deploy

<!-- MarkdownTOC -->

- [Installation](#installation)
	- [Install required tools](#install-required-tools)
- [Setup](#setup)
	- [Install package with upip](#install-package-with-upip)
	- [Manually](#manually)
		- [Upload files to board](#upload-files-to-board)
- [Usage](#usage)
- [Contributing](#contributing)
	- [Unittests](#unittests)
- [Credits](#credits)

<!-- /MarkdownTOC -->

## Installation

### Install required tools

Python3 must be installed on your system. Check the current Python version
with the following command

```bash
python --version
python3 --version
```

Depending on which command `Python 3.x.y` (with x.y as some numbers) is
returned, use that command to proceed.

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Setup

### Install package with upip

Connect the MicroPython device to a network (if possible)

```python
import network
station = network.WLAN(network.STA_IF)
station.connect('SSID', 'PASSWORD')
station.isconnected()
```

and install this lib on the MicroPython device like this

```python
import upip
upip.install('micropython-package-template')
```

### Manually

#### Upload files to board

Copy the module to the MicroPython board and import them as shown below
using [Remote MicroPython shell][ref-remote-upy-shell]

Open the remote shell with the following command. Additionally use `-b 115200`
in case no CP210x is used but a CH34x.

```bash
rshell --port /dev/tty.SLAB_USBtoUART --editor nano
```

Perform the following command inside the `rshell` to copy all files and
folders to the device

```bash
mkdir /pyboard/lib
mkdir /pyboard/lib/be_upy_blink

cp be_upy_blink/* /pyboard/lib/be_upy_blink

cp examples/main.py /pyboard
cp examples/boot.py /pyboard
```

## Usage

```python
from be_upy_blink import flash_led
from machine import Pin

led_pin = Pin(4, Pin.OUT)

flash_led(pin=led_pin, amount=3)
# flash_led(pin=led_pin, amount=3, on_time=1, off_time=3)
```

## Contributing

### Unittests

Run the unittests locally with the following command after installing this
package in a virtual environment

```bash
# run all tests
nose2 --config tests/unittest.cfg

# run only one specific tests
nose2 tests.test_blink.TestBlink.test_flash_led
```

Generate the coverage files with

```bash
python create_report_dirs.py
coverage html
```

The coverage report is placed at `reports/coverage/html/index.html`

## Credits

Based on the [PyPa sample project][ref-pypa-sample].

<!-- Links -->
[ref-remote-upy-shell]: https://github.com/dhylands/rshell
[ref-pypa-sample]: https://github.com/pypa/sampleproject
