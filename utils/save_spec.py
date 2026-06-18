def save_spec(testcase_id, markdown):

    file_path = (
        f"specs/{testcase_id}.md"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(markdown)

    return file_path