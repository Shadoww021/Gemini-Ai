#Mohammad Mahdi Rajabali
#40211360024
def get_tasks():
    n = int(input("Please enter the number of tasks: "))
    tasks = []
    print("Please enter the rewards for each task: ")
    for i in range(n):
        reward = int(input("Reward for task #{i}: ".format(i=i)))
        tasks.append(reward)
    return tasks

def get_edges():
    edges = []
    print("Please enter the edges in the format of 'i j w' (one per line, enter -1 to finish)")
    while True:
        line = input()
        if line == "-1":
            break
        try:
            i, j, w = map(int, line.split())
            edges.append((i, j, w))
        except ValueError:
            print("Invalid input format. Please use 'i j w'.")
    return edges

def dijkstra(start, n, edges):
    graph = [[] for _ in range(n)]
    for i, j, w in edges:
        graph[i].append((j, w))
        graph[j].append((i, w))

    distances = [float('infinity')] * n
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, curr = heapq.heappop(pq)
        if curr_dist > distances[curr]:
            continue
        for next_node, weight in graph[curr]:
            distance = curr_dist + weight
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(pq, (distance, next_node))

    return distances

def longest_common_substring_length(x, y):
    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]     #dp=Dynamic programng
    max_length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0

    return max_length

def max_profit(time_limit, rewards):
    n = len(rewards)
    tasks_with_data = [(rewards[i], i) for i in range(n)]
    tasks_with_data.sort(reverse=True)

    time_slots = [False] * (time_limit + 1)
    total_profit = 0
    tasks_scheduled = 0

    for reward, _ in tasks_with_data:
        for slot in range(time_limit, -1, -1):
            if not time_slots[slot]:
                time_slots[slot] = True
                total_profit += reward
                tasks_scheduled += 1
                break
        if tasks_scheduled == time_limit:
            break

    return total_profit

import heapq

def main():
    while True:
        print("\n1. Shortest distance from the starting point to other nodes")
        print("2. Longest common substring length")
        print("3. Calculate the maximum profit")
        print("4. Exit")
        choice = input("Please choose an item: ")

        if choice == "1":
            try:
                start = int(input("Please enter the starting node: "))
                n = int(input("Please enter the number of nodes: "))
                edges = get_edges()
                result = dijkstra(start, n, edges)
                print("Shortest distances:", result)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == "2":
            try:
                x = input("Please enter the first string: ")
                y = input("Please enter the second string: ")
                result = longest_common_substring_length(x, y)
                print("Length of longest common substring:", result)
            except Exception:
                print("An error occurred. Please try again.")
        elif choice == "3":
            try:
                time_limit = int(input("Please enter the time limit: "))
                tasks = get_tasks()
                result = max_profit(time_limit, tasks)
                print("Maximum profit:", result)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Wrong choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

#Mohammad Mahdi Rajabali
#40211360024


if 1:
    print('yes')