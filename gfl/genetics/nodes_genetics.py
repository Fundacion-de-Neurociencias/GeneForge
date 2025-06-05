from .core import Node

class MendelLaw(Node):
    def __init__(self, name, description):
        super().__init__('mendel_law', name=name, description=description)

class GeneticTechnique(Node):
    def __init__(self, name, components, mechanism):
        super().__init__('genetic_technique', name=name, components=components, mechanism=mechanism)

class Application(Node):
    def __init__(self, domain, goal, method):
        super().__init__('application', domain=domain, goal=goal, method=method)

class AITool(Node):
    def __init__(self, purpose, technology, integrated_with):
        super().__init__('ai_tool', purpose=purpose, technology=technology, integrated_with=integrated_with)

class EthicsGuideline(Node):
    def __init__(self, principle, recommendation):
        super().__init__('ethics_guideline', principle=principle, recommendation=recommendation)
