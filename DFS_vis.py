import pygame
import random

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Labyrinth algorithm")
pygame.init()

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Spot:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = WHITE
		self.width = width
		self.total_rows = total_rows

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))


def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows)
			grid[i].append(spot)
	grid[0][0].color = BLACK

	for i in range(rows):
		for j in range(rows):
			if random.randint(1,4) == 1:
				grid[i][j].color = BLACK

	grid[random.randint(1,49)][random.randint(1,49)].color = RED
	grid[0][0].color = GREEN

	return grid


def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()



def algorithm(grid, rows, win, width):
	visited = set()
	poss_way = [(0,1), (1,0)]


	start_tick = pygame.time.get_ticks()

	while poss_way:
		curr_search = poss_way.pop()
		x,y = curr_search[0], curr_search[1]

		if grid[x][y].color == BLACK:
			continue
		else:
			if (x,y) in visited:
				continue

			visited.add((x,y))

			grid[x][y].color = GREEN
			draw(win, grid, rows, width)
			pygame.time.wait(10)

			if y > 0 and grid[x][y-1].color != BLACK:
				poss_way.append((x,y-1))
				if grid[x][y-1].color == RED:
					return True

			if x > 0 and grid[x-1][y].color != BLACK:
				poss_way.append((x-1,y))
				if grid[x-1][y].color == RED:
					return True

			if  x < (rows-1) and grid[x+1][y].color != BLACK:
				poss_way.append((x+1,y))	
				if grid[x+1][y].color == RED:
					return True

			if  y < (rows-1) and grid[x][y+1].color != BLACK:
				poss_way.append((x,y+1))
				if grid[x][y+1].color == RED:
					return True


def main(win, width):	
	ROWS = 50
	grid = make_grid(ROWS, width)

	run = True
	found = False

	while run:
		draw(win, grid, ROWS, width)

		if not found:
			found = algorithm(grid, ROWS, win, WIDTH)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False


	pygame.quit()

main(WIN, WIDTH)