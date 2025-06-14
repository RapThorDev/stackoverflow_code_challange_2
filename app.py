from enum import Enum
from math import ceil
import sys
from typing import Dict
from random import Random


AVAILABLE_KEYS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7]

class CellType(Enum):
    POSITION = "P", # Next Position
    COMMAND = "C", # Command
    VALUE = "V", # Value

class Cell:
    def __init__(self, cell_type: CellType, value: int | None):
        self.type = cell_type
        self.value = value

    def p_cell(value):
        return Cell(CellType.POSITION, value)
    
    def c_cell(value):
        return Cell(CellType.COMMAND, value)
    
    def v_cell(value):
        return Cell(CellType.VALUE, value)

class Block:
    cell_dictionary: Dict[int, Cell]

    def __init__(self, cell_dictionary: Dict[int, Cell]):
        self.cell_dictionary = cell_dictionary

    def init(
            self,
            current_position_cell_key: int, 
            next_block_key: int, 
            ascii_dec_value: int,
            is_first_char: bool = False
            ):
        
        p_cell = Cell.p_cell(next_block_key)
        
        c_and_v_cells = self.value_cells_from_ascii_dec_value(
            ascii_dec_value, 
            self.__first_value_cell_key_by_position_cell_key(current_position_cell_key),
            is_first_char
            )
        
        cell_dictionary = {current_position_cell_key: p_cell}
        cell_dictionary.update(c_and_v_cells)

        return Block(cell_dictionary)

    def next_block_key(self) -> int | None:
        return self.__p_cell().value
    
    def ascii_dec_value(self) -> int | None:
        command_cell = self.__c_cell()

        if (self.__is_null_by_command_value(command_cell.value)):
            return None
        else:
            plus_value = self.__ascii_plus_dec_value_by_command_value()
            value_cells: Dict[int, int] = {}
            
            for value_cell_key in self.__value_cell_keys_by_command_key(command_cell):
                value_cell = self.cell_dictionary.get(value_cell_key)
                if value_cell.value != None:
                    value_cells[value_cell_key] = value_cell.value

            can_subdivide_with_ten = len(value_cells) > 1 and value_cells.get(3) == 1
            current_value = None
            for index, (key, value) in value_cells:
                if key != 3:
                    current_value = int(f"{key}0") if can_subdivide_with_ten else int(f"{key}{value}")
            if current_value == None:
                return current_value
            else:
                return current_value + plus_value
    
    def value_cells_from_ascii_dec_value(
            self, 
            ascii_dec_value: int | False, 
            first_value_cell_key: int, 
            is_first_char: bool = False
            ) -> Dict[int, Cell]:
        if (ascii_dec_value >= 32 and ascii_dec_value <= 99):
            ascii_dec_value_str = str(ascii_dec_value)
            if is_first_char:
                return { 
                    ascii_dec_value_str[0]: Cell.v_cell(ascii_dec_value_str[1]),
                    first_value_cell_key - 1: Cell.c_cell(5)
                    }
            else:
                return { ascii_dec_value_str[0]: Cell.v_cell(ascii_dec_value_str[1]) }
        elif (ascii_dec_value >= 100 and ascii_dec_value <= 167):
            ascii_dec_value_str = str(ascii_dec_value - 68)
            c_cell_value = 10 - 1 if is_first_char else 1
            return { 
                ascii_dec_value_str[0]: Cell.v_cell(ascii_dec_value_str[1]),
                first_value_cell_key - 1: Cell.c_cell(c_cell_value)
                }
        elif (ascii_dec_value >= 168 and ascii_dec_value <= 235):
            ascii_dec_value_str = str(ascii_dec_value - 68 - 68)
            c_cell_value = 10 - 2 if is_first_char else 2
            return { 
                ascii_dec_value_str[0]: Cell.v_cell(ascii_dec_value_str[1]),
                first_value_cell_key - 1: Cell.c_cell(c_cell_value)
                }
        elif (ascii_dec_value >= 236 and ascii_dec_value <= 255):
            ascii_dec_value_str = str(ascii_dec_value - 68 - 68 - 68)
            c_cell_value = 10 - 3 if is_first_char else 3
            return { 
                ascii_dec_value_str[0]: Cell.v_cell(ascii_dec_value_str[1]),
                first_value_cell_key - 1: Cell.c_cell(c_cell_value) 
                }
        else:
            c_cell_value = Random.choice([4, 6])
            v_cell_key = Random.choice(self.__value_cell_keys_by_command_key(first_value_cell_key - 1))
            v_cell_value = Random.choice(AVAILABLE_KEYS)
            return {
                first_value_cell_key - 1: Cell.c_cell(c_cell_value),
                v_cell_key: Cell.v_cell(v_cell_value)
            }

    def __value_cell_keys_by_command_key(command_key: int) -> list[int]:
        start_key = AVAILABLE_KEYS.index(command_key) + 1
        return AVAILABLE_KEYS[start_key:start_key + 7]

    def __ascii_plus_dec_value_by_command_value(self, command_value: int) -> int:
        plus_value = 0
        if (command_value == 1 or command_value == 9):
            plus_value = 68
        elif (command_value == 2 or command_value == 8):
            plus_value = 2 * 68
        elif (command_value == 3 or command_value == 7):
            plus_value = 3 * 68

        return plus_value
    
    def __is_null_by_command_value(self, command_value) -> bool:
        return command_value == 4 or command_value == 6
    
    def __first_value_cell_key_by_position_cell_key(self, position_key) -> int:
        return AVAILABLE_KEYS.index(position_key) + 2
        
    def __p_cell(self) -> Cell:
        return next(cell for cell in self.cell_dictionary.values() if cell.type == CellType.POSITION)

    def __c_cell(self) -> Cell:
        return next(cell for cell in self.cell_dictionary.values() if cell.type == CellType.COMMAND)


class Board:
    """ block_dictionary
        {
            1: Block,
            ...,
            9: Block
        }
    """
    available_block_keys = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    block_dictionary: Dict[int, Block]

    def __init__(self, block_dictionary: Dict[int, Block]):
        self.block_dictionary = block_dictionary

class Main:
    test_sudoku_board = Board({
        1: Block({1: Cell.p_cell(2), 2: Cell.c_cell(5), 8: Cell.v_cell(3)}),
    })

    def main(self, argv):
        sudoku_structure: list[Board] = self.__init_sudoku_structure(argv[1])

        sudoku_board = {
            # Block 1-9
            1: {
                # Cell 1-9
                1: {type: ""}
            }
        }

    def __init_sudoku_structure(self, string: str) -> list[Board]:
        boards_count = self.__boards_count(string)

        return []


    def __boards_count(self, string: str):
        return ceil(len(string) / 9)

if __name__ == "__main__":
    Main.main(sys.argv)
