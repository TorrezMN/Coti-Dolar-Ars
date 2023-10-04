#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.


from scripts.el_cronista import el_cronista_main


if __name__ == "__main__":
    try:
        el_cronista_main()
    except Exception as e:
        print(e)
