# Review 3/26/24 Mauro Piccininni

# Exam Will be on modules 4-8 (3/28)

# Queue with linked list
#Doubly linked list
    # Node 0 is the head
    # node 1 is the tail
    # I need to keep track of both

#Recursion
    # A problem solving technique that involves breaking a problem into smaller subproblems of the same type
    # This means that they can run directly
# Ex: Fibonacci Numbers using recursion

# Two Ways to think about and/or implement DP Algorithims 
    #Top Down (Memorization)
    #Bottom Up (Tabulation)

# Top-Down (Memorization Visualization) 
    # 1. Start with the original problem
    # 2. Break the problem into smaller subproblems
    # 3. Solve the subproblems
    # 4. Store the results of the subproblems
    # 5. Return the result of the original problem

# Bottom-Up (Tabulation Visualization)
    # 1. Start with the smallest subproblems
    # 2. Solve the smallest subproblems
    # 3. Store the results of the smallest subproblems
    # 4. Solve the next smallest subproblems
    # 5. Store the results of the next smallest subproblems
    # 6. Continue solving and storing results until the original problem is solved
    # 7. Return the result of the original problem

# Greedy Algorithm 
    # A greedy algorithm is an algorithmic strategy that makes the best 
    #optimal choice at each small stage with the hope of finding the global optimum.
    # This means that the algorithm picks the best solution 

#Mod 6
    # Chapter 11: Binary Search
    # Chapter 12: 

# Binary Search Implementation
    # 1. Start with the entire list
    # 2. Find the middle element
    # 3. If the middle element is the target, return the index
    # 4. If the target is less than the middle element, search the left half
    # 5. If the target is greater than the middle element, search the right half
    # 6. Repeat steps 2-5 until the target is found or the list is empty

# Binary Search Example
def BS (array, element, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if array[mid] == element:
            return mid
        if array[mid] < element:
            return BS(array, element, mid+1, end)
        else:
            return BS(array, element, start, mid-1)
        
# The tree of function calls is a single chain of length at most O(log n). 
        # Why log n? 
        #Because the size of the problem is halved at each step.
        # This is the number of ties you can cut n in half before it gets down to 1. 
        # The asymtotic running time is O(log n)

#Quadratic Algorithims 
        # Bubble Sort
            # after x calls, the last x items are sorted
        # Selection Sort
            # after x calls, the first x items are sorted
        # Insertion sort
            # after x calls, the first x items are sorted
            # Idea: Sort as you go
        
# What is the difference between selection sort and insertion sort?
    # Selection sort selects the smallest element and moves it to the front
    # Insertion sort selects the next element and inserts it in the correct position

# Mod 7: Divide and Conquer
    # A problem solving technique that involves breaking a problem into smaller subproblems of the same type
    # This means that they can run directly
    # The subproblems are solved and then combined to solve the original problem
    # The subproblems are solved using recursion
        
        # DiVIDE AND CONQUER IS ONE OF SEVERAL POWERFUL TECHNIQUES FOR ALGORITHIM DESIGN
        
        #Divide
            #Break the problem into smaller subproblems
            #Solve the subproblems
        #Conquer
            #Combine the solutions of the subproblems to solve the original problem
        #Combine
            #Combine the solutions of the subproblems to solve the original problem
        

    # Merge Sort
        # A sorting algorithm that uses the divide and conquer technique
        # The list is divided into two halves
        # The two halves are sorted recursively
        # The sorted halves are merged to produce a single sorted list
        # The base case is when the list has one element
        # The time complexity of merge sort is O(n log n)
        # The space complexity of merge sort is O(n)
        # Merge sort is a stable sorting algorithm
        # Merge sort is not an in-place sorting algorithm
        # Merge sort is a comparison-based sorting algorithm

        # Quicksort
            # A sorting algorithm that uses the divide and conquer technique
            # A pivot element is selected
            # The list is partitioned around the pivot element
            # The two partitions are sorted recursively
            # The base case is when the list has one element
            # The time complexity of quicksort is O(n log n)
            # The space complexity of quicksort is O(log n)
            # Quicksort is an unstable sorting algorithm
            # Quicksort is an in-place sorting algorithm
            # Quicksort is a comparison-based sorting algorithm
        
        #Quicksort time complexity
            # Best case: O(n log n)
            # Average case: O(n log n)
            # Worst case: O(n^2)
        
