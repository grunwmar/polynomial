import os
import math
import numbers
import random


class Polynomial:

    def __init__(self, *coefficients):
        self._coefficients = coefficients
        self._var_labels = 3*list('abcdfghkmnpqrtstuvwxyz') \
         + 2*list('αβγδεζηθκλμνξπρστφχψω') \
         + ['🐘', '🐎', '🐭', '🐢', '🐬', '🐧','🐫']

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
        ch = random.choice(self._var_labels)
        return f"({ch} » {self[ch]})"


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
