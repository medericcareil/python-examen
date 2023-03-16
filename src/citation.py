import random
from data.citations import kaamelott_citations

class Citation:

    def __init__(self) -> None:
        self._citation = ''

    def get_citation(self) -> str:
        return self._citation

    def set_citation(self, new_citation : str) -> str:
        self._citation = new_citation

    def random_citation(self) -> str:
        self._citation = random.choice(kaamelott_citations)
        return self.get_citation()
