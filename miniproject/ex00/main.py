from checkmate import *

def main():
    board = """\
Q...
....
..K.
...."""

    print("Result: ", end="")
    checkmate(board)
    
if __name__ == "__main__":
    main()