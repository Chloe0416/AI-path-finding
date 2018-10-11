from node import Node


def best_first_search(grid, start, goal):
    current_value = start.value
    current_x = start.x
    current_y = start.y

    parent_x = current_x
    parent_y = current_y

    expanded = [(current_x, current_y)]
    next = [grid[current_x][current_y], current_x, current_y]
    while current_x != goal.x or current_y != goal.y:
        print("(" + str(current_x) + "," + str(current_y) + ")")
        distance = 4
        if current_x + 1 < len(grid) and (parent_x != current_x + 1 or parent_y != current_y) \
                and (current_x + 1, current_y) not in expanded:
            rightdistance = abs(current_value - grid[current_x + 1][current_y])
            if distance > rightdistance:
                distance = rightdistance
                next[0] = grid[current_x + 1][current_y]
                next[1] = current_x + 1
                next[2] = current_y

        if current_y + 1 < len(grid[0]) and (parent_x != current_x or parent_y != current_y+1) \
                and (current_x, current_y + 1) not in expanded:
            downdistance = abs(current_value - grid[current_x][current_y+1])
            if distance > downdistance:
                distance = downdistance
                next[0] = grid[current_x][current_y + 1]
                next[1] = current_x
                next[2] = current_y + 1

        if current_x - 1 >= 0 and (parent_x != current_x-1 or parent_y != current_y) \
                and (current_x - 1, current_y) not in expanded:
            leftdistance = abs(current_value - grid[current_x-1][current_y])
            if distance > leftdistance:
                distance = leftdistance
                next[0] = grid[current_x - 1][current_y]
                next[1] = current_x - 1
                next[2] = current_y

        if current_y - 1 >= 0 and (parent_x != current_x or parent_y != current_y - 1) \
                and (current_x, current_y - 1) not in expanded:
            updistance = abs(current_value - grid[current_x][current_y - 1])
            if distance > updistance:
                next[0] = grid[current_x][current_y - 1]
                next[1] = current_x
                next[2] = current_y - 1

        parent_x = current_x
        parent_y = current_y
        current_value = next[0]
        current_x = next[1]
        current_y = next[2]
        expanded.append((current_x, current_y))


def a_star_search(grid, start, goal):
    current_value = start.value
    current_x = start.x
    current_y = start.y

    parent_x = current_x
    parent_y = current_y
    total_cost = 0
    expanded = [(current_x, current_y)]
    next = [grid[current_x][current_y], current_x, current_y]
    while current_x != goal.x or current_y != goal.y:
        print("(" + str(current_x) + "," + str(current_y) + ")")
        cost = 1000

        if current_x + 1 < len(grid) and (parent_x != current_x+1 or parent_y != current_y) \
                and (current_x + 1, current_y) not in expanded:
            rightdistance = abs(current_value - grid[current_x + 1][current_y])
            g = rightdistance + grid[current_x + 1][current_y]
            if cost > g and rightdistance < 4:
                cost = g
                next[0] = grid[current_x + 1][current_y]
                next[1] = current_x + 1
                next[2] = current_y

        if current_y + 1 < len(grid[0]) and (parent_x != current_x or parent_y != current_y+1) \
                and (current_x, current_y + 1) not in expanded:
            downdistance = abs(current_value - grid[current_x][current_y + 1])
            g = downdistance + grid[current_x][current_y + 1]
            if cost > g and downdistance < 4:
                cost = g
                next[0] = grid[current_x][current_y + 1]
                next[1] = current_x
                next[2] = current_y + 1

        if current_x - 1 >= 0 and (parent_x != current_x-1 or parent_y != current_y) \
                and (current_x - 1, current_y) not in expanded:
            leftdistance = abs(current_value - grid[current_x - 1][current_y])
            g = leftdistance + grid[current_x - 1][current_y]
            if cost > g and leftdistance < 4:
                cost = g
                next[0] = grid[current_x - 1][current_y]
                next[1] = current_x - 1
                next[2] = current_y

        if current_y - 1 >= 0 and (parent_x != current_x or parent_y != current_y-1) \
                and (current_x, current_y - 1) not in expanded:
            updistance = abs(current_value - grid[current_x][current_y - 1])
            g = updistance + grid[current_x][current_y - 1]
            if cost > g and updistance < 4:
                cost = g
                next[0] = grid[current_x][current_y - 1]
                next[1] = current_x
                next[2] = current_y - 1

        parent_x = current_x
        parent_y = current_y
        current_value = next[0]
        current_x = next[1]
        current_y = next[2]
        total_cost += (cost - next[0])
        expanded.append((current_x, current_y))


test_file = open("test_data.txt", "r")
get_size = test_file.readline()
size = int(get_size)

get_location = test_file.readline()
location = []
for i in range(len(get_location)):
    if get_location[i] in "1234567890":
        location.append(int(get_location[i]))

grid = [0] * size
for i in range(size):
    grid[i] = [0] * size
for x in range(size):
    get_location = test_file.readline()
    y = 0
    for j in range(len(get_location)):
        if get_location[j] in "1234567890":
            grid[x][y] = int(get_location[j])
            y += 1

test_file.close()

x1 = location[0]
y1 = location[1]
x2 = location[2]
y2 = location[3]
start = Node(grid[x1][y1], x1, y1)
goal = Node(grid[x2][y2], x2, y2)

print("The path by best first search is : ")
best_first_search(grid, start, goal)
print("(" + str(goal.x) + "," + str(goal.y) + ")\n")

print("The path by A * search is : ")
a_star_search(grid, start, goal)
print("(" + str(goal.x) + "," + str(goal.y) + ")")
