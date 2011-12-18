#!/usr/bin/python
# org-photos.py

import argparse
import datetime
import glob
import pyexiv2
import os
import shutil
import sys

__author__ = "Corey Oliver"
__email__ = "corey.jon.oliver@gmail.com"

def main():
    parser = argparse.ArgumentParser(description=
                                     'This tool allows for the organization ' +
                                     'of a directory of images into a ' +
                                     'year-month-day directory hierarchy ' +
                                     'based on the meta-data of each photo. ' +
                                     'Non-image files or images files ' +
                                     'containing no DateTime attribute are ' +
                                     'ignored.')
    parser.add_argument('directory',
                        help='the directory to organize')
    parser.add_argument('-w', action='store_true',
                        help='request warnings')
    args = parser.parse_args()

    dir = args.directory

    img_fns = glob.glob(os.path.join(dir, '*'))
    img_cnt = 0

    for fn in img_fns:
        try:
            image = pyexiv2.Image(fn)
            image.readMetadata()
        except IOError:
            if args.w:
                print >> sys.stderr, '%s: The file contains data of an unknown image type' % fn
            continue

        if 'Exif.Image.DateTime' in image.exifKeys():
            day, month, year = image['Exif.Image.DateTime'].strftime('%d:%m:%Y').split(':')
            img_dir = os.path.join(dir, year, month, day)
            if not os.path.exists(img_dir):
                os.makedirs(img_dir)

            shutil.copy2(fn, img_dir)
            img_cnt += 1
        else:
            if args.w:
                print >> sys.stderr, '%s: The file contains no DateTime attribute' % fn
            continue


    print '\n%d images processed and organized.\n' % img_cnt

if __name__ == '__main__':
    main()
