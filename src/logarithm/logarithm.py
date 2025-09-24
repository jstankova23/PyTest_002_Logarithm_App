# Logaritmus je inverzní operace k umocňování.  
# logaritmus čísla = exponent x, na který musím umocnit základ b, abych získala logaritmované číslo a;
# logaritmus čísla a při základu b: 
# log(a, b) = x nebo-li log_b(a) = x nebo-li b^x = a   
# Příklad:  
# log₂(8) = 3, protože 2³ = 8

# **a** … logaritmované číslo/argument logaritmu/výsledek umocněné báze, (musí být kladné);
# **b** … základ/báze logaritmu (musí být kladné a různé od 1);
# **x** … výsledek, exponent, logaritmus čísla a při základu b;

# definice funkce log vyvolá 3 výjimky, které testuje zvlášť parametrizovaná funkce test_log_exceptions:
# ValueError – logaritmované číslo **a** ≤ 0  
# ZeroDivisionError – základ logaritmu **b** ≤ 0  
# NameError – základ logaritmu **b** = 1  

import math

def log(a, b):
    if a <= 0:
        raise ValueError("Cannot take log of non-positive number!")
    if b <= 0:
        raise ZeroDivisionError("Cannot take log with non-positive base!")
    if b == 1:
        raise NameError("Cannot take log with base 1!")
    return math.log(a, b)

