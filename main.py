import pygame


sudoku = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

size: int = 500
rows: int = 9

window: pygame.surface.Surface = pygame.display.set_mode((size, size))
window.fill((255, 255, 255))


def main() -> None:
    pygame.init()

    play = True

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

        solve()

    pygame.quit()


def solve():
    global sudoku
    global window

    window.fill((255, 255, 255))
    draw_sudoku_grid()
    pygame.display.update()
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for n in range(1, 10):
                    if is_sudoku_valid(i, j, n):
                        window.fill((255, 255, 255))
                        draw_sudoku_grid()
                        pygame.display.update()
                        sudoku[i][j] = n
                        cell_size = size // 9
                        rect = pygame.Rect(
                            j * cell_size, i * cell_size, cell_size, cell_size
                        )
                        pygame.draw.rect(window, (0, 255, 0), rect, 4)
                        pygame.display.update()
                        pygame.time.delay(100)
                        solve()
                        sudoku[i][j] = 0
                        cell_size = size // 9
                        rect = pygame.Rect(
                            j * cell_size, i * cell_size, cell_size, cell_size
                        )
                        pygame.draw.rect(window, (255, 0, 0), rect, 4)
                        pygame.display.update()
                        pygame.time.delay(100)
                return

    input("More?")


def is_sudoku_valid(x, y, num):
    global sudoku

    print("Checking row")
    # Check if num can fit in row x
    for i in range(9):
        print(f"({x},{i}) is {sudoku[x][i]} == {num}")
        if sudoku[x][i] == num:
            print("invalid")
            return False
    print("row: OK")

    print("Checking col")
    # Check if num can fit in column y
    for i in range(9):
        print(f"({i},{y}) is {sudoku[i][y]} == {num}")
        if sudoku[i][y] == num:
            print("invalid")
            return False
    print("col: OK")

    print("Checking box")
    # Check if num can fit in it's corresponding 3x3 box
    x0 = 3 * (x // 3)
    y0 = 3 * (y // 3)
    print(f"Box origin at ({x0}, {y0})")
    for i in range(3):
        for j in range(3):
            print(f"({x0+i},{y0+j}) is {sudoku[x0+i][y0+j]} == {num}")
            if sudoku[x0 + i][y0 + j] == num:
                print("invalid")
                return False
    print("box: OK")

    print("OK")
    return True


def draw_sudoku_grid():
    global window
    global size
    global sudoku

    board_size = size  # Set the size of the board
    rect = pygame.Rect(0, 0, board_size, board_size)
    pygame.draw.rect(window, (0, 0, 0), rect, 3)

    box_size = board_size // 3  # Set the size of the box
    for y in range(3):
        for x in range(3):
            rect = pygame.Rect(x * box_size, y * box_size, box_size, box_size)
            pygame.draw.rect(window, (0, 0, 0), rect, 2)

    cell_size = box_size // 3  # Set the size of single cell
    cell_content_offset = cell_size / 5
    for y, row in enumerate(sudoku):
        for x, num in enumerate(row):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            pygame.draw.rect(window, (0, 0, 0), rect, 1)
            font = pygame.font.Font(
                "Delicious_Handrawn/DeliciousHandrawn-Regular.ttf", 30
            )
            img = font.render(str(num) if num else "", True, (0, 0, 255))
            # rect = img.get_rect()
            # pygame.draw.rect(img, (255,0,0), rect, 1)
            window.blit(
                img,
                (
                    x * cell_size + cell_content_offset * 2,
                    y * cell_size + cell_content_offset,
                ),
            )


if __name__ == "__main__":
    main()
