# TESTOVACÍ PARAMETRIZOVANÉ FUNKCE pro logaritmus čísla a výjimky
# Logaritmus je inverzní operace k umocňování.  
# logaritmus čísla = exponent x, na který musím umocnit základ b, abych získala logaritmované číslo a;
# logaritmus čísla a při základu b: 
# log(a, b) = x nebo-li log_b(a) = x nebo-li b^x = a   
# Příklad:  
# log₂(8) = 3, protože 2³ = 8

# **a** … logaritmované číslo/argument logaritmu/výsledek umocněné báze, (musí být kladné);
# **b** … základ/báze logaritmu (musí být kladné a různé od 1);
# **x** … výsledek, exponent, logaritmus čísla a při základu b;


import pytest
from src.logarithm import log

# 1. Parametrizovaná funkce pro otestování logaritmu   
@pytest.mark.parametrize(
    "a, b, exponent",
    [
        (8, 2, 3),          # log_8(2) = 3 ... 2³ = 8; 2^3 = 8
        (9, 3, 2),          # log_9(3) = 2 ... 3² = 9; 3^3 = 9
        (10000, 10, 4)      # log_10000(10) = 4 ... 10⁴ = 10000; 10^4 = 10000
    ],
)
def test_log(a, b, exponent):
    assert log(a, b) == exponent


# 2. Parametrizovaná funkce pro otestování výjimek logaritmu   
# ValueError – logaritmované číslo **a** ≤ 0  
# ZeroDivisionError – základ logaritmu **b** ≤ 0  
# NameError – základ logaritmu **b** = 1  
@pytest.mark.parametrize(
    "a, b, expected_exception, expected_message",
    [
        (0, 2, ValueError, "Cannot take log of non-positive number!"),
        (10, -1, ZeroDivisionError, "Cannot take log with non-positive base!"),
        (10, 1, NameError, "Cannot take log with base 1!")
    ],
)
def test_log_exceptions(a, b, expected_exception, expected_message):
    with pytest.raises(expected_exception) as exc:
        log(a, b)
    assert str(exc.value) == expected_message

