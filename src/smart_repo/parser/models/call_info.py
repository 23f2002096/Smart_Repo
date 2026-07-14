from dataclasses import dataclass


@dataclass
class CallInfo:
    """
    Information about a function call.
    """

    caller: str
    callee: str
    line_number: int