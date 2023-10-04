#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.


from scripts.el_cronista import el_cronista_main
from scripts.la_nacion import la_nacion_main


if __name__ == "__main__":
    try:
        el_cronista_main()
        la_nacion_main()
    except Exception as e:
        print(e)
