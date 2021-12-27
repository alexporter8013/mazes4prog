from typing import List
from functools import cached_property
from random import randint

import PIL

from .cell import Cell


class Grid:
    def __init__(self, rows: int, columns: int):
        self._rows = rows
        self._columns = columns
        self._cells: List[Cell] = []
        self.prepare_grid()
        self.configure_cells()
        
    def prepare_grid(self):
        for row in range(self._rows):
            for col in range(self._columns):
                self._cells.append(Cell(row, col))
    
    def configure_cells(self):
        for cell in self._cells:
            row = cell.row
            col = cell.column
            
            cell.north = self[row - 1, col]
            cell.south = self[row + 1, col]
            cell.west = self[row, col - 1]
            cell.east = self[row, col + 1]
    
    @cached_property
    def rows(self) -> int:
        return self._rows
    
    @cached_property
    def columns(self) -> int:
        return self._columns
    
    def __getitem__(self, idx) -> Cell:
        row, column = idx
        if row not in range(self.rows):
            return None
        if column not in range(self.columns):
            return None

        idx = row * self.columns + column
        return self._cells[idx]
    
    @cached_property
    def size(self):
        return self.rows * self.columns
    
    @property
    def random_cell(self):
        row = randint(0, self.rows - 1)
        col = randint(0, self.columns - 1)
        
        return self[row, col]
    
    @property
    def cell_iter(self):
        for cell in self._cells:
            yield cell
        
    def __str__(self) -> str:
        output = "+" + "---+" * self.columns + "\n"
        
        for row in range(self.rows):
            top = "|"
            bottom = "+"

            for col in range(self.columns):
                cell = self[row, col] or Cell(-1, -1)
                body = "   "
                east_boundary = " " if cell.is_linked(cell.east) else "|"
                south_boundary = "   " if cell.is_linked(cell.south) else "---"
                corner = "+"
                
                top += body + east_boundary
                bottom += south_boundary + corner
                
            output += top + "\n"
            output += bottom + "\n"
        
        return output
