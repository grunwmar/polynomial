import os
import math
import numbers
import random
import itertools
import base64


class Polynomial:

    _VAR_LABELS = 'x'


    @classmethod
    def set_var_labels(cls, iterable):
        cls._VAR_LABELS = iterable


    def __init__(self, *coefficients):
        self._coefficients = coefficients


    def __getitem__(self, char):
        exp_map = '⁰¹²³⁴⁵⁶⁷⁸⁹'
        monome_list = []

        for k, a in enumerate(self._coefficients):
            if a == 0:
                continue
            if a < 0:
                sign = '- '
            else:
                sign = '+ '

            e = ''
            for i in str(k):
                e += exp_map[int(i)]

            abs_a = abs(a)
            if k == 0:
                monome_list.append(f'{sign}{abs_a}')
            else:
                monome_list.append(f'{sign}{abs_a}{char}{e}')

        monome_list.reverse()
        poly_str = ' '.join(monome_list)

        if poly_str.startswith('+ '):
            poly_str = poly_str[2:]

        return poly_str


    def __str__(self):
        ch = random.choice(self._VAR_LABELS)
        return f"{self[ch]}"


    def __tuple__(self):
        return tuple(*self._coefficients)


    def evaluate(self, x):
        value = sum(coeff * (x ** exp) for exp, coeff in \
        enumerate(self._coefficients))
        return value


    def __call__(self, x):
        return self.evaluate(x)


    @property
    def get_lambda(self):
        return lambda x: sum(coeff * (x ** exp) for exp, coeff in \
        enumerate(self._coefficients))


    @property
    def coefficients(self):
        return self._coefficients


    def __add__(self, polynomial):
        if not isinstance(polynomial, __class__):
            raise ValueError
        new_coeffs = []
        for a,b in itertools.zip_longest(self._coefficients, polynomial._coefficients, fillvalue=0):
            new_coeffs.append(a + b)
        return __class__(*new_coeffs)


    def __sub__(self, polynomial):
        if not isinstance(polynomial, __class__):
            raise ValueError
        return (-1 * polynomial) + self


    def __rmul__(self, number):
        if not isinstance(number, numbers.Number):
            raise ValueError
        new_coeffs = map(lambda x: number * x, self._coefficients)
        return self.__class__(*new_coeffs)


    def __mul__(self, polynomial):
        if not isinstance(polynomial, __class__):
            raise ValueError
        coeffs_a = self._coefficients
        coeffs_b = polynomial.coefficients

        monomes = dict()
        new_coeffs = []
        for i, a in enumerate(coeffs_a):
            for j, b in enumerate(coeffs_b):
                k, c = i+j, a*b
                if monomes.get(k) is None:
                    monomes[k]  = c
                else:
                    monomes[k] += c

        # to ensure sorted values
        new_coeffs = [monomes[i] for i in range(len(monomes))]
        return self.__class__(*new_coeffs)


    def __truediv__(self, number):
        if not isinstance(number, numbers.Number):
            raise ValueError
        return (1/number) * self


    _EASTEREGG_BK = None

    @classmethod
    def easteregg(cls):
        _EASTEREGG64 = '8J+QtfCfkKnwn5C08J+Qq/CfkJjwn5Ct8J+Qp/CfkKLwn5CN8J+QrPCfkJ7wn4y88J+NgPCfjYTwn42G8J+NuvCfjI3wn5qC8J+ahvCfmpzwn5qA8J+SjvCfjrXwn5K+8J+TuvCfk5o='
        _EASTEREGG = base64.b64decode(_EASTEREGG64.encode('ascii')).decode('utf-8')
        _EASTEREGG_NEW = [f'·{c}' for c in _EASTEREGG]
        cls._EASTEREGG_BK = cls._VAR_LABELS
        cls._VAR_LABELS = _EASTEREGG_NEW

    @classmethod
    def deactivate_easteregg(cls):
        cls._VAR_LABELS = cls._EASTEREGG_BK


...
