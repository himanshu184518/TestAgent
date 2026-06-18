import subprocess

def executor_node(state):

    test_path = state["test_path"]

    print(
        f"\nExecuting: {test_path}"
    )

    result = subprocess.run(
        f'npx playwright test "{test_path}"',
        shell=True,
        capture_output=True,
        text=True
    )

    if result.returncode == 0:

        print(
            "\nTEST PASSED"
        )

        return {
            "status": "PASSED",
            "execution_result":
                result.stdout
        }

    print(
        "\nTEST FAILED"
    )

    print(result.stderr)

    return {
        "status": "FAILED",
        "execution_result":
            result.stderr
    }