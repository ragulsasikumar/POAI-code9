class BlockWorld:
    def __init__(self, blocks):
        self.stacks = [[b] for b in blocks]

    def find_block(self, block):
        for i, stack in enumerate(self.stacks):
            if block in stack:
                return i, stack.index(block)
        return None, None

    def is_clear(self, block):
        stack_i, pos = self.find_block(block)
        return pos == len(self.stacks[stack_i]) - 1

    def move(self, block, destination):
        from_i, from_pos = self.find_block(block)
        if from_i is None:
            return False
        if not self.is_clear(block):
            return False
        if destination == 'table':
            self.stacks.append([block])
            self.stacks[from_i].pop()
            if not self.stacks[from_i]:
                self.stacks.pop(from_i)
            return True
        to_i, to_pos = self.find_block(destination)
        if to_i is None or not self.is_clear(destination):
            return False
        self.stacks[to_i].append(block)
        self.stacks[from_i].pop()
        if not self.stacks[from_i]:
            self.stacks.pop(from_i)
        return True

    def state(self):
        return [stack[:] for stack in self.stacks]

bw = BlockWorld(['A', 'B', 'C'])
bw.move('A', 'table')
bw.move('B', 'A')
bw.move('C', 'B')
print(bw.state())
