import unittest
from packages.core import IsolatedAgent, VertexAI

class TestIsolatedAgent(unittest.TestCase):
    def test_run(self):
        isolated_agent = IsolatedAgent('test_node', VertexAI(model='test_model'))
        isolated_agent.run()

if __name__ == '__main__':
    unittest.main()