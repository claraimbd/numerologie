import monnaie


def test_devise():
    assert monnaie.dollar(1).devise == "USD"
    assert monnaie.franc(1).devise == "CHF"


def test_multiplication_dollar():
    cinq = monnaie.dollar(5)
    dix = cinq * 2
    assert dix == monnaie.dollar(10)
   
def test_égalité_dollar():
    assert monnaie.dollar(5) == monnaie.dollar(5)
    assert monnaie.dollar(5) != monnaie.dollar(8)

def test_différence_franc_dollar():
    assert monnaie.franc(5) != monnaie.dollar(5)
