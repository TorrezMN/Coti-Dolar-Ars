#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.


from scripts.el_cronista import el_cronista_main
from scripts.la_nacion import la_nacion_main
from scripts.ambito import ambito_main
from scripts.infobae import infobae_main


if __name__ == "__main__":

    try:
        print('='*44)
        print("Running EL CRONISTA.")
        print('='*44)
        el_cronista_main()
    except Exception as e:
        print("El Cronista", e)

    try:
        print('='*44)
        print("Running LA NACION.")
        print('='*44)
        la_nacion_main()
    except Exception as e:
        print("La Nacion", e)

    try:
        print('='*44)
        print("Running AMBITO.")
        print('='*44)
        ambito_main()
    except Exception as e:
        print("Ambito", e)

    try:
        print('='*44)
        print("Running INFOBAE.")
        print('='*44)
        infobae_main()
    except Exception as e:
        print("Infobae", e)
