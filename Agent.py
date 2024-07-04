import os

class CheckPlan:
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

    def read_file(self, check=False, plan=None):
        with open(self.input_file, 'r') as f:
            lines = f.readlines()
            if check:
                lines.insert(1, plan)

            self.plan = list(lines[1].strip())
            self.map = [list(line.strip()) for line in lines[2:]]
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

    def get_uncleaned(self):
        all_uncleaned_cells = set(self.empty_cells)
        start_positions = self.start_positions if self.start_positions else self.empty_cells
        for start in start_positions:
            cleaned_cells = {start}
            pos = start
            for move in self.plan:
                pos = self.move(pos, move)
                cleaned_cells.add(pos)
            uncleaned_cells = [cell for cell in self.empty_cells if cell not in cleaned_cells]
            self.potentially_uncleaned_cells.update(uncleaned_cells)

        return self.potentially_uncleaned_cells

    def solve(self):
        sol = ""
        uncleaned_cells = self.get_uncleaned()
        if len(uncleaned_cells) == 0:
            sol += "GOOD PLAN\n"
        else:
            sol += "BAD PLAN\n"
            for cell in sorted(uncleaned_cells, key=lambda x: (x[1], x[0])):
                sol += "{}, {}\n".format(cell[1], cell[0])
        with open(self.output_file, 'w') as f:
            f.write(sol)

    def check(self):
        uncleaned_cells = self.get_uncleaned()
        if len(uncleaned_cells) == 0:
            return True

        return False


def automatic_grading(start, end):
    failed_files = []
    problem_files = os.listdir('example-problems/')[start:end]
    solution_files = os.listdir('example-solutions/')[start:end]
    my_files = os.listdir('my-solutions/')[start:end]
    counter = 0
    for i in range(len(problem_files)):
        with open(os.path.join('example-solutions/', solution_files[i]), 'r') as f:
            solution = f.readlines()
        with open(os.path.join('my-solutions/', my_files[i]), 'r') as f:
            my_solution = f.readlines()
        if set(my_solution) == set(solution):
            counter += 1
        else:
            print('Test case {} failed'.format(problem_files[i]))
            print('Expected: {}'.format(solution))
            print('Got: {}'.format(my_solution))
            print('-------------------')
            failed_files.append(str(problem_files[i]).split('.')[0].split('_')[1:])
    print('Passed {} out of {}'.format(counter, end - start))
    print('Failed files: {}'.format(failed_files))

def example_submitting():
    start, end = 0, 60
    folder = './example-problems/'
    files = os.listdir(folder)[start:end]
    for file in files:
        cp = CheckPlan(os.path.join(folder, file))
        cp.read_file()
        cp.solve()
    automatic_grading(start, end)

def submitting():
    start, end = 0, 60
    folder = './problems/'
    files = os.listdir(folder)[start:end]
    for file in files:
        cp = CheckPlan(os.path.join(folder, file))
        cp.read_file()
        cp.solve()

if __name__ == '__main__':
    submitting()
