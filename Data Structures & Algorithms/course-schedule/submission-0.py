class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Create an adjacency list for every course 
        #Create an indegree array filled with zeros 
        adj_list = []
        indegree = []
        for course in range(numCourses):
            adj_list.append([])
            indegree.append(0)

        #Process every [course, prerequisite] pair
        for course, prerequisite in prerequisites:
            #Map the prerequisite to the list of courses that depends on it 
            adj_list[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()

        #Courses with no prerequisite should be processed first 
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        completed_courses = 0 
        while queue:
            #Remove one available course from queue
            current_course = queue.popleft()
            #Increment the count of completed courses 
            completed_courses += 1

            #Iterate through every course that depends on the completed course 
            for neighbour in adj_list[current_course]:
                #Decrease the dependent course indegree 
                indegree[neighbour] -= 1
                #If it becomes 0, add it to queue
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        #Return whether the number of completed courses equal to total number of courses 
        return completed_courses == numCourses
            