#!/usr/bin/env python
# coding: utf-8

# In[2]:


import p1

def test_p1_prime():
    assert p1.smallest_factor(7) == 7, "failed on prime number"

def test_pers_even():
    assert p1.smallest_factor(8) == 2, "failed on even number"

def test_pers_odd():
    assert p1.smallest_factor(9) == 3, "failed on odd number"

