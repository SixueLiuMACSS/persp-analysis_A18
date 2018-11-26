#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pytest
import p3

def test_p3():
    assert p3.operate(4, 2, '+') == 6, "failed on addition"
    assert p3.operate(2, 4, '-') == -2, "failed on subtraction"
    assert p3.operate(4, 2, '*') == 8, "failed on multiplication"
    assert p3.operate(9, 3, '/') == 3, "failed on division"
    with pytest.raises(TypeError) as excinfo1:
        p3.operate(4, 0, 8)
    assert excinfo1.value.args[0] == "oper must be a string"
    with pytest.raises(ZeroDivisionError) as excinfo2:
        p3.operate(4, 0, '/')
    assert excinfo2.value.args[0] == "division by zero is undefined"
    with pytest.raises(ValueError) as excinfo3:
        p3.operate(4, 0, '&')
    assert excinfo3.value.args[0] == "oper must be one of '+', '/', '-', or '*'"
    

