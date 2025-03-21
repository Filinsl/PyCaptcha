# PyCaptcha

`PyCaptcha` is a Python utility for generating CAPTCHA images with random alphanumeric text and adding visual noise (lines, dots, symbols) to make it more difficult for bots to recognize. The utility uses the `PIL` (Pillow) library for image creation and processing.

## Features
- Generates CAPTCHA images with random text consisting of letters and digits.
- Adds visual noise:
  - Random symbols in the background.
  - Random colored lines.
  - Noise in the form of random dots.
- Supports tilted text and small vertical shifts to make recognition harder.
- Automatically saves images with sequential filenames (`captcha1.png`, `captcha2.png`, and so on).

## Requirements
- Python 3.x
- The `Pillow` library for image processing.

To install dependencies, run the following command:

```bash
pip install pillow
