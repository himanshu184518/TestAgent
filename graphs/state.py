from typing import TypedDict

class TestState(TypedDict, total=False):

    testcase: dict

    testcase_id: str

    spec_path: str

    plan_path: str

    test_path: str

    execution_result: str

    status: str

    validation_result: dict

    error_message: str