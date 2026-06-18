def route_execution(state):

    if state["status"] == "PASSED":
        return "status"

    return "healer"