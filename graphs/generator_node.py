from pathlib import Path

def generator_node(state):

    testcase_id = state["testcase_id"]

    plan_path = state["plan_path"]

    with open(plan_path, "r", encoding="utf-8") as f:
        plan = f.read()

    generated_test = f"""
import {{ test, expect }} from '@playwright/test';

test('{testcase_id}', async ({{ page }}) => {{

    // Generated from
    // {plan_path}

    await page.goto('https://example.com');

}});
"""

    Path("tests").mkdir(exist_ok=True)

    test_path = f"tests/{testcase_id}.spec.ts"

    with open(test_path, "w", encoding="utf-8") as f:
        f.write(generated_test)

    return {
        "test_path": test_path
    }