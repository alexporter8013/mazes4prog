from typing import Set


class Cell:
    def __init__(self, row: int, column: int) -> None:
        self._neighbors = set()
        self._links = set()
        self._row = row
        self._column = column
        self.north: 'Cell' = None
        self.south: 'Cell' = None
        self.east: 'Cell' = None
        self.west: 'Cell' = None
        
    def link(self, other: 'Cell', bidirectional = True):
        self._links.add(other)
        if bidirectional:
            other.link(self, False)
    
    def unlink(self, other: 'Cell', bidirectional = True):
        self._links.remove(other)
        if bidirectional:
            other.unlink(self)
    
    @property
    def neighbors(self) -> Set['Cell']:
        ret = []
        
        if self.north is not None:
            ret.append(self.north)
        if self.south is not None:
            ret.append(self.south)
        if self.east is not None:
            ret.append(self.east)
        if self.west is not None:
            ret.append(self.west)
        
        return set(ret)
    
    @property
    def links(self) -> Set['Cell']:
        return set(self._links)
    
    def is_linked(self, other: 'Cell') -> bool:
        return other in self._links
    
    @property
    def row(self) -> int:
        return self._row
    
    @property
    def column(self) -> list:
        return self._column
    