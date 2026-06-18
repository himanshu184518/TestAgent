from langgraph.graph import (
    StateGraph,
    END
)

from graphs.state import TestState

from agents.validator import (
    validate_testcase
)

from agents.markdown_builder import (
    build_markdown
)

from graphs.status_node import (
    status_node
)

workflow = StateGraph(TestState)

workflow.add_node(
    "validator",
    validate_testcase
)

workflow.add_node(
    "markdown_builder",
    build_markdown
)

workflow.add_node(
    "status",
    status_node
)

workflow.set_entry_point(
    "validator"
)

workflow.add_edge(
    "validator",
    "markdown_builder"
)

workflow.add_edge(
    "markdown_builder",
    "status"
)

workflow.add_edge(
    "status",
    END
)

graph = workflow.compile()