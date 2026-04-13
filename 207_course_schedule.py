"""
LeetCode 207. Course Schedule

Problem summary:
- You are given the number of courses and a list of prerequisite pairs.
- Return True if it is possible to finish all courses.
"""


class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = [course for course in range(numCourses) if indegree[course] == 0]
        completed = 0
        front = 0

        while front < len(queue):
            course = queue[front]
            front += 1
            completed += 1

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses
