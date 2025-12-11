import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    # Call the refactored function with known test values
    result = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Verify anonymized text
    assert result.text == "My name is BIP."

    # There should be exactly one operator result
    assert len(result.items) == 1
    item = result.items[0]

    # OperatorResult fields accessed as attributes
    assert item.start == 11
    assert item.end == 14
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"
