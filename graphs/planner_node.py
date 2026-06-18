from pathlib import Path

def planner_node(state):

    testcase_id = state["testcase_id"]

    spec_path = state["spec_path"]

    with open(spec_path, "r", encoding="utf-8") as f:
        spec_content = f.read()

    plan_content = f"""
# Execution Plan

Generated from:

{spec_path}

Review steps and prepare automation.
"""

    plan_path = f"plans/{testcase_id}-plan.md"

    Path("plans").mkdir(exist_ok=True)

    with open(plan_path, "w", encoding="utf-8") as f:
        f.write(plan_content)

    return {
        "plan_path": plan_path
    }