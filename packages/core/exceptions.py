class OrchestrusError(Exception):
    """Base exception class for all orchestrus exceptions."""

    def __init__(self, message: str):
        self.message: str = message
        super().__init__(message)


class OrchestrationError(OrchestrusError):
    """Raised when there is an error during orchestration."""

    def __init__(self, message: str):
        super().__init__(message)


class NodeExecutorError(OrchestrusError):
    """Raised when there is an error during node execution."""

    def __init__(self, message: str):
        super().__init__(message)
