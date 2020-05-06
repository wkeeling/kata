from collections import deque


class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def __repr__(self):
        return self.name


class Point:
    def __init__(self, x, y, maze):
        self.name = str((x, y))
        self.x = x
        self.y = y
        self.maze = maze

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @property
    def neighbours(self):
        neighbours = []
        for x in (max(self.x - 1, 0), self.x + 1):
            try:
                v = self.maze[x][self.y]
                if v:
                    p = Point(x, self.y, self.maze)
                    if p not in neighbours:
                        neighbours.append(p)
            except IndexError:
                pass

        for y in (max(self.y - 1, 0), self.y + 1):
            try:
                v = self.maze[self.x][y]
                if v:
                    p = Point(self.x, y, self.maze)
                    if p not in neighbours:
                        neighbours.append(p)
            except IndexError:
                pass

            return neighbours

    def __repr__(self):
        return self.name


class MazePoint:
    def __init__(self, x, y, value, maze):
        self.x = x
        self.y = y
        self.value = value
        self.maze = maze

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return str((self.x, self.y))

    @property
    def neighbours(self):
        neighbours = []
        for x in (max(self.x - 1, 0), self.x + 1):
            try:
                p = self.maze[x][self.y]
                if p.value and p not in neighbours:
                    neighbours.append(p)
            except IndexError:
                pass

        for y in (max(self.y - 1, 0), self.y + 1):
            try:
                p = self.maze[self.x][y]
                if p.value and p not in neighbours:
                    neighbours.append(p)
            except IndexError:
                pass

            return neighbours


def create_tree():
    a = Node('a')
    b = Node('b', parent=a)
    c = Node('c', parent=a)
    a.children.extend([b, c])
    d = Node('d', parent=b)
    e = Node('e', parent=b)
    b.children.extend([d, e])
    f = Node('f', parent=c)
    g = Node('g', parent=c)
    c.children.extend([f, g])

    return a


q = deque()  # Used as a first in, first out queue


def bfs():
    while len(q) > 0:
        # print('Queue contains: {}'.format(q))
        n = q.pop()

        for child in n.neighbours:
            if not hasattr(child, 'visited'):
                print(child)
                q.appendleft(child)

        n.visited = True


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for n in graph[vertex] - set(path):
            if n == goal:
                yield path + [n]
            else:
                queue.append((n, path + [n]))


def test_bfs():
    t = create_tree()

    q.appendleft(t)
    bfs()


def test_maze():
    m = [[1, 0, 1, 1, 1, 1],
         [1, 0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1, 1],
         [1, 1, 1, 0, 1, 1]]

    maze = {}

    for y, v1 in enumerate(m):
        for x, v2 in enumerate(v1):
            neighbours = set()
            current = (x, y, m[y][x])
            try:
                neighbours.add((max(x - 1, 0), y, m[y][max(x - 1, 0)]))
            except IndexError:
                pass
            try:
                neighbours.add((x + 1, y, m[y][x + 1]))
            except IndexError:
                pass
            try:
                neighbours.add((x, y + 1, m[y + 1][x]))
            except IndexError:
                pass
            try:
                neighbours.add((x, max(y - 1, 0), m[max(y - 1, 0)][x]))
            except IndexError:
                pass
            try:
                neighbours.remove(current)
            except KeyError:
                pass

            maze[(x, y, m[y][x])] = neighbours

    print(list(bfs_paths(maze, (0, 0, 1), (5, 3, 1))))
