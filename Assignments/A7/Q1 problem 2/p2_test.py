#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import p2

def test_p2_month():
    assert p2.month_length('January') == 31, "failed on January"
    assert p2.month_length('April') == 30, "failed on April"
    assert p2.month_length('February', leap_year=True) == 29, "failed on February_leap_year"
    assert p2.month_length('February', leap_year=False) == 28, "failed on February_not_leap_year"
    assert p2.month_length('Other') == None, "failed on other_cases"