from packages.core import AgentGraph, IsolatedAgent, VertexAI
from packages.utils.logging import setup_logging

class Orchestrator:
    def __init__(self):
        self.agent_graph = AgentGraph()
        setup_logging(level=logging.INFO)

    def run(self):
        self.agent_graph.run()