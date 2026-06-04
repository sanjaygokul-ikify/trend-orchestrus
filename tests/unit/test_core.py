import unittest
from packages.core import AgentGraph, VertexAI

class TestAgentGraph(unittest.TestCase):
    def test_add_node(self):
        agent_graph = AgentGraph()
        vertex_ai = VertexAI(model='test_model')
        agent_graph.add_node('test_node', vertex_ai, {})
        self.assertIn('test_node', agent_graph.graph)

    def test_run(self):
        agent_graph = AgentGraph()
        vertex_ai = VertexAI(model='test_model')
        agent_graph.add_node('test_node', vertex_ai, {})
        agent_graph.run()

if __name__ == '__main__':
    unittest.main()