from decimal import Decimal
from traitement import traitement

def test_traitement():
    l = [
        ["2024", "FR1", "FR", "BNP", "DE1", "DE", Decimal("100"), "EUR"],
        ["2024", "FR1", "FR", "BNP", "DE1", "DE", Decimal("200"), "EUR"],
        ["2024", "FR2", "FR", "LCL", "DE2", "DE", Decimal("300"), "EUR"],
    ]

    iban_som, banq_som, dest_som = traitement(l)

    assert iban_som["FR1"] == Decimal("300")
    assert iban_som["FR2"] == Decimal("300")

    assert banq_som["BNP"] == Decimal("300")
    assert banq_som["LCL"] == Decimal("300")

    assert dest_som["DE1"] == Decimal("300")
    assert dest_som["DE2"] == Decimal("300")