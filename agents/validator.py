def validate_testcase(state):

    testcase = state["testcase"]

    issues = []

    if not testcase["scenario"]:
        issues.append("Scenario missing")

    if not testcase["steps"]:
        issues.append("Steps missing")

    if not testcase["expected_result"]:
        issues.append("Expected Result missing")

    return {
        "validation_result": {
            "status": "valid" if not issues else "invalid",
            "issues": issues
        }
    }