from pydantic import BaseModel


class TestCase(BaseModel):

    testcase_id: str
    scenario: str
    steps: str
    expected_result: str