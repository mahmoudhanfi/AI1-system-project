from Agent import CheckPlan
import random
import os
class findPlan:
    def __init__(self, file):

        self.map = None
        self.start_positions = []
        self.plan = None
        self.portals = []
        self.empty_cells = []
        self.cleaned_cells = set()
        self.potentially_uncleaned_cells = set()
        self.input_file = file
        self.output_file = file.replace('problem', 'solution')
        self.output_file = self.output_file.replace('example', 'my')

    def read_file(self):
        with open(self.input_file, 'r') as f:
            lines = f.readlines()
            self.plan = list(lines[1].strip())
            self.map = [list(line.strip()) for line in lines[1:]]
            for i in range(len(self.map)):
                for j in range(len(self.map[0])):
                    if self.map[i][j] == 'S':
                        self.start_positions.append((i, j))
                    elif self.map[i][j] == ' ':
                        self.empty_cells.append((i, j))
                    elif self.map[i][j] == 'P':
                        self.portals.append((i, j))

    def move(self, pos, direction):
        old_pos = pos
        if direction == 'N':
            if pos[0] - 1 >= 0 and self.map[pos[0] - 1][pos[1]] != 'X':
                pos = (pos[0] - 1, pos[1])
        elif direction == 'E':
            if pos[1] + 1 < len(self.map[0]) and self.map[pos[0]][pos[1] + 1] != 'X':
                pos = (pos[0], pos[1] + 1)
        elif direction == 'S':
            if pos[0] + 1 < len(self.map) and self.map[pos[0] + 1][pos[1]] != 'X':
                pos = (pos[0] + 1, pos[1])
        elif direction == 'W':
            if pos[1] - 1 >= 0 and self.map[pos[0]][pos[1] - 1] != 'X':
                pos = (pos[0], pos[1] - 1)

        return self.teleport(pos, old_pos)

    def teleport(self, pos, old_pos):
        if pos in self.portals and pos != old_pos:
            for portal in self.portals:
                if portal != pos:
                    return portal
        return pos

    import random

    def generate_random_plan(self,steps):
        directions = ['N', 'E', 'W', 'S']
        plan = [random.choice(directions) for _ in range(steps)]
        return plan


    def solve(self):
        limit = 100
        while True:
            plan = self.generate_random_plan(limit)
            checker = CheckPlan(self.input_file)
            checker.read_file(check=True, plan=''.join(plan))
            if checker.check():
                sol = plan
                break
            limit += 5
        with open(self.output_file, 'w') as f:
            print(len(sol))
            f.write(''.join(sol))

def automatic_grading(start, end):
    my_files = os.listdir('my-solutions/')[start:end]
    counter = 0
    for file in my_files:
        with open('my-solutions/' + file, 'r') as f:
            lines = f.read()
            counter += len(lines)
    print("Total number of steps for problems {} to {} is: {}".format(start, end, counter))

def example_submitting():
    start, end = 60, 120
    folder = './example-problems/'
    files = os.listdir(folder)[start:end]
    for file in files:
        cp = findPlan(os.path.join(folder, file))
        cp.read_file()
        cp.solve()
    automatic_grading(start, end)


def submitting():
    start, end = 100, 120
    folder = './problems/'
    files = os.listdir(folder)[start:end]
    for file in files:
        cp = findPlan(os.path.join(folder, file))
        cp.read_file()
        cp.solve()
    automatic_grading(start, end)


if __name__ == '__main__':
    submitting()
