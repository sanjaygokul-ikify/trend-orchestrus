from typing import Dict, List
from logging import Logger
import logging
from .types import VertexAI, IsolatedAgent
from .exceptions import OrchestrationError


class AgentGraph:
    def __init__(self):
        self.graph: Dict[str, List[VertexAI]] = {}
        self.logger: Logger = logging.getLogger(__name__)

    def add_node(self, node_id: str, llm: VertexAI, resources: Dict[str, str]) -> None:
        self.graph[node_id] = [llm]
        self.logger.info(f"Added node {node_id} with resources {resources}")

    def run(self) -> None:
        for node_id, vertex_ai_list in self.graph.items():
            for vertex_ai in vertex_ai_list:
                try:
                    vertex_ai.run()
                except Exception as e:
                    self.logger.error(f"Error running node {node_id}: {str(e)}")
                    raise OrchestrationError(f"Error running node {node_id}: {str(e)}")


class KernelLevelIsolation:
    def __init__(self):
        self.logger: Logger = logging.getLogger(__name__)

    def isolate(self, node_id: str) -> None:
        self.logger.info(f"Isolating node {node_id}")
        # Implement kernel-level isolation using Firecracker microVMs

    def deisolate(self, node_id: str) -> None:
        self.logger.info(f"Deisolating node {node_id}")
        # Implement deisolation


class DeadlineSchedulingAlgorithm:
    def __init__(self):
        self.logger: Logger = logging.getLogger(__name__)

    def schedule(self, node_id: str) -> None:
        self.logger.info(f"Scheduling node {node_id}")
        # Implement deadline scheduling algorithm


class FairShareSchedulingAlgorithm:
    def __init__(self):
        self.logger: Logger = logging.getLogger(__name__)

    def schedule(self, node_id: str) -> None:
        self.logger.info(f"Scheduling node {node_id}")
        # Implement fair share scheduling algorithm


class HierarchicalSchedulingAlgorithm:
    def __init__(self):
        self.logger: Logger = logging.getLogger(__name__)
        self.deadline_scheduling_algorithm: DeadlineSchedulingAlgorithm = DeadlineSchedulingAlgorithm()
        self.fair_share_scheduling_algorithm: FairShareSchedulingAlgorithm = FairShareSchedulingAlgorithm()

    def schedule(self, node_id: str) -> None:
        self.deadline_scheduling_algorithm.schedule(node_id)
        self.fair_share_scheduling_algorithm.schedule(node_id)