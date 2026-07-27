import random
import time
import os

ROWS = 8
COLS = 8

def generate_guaranteed_maze():
    start = (0, 0)
    target = (ROWS - 1, COLS - 1)
    
    while True:
        walls = set()
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) != start and (r, c) != target and random.random() < 0.2:
                    walls.add((r, c))
        
        if has_path(start, target, walls):
            return start, target, walls

def has_path(start, target, walls):
    queue = [start]
    visited = {start}
    
    while queue:
        curr = queue.pop(0)
        if curr == target:
            return True
            
        r, c = curr
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            next_pos = (nr, nc)
            if 0 <= nr < ROWS and 0 <= nc < COLS and next_pos not in walls and next_pos not in visited:
                visited.add(next_pos)
                queue.append(next_pos)
                
    return False

def print_board(pos, target, walls):
    os.system('cls' if os.name == 'nt' else 'clear')
    for r in range(ROWS):
        row_str = ""
        for c in range(COLS):
            cell = (r, c)
            if cell == pos:
                row_str += " 🟡 "
            elif cell == target:
                row_str += " 🍒 "
            elif cell in walls:
                row_str += " 🧱 "
            else:
                row_str += "  · "
        print(row_str)
    print("\n" + "="*25)

def play_game():
    start, target, walls = generate_guaranteed_maze()
    pos = start
    path = [pos]
    
    print("🤖 Random Maze Automated Pac-Man Simulation")
    time.sleep(1)
    
    while pos != target:
        print_board(pos, target, walls)
        time.sleep(0.5)
        
        r, c = pos
        tr, tc = target
        
        possible_moves = [
            (r + 1, c),
            (r, c + 1),
            (r - 1, c),
            (r, c - 1)
        ]
        
        best_move = None
        min_distance = 999
        
        for next_pos in possible_moves:
            nr, nc = next_pos
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if next_pos not in walls:
                    distance = abs(nr - tr) + abs(nc - tc)
                    if distance < min_distance and next_pos not in path:
                        min_distance = distance
                        best_move = next_pos
                        
        if best_move is None:
            for next_pos in possible_moves:
                nr, nc = next_pos
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if next_pos not in walls:
                        best_move = next_pos
                        break
                        
        if best_move is None:
            print("❌ Pac-Man is blocked!")
            break
            
        pos = best_move
        path.append(pos)
        
    print_board(pos, target, walls)
    if pos == target:
        print("🎉 Success! Pac-Man reached the fruit through the random maze!")
    else:
        print("Game Over.")

if __name__ == "__main__":
    play_game()
