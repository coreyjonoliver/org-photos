org-photos
================================================================
Corey Oliver, 2010-2011

This tool allows for the organization of a directory of images into a
year-month-day directory hierarchy based on the meta-data of each
photo. Non-image files or images files containing no DateTime
attribute are ignored.

Requirements
------------
  * Python
  * argparse
  
  argparse is included in the 2.7 and 3.2 distributions of Python. If
  you do not have either of these versions the recommended way to
  obtain argparse is with the tool [pip][1]: `pip install argparse`.
  
  * [pyexiv2][2]

Usage
-----

`org-photos [-h] [-w] directory`

`directory` type directory to organize

`-w` request warnings

Example:

If the meta-data for a photo in the directory `foo` contains a
DateTime attribute of "1-30-2010". Upon running `org-photos foo` the
following directory structure is created in the `foo` directory (if it
does not already exist): `2010/1/30`. The photo is then copied into
the directory `2010/1/30`.

License
-------

Copyright (c) 2011, Corey Oliver, corey.jon.oliver@gmail.com

Permission to use, copy, modify, and/or distribute this software for
any purpose with or without fee is hereby granted, provided that the
above copyright notice and this permission notice appear in all
copies.

THE SOFTWARE IS PROVIDED “AS IS” AND THE AUTHOR DISCLAIMS ALL
WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR
PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.

[1]: http://pypi.python.org/pypi/pip
[2]: http://tilloy.net/dev/pyexiv2/