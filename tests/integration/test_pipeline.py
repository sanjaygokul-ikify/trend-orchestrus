import unittest
from packages.core import AgentGraph, IsolatedAgent, VertexAI
from packages.services import Orchestrator

class TestPipeline(unittest.TestCase):
    def testPipeline(self):
        orchestrator = Orchestrator()
        vertex_ai = VertexAI(model='test_model')
        agent_graph = AgentGraph()
        agent_graph.add_node('test_node', vertex_ai, {})
        orchestrator.run()

if __name__ == '__main__':
    unittest.main()