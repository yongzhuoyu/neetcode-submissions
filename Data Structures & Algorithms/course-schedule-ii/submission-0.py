class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = []
        indegree = []

        for course in range(numCourses):
            adj_list.append([])
            indegree.append(0)

        for course, prerequisite in prerequisites:
            adj_list[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        order = []

        while queue:
            current_course = queue.popleft()
            #Append course to order 
            order.append(current_course)

            for neighbour in adj_list[current_course]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        #After BFS, check whether order contains numCourses courses 
        if len(order) == numCourses:
            #If every course are processed, return the processing order 
            return order 
        else:
            #Otherwise a cycle exist and we return empty array
            return []