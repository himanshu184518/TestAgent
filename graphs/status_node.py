import json
from pathlib import Path


def status_node(state):

    Path("status").mkdir(exist_ok=True)

    file_path = (
        f"status/{state['testcase_id']}.json"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            {
                "testcase_id":
                    state["testcase_id"],

                "status":
                    state["status"],

                "spec_path":
                    state["spec_path"]
            },
            f,
            indent=4
        )

    return state