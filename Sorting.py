
class sortAlgo():

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    '''
    Time Complexity: Worst(O(n*n)) Best(0(n))
    Auxiliary Space: O(n) (recursive : call stack)

    In computer graphics, it is popular for its capability 
    to detect a tiny error (like a swap of just two elements) 
    in almost-sorted arrays and fix it with just linear 
    complexity (2n). 
    '''
    def bubble_Sort(self, n=None):
        if n is None:
            n = self.length
        count = False
 
        # Base case
        if n == 1:
            return
        # One pass of bubble sort. After
        # this pass, the largest element
        # is moved (or bubbled) to end.
        for i in range(0,n):
            for j in range(0,n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    yield self.array, [j+1], [], []
                    count =  True
            # Check if any recursion happens or not
            if (not count):
                return
            count = False

    '''
    Time complexity : 0(n*n)
    Space complexity : 0(1)

    not stable if doublon exist

    The selection sort never makes more than O(N) swaps 
    and can be useful when memory write is a costly operation. 
    '''
    def selection_Sort(self):
        # Traverse through all array elements
        for i in range(self.length):
            
            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i+1, self.length):
                yield self.array, [j], [i], [min_idx]

                if self.array[min_idx] > self.array[j]:
                    min_idx = j
                    
            # Swap the found minimum element with
            # the first element       
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
    
    def stable_Selection_Sort(self):
        # Traverse through all array elements
        for i in range(self.length):
    
            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, self.length):
                if self.array[min_idx] > self.array[j]:
                    min_idx = j
    
            # Move minimum element at current i
            key = self.array[min_idx]
            while min_idx > i:
                self.array[min_idx] = self.array[min_idx - 1]
                min_idx -= 1
            self.array[i] = key

    '''
    Time complexity : 0(n*n)
    Space complexity : 0(1)

    stable : yes

    Insertion sort is used when number of elements is small. 
    It can also be useful when input array is almost sorted
    '''
    def insertion_Sort(self):
        # Traverse through 1 to len(arr)
        for i in range(1, self.length):
    
            key = self.array[i]
    
            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i
            while j >= 1 and key < self.array[j - 1] :
                    yield self.array, [i], [j], []

                    self.array[j] = self.array[j - 1]
                    j -= 1

            self.array[j] = key
            yield self.array, [], [i], [j]
    
    '''
    Improve insertion sort : 
    Time complexity : 0(n*log(n))
    Space complexity : 0(1)
    '''

    def binary_Search(self, item, low, high):
        while (low <= high):
            mid = low + (high - low) // 2
            if (item == self.array[mid]):
                return mid + 1
            elif (item > self.array[mid]):
                low = mid + 1
            else:
                high = mid - 1
        return low
      
    def binary_search_recursive(self, val, start, end):
        # we need to distinugish whether we 
        # should insert before or after the 
        # left boundary. imagine [0] is the last 
        # step of the binary search and we need 
        # to decide where to insert -1
        if start == end:
            if self.array[start] > val:
                return start
            else:
                return start+1
    
        # this occurs if we are moving 
        # beyond left's boundary meaning 
        # the left boundary is the least 
        # position to find a number greater than val
        if start > end:
            return start
    
        mid = (start+end)//2
        if self.array[mid] < val:
            return self.binary_search_recursive(val, mid+1, end)
        elif self.array[mid] > val:
            return self.binary_search_recursive(val, start, mid-1)
        else:
            return mid

    def binary_insertion_Sort(self):
        for i in range (self.length): 
            j = i - 1
            selected = self.array[i]
            
            # find location where selected should be inseretd
            loc = self.binary_Search(selected, 0, j)
            
            # Move all elements after location to create space
            while (j >= loc):
                yield self.array, [i], [j + 1], [loc]
                self.array[j + 1] = self.array[j]
                j-=1

            yield self.array, [], [i], [j+1]
            self.array[j + 1] = selected

    '''
    Time complexity : 0(n*log(n))
    Space complexity : 0(1)
    stable : no
    '''
    def partition(self,low,high):
            # Choose the rightmost element as pivot
            pivot = self.array[high]

            # Pointer for greater element
            i = low - 1

            # Traverse through all elements
            # compare each element with pivot
            for j in range(low, high):
                if self.array[j] <= pivot:
                    # If element smaller than pivot is found
                    # swap it with the greater element pointed by i
                    i = i + 1

                    # Swapping element at i with element at j
                    self.array[i],self.array[j] = self.array[j], self.array[i]

            # Swap the pivot element with 
            # the greater element specified by i
            self.array[i+1],self.array[high] = self.array[high], self.array[i+1]

            # Return the position from where partition is done
            return i + 1

    def quick_Sort(self, low = 0, high = -1):

        if(high == -1): high = self.length - 1
        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pivot = self.partition(low,high)

            # Recursive call on the left of pivot
            self.quick_Sort(low, pivot - 1)

            # Recursive call on the right of pivot
            self.quick_Sort(pivot + 1, high)

    '''
    Time complexity : 0(n*log(n))
    Space complexity : 0(n) (recursive call stack)
    '''
    def merge_Sort(self):

        def helper(arr):
            if len(arr) > 1:
                # Finding the mid of the array
                mid = len(arr)//2
        
                # Dividing the array elements
                L, R = arr[:mid], arr[mid:]

                # Sorting the first half
                helper(L)
                # Sorting the second half
                helper(R)
        
                i = j = k = 0
                # Copy data to temp arrays L[] and R[]
                while i < len(L) and j < len(R):
                    if L[i] <= R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    
                    k += 1
        
                # Checking if any element was left
                while i < len(L):
                    arr[k] = L[i]
                    self.array[k] = arr[k]
                    i += 1
                    k += 1
        
                while j < len(R):
                    arr[k] = R[j]
                    self.array[k] = arr[k]
                    j += 1
                    k += 1

        helper(self.array)


