import math


class Vector:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.k = 0

    def copy(self, v):
        self.i = v.i
        self.j = v.j
        self.k = v.k

    def set(self, ii, jj, kk):
        self.i = ii
        self.j = jj
        self.k = kk

    def set_module(self, mod):
        self.divide(self.module())
        self.multiply(mod)

    def add(self, v):
        self.i += v.i
        self.j += v.j
        self.k += v.k

    def subtract(self, v):
        self.i -= v.i
        self.j -= v.j
        self.k -= v.k

    def multiply(self, n):
        self.i *= n
        self.j *= n
        self.k *= n

    def divide(self, n):
        self.i /= n
        self.j /= n
        self.k /= n

    def module(self):
        m = math.sqrt(self.prod_int(self, self))
        return m

    def proj_vec(self, v1, v2):
        p = self.prod_int(v1, v2)
        if p < 0:
            p *= -1
        m = v1.module()
        m *= m
        p /= m
        self.copy(v1)
        self.multiply(p)

    def prod_vec(self, v1, v2):
        self.i = v1.j * v2.k - v2.j * v1.k
        self.j = v2.i * v1.k - v1.i * v2.k
        self.k = v1.i * v2.j - v2.i * v1.j

    def prod_int(self, v1, v2):
        p = v1.i * v2.i + v1.j * v2.j + v1.k * v2.k
        return p

    def cos_ang(self, v1, v2):
        p = self.prod_int(v1, v2)
        p /= v1.module()
        p /= v2.module()
        return p
