from utils.excel_reader import load_testcases
from graphs.workflow import graph

testcases = load_testcases("data/testcases.xlsx")

for testcase in testcases:

    result = graph.invoke(
        {
            "testcase": testcase.model_dump()
        }
    )

    print(result)