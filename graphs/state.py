from typing import TypedDict


class TestState(TypedDict, total=False):

    testcase: dict

    testcase_id: str

    spec_path: str

    status: str

    error_message: str

    validation_result: dict