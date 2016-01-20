#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

import yaml

print(yaml.__version__)

root = os.path.abspath(os.path.dirname(__file__))
conf_path = os.path.join(root, 'etc/test.yaml')


def read_conf():
    return yaml.load(open(conf_path))


def main():
    print(read_conf())


if __name__ == '__main__':
    main()
