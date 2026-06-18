from graphs.executor_node import executor_node

result = executor_node(
    {
        "test_path": "tests/TC001.spec.ts"
    }
)

print(result)