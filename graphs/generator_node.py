from pathlib import Path

def generator_node(state):

    testcase_id = state["testcase_id"]

    plan_path = state["plan_path"]

    generated_test = f"""
import {{ test, expect }} from '@playwright/test';

test('{testcase_id}', async ({{ page }}) => {{

    await page.goto(
        'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    );

    await expect(
        page.locator(
            'input[name="username"]'
        )
    ).toBeVisible();

}});
"""

    Path("tests").mkdir(
        exist_ok=True
    )

    test_path = (
        f"tests/{testcase_id}.spec.ts"
    )

    with open(
        test_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            generated_test
        )

    return {
        "test_path": test_path
    }