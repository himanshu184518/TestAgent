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

from graphs.planner_node import (
    planner_node
)

from graphs.generator_node import (
    generator_node
)

from graphs.executor_node import (
    executor_node
)

from graphs.status_node import (
    status_node
)

workflow = StateGraph(
    TestState
)

workflow.add_node(
    "validator",
    validate_testcase
)

workflow.add_node(
    "markdown_builder",
    build_markdown
)

workflow.add_node(
    "planner",
    planner_node
)

workflow.add_node(
    "generator",
    generator_node
)

workflow.add_node(
    "executor",
    executor_node
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
    "planner"
)

workflow.add_edge(
    "planner",
    "generator"
)

workflow.add_edge(
    "generator",
    "executor"
)

workflow.add_edge(
    "executor",
    "status"
)

workflow.add_edge(
    "status",
    END
)

graph = workflow.compile()