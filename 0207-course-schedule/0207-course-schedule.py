from collections import defaultdict, deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # create an adjacency list to represent the directed graph
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            
        # array to store the number of incoming edges for each node in the graph
        
        indegrees = [0] * numCourses
        for prereq, _ in prerequisites:
            indegrees[prereq] += 1
            
        # add all the nodes with indegree 0 to a queue
        
        queue = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)
                
        # topological sort
        
        while queue:
            course = queue.popleft()
            for prereq in graph[course]:
                indegrees[prereq] -= 1
                if indegrees[prereq] == 0:
                    queue.append(prereq)
                    
        # check if we removed all the courses
        return all(indegree == 0 for indegree in indegrees)