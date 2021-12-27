from random import sample
from .grid import Grid


class BinaryTree:
    
    @classmethod
    def on(cls, grid: Grid):
        for cell in grid.cell_iter:
            neighbors = []
            if cell.north is not None:
                neighbors.append(cell.north)
            if cell.east is not None:
                neighbors.append(cell.east)
            
            if len(neighbors) > 0:
                cell.link(sample(neighbors, 1)[0])
