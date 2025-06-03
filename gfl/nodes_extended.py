from dataclasses import dataclass

@dataclass
class RetroviralElement:
    locus: str
    activity: str = "unknown"  # e.g., 'silenced', 'transcribed', 'active'

@dataclass
class MitochondrialGene:
    name: str
    function: str = "unknown"  # e.g., 'oxidative_phosphorylation', 'tRNA', 'rRNA'

@dataclass
class piRNA:
    origin_locus: str
    target: str
    mode: str = "silencing"  # e.g., 'silencing', 'regulation'

@dataclass
class Transposon:
    family: str
    insertion_site: str
    mobility: bool = False  # True if active
