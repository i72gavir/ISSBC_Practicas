# -*- coding: utf-8 -*-
"""

@author: Rafa
"""

for s, p, o in someGraph:
    if not (s, p, o) in someGraph:
        raise Exception("Iterator / Container Protocols are Broken!!")