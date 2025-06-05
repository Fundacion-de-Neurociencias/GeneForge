from gf.core import Node

class GeneticTechnique(Node):
    def __init__(self, name, components, mechanism):
        super().__init__('genetic_technique', name=name, components=components, mechanism=mechanism)
