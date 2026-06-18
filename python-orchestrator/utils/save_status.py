import json
from pathlib import Path

def save_status(
        testcase_id,
        status,
        message=""
):

    Path("status").mkdir(
        exist_ok=True
    )

    data = {
        "testcase_id": testcase_id,
        "status": status,
        "message": message
    }

    with open(
        f"status/{testcase_id}.json",
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )