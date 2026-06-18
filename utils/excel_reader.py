import pandas as pd

from models.schemas import TestCase


def load_testcases(file_path):

    df = pd.read_excel(file_path)

    testcases = []

    for row in df.iterrows():

        r = row[1]

        testcase = TestCase(
            testcase_id=str(r["TestCaseID"]),
            scenario=str(r["Scenario"]),
            steps=str(r["Steps"]),
            expected_result=str(r["ExpectedResult"])
        )

        testcases.append(testcase)

    return testcases