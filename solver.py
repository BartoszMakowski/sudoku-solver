from typing import List, Set


N = 9
ALL_NUMBERS = set(range(1,10))


class SudokuSolver:
    board: List[List[int]] = None    
    
    def __init__(self, board) -> None:
        self.board = board
        self.solved = False
        
    def solve(self) -> None:
        while not self.solved:
            self.solved = self._solve()
    
    def _solve(self) -> bool:
        solved = True
        for x in range(N):
            for y in range(N):
                if self.board[x][y] == 0:
                    values = self.get_field_possibilities((x,y))
                    if len(values) == 1:
                        self.board[x][y] = values.pop()
                    else:
                        solved = False
        return solved
                    
    def get_field_possibilities(self, position) -> Set[int]:
        return self._get_possibilities_from_square(position) & self._get_possibilities_from_vertical(position) & self._get_possibilities_from_horizontal(position)
    
    def _get_possibilities_from_square(self, position) -> Set[int]:
        base_x = 3 * (position[0] // 3)
        base_y = 3 * (position[1] // 3)
        
        taken = set()
        for i in range(3):
            taken |= set(self.board[base_x+i][base_y:base_y+3])
        return ALL_NUMBERS - taken
    
    def _get_possibilities_from_vertical(self, position) -> Set[int]:
        taken = {self.board[position[0]][y] for y in range(N)}
        return ALL_NUMBERS - taken
    
    def _get_possibilities_from_horizontal(self, position) -> Set[int]:
        taken = {self.board[x][position[1]] for x in range(N)}
        return ALL_NUMBERS - taken
