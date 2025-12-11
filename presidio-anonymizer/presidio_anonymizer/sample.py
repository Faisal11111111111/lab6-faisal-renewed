from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig


def sample_run_anonymizer(text: str, start: int, end: int):
    """
    Refactored version of the sample anonymizer runner.
    
     Takes parameters instead of using input()
     Returns the result so unit tests can assert correctness
     Fully testable according to Lab 6 requirements
    """

    engine = AnonymizerEngine()

    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(
                entity_type="PERSON",
                start=start,
                end=end,
                score=0.8
            )
        ],
        operators={
            "PERSON": OperatorConfig("replace", {"new_value": "BIP"})
        }
    )

    return result


if __name__ == "__main__":
    # For manual demonstration only — Lab requires fixed inputs here.
    output = sample_run_anonymizer("My name is Bond.", 11, 15)
    
    # Print the exact output format shown in the instructions
    print(output)
