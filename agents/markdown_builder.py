from pathlib import Path


def build_markdown(state):

    tc = state["testcase"]

    testcase_id = tc["testcase_id"]

    markdown = f"""
# {testcase_id}

## Scenario

{tc["scenario"]}

## Steps

{tc["steps"]}

## Expected Result

{tc["expected_result"]}
"""

    Path("specs").mkdir(exist_ok=True)

    spec_path = f"specs/{testcase_id}.md"

    with open(
        spec_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(markdown)

    return {
        "testcase_id": testcase_id,
        "spec_path": spec_path,
        "status": "SPEC_GENERATED"
    }