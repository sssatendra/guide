questions = [
    {
        "title": "Two Sum",
        "category": "Arrays & Hashing",
        "difficulty": "Easy",
        "explanation": """Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

**Pattern:** Hashing. Instead of checking every pair (O(n²)), we iterate through the array once. For each element `num`, we calculate the `complement = target - num`. If the complement exists in our hash map, we found our pair. Otherwise, we add `num` to the map.""",
        "diagram": """flowchart LR
    A["Start"] --> B{"Calculate Complement: target - nums[i]"}
    B --> C{"Complement in HashMap?"}
    C -->|Yes| D["Return [map[complement], i]"]
    C -->|No| E["Add nums[i] to HashMap"]
    E --> B""",
        "test_cases": [{'input': 'nums = [2,7,11,15], target = 9', 'output': '[0, 1]'}, {'input': 'nums = [3,2,4], target = 6', 'output': '[1, 2]'}, {'input': 'nums = [3,3], target = 6', 'output': '[0, 1]'}],
        "js_code": """function twoSum(nums, target) {
    const map = new Map();
    
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        
        if (map.has(complement)) {
            return [map.get(complement), i];
        }
        
        map.set(nums[i], i);
    }
    
    return []; // No solution found
}""",
        "py_code": """def twoSum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
        
    return []""",
        "solution_explanation": "We iterate through the list exactly once. The hash map allows O(1) lookups. Time Complexity: O(n), Space Complexity: O(n).",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up a Hash Map (or Set) to store elements we have seen so far.<br>2. <strong>Iteration:</strong> Loop through the array one element at a time.<br>3. <strong>Lookup:</strong> For each element, calculate the required complement or check if the element exists in our Map.<br>4. <strong>Match Found:</strong> If found, we have our answer (return the indices or boolean).<br>5. <strong>State Update:</strong> If not found, add the current element to the Map for future lookups.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up a Hash Map (or Set) to store elements we have seen so far.<br>2. <strong>Iteration:</strong> Loop through the array one element at a time.<br>3. <strong>Lookup:</strong> For each element, calculate the required complement or check if the element exists in our Map.<br>4. <strong>Match Found:</strong> If found, we have our answer (return the indices or boolean).<br>5. <strong>State Update:</strong> If not found, add the current element to the Map for future lookups.",
    },
    {
        "title": "Longest Substring Without Repeating Characters",
        "category": "Sliding Window",
        "difficulty": "Medium",
        "explanation": """Given a string `s`, find the length of the longest substring without repeating characters.

**Pattern:** Sliding Window. We use two pointers (`left` and `right`) to represent a window. We expand the window by moving `right`. If we encounter a duplicate character, we shrink the window from the `left` until the duplicate is removed. We use a Set or Map to track characters currently in the window.""",
        "diagram": """flowchart TD
    A["Right Pointer Moves"] --> B{"Char in Set?"}
    B -->|No| C["Add Char to Set, Update Max Length"]
    B -->|Yes| D["Remove Char at Left Pointer, Move Left++"]
    C --> A
    D --> B""",
        "test_cases": [{'input': "s = 'abcabcbb'", 'output': "3 ('abc')"}, {'input': "s = 'bbbbb'", 'output': "1 ('b')"}, {'input': "s = 'pwwkew'", 'output': "3 ('wke')"}],
        "js_code": """function lengthOfLongestSubstring(s) {
    const set = new Set();
    let left = 0;
    let maxLength = 0;
    
    for (let right = 0; right < s.length; right++) {
        while (set.has(s[right])) {
            set.delete(s[left]);
            left++;
        }
        set.add(s[right]);
        maxLength = Math.max(maxLength, right - left + 1);
    }
    
    return maxLength;
}""",
        "py_code": """def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
        
    return max_length""",
        "solution_explanation": "Both pointers move from left to right at most once, giving an O(n) time complexity. Space complexity is O(min(n, m)) where m is the size of the charset (e.g., 26 for letters).",
        "js_walkthrough": "1. <strong>Window Setup:</strong> Initialize `left` and `right` pointers at the beginning. Set up state variables (like current sum or distinct characters).<br>2. <strong>Expand Window:</strong> Advance the `right` pointer to include new elements into the window.<br>3. <strong>Shrink Window:</strong> If the window condition becomes invalid, advance the `left` pointer to shrink the window until it's valid again.<br>4. <strong>Track Optimal:</strong> At each valid step, update the max or min window size found so far.<br>5. <strong>Result:</strong> Return the optimal window measurement.",
        "py_walkthrough": "1. <strong>Window Setup:</strong> Initialize `left` and `right` pointers at the beginning. Set up state variables (like current sum or distinct characters).<br>2. <strong>Expand Window:</strong> Advance the `right` pointer to include new elements into the window.<br>3. <strong>Shrink Window:</strong> If the window condition becomes invalid, advance the `left` pointer to shrink the window until it's valid again.<br>4. <strong>Track Optimal:</strong> At each valid step, update the max or min window size found so far.<br>5. <strong>Result:</strong> Return the optimal window measurement.",
    },
    {
        "title": "Merge Intervals",
        "category": "Arrays & Sorting",
        "difficulty": "Medium",
        "explanation": """Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

**Pattern:** Sorting. First, sort the intervals by their start times. Then, iterate through them. If the current interval's start time is less than or equal to the previous interval's end time, they overlap. We merge them by updating the previous interval's end time to the maximum of both.""",
        "diagram": """flowchart LR
    A["Sort Intervals by Start Time"] --> B["Push first interval to merged array"]
    B --> C{"Current start <= Last merged end?"}
    C -->|"Yes: Overlap"| D["Update Last merged end = MAX(ends)"]
    C -->|"No: Disjoint"| E["Push current to merged array"]
    D --> F["Next Interval"]
    E --> F
    F --> C""",
        "test_cases": [{'input': 'intervals = [[1,3],[2,6],[8,10],[15,18]]', 'output': '[[1,6],[8,10],[15,18]]'}, {'input': 'intervals = [[1,4],[4,5]]', 'output': '[[1,5]]'}],
        "js_code": """function merge(intervals) {
    if (intervals.length <= 1) return intervals;
    
    // Sort by start time
    intervals.sort((a, b) => a[0] - b[0]);
    
    const merged = [intervals[0]];
    
    for (let i = 1; i < intervals.length; i++) {
        const current = intervals[i];
        const lastMerged = merged[merged.length - 1];
        
        if (current[0] <= lastMerged[1]) {
            // Overlapping intervals, update the end
            lastMerged[1] = Math.max(lastMerged[1], current[1]);
        } else {
            // Non-overlapping, push to result
            merged.push(current);
        }
    }
    
    return merged;
}""",
        "py_code": """def merge(intervals):
    if not intervals:
        return []
        
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_merged = merged[-1]
        
        if current[0] <= last_merged[1]:
            # Overlap: update end time
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # Disjoint: add new interval
            merged.append(current)
            
    return merged""",
        "solution_explanation": "Time Complexity is O(n log n) due to sorting. The iteration takes O(n). Space Complexity is O(n) to store the merged intervals or O(1) if sorting in place.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "LRU Cache",
        "category": "Design & Data Structures",
        "difficulty": "Medium",
        "explanation": """Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the `LRUCache` class with `get(key)` and `put(key, value)` both running in O(1) average time complexity.

**Pattern:** HashMap + Doubly Linked List. The HashMap provides O(1) access to nodes. The Doubly Linked List allows us to move nodes to the 'most recently used' position (head) or evict from the 'least recently used' position (tail) in O(1) time.""",
        "diagram": """flowchart TD
    A["HashMap: Key -> Node"] -.-> B["Doubly Linked List"]
    B -->|Head| C["Most Recently Used"]
    B -->|Tail| D["Least Recently Used"]
    E["Get/Put operation"] --> F["Move Node to Head"]
    G["Capacity Full"] --> H["Remove Node at Tail"]
    H --> I["Delete Key from HashMap"]""",
        "test_cases": [{'input': 'capacity = 2, put(1,1), put(2,2), get(1), put(3,3), get(2)', 'output': 'null, null, 1, null, -1 (2 was evicted)'}],
        "js_code": """class Node {
    constructor(key, value) {
        this.key = key;
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}

class LRUCache {
    constructor(capacity) {
        this.capacity = capacity;
        this.map = new Map();
        
        // Dummy head and tail
        this.head = new Node(0, 0);
        this.tail = new Node(0, 0);
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }
    
    _remove(node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    
    _add(node) {
        // Add right after dummy head
        node.next = this.head.next;
        node.prev = this.head;
        this.head.next.prev = node;
        this.head.next = node;
    }
    
    get(key) {
        if (this.map.has(key)) {
            const node = this.map.get(key);
            this._remove(node);
            this._add(node); // Move to front
            return node.value;
        }
        return -1;
    }
    
    put(key, value) {
        if (this.map.has(key)) {
            this._remove(this.map.get(key));
        }
        
        const newNode = new Node(key, value);
        this._add(newNode);
        this.map.set(key, newNode);
        
        if (this.map.size > this.capacity) {
            // Evict LRU from tail
            const lru = this.tail.prev;
            this._remove(lru);
            this.map.delete(lru.key);
        }
    }
}""",
        "py_code": """class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node
        
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right (most recent)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]""",
        "solution_explanation": "By combining a Hash Map with a Doubly Linked List, both `get` and `put` run in true O(1) time complexity. Note: Python's built-in `OrderedDict` can also solve this trivially, but interviewers usually want the manual LL implementation.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Number of Islands",
        "category": "Graphs & DFS",
        "difficulty": "Medium",
        "explanation": """Given an `m x n` 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

**Pattern:** Graph Traversal (DFS/BFS). We iterate through every cell in the grid. When we find a '1', we have found an island. We increment our island count, and trigger a DFS to mark all connected '1's as visited (e.g. turning them to '0') so we don't count them again.""",
        "diagram": """flowchart TD
    A["Iterate through Grid"] --> B{"Cell == '1'?"}
    B -->|Yes| C["Increment Island Count"]
    C --> D["Run DFS to flip connected '1's to '0'"]
    D --> A
    B -->|No| A""",
        "test_cases": [{'input': "grid = [\n  ['1','1','0','0','0'],\n  ['1','1','0','0','0'],\n  ['0','0','1','0','0'],\n  ['0','0','0','1','1']\n]", 'output': '3'}],
        "js_code": """function numIslands(grid) {
    if (!grid || grid.length === 0) return 0;
    
    let count = 0;
    const rows = grid.length;
    const cols = grid[0].length;
    
    const dfs = (r, c) => {
        // Boundary checks + water check
        if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] === '0') {
            return;
        }
        
        // Mark as visited by mutating original grid
        grid[r][c] = '0';
        
        // Visit all 4 directions
        dfs(r - 1, c); // up
        dfs(r + 1, c); // down
        dfs(r, c - 1); // left
        dfs(r, c + 1); // right
    };
    
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === '1') {
                count++;
                dfs(r, c);
            }
        }
    }
    
    return count;
}""",
        "py_code": """def numIslands(grid):
    if not grid:
        return 0
        
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
            return
            
        grid[r][c] = "0"
        
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)
        
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)
                
    return islands""",
        "solution_explanation": "Time Complexity: O(M * N) where M is rows and N is cols, because we visit every cell at least once. Space Complexity: worst case O(M * N) call stack size in case the grid is filled entirely with lands.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Reverse Linked List",
        "category": "Linked Lists",
        "difficulty": "Easy",
        "explanation": """Given the `head` of a singly linked list, reverse the list, and return the reversed list.

**Pattern:** Iterative Pointer Manipulation. We maintain three pointers: `prev`, `curr`, and `next`. As we iterate, we save `next`, point `curr.next` to `prev`, and shift both `prev` and `curr` forward.""",
        "diagram": """flowchart LR
    A["Prev: null"] -.-> B["Curr: 1"]
    B --> C["Next: 2"]
    C --> D["3"]
    B -.->|"curr.next = prev"| A
    style B stroke:#6366f1,stroke-width:2px""",
        "test_cases": [{'input': 'head = [1,2,3,4,5]', 'output': '[5,4,3,2,1]'}, {'input': 'head = [1,2]', 'output': '[2,1]'}],
        "js_code": """function reverseList(head) {
    let prev = null;
    let curr = head;
    
    while (curr !== null) {
        let nextTemp = curr.next; // Store next node
        curr.next = prev;         // Reverse the link
        prev = curr;              // Move prev forward
        curr = nextTemp;          // Move curr forward
    }
    
    return prev; // New head
}""",
        "py_code": """def reverseList(head):
    prev, curr = None, head
    
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    return prev""",
        "solution_explanation": "Time Complexity: O(N) since we touch every node once. Space Complexity: O(1) as we are only using pointers.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Valid Parentheses",
        "category": "Stack",
        "difficulty": "Easy",
        "explanation": """Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid. A valid string must close brackets in the correct order.

**Pattern:** Stack. Push opening brackets to a stack. When encountering a closing bracket, pop the top of the stack and check if it matches the corresponding opening bracket.""",
        "diagram": """flowchart TD
    A["Read Char"] --> B{"Is Opening Bracket?"}
    B -->|Yes| C["Push to Stack"]
    B -->|No| D["Pop Stack"]
    D --> E{"Matches Closing Bracket?"}
    E -->|No| F["Return False"]
    E -->|Yes| A""",
        "test_cases": [{'input': "s = '()[]{}'", 'output': 'true'}, {'input': "s = '(]'", 'output': 'false'}, {'input': "s = '([)]'", 'output': 'false'}],
        "js_code": """function isValid(s) {
    const stack = [];
    const map = {
        ')': '(',
        '}': '{',
        ']': '['
    };
    
    for (let i = 0; i < s.length; i++) {
        const char = s[i];
        
        if (map[char]) {
            // It's a closing bracket
            const topElement = stack.length === 0 ? '#' : stack.pop();
            if (topElement !== map[char]) {
                return false;
            }
        } else {
            // It's an opening bracket
            stack.push(char);
        }
    }
    
    return stack.length === 0;
}""",
        "py_code": """def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
            
    return not stack""",
        "solution_explanation": "Time Complexity: O(N). Space Complexity: O(N) worst case if all characters are opening brackets.",
        "js_walkthrough": "1. <strong>Stack Initialization:</strong> Create an empty array to act as a stack.<br>2. <strong>Iteration:</strong> Loop through the elements or characters of the input.<br>3. <strong>Push/Pop Logic:</strong> Depending on the problem, push items onto the stack. If a condition is met (like a matching closing bracket or a greater element), pop from the stack.<br>4. <strong>Evaluation:</strong> Process the popped elements to build the result.<br>5. <strong>Final Check:</strong> Return the result, or check if the stack is completely empty (for validation problems).",
        "py_walkthrough": "1. <strong>Stack Initialization:</strong> Create an empty array to act as a stack.<br>2. <strong>Iteration:</strong> Loop through the elements or characters of the input.<br>3. <strong>Push/Pop Logic:</strong> Depending on the problem, push items onto the stack. If a condition is met (like a matching closing bracket or a greater element), pop from the stack.<br>4. <strong>Evaluation:</strong> Process the popped elements to build the result.<br>5. <strong>Final Check:</strong> Return the result, or check if the stack is completely empty (for validation problems).",
    },
    {
        "title": "Validate Binary Search Tree",
        "category": "Trees",
        "difficulty": "Medium",
        "explanation": """Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST means left subtrees contain only nodes strictly less than the parent, and right subtrees contain nodes strictly greater.

**Pattern:** Recursive DFS with Range Validation. We pass down a `min` and `max` bound. At every node, we check if `min < node.val < max`. When branching left, the `max` becomes the parent's value. When branching right, the `min` becomes the parent's value.""",
        "diagram": """flowchart TD
    A["DFS Node"] --> B{"min < val < max ?"}
    B -->|No| C["Return False"]
    B -->|Yes| D["DFS Left: Update Max = val"]
    B -->|Yes| E["DFS Right: Update Min = val"]""",
        "test_cases": [{'input': 'root = [2,1,3]', 'output': 'true'}, {'input': 'root = [5,1,4,null,null,3,6]', 'output': 'false'}],
        "js_code": """function isValidBST(root) {
    function validate(node, min, max) {
        if (node === null) return true;
        
        if ((min !== null && node.val <= min) || 
            (max !== null && node.val >= max)) {
            return false;
        }
        
        return validate(node.left, min, node.val) && 
               validate(node.right, node.val, max);
    }
    
    return validate(root, null, null);
}""",
        "py_code": """def isValidBST(root):
    def validate(node, low, high):
        if not node:
            return True
            
        if node.val <= low or node.val >= high:
            return False
            
        return (validate(node.left, low, node.val) and 
                validate(node.right, node.val, high))
                
    return validate(root, float('-inf'), float('inf'))""",
        "solution_explanation": "Time Complexity: O(N) because we visit each node exactly once. Space Complexity: O(H) where H is the height of the tree (due to the recursive call stack).",
        "js_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
        "py_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
    },
    {
        "title": "Climbing Stairs",
        "category": "Dynamic Programming",
        "difficulty": "Easy",
        "explanation": """You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Pattern:** Fibonacci Sequence / Bottom-Up DP. The number of ways to reach step `n` is the sum of ways to reach step `n-1` and step `n-2`. Instead of an O(N) array, we only need to keep track of the last two calculated steps to optimize space to O(1).""",
        "diagram": """flowchart LR
    A["Step 1: 1 way"] --> B["Step 2: 2 ways"]
    B --> C["Step 3: 1+2 = 3 ways"]
    C --> D["Step 4: 2+3 = 5 ways"]""",
        "test_cases": [{'input': 'n = 2', 'output': '2'}, {'input': 'n = 3', 'output': '3'}, {'input': 'n = 5', 'output': '8'}],
        "js_code": """function climbStairs(n) {
    if (n <= 2) return n;
    
    let oneStepBefore = 2;
    let twoStepsBefore = 1;
    let allWays = 0;
    
    for (let i = 3; i <= n; i++) {
        allWays = oneStepBefore + twoStepsBefore;
        twoStepsBefore = oneStepBefore;
        oneStepBefore = allWays;
    }
    
    return allWays;
}""",
        "py_code": """def climbStairs(n: int) -> int:
    if n <= 2:
        return n
        
    one, two = 1, 1
    
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
        
    return one""",
        "solution_explanation": "Time Complexity: O(N). Space Complexity: O(1) since we only use two pointers instead of a full DP array.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Top K Frequent Elements",
        "category": "Heaps & Bucket Sort",
        "difficulty": "Medium",
        "explanation": """Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

**Pattern:** Bucket Sort. After counting the frequency of each element using a Map, we create an array of 'buckets' where the index represents the frequency, and the value is a list of elements with that frequency. Then we scan from the highest frequency downwards.""",
        "diagram": """flowchart TD
    A["Count Frequencies"] --> B["Array of Buckets"]
    B --> C["Index = Frequency, Value = [Nums]"]
    C --> D["Iterate Backwards from Length to 0"]
    D --> E["Collect K elements"]""",
        "test_cases": [{'input': 'nums = [1,1,1,2,2,3], k = 2', 'output': '[1, 2]'}, {'input': 'nums = [1], k = 1', 'output': '[1]'}],
        "js_code": """function topKFrequent(nums, k) {
    const count = new Map();
    for (const num of nums) {
        count.set(num, (count.get(num) || 0) + 1);
    }
    
    const buckets = Array(nums.length + 1).fill().map(() => []);
    
    for (const [num, freq] of count.entries()) {
        buckets[freq].push(num);
    }
    
    const result = [];
    for (let i = buckets.length - 1; i >= 0; i--) {
        if (buckets[i].length > 0) {
            result.push(...buckets[i]);
            if (result.length >= k) {
                return result.slice(0, k);
            }
        }
    }
}""",
        "py_code": """def topKFrequent(nums, k):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        
    # Buckets: index = frequency
    freq = [[] for i in range(len(nums) + 1)]
    for num, c in count.items():
        freq[c].append(num)
        
    res = []
    # Iterate from max frequency to 0
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res""",
        "solution_explanation": "By using Bucket Sort, we achieve O(N) Time Complexity. Sorting would have taken O(N log N). Using a Min-Heap takes O(N log K). Space Complexity is O(N).",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Best Time to Buy and Sell Stock",
        "category": "Arrays",
        "difficulty": "Easy",
        "explanation": """You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

**Pattern:** Sliding Window / Two Pointers. Keep track of the lowest price seen so far (`min_price`). For every subsequent price, calculate the potential profit (`price - min_price`) and update `max_profit` if it's larger.""",
        "diagram": """flowchart LR
    A["Initialize min_price = inf, max_profit = 0"] --> B["Iterate through prices"]
    B --> C{"price < min_price?"}
    C -->|Yes| D["min_price = price"]
    C -->|No| E["max_profit = MAX(max_profit, price - min_price)"]
    D --> B
    E --> B""",
        "test_cases": [{'input': 'prices = [7,1,5,3,6,4]', 'output': '5 (Buy at 1, Sell at 6)'}, {'input': 'prices = [7,6,4,3,1]', 'output': '0 (No profit possible)'}],
        "js_code": """function maxProfit(prices) {
    let minPrice = Infinity;
    let maxProfit = 0;
    
    for (let i = 0; i < prices.length; i++) {
        if (prices[i] < minPrice) {
            minPrice = prices[i];
        } else if (prices[i] - minPrice > maxProfit) {
            maxProfit = prices[i] - minPrice;
        }
    }
    
    return maxProfit;
}""",
        "py_code": """def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
            
    return max_profit""",
        "solution_explanation": "Time Complexity: O(N) since we iterate through the prices array exactly once. Space Complexity: O(1) as we only use two variables for state.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Contains Duplicate",
        "category": "Arrays & Hashing",
        "difficulty": "Easy",
        "explanation": """Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

**Pattern:** Hashing. Use a HashSet to keep track of seen elements. If we encounter an element already in the HashSet, we found a duplicate.""",
        "diagram": """flowchart TD
    A["Iterate Array"] --> B{"Element in HashSet?"}
    B -->|Yes| C["Return True"]
    B -->|No| D["Add Element to HashSet"]
    D --> A
    A -.-> E["Loop Ends -> Return False"]""",
        "test_cases": [{'input': 'nums = [1,2,3,1]', 'output': 'true'}, {'input': 'nums = [1,2,3,4]', 'output': 'false'}],
        "js_code": """function containsDuplicate(nums) {
    const seen = new Set();
    
    for (const num of nums) {
        if (seen.has(num)) {
            return true;
        }
        seen.add(num);
    }
    
    return false;
}""",
        "py_code": """def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# One-liner alternative:
# return len(set(nums)) != len(nums)""",
        "solution_explanation": "Time Complexity: O(N) because adding to/searching in a Set takes O(1) on average. Space Complexity: O(N) worst case if there are no duplicates.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up a Hash Map (or Set) to store elements we have seen so far.<br>2. <strong>Iteration:</strong> Loop through the array one element at a time.<br>3. <strong>Lookup:</strong> For each element, calculate the required complement or check if the element exists in our Map.<br>4. <strong>Match Found:</strong> If found, we have our answer (return the indices or boolean).<br>5. <strong>State Update:</strong> If not found, add the current element to the Map for future lookups.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up a Hash Map (or Set) to store elements we have seen so far.<br>2. <strong>Iteration:</strong> Loop through the array one element at a time.<br>3. <strong>Lookup:</strong> For each element, calculate the required complement or check if the element exists in our Map.<br>4. <strong>Match Found:</strong> If found, we have our answer (return the indices or boolean).<br>5. <strong>State Update:</strong> If not found, add the current element to the Map for future lookups.",
    },
    {
        "title": "Product of Array Except Self",
        "category": "Arrays",
        "difficulty": "Medium",
        "explanation": """Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. You must write an algorithm that runs in O(n) time and without using the division operation.

**Pattern:** Prefix & Suffix Products. Calculate the product of all elements to the left of `i` and multiply it by the product of all elements to the right of `i`.""",
        "diagram": """flowchart LR
    A["Array: [1, 2, 3, 4]"] --> B["Left Products: [1, 1, 2, 6]"]
    A --> C["Right Products: [24, 12, 4, 1]"]
    B --> D["Result: [24, 12, 8, 6]"]
    C --> D""",
        "test_cases": [{'input': 'nums = [1,2,3,4]', 'output': '[24,12,8,6]'}, {'input': 'nums = [-1,1,0,-3,3]', 'output': '[0,0,9,0,0]'}],
        "js_code": """function productExceptSelf(nums) {
    const n = nums.length;
    const result = new Array(n).fill(1);
    
    let leftProduct = 1;
    for (let i = 0; i < n; i++) {
        result[i] = leftProduct;
        leftProduct *= nums[i];
    }
    
    let rightProduct = 1;
    for (let i = n - 1; i >= 0; i--) {
        result[i] *= rightProduct;
        rightProduct *= nums[i];
    }
    
    return result;
}""",
        "py_code": """def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
        
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
        
    return result""",
        "solution_explanation": "Time Complexity: O(N) with two passes. Space Complexity: O(1) extra space (excluding the output array).",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Maximum Subarray",
        "category": "Arrays / DP",
        "difficulty": "Medium",
        "explanation": """Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

**Pattern:** Kadane's Algorithm. We maintain a running sum. If the running sum ever dips below 0, it is actively hurting our subarray total, so we reset it to 0.""",
        "diagram": """flowchart TD
    A["Iterate Array"] --> B["current_sum += num"]
    B --> C["max_sum = MAX(max_sum, current_sum)"]
    C --> D{"current_sum < 0?"}
    D -->|Yes| E["current_sum = 0"]
    D -->|No| A
    E --> A""",
        "test_cases": [{'input': 'nums = [-2,1,-3,4,-1,2,1,-5,4]', 'output': '6 ([4,-1,2,1])'}, {'input': 'nums = [1]', 'output': '1'}],
        "js_code": """function maxSubArray(nums) {
    let maxSum = nums[0];
    let currentSum = 0;
    
    for (let i = 0; i < nums.length; i++) {
        if (currentSum < 0) {
            currentSum = 0;
        }
        currentSum += nums[i];
        maxSum = Math.max(maxSum, currentSum);
    }
    
    return maxSum;
}""",
        "py_code": """def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = 0
    
    for num in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += num
        max_sum = max(max_sum, current_sum)
        
    return max_sum""",
        "solution_explanation": "Time Complexity: O(N). Space Complexity: O(1) since we only maintain two sum variables.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Maximum Product Subarray",
        "category": "Arrays / DP",
        "difficulty": "Medium",
        "explanation": """Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

**Pattern:** DP tracking Min & Max. Because multiplying two negative numbers yields a positive, we must track BOTH the running minimum product and running maximum product at each step.""",
        "diagram": """flowchart LR
    A["Current Element"] --> B["Temp Max = MAX(n, n * max, n * min)"]
    A --> C["Min = MIN(n, n * max, n * min)"]
    B --> D["Max = Temp Max"]
    D --> E["Global Max = MAX(Global Max, Max)"]""",
        "test_cases": [{'input': 'nums = [2,3,-2,4]', 'output': '6 ([2,3])'}, {'input': 'nums = [-2,0,-1]', 'output': '0'}],
        "js_code": """function maxProduct(nums) {
    let res = Math.max(...nums);
    let curMin = 1, curMax = 1;
    
    for (let n of nums) {
        if (n === 0) {
            curMin = 1;
            curMax = 1;
            continue;
        }
        let temp = curMax * n;
        curMax = Math.max(n * curMax, n * curMin, n);
        curMin = Math.min(temp, n * curMin, n);
        res = Math.max(res, curMax);
    }
    return res;
}""",
        "py_code": """def maxProduct(nums):
    res = max(nums)
    curMin, curMax = 1, 1
    
    for n in nums:
        if n == 0:
            curMin, curMax = 1, 1
            continue
            
        temp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(temp, n * curMin, n)
        res = max(res, curMax)
        
    return res""",
        "solution_explanation": "Time Complexity: O(N). Space Complexity: O(1).",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Find Minimum in Rotated Sorted Array",
        "category": "Binary Search",
        "difficulty": "Medium",
        "explanation": """Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. Find the minimum element in O(log n) time.

**Pattern:** Binary Search. If the `mid` element is greater than the `right` element, the minimum must be to the right (the array drops off). Otherwise, the minimum is at `mid` or to the left.""",
        "diagram": """flowchart TD
    A["left, right = 0, n-1"] --> B{"left < right?"}
    B -->|Yes| C["mid = (left + right) / 2"]
    C --> D{"nums[mid] > nums[right]?"}
    D -->|Yes| E["left = mid + 1"]
    D -->|No| F["right = mid"]
    E --> B
    F --> B
    B -->|No| G["Return nums[left]"]""",
        "test_cases": [{'input': 'nums = [3,4,5,1,2]', 'output': '1'}, {'input': 'nums = [4,5,6,7,0,1,2]', 'output': '0'}],
        "js_code": """function findMin(nums) {
    let left = 0;
    let right = nums.length - 1;
    
    while (left < right) {
        let mid = Math.floor((left + right) / 2);
        
        if (nums[mid] > nums[right]) {
            // Minimum is to the right
            left = mid + 1;
        } else {
            // Minimum is at mid or to the left
            right = mid;
        }
    }
    
    return nums[left];
}""",
        "py_code": """def findMin(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
            
    return nums[left]""",
        "solution_explanation": "Time Complexity: O(log N) due to binary search space halving. Space Complexity: O(1).",
        "js_walkthrough": "1. <strong>Boundary Setup:</strong> Set `left = 0` and `right = length - 1`.<br>2. <strong>Loop:</strong> Use `while (left <= right)`.<br>3. <strong>Midpoint:</strong> Calculate `mid`.<br>4. <strong>Comparison:</strong> If the mid element is the target, return it. If the target is greater, search the right half (`left = mid + 1`). If smaller, search the left half (`right = mid - 1`).<br>5. <strong>Result:</strong> Return -1 if the loop exits without finding the target.",
        "py_walkthrough": "1. <strong>Boundary Setup:</strong> Set `left = 0` and `right = len() - 1`.<br>2. <strong>Loop:</strong> Use `while (left <= right)`.<br>3. <strong>Midpoint:</strong> Calculate `mid`.<br>4. <strong>Comparison:</strong> If the mid element is the target, return it. If the target is greater, search the right half (`left = mid + 1`). If smaller, search the left half (`right = mid - 1`).<br>5. <strong>Result:</strong> Return -1 if the loop exits without finding the target.",
    },
    {
        "title": "Search in Rotated Sorted Array",
        "category": "Binary Search",
        "difficulty": "Medium",
        "explanation": """Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

**Pattern:** Binary Search with Sorted Half check. In any rotated sorted array, splitting it in half will result in at least one strictly sorted half. We check if `target` falls within the bounds of the sorted half. If it does, we search that half. Otherwise, we search the other half.""",
        "diagram": """flowchart TD
    A["Calculate Mid"] --> B{"Is Left Half Sorted?"}
    B -->|Yes| C{"Target in Left Range?"}
    C -->|Yes| D["Search Left"]
    C -->|No| E["Search Right"]
    B -->|No| F{"Target in Right Range?"}
    F -->|Yes| G["Search Right"]
    F -->|No| H["Search Left"]""",
        "test_cases": [{'input': 'nums = [4,5,6,7,0,1,2], target = 0', 'output': '4'}, {'input': 'nums = [4,5,6,7,0,1,2], target = 3', 'output': '-1'}],
        "js_code": """function search(nums, target) {
    let left = 0, right = nums.length - 1;
    
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        
        if (nums[mid] === target) return mid;
        
        // Left sorted portion
        if (nums[left] <= nums[mid]) {
            if (target > nums[mid] || target < nums[left]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        } 
        // Right sorted portion
        else {
            if (target < nums[mid] || target > nums[right]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
    }
    
    return -1;
}""",
        "py_code": """def search(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] == target:
            return mid
            
        # Left sorted portion
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # Right sorted portion
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
                
    return -1""",
        "solution_explanation": "Time Complexity: O(log N). Space Complexity: O(1).",
        "js_walkthrough": "1. <strong>Boundary Setup:</strong> Set `left = 0` and `right = length - 1`.<br>2. <strong>Loop:</strong> Use `while (left <= right)`.<br>3. <strong>Midpoint:</strong> Calculate `mid`.<br>4. <strong>Comparison:</strong> If the mid element is the target, return it. If the target is greater, search the right half (`left = mid + 1`). If smaller, search the left half (`right = mid - 1`).<br>5. <strong>Result:</strong> Return -1 if the loop exits without finding the target.",
        "py_walkthrough": "1. <strong>Boundary Setup:</strong> Set `left = 0` and `right = len() - 1`.<br>2. <strong>Loop:</strong> Use `while (left <= right)`.<br>3. <strong>Midpoint:</strong> Calculate `mid`.<br>4. <strong>Comparison:</strong> If the mid element is the target, return it. If the target is greater, search the right half (`left = mid + 1`). If smaller, search the left half (`right = mid - 1`).<br>5. <strong>Result:</strong> Return -1 if the loop exits without finding the target.",
    },
    {
        "title": "3Sum",
        "category": "Two Pointers",
        "difficulty": "Medium",
        "explanation": """Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that they sum to zero. Notice that the solution set must not contain duplicate triplets.

**Pattern:** Sort + Two Pointers. Sort the array first. Iterate through the array treating each element as a fixed `target = -nums[i]`. Then use a left and right pointer to find a two-sum match. To avoid duplicates, skip identical values.""",
        "diagram": """flowchart TD
    A["Sort Array"] --> B["Iterate i from 0 to n-2"]
    B --> C["Skip duplicate nums[i]"]
    C --> D["left = i+1, right = n-1"]
    D --> E{"Sum == 0?"}
    E -->|Yes| F["Add to results, Skip duplicate left/right"]
    E -->|Too Small| G["left++"]
    E -->|Too Big| H["right--"]""",
        "test_cases": [{'input': 'nums = [-1,0,1,2,-1,-4]', 'output': '[[-1,-1,2],[-1,0,1]]'}, {'input': 'nums = [0,1,1]', 'output': '[]'}],
        "js_code": """function threeSum(nums) {
    nums.sort((a, b) => a - b);
    const res = [];
    
    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue; // Skip duplicates
        
        let l = i + 1;
        let r = nums.length - 1;
        
        while (l < r) {
            const sum = nums[i] + nums[l] + nums[r];
            
            if (sum > 0) {
                r--;
            } else if (sum < 0) {
                l++;
            } else {
                res.push([nums[i], nums[l], nums[r]]);
                l++;
                while (nums[l] === nums[l - 1] && l < r) {
                    l++; // Skip duplicates
                }
            }
        }
    }
    
    return res;
}""",
        "py_code": """def threeSum(nums):
    res = []
    nums.sort()
    
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
            
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res""",
        "solution_explanation": "Time Complexity: O(N^2) due to nested loop and two pointers. Sorting takes O(N log N). Space Complexity: O(1) or O(N) depending on sorting algorithm.",
        "js_walkthrough": "1. <strong>Pointers Setup:</strong> Initialize two pointers, typically `left` at the start and `right` at the end of the array.<br>2. <strong>Iteration:</strong> Use a `while (left < right)` loop to process elements.<br>3. <strong>Condition Check:</strong> Calculate the sum or difference of the elements at the pointers.<br>4. <strong>Update Pointers:</strong> Depending on the result, move the `left` pointer forward or the `right` pointer backward to get closer to the target.<br>5. <strong>Result:</strong> Return the best pair or accumulated result.",
        "py_walkthrough": "1. <strong>Pointers Setup:</strong> Initialize two pointers, typically `left` at the start and `right` at the end of the array.<br>2. <strong>Iteration:</strong> Use a `while (left < right)` loop to process elements.<br>3. <strong>Condition Check:</strong> Calculate the sum or difference of the elements at the pointers.<br>4. <strong>Update Pointers:</strong> Depending on the result, move the `left` pointer forward or the `right` pointer backward to get closer to the target.<br>5. <strong>Result:</strong> Return the best pair or accumulated result.",
    },
    {
        "title": "Container With Most Water",
        "category": "Two Pointers",
        "difficulty": "Medium",
        "explanation": """You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container, such that the container contains the most water.

**Pattern:** Two Pointers. Place pointers at the ends of the array. Area is limited by the shorter line. So, to maximize area, always move the pointer that points to the shorter line inward.""",
        "diagram": """flowchart LR
    A["left = 0, right = n-1"] --> B{"left < right?"}
    B --> C["Area = (right - left) * MIN(heights)"]
    C --> D{"height[left] < height[right]?"}
    D -->|Yes| E["left++"]
    D -->|No| F["right--"]
    E --> B
    F --> B""",
        "test_cases": [{'input': 'height = [1,8,6,2,5,4,8,3,7]', 'output': '49 (between index 1 and 8)'}, {'input': 'height = [1,1]', 'output': '1'}],
        "js_code": """function maxArea(height) {
    let l = 0;
    let r = height.length - 1;
    let res = 0;
    
    while (l < r) {
        const area = (r - l) * Math.min(height[l], height[r]);
        res = Math.max(res, area);
        
        if (height[l] < height[r]) {
            l++;
        } else {
            r--;
        }
    }
    
    return res;
}""",
        "py_code": """def maxArea(height):
    l, r = 0, len(height) - 1
    res = 0
    
    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)
        
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
            
    return res""",
        "solution_explanation": "Time Complexity: O(N). Space Complexity: O(1).",
        "js_walkthrough": "1. <strong>Pointers Setup:</strong> Initialize two pointers, typically `left` at the start and `right` at the end of the array.<br>2. <strong>Iteration:</strong> Use a `while (left < right)` loop to process elements.<br>3. <strong>Condition Check:</strong> Calculate the sum or difference of the elements at the pointers.<br>4. <strong>Update Pointers:</strong> Depending on the result, move the `left` pointer forward or the `right` pointer backward to get closer to the target.<br>5. <strong>Result:</strong> Return the best pair or accumulated result.",
        "py_walkthrough": "1. <strong>Pointers Setup:</strong> Initialize two pointers, typically `left` at the start and `right` at the end of the array.<br>2. <strong>Iteration:</strong> Use a `while (left < right)` loop to process elements.<br>3. <strong>Condition Check:</strong> Calculate the sum or difference of the elements at the pointers.<br>4. <strong>Update Pointers:</strong> Depending on the result, move the `left` pointer forward or the `right` pointer backward to get closer to the target.<br>5. <strong>Result:</strong> Return the best pair or accumulated result.",
    },
    {
        "title": "Minimum Window Substring",
        "category": "Sliding Window",
        "difficulty": "Hard",
        "explanation": """Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string.

**Pattern:** Sliding Window + Hash Map. Track character frequencies of `t`. Expand window by moving `right` until all characters are found (`have == need`). Then shrink from the `left` to minimize the window while still maintaining the condition.""",
        "diagram": """flowchart TD
    A["Expand Right Pointer"] --> B{"Window has all 't' chars?"}
    B -->|No| A
    B -->|Yes| C["Record Window Size"]
    C --> D["Shrink Left Pointer"]
    D --> E{"Still valid window?"}
    E -->|Yes| C
    E -->|No| A""",
        "test_cases": [{'input': "s = 'ADOBECODEBANC', t = 'ABC'", 'output': "'BANC'"}, {'input': "s = 'a', t = 'a'", 'output': "'a'"}],
        "js_code": """function minWindow(s, t) {
    if (t === "") return "";

    let countT = {};
    let window = {};

    for (let c of t) {
        countT[c] = (countT[c] || 0) + 1;
    }

    let have = 0, need = Object.keys(countT).length;
    let res = [-1, -1], resLen = Infinity;
    let l = 0;

    for (let r = 0; r < s.length; r++) {
        let c = s[r];
        window[c] = (window[c] || 0) + 1;

        if (countT[c] && window[c] === countT[c]) {
            have += 1;
        }

        while (have === need) {
            // Update result
            if ((r - l + 1) < resLen) {
                res = [l, r];
                resLen = (r - l + 1);
            }
            // Pop left from window
            let leftChar = s[l];
            window[leftChar] -= 1;
            if (countT[leftChar] && window[leftChar] < countT[leftChar]) {
                have -= 1;
            }
            l += 1;
        }
    }
    return resLen !== Infinity ? s.substring(res[0], res[1] + 1) : "";
}""",
        "py_code": """def minWindow(s: str, t: str) -> str:
    if t == "": return ""
    
    countT, window = {}, {}
    for c in t: countT[c] = 1 + countT.get(c, 0)
        
    have, need = 0, len(countT)
    res, resLen = [-1, -1], float('inf')
    l = 0
    
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)
        
        if c in countT and window[c] == countT[c]:
            have += 1
            
        while have == need:
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = r - l + 1
            
            # Pop left
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
            
    l, r = res
    return s[l:r+1] if resLen != float('inf') else "" """,
        "solution_explanation": "Time Complexity: O(N + M) where N is length of s, M is length of t. Space: O(1) since charset is fixed (ASCII).",
        "js_walkthrough": "1. <strong>Window Setup:</strong> Initialize `left` and `right` pointers at the beginning. Set up state variables (like current sum or distinct characters).<br>2. <strong>Expand Window:</strong> Advance the `right` pointer to include new elements into the window.<br>3. <strong>Shrink Window:</strong> If the window condition becomes invalid, advance the `left` pointer to shrink the window until it's valid again.<br>4. <strong>Track Optimal:</strong> At each valid step, update the max or min window size found so far.<br>5. <strong>Result:</strong> Return the optimal window measurement.",
        "py_walkthrough": "1. <strong>Window Setup:</strong> Initialize `left` and `right` pointers at the beginning. Set up state variables (like current sum or distinct characters).<br>2. <strong>Expand Window:</strong> Advance the `right` pointer to include new elements into the window.<br>3. <strong>Shrink Window:</strong> If the window condition becomes invalid, advance the `left` pointer to shrink the window until it's valid again.<br>4. <strong>Track Optimal:</strong> At each valid step, update the max or min window size found so far.<br>5. <strong>Result:</strong> Return the optimal window measurement.",
    },
    {
        "title": "Valid Anagram",
        "category": "Strings / Hashing",
        "difficulty": "Easy",
        "explanation": """Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

**Pattern:** Character Counting. We can either sort both strings and compare (O(N log N)), or count the frequency of each character in the first string and subtract the frequency for the second string (O(N)). If all counts reach exactly zero, they are anagrams.""",
        "diagram": """flowchart LR
    A["Iterate through 's'"] --> B["Increment count[char]"]
    B --> C["Iterate through 't'"]
    C --> D["Decrement count[char]"]
    D --> E{"Are all counts 0?"}
    E -->|Yes| F["True"]
    E -->|No| G["False"]""",
        "test_cases": [{'input': "s = 'anagram', t = 'nagaram'", 'output': 'true'}, {'input': "s = 'rat', t = 'car'", 'output': 'false'}],
        "js_code": """function isAnagram(s, t) {
    if (s.length !== t.length) return false;
    
    const count = new Array(26).fill(0);
    const base = 'a'.charCodeAt(0);
    
    for (let i = 0; i < s.length; i++) {
        count[s.charCodeAt(i) - base]++;
        count[t.charCodeAt(i) - base]--;
    }
    
    for (let i = 0; i < 26; i++) {
        if (count[i] !== 0) return false;
    }
    
    return true;
}""",
        "py_code": """def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
        
    countS, countT = {}, {}
    
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
        
    return countS == countT
    
# Alternative Pythonic approach:
# from collections import Counter
# return Counter(s) == Counter(t)""",
        "solution_explanation": "Time Complexity: O(N) where N is the length of the string. Space Complexity: O(1) because the size of the character set (26 lowercase English letters) is constant.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Group Anagrams",
        "category": "Strings / Hashing",
        "difficulty": "Medium",
        "explanation": """Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

**Pattern:** Hashing with Custom Keys. Anagrams will have the exact same character counts. So, instead of sorting strings to use as a hash map key (O(K log K)), we can use an array of 26 character counts as the key (O(K)).""",
        "diagram": """flowchart TD
    A["Iterate through 'strs'"] --> B["Create array of size 26 for char counts"]
    B --> C["Count chars in string"]
    C --> D["Convert array to tuple/string key"]
    D --> E["HashMap[key].append(string)"]
    E --> F["Return HashMap values"]""",
        "test_cases": [{'input': "strs = ['eat','tea','tan','ate','nat','bat']", 'output': "[['bat'],['nat','tan'],['ate','eat','tea']]"}, {'input': "strs = ['']", 'output': "[['']]"}],
        "js_code": """function groupAnagrams(strs) {
    const map = new Map();
    
    for (const s of strs) {
        const count = new Array(26).fill(0);
        const base = 'a'.charCodeAt(0);
        
        for (const char of s) {
            count[char.charCodeAt(0) - base]++;
        }
        
        // Convert array to a string key (e.g., '1,0,0,1...')
        const key = count.join(',');
        
        if (!map.has(key)) {
            map.set(key, []);
        }
        map.get(key).push(s);
    }
    
    return Array.from(map.values());
}""",
        "py_code": """from collections import defaultdict

def groupAnagrams(strs):
    ans = defaultdict(list)
    
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
            
        # Lists cannot be dict keys in python, so convert to tuple
        ans[tuple(count)].append(s)
        
    return list(ans.values())""",
        "solution_explanation": "Time Complexity: O(M * N) where M is the number of strings and N is the average length of a string. Space Complexity: O(M * N) to store the result in the hash map.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Valid Palindrome",
        "category": "Strings / Two Pointers",
        "difficulty": "Easy",
        "explanation": """A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

**Pattern:** Two Pointers. Place pointers at the beginning and end of the string. Skip non-alphanumeric characters. If the characters at the left and right pointers don't match, return false. Otherwise, move them inward.""",
        "diagram": """flowchart LR
    A["left = 0, right = n-1"] --> B{"left < right?"}
    B --> C{"Is left/right alphanumeric?"}
    C -->|No| D["Skip inward"]
    C -->|Yes| E{"Match?"}
    E -->|No| F["Return False"]
    E -->|Yes| G["left++, right--"]
    D --> B
    G --> B""",
        "test_cases": [{'input': "s = 'A man, a plan, a canal: Panama'", 'output': 'true'}, {'input': "s = 'race a car'", 'output': 'false'}],
        "js_code": """function isPalindrome(s) {
    let l = 0;
    let r = s.length - 1;
    
    const isAlphanumeric = (char) => {
        return /^[a-zA-Z0-9]+$/.test(char);
    };
    
    while (l < r) {
        while (l < r && !isAlphanumeric(s[l])) l++;
        while (l < r && !isAlphanumeric(s[r])) r--;
        
        if (s[l].toLowerCase() !== s[r].toLowerCase()) {
            return false;
        }
        
        l++;
        r--;
    }
    
    return true;
}""",
        "py_code": """def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
            
        if s[l].lower() != s[r].lower():
            return False
            
        l += 1
        r -= 1
        
    return True""",
        "solution_explanation": "Time Complexity: O(N) where N is the length of the string. Space Complexity: O(1) as we are checking characters in-place without creating a new filtered string.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Longest Palindromic Substring",
        "category": "Strings / Expand Around Center",
        "difficulty": "Medium",
        "explanation": """Given a string `s`, return the longest palindromic substring in `s`.

**Pattern:** Expand Around Center. A palindrome mirrors around its center. The center can be a single character (odd length palindrome) or between two characters (even length). We iterate through each character in the string, treating it as the center, and expand outwards as long as it remains a palindrome.""",
        "diagram": """flowchart TD
    A["Iterate over string 'i'"] --> B["Expand Around Center (Odd: i, i)"]
    A --> C["Expand Around Center (Even: i, i+1)"]
    B --> D["Update Max Palindrome if larger"]
    C --> D
    D --> A""",
        "test_cases": [{'input': "s = 'babad'", 'output': "'bab' or 'aba'"}, {'input': "s = 'cbbd'", 'output': "'bb'"}],
        "js_code": """function longestPalindrome(s) {
    let res = "";
    let resLen = 0;
    
    for (let i = 0; i < s.length; i++) {
        // Odd length
        let l = i, r = i;
        while (l >= 0 && r < s.length && s[l] === s[r]) {
            if ((r - l + 1) > resLen) {
                res = s.substring(l, r + 1);
                resLen = r - l + 1;
            }
            l--; r++;
        }
        
        // Even length
        l = i; r = i + 1;
        while (l >= 0 && r < s.length && s[l] === s[r]) {
            if ((r - l + 1) > resLen) {
                res = s.substring(l, r + 1);
                resLen = r - l + 1;
            }
            l--; r++;
        }
    }
    
    return res;
}""",
        "py_code": """def longestPalindrome(s: str) -> str:
    res = ""
    resLen = 0
    
    for i in range(len(s)):
        # Odd length palindromes
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1
            r += 1
            
        # Even length palindromes
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1
            r += 1
            
    return res""",
        "solution_explanation": "Time Complexity: O(N^2) because expanding around the center can take O(N) time and we do it for each of the N centers. Space Complexity: O(1).",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Palindromic Substrings",
        "category": "Strings / DP",
        "difficulty": "Medium",
        "explanation": """Given a string `s`, return the number of palindromic substrings in it. A string is a palindrome when it reads the same backward as forward.

**Pattern:** Expand Around Center. Similar to Longest Palindromic Substring, we treat each index (and the space between indices) as a center, expand outwards, and increment a counter for every valid palindrome we form.""",
        "diagram": """flowchart LR
    A["Initialize Count = 0"] --> B["Iterate 'i' over string"]
    B --> C["Count += Expand(i, i)"]
    B --> D["Count += Expand(i, i+1)"]
    C --> B
    D --> B""",
        "test_cases": [{'input': "s = 'abc'", 'output': "3 ('a', 'b', 'c')"}, {'input': "s = 'aaa'", 'output': "6 ('a', 'a', 'a', 'aa', 'aa', 'aaa')"}],
        "js_code": """function countSubstrings(s) {
    let count = 0;
    
    const countPali = (l, r) => {
        let res = 0;
        while (l >= 0 && r < s.length && s[l] === s[r]) {
            res++;
            l--;
            r++;
        }
        return res;
    };
    
    for (let i = 0; i < s.length; i++) {
        count += countPali(i, i);     // Odd length
        count += countPali(i, i + 1); // Even length
    }
    
    return count;
}""",
        "py_code": """def countSubstrings(s: str) -> int:
    res = 0
    
    for i in range(len(s)):
        # Odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
            
        # Even length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
            
    return res""",
        "solution_explanation": "Time Complexity: O(N^2) as we do an O(N) expansion at each of the N characters. Space Complexity: O(1).",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Linked List Cycle",
        "category": "Linked Lists / Two Pointers",
        "difficulty": "Easy",
        "explanation": """Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

**Pattern:** Fast and Slow Pointers (Floyd's Tortoise and Hare). Maintain two pointers. The slow pointer moves one step at a time while the fast pointer moves two steps. If there is a cycle, the fast pointer will eventually loop around and meet the slow pointer.""",
        "diagram": """flowchart LR
    A["Slow (1 step)"] -.-> B["Fast (2 steps)"]
    B --> C{"Fast == Slow?"}
    C -->|Yes| D["Cycle Exists (True)"]
    C -->|No| E{"Fast or Fast.next == Null?"}
    E -->|Yes| F["No Cycle (False)"]
    E -->|No| A""",
        "test_cases": [{'input': 'head = [3,2,0,-4], pos = 1', 'output': 'true'}, {'input': 'head = [1,2], pos = 0', 'output': 'true'}, {'input': 'head = [1], pos = -1', 'output': 'false'}],
        "js_code": """function hasCycle(head) {
    if (!head || !head.next) return false;
    
    let slow = head;
    let fast = head;
    
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
        
        if (slow === fast) {
            return true;
        }
    }
    
    return false;
}""",
        "py_code": """def hasCycle(head):
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
            
    return False""",
        "solution_explanation": "Time Complexity: O(N). If no cycle, fast reaches end in N/2. If cycle, fast catches slow in less than N steps. Space Complexity: O(1).",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Merge Two Sorted Lists",
        "category": "Linked Lists",
        "difficulty": "Easy",
        "explanation": """You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list.

**Pattern:** Dummy Node + Two Pointers. Use a dummy node to easily keep track of the head of the new list. Compare the nodes of `list1` and `list2`, append the smaller one to our new list, and move that pointer forward. Finally, append any remaining nodes.""",
        "diagram": """flowchart TD
    A["Dummy Node"] --> B{"L1.val <= L2.val ?"}
    B -->|Yes| C["Tail.next = L1, L1 = L1.next"]
    B -->|No| D["Tail.next = L2, L2 = L2.next"]
    C --> E["Tail = Tail.next"]
    D --> E
    E --> B
    B -.-> F["Append remaining L1 or L2"]""",
        "test_cases": [{'input': 'list1 = [1,2,4], list2 = [1,3,4]', 'output': '[1,1,2,3,4,4]'}, {'input': 'list1 = [], list2 = []', 'output': '[]'}],
        "js_code": """function mergeTwoLists(list1, list2) {
    const dummy = new ListNode();
    let tail = dummy;
    
    while (list1 && list2) {
        if (list1.val < list2.val) {
            tail.next = list1;
            list1 = list1.next;
        } else {
            tail.next = list2;
            list2 = list2.next;
        }
        tail = tail.next;
    }
    
    // Append remaining
    if (list1) tail.next = list1;
    if (list2) tail.next = list2;
    
    return dummy.next;
}""",
        "py_code": """def mergeTwoLists(list1, list2):
    dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
        
    return dummy.next""",
        "solution_explanation": "Time Complexity: O(N + M) where N and M are lengths of the lists. Space Complexity: O(1) as we are only adjusting pointers of existing nodes.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Merge k Sorted Lists",
        "category": "Linked Lists / Heaps",
        "difficulty": "Hard",
        "explanation": """You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

**Pattern:** Divide and Conquer OR Min-Heap. Divide & Conquer repeatedly pairs up lists and merges them using the 'Merge Two Sorted Lists' logic, bringing the total lists from K down to 1. A Min-Heap approach pushes the head of each list into a heap, pops the minimum, and pushes the next node from that list.""",
        "diagram": """flowchart TD
    A["Lists: [L1, L2, L3, L4]"] --> B["Pairwise Merge"]
    B --> C["[Merge(L1, L2), Merge(L3, L4)]"]
    C --> D["[Merged_12, Merged_34]"]
    D --> E["Merge(Merged_12, Merged_34)"]
    E --> F["Final Sorted List"]""",
        "test_cases": [{'input': 'lists = [[1,4,5],[1,3,4],[2,6]]', 'output': '[1,1,2,3,4,4,5,6]'}, {'input': 'lists = []', 'output': '[]'}],
        "js_code": """// Divide and Conquer Approach
function mergeKLists(lists) {
    if (!lists || lists.length === 0) return null;
    
    while (lists.length > 1) {
        const mergedLists = [];
        for (let i = 0; i < lists.length; i += 2) {
            const l1 = lists[i];
            const l2 = (i + 1 < lists.length) ? lists[i + 1] : null;
            mergedLists.push(mergeTwoLists(l1, l2));
        }
        lists = mergedLists;
    }
    
    return lists[0];
}

function mergeTwoLists(l1, l2) {
    let dummy = new ListNode();
    let tail = dummy;
    while (l1 && l2) {
        if (l1.val < l2.val) {
            tail.next = l1; l1 = l1.next;
        } else {
            tail.next = l2; l2 = l2.next;
        }
        tail = tail.next;
    }
    tail.next = l1 || l2;
    return dummy.next;
}""",
        "py_code": """# Min Heap Approach
import heapq

def mergeKLists(lists):
    # Need wrapper because ListNode doesn't support < operator natively
    class Wrapper:
        def __init__(self, node):
            self.node = node
        def __lt__(self, other):
            return self.node.val < other.node.val

    heap = []
    for l in lists:
        if l:
            heapq.heappush(heap, Wrapper(l))
            
    dummy = ListNode()
    curr = dummy
    
    while heap:
        node = heapq.heappop(heap).node
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, Wrapper(node.next))
            
    return dummy.next""",
        "solution_explanation": "Divide & Conquer Time: O(N log K) where K is number of lists, N is total nodes. Space: O(K) lists generated or O(1) if modifying in-place. Min-Heap Time: O(N log K) as heap size never exceeds K. Space: O(K).",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Remove Nth Node From End of List",
        "category": "Linked Lists / Two Pointers",
        "difficulty": "Medium",
        "explanation": """Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

**Pattern:** Two Pointers (Delayed Start). Create a dummy node. Use a `left` and `right` pointer. Move `right` forward by `n` steps. Then move both pointers forward until `right` reaches the end. `left` will now be right before the node we need to remove.""",
        "diagram": """flowchart LR
    A["Dummy"] --> B["1"]
    B --> C["2"]
    C --> D["3"]
    D --> E["4"]
    E --> F["5"]
    G["Right Pointer initially moved N steps ahead"] -.-> E
    H["Left Pointer (starts at Dummy)"] -.-> A
    G -.->|Move both| F
    H -.->|Move both| C
    C -.->|"Delete Next"| E""",
        "test_cases": [{'input': 'head = [1,2,3,4,5], n = 2', 'output': '[1,2,3,5]'}, {'input': 'head = [1], n = 1', 'output': '[]'}],
        "js_code": """function removeNthFromEnd(head, n) {
    const dummy = new ListNode(0, head);
    let left = dummy;
    let right = head;
    
    // Move right pointer n steps ahead
    while (n > 0 && right) {
        right = right.next;
        n -= 1;
    }
    
    // Move both until right reaches end
    while (right) {
        left = left.next;
        right = right.next;
    }
    
    // Delete the node
    left.next = left.next.next;
    
    return dummy.next;
}""",
        "py_code": """def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head
    
    for _ in range(n):
        right = right.next
        
    while right:
        left = left.next
        right = right.next
        
    left.next = left.next.next
    return dummy.next""",
        "solution_explanation": "Time Complexity: O(N) as we traverse the list exactly once. Space Complexity: O(1) as we only allocate pointers.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Reorder List",
        "category": "Linked Lists",
        "difficulty": "Medium",
        "explanation": """You are given the head of a singly linked-list. Reorder it so it alternates between the first half nodes and the reversed second half nodes: `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...`

**Pattern:** Midpoint + Reverse + Merge. 1. Use Fast/Slow pointers to find the middle. 2. Reverse the second half of the list. 3. Merge the two halves alternately.""",
        "diagram": """flowchart TD
    A["Find Middle (Slow/Fast)"] --> B["Reverse Second Half"]
    B --> C["Merge Alternating"]
    C --> D["L1 -> R1 -> L2 -> R2 ..."]""",
        "test_cases": [{'input': 'head = [1,2,3,4]', 'output': '[1,4,2,3]'}, {'input': 'head = [1,2,3,4,5]', 'output': '[1,5,2,4,3]'}],
        "js_code": """function reorderList(head) {
    if (!head || !head.next) return;
    
    // 1. Find middle
    let slow = head;
    let fast = head.next;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }
    
    // 2. Reverse second half
    let second = slow.next;
    slow.next = null; // Sever the first half
    let prev = null;
    while (second) {
        let temp = second.next;
        second.next = prev;
        prev = second;
        second = temp;
    }
    
    // 3. Merge two halves
    let first = head;
    second = prev; // Head of reversed second half
    while (second) {
        let tmp1 = first.next;
        let tmp2 = second.next;
        
        first.next = second;
        second.next = tmp1;
        
        first = tmp1;
        second = tmp2;
    }
}""",
        "py_code": """def reorderList(head):
    if not head: return
    
    # 1. Find middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # 2. Reverse second half
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
        
    # 3. Merge two halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2""",
        "solution_explanation": "Time Complexity: O(N). Finding the middle takes N/2, reversing takes N/2, merging takes N/2. Space Complexity: O(1).",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Invert Binary Tree",
        "category": "Trees",
        "difficulty": "Easy",
        "explanation": """Given the `root` of a binary tree, invert the tree, and return its root.

**Pattern:** DFS / Recursive traversal. For every node, we simply swap its left and right children, then recursively call the invert function on both the new left and right subtrees.""",
        "diagram": """flowchart TD
    A["4"] --> B["2"]
    A --> C["7"]
    B --> D["1"]
    B --> E["3"]
    C --> F["6"]
    C --> G["9"]
    
    A2["4"] --> C2["7"]
    A2 --> B2["2"]
    C2 --> G2["9"]
    C2 --> F2["6"]
    B2 --> E2["3"]
    B2 --> D2["1"]
    
    A -.->|Invert| A2""",
        "test_cases": [{'input': 'root = [4,2,7,1,3,6,9]', 'output': '[4,7,2,9,6,3,1]'}, {'input': 'root = [2,1,3]', 'output': '[2,3,1]'}],
        "js_code": """function invertTree(root) {
    if (root === null) return null;
    
    // Swap the children
    const temp = root.left;
    root.left = root.right;
    root.right = temp;
    
    // Recursively invert subtrees
    invertTree(root.left);
    invertTree(root.right);
    
    return root;
}""",
        "py_code": """def invertTree(root):
    if not root:
        return None
        
    # Swap children
    root.left, root.right = root.right, root.left
    
    # Recurse
    invertTree(root.left)
    invertTree(root.right)
    
    return root""",
        "solution_explanation": "Time Complexity: O(N) because we visit each node exactly once. Space Complexity: O(H) where H is the height of the tree (for the recursion stack). In the worst case (skewed tree), O(N).",
        "js_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
        "py_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
    },
    {
        "title": "Maximum Depth of Binary Tree",
        "category": "Trees",
        "difficulty": "Easy",
        "explanation": """Given the `root` of a binary tree, return its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Pattern:** Depth First Search (DFS). The maximum depth of any node is `1 + max(depth(left_child), depth(right_child))`.""",
        "diagram": """flowchart TD
    A["Root (Depth = 1 + Max(L, R))"] --> B["Left Subtree"]
    A --> C["Right Subtree"]
    B --> D["..."]
    C --> E["..."]""",
        "test_cases": [{'input': 'root = [3,9,20,null,null,15,7]', 'output': '3'}, {'input': 'root = [1,null,2]', 'output': '2'}],
        "js_code": """function maxDepth(root) {
    if (root === null) return 0;
    
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}""",
        "py_code": """def maxDepth(root):
    if not root:
        return 0
        
    return 1 + max(maxDepth(root.left), maxDepth(root.right))""",
        "solution_explanation": "Time Complexity: O(N) because we visit each node once. Space Complexity: O(H) where H is the tree's height for the call stack.",
        "js_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
        "py_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
    },
    {
        "title": "Same Tree",
        "category": "Trees",
        "difficulty": "Easy",
        "explanation": """Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

**Pattern:** Simultaneous DFS. We traverse both trees at the same time. If both current nodes are null, it's valid. If only one is null, or their values differ, it's invalid. If they match, recursively check the left children and right children.""",
        "diagram": """flowchart TD
    A{"Are both nodes null?"} -->|Yes| B["Return True"]
    A -->|No| C{"Is one null or vals differ?"}
    C -->|Yes| D["Return False"]
    C -->|No| E["Recurse: sameTree(left) AND sameTree(right)"]""",
        "test_cases": [{'input': 'p = [1,2,3], q = [1,2,3]', 'output': 'true'}, {'input': 'p = [1,2], q = [1,null,2]', 'output': 'false'}],
        "js_code": """function isSameTree(p, q) {
    if (!p && !q) return true;
    if (!p || !q || p.val !== q.val) return false;
    
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}""",
        "py_code": """def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
        
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)""",
        "solution_explanation": "Time Complexity: O(N) where N is the number of nodes in the smaller tree. Space Complexity: O(H) where H is the height of the smaller tree.",
        "js_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
        "py_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
    },
    {
        "title": "Subtree of Another Tree",
        "category": "Trees",
        "difficulty": "Easy",
        "explanation": """Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

**Pattern:** DFS + Same Tree. For every node in `root`, we check if the tree starting at that node is identical to `subRoot` using the 'Same Tree' logic.""",
        "diagram": """flowchart TD
    A["Iterate through Root nodes"] --> B{"Is SameTree(curr, subRoot)?"}
    B -->|Yes| C["Return True"]
    B -->|No| D["Check left and right subtrees"]
    D --> A""",
        "test_cases": [{'input': 'root = [3,4,5,1,2], subRoot = [4,1,2]', 'output': 'true'}, {'input': 'root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]', 'output': 'false'}],
        "js_code": """function isSubtree(root, subRoot) {
    if (!subRoot) return true;
    if (!root) return false;
    
    if (isSameTree(root, subRoot)) return true;
    
    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
}

function isSameTree(p, q) {
    if (!p && !q) return true;
    if (!p || !q || p.val !== q.val) return false;
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}""",
        "py_code": """def isSubtree(root, subRoot):
    if not subRoot: return True
    if not root: return False
    
    if isSameTree(root, subRoot):
        return True
        
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
    
def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)""",
        "solution_explanation": "Time Complexity: O(M * N) where M is nodes in root and N is nodes in subRoot. For each node in M, we potentially do a full SameTree comparison of size N. Space Complexity: O(H_root + H_subRoot).",
        "js_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
        "py_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
    },
    {
        "title": "Lowest Common Ancestor of a BST",
        "category": "Trees",
        "difficulty": "Medium",
        "explanation": """Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

**Pattern:** BST Properties. In a BST, the left children are smaller and right children are larger. If both `p` and `q` are greater than the current node, the LCA must be in the right subtree. If both are less, it must be in the left. If they split (one is less, one is greater, or one equals the current node), the current node is the LCA.""",
        "diagram": """flowchart TD
    A{"p.val < curr.val AND q.val < curr.val?"} -->|Yes| B["curr = curr.left"]
    A -->|No| C{"p.val > curr.val AND q.val > curr.val?"}
    C -->|Yes| D["curr = curr.right"]
    C -->|No| E["curr is LCA"]""",
        "test_cases": [{'input': 'root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8', 'output': '6'}, {'input': 'root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4', 'output': '2'}],
        "js_code": """function lowestCommonAncestor(root, p, q) {
    let curr = root;
    
    while (curr) {
        if (p.val > curr.val && q.val > curr.val) {
            curr = curr.right;
        } else if (p.val < curr.val && q.val < curr.val) {
            curr = curr.left;
        } else {
            return curr;
        }
    }
    
    return null;
}""",
        "py_code": """def lowestCommonAncestor(root, p, q):
    curr = root
    
    while curr:
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            return curr
            
    return None""",
        "solution_explanation": "Time Complexity: O(H) where H is the height of the tree. In worst case (skewed tree), O(N). Space Complexity: O(1) because we are doing this iteratively without the call stack.",
        "js_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
        "py_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
    },
    {
        "title": "Binary Tree Level Order Traversal",
        "category": "Trees",
        "difficulty": "Medium",
        "explanation": """Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

**Pattern:** Breadth-First Search (BFS). Use a queue. We process nodes level by level. By recording the size of the queue at the start of the loop, we know exactly how many nodes belong to the current level.""",
        "diagram": """flowchart TD
    A["Initialize Queue with Root"] --> B{"Is Queue Empty?"}
    B -->|No| C["Get queue length (level size)"]
    C --> D["For each node in level: append val, enqueue children"]
    D --> E["Append level array to result"]
    E --> B
    B -->|Yes| F["Return Result"]""",
        "test_cases": [{'input': 'root = [3,9,20,null,null,15,7]', 'output': '[[3],[9,20],[15,7]]'}, {'input': 'root = [1]', 'output': '[[1]]'}],
        "js_code": """function levelOrder(root) {
    const res = [];
    if (!root) return res;
    
    const queue = [root];
    
    while (queue.length > 0) {
        const levelSize = queue.length;
        const currentLevel = [];
        
        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift(); // O(N) shift is slow in JS, but acceptable here. Can use an index pointer for true O(1)
            currentLevel.push(node.val);
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        
        res.push(currentLevel);
    }
    
    return res;
}""",
        "py_code": """from collections import deque

def levelOrder(root):
    res = []
    if not root:
        return res
        
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        res.append(current_level)
        
    return res""",
        "solution_explanation": "Time Complexity: O(N) since each node is processed exactly once. Space Complexity: O(N) because the bottom level of a binary tree can contain up to N/2 nodes, which sit in the queue.",
        "js_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
        "py_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
    },
    {
        "title": "Validate Binary Search Tree",
        "category": "Trees",
        "difficulty": "Medium",
        "explanation": """Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

**Pattern:** DFS with Boundaries. Every node in a BST has strict upper and lower bounds. As we traverse down the tree, we update these bounds. Going left updates the maximum bound. Going right updates the minimum bound.""",
        "diagram": """flowchart TD
    A["Node(val)"] --> B["Validate Left: (min, val)"]
    A --> C["Validate Right: (val, max)"]
    B --> D{"is val < parent?"}
    C --> E{"is val > parent?"}""",
        "test_cases": [{'input': 'root = [2,1,3]', 'output': 'true'}, {'input': 'root = [5,1,4,null,null,3,6]', 'output': 'false'}],
        "js_code": """function isValidBST(root) {
    const valid = (node, left, right) => {
        if (!node) return true;
        
        if (!(node.val > left && node.val < right)) {
            return false;
        }
        
        return valid(node.left, left, node.val) && 
               valid(node.right, node.val, right);
    };
    
    return valid(root, -Infinity, Infinity);
}""",
        "py_code": """def isValidBST(root):
    def valid(node, left, right):
        if not node:
            return True
            
        if not (left < node.val < right):
            return False
            
        return valid(node.left, left, node.val) and \
               valid(node.right, node.val, right)
               
    return valid(root, float('-inf'), float('inf'))""",
        "solution_explanation": "Time Complexity: O(N) to visit every node once. Space Complexity: O(H) for the call stack, where H is the height of the tree.",
        "js_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
        "py_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
    },
    {
        "title": "Kth Smallest Element in a BST",
        "category": "Trees",
        "difficulty": "Medium",
        "explanation": """Given the `root` of a binary search tree, and an integer `k`, return the `kth` smallest value (1-indexed) of all the values of the nodes in the tree.

**Pattern:** In-order Traversal. An in-order traversal of a BST (Left, Node, Right) visits the nodes in strictly sorted ascending order. We can perform an iterative or recursive in-order traversal and stop when we've processed `k` elements.""",
        "diagram": """flowchart LR
    A["Traverse Left"] --> B["Process Node"]
    B --> C{"k == 0?"}
    C -->|Yes| D["Return val"]
    C -->|No| E["k--"]
    E --> F["Traverse Right"]""",
        "test_cases": [{'input': 'root = [3,1,4,null,2], k = 1', 'output': '1'}, {'input': 'root = [5,3,6,2,4,null,null,1], k = 3', 'output': '3'}],
        "js_code": """// Iterative Stack Approach
function kthSmallest(root, k) {
    const stack = [];
    let curr = root;
    let n = 0;
    
    while (curr || stack.length > 0) {
        while (curr) {
            stack.push(curr);
            curr = curr.left;
        }
        
        curr = stack.pop();
        n++;
        if (n === k) return curr.val;
        
        curr = curr.right;
    }
    
    return -1;
}""",
        "py_code": """def kthSmallest(root, k):
    stack = []
    curr = root
    n = 0
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
            
        curr = stack.pop()
        n += 1
        if n == k:
            return curr.val
            
        curr = curr.right
        
    return -1""",
        "solution_explanation": "Time Complexity: O(H + K). We traverse down to the leftmost leaf (O(H)) and then process K nodes. Space Complexity: O(H) for the stack.",
        "js_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
        "py_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
    },
    {
        "title": "Top K Frequent Elements",
        "category": "Heaps",
        "difficulty": "Medium",
        "explanation": """Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

**Pattern:** Bucket Sort. After counting frequencies using a Hash Map, create an array of arrays (`buckets`), where the index represents the frequency, and the value is a list of numbers that appear that many times. Traverse the buckets backwards (from highest frequency) until `k` items are found.""",
        "diagram": """flowchart TD
    A["Count Frequencies"] --> B["Create Bucket Array"]
    B --> C["Bucket[freq].append(num)"]
    C --> D["Iterate Bucket from end"]
    D --> E["Gather K elements"]""",
        "test_cases": [{'input': 'nums = [1,1,1,2,2,3], k = 2', 'output': '[1,2]'}, {'input': 'nums = [1], k = 1', 'output': '[1]'}],
        "js_code": """function topKFrequent(nums, k) {
    const count = new Map();
    const freq = Array.from({ length: nums.length + 1 }, () => []);
    
    // Count frequencies
    for (const num of nums) {
        count.set(num, (count.get(num) || 0) + 1);
    }
    
    // Populate bucket array
    for (const [num, countVal] of count) {
        freq[countVal].push(num);
    }
    
    const res = [];
    // Iterate from end
    for (let i = freq.length - 1; i > 0; i--) {
        for (const num of freq[i]) {
            res.push(num);
            if (res.length === k) return res;
        }
    }
    
    return res;
}""",
        "py_code": """def topKFrequent(nums, k):
    count = {}
    freq = [[] for _ in range(len(nums) + 1)]
    
    for num in nums:
        count[num] = 1 + count.get(num, 0)
        
    for num, countVal in count.items():
        freq[countVal].append(num)
        
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res
                
    return res""",
        "solution_explanation": "Time Complexity: O(N) because counting and bucket creation are both linear time. Space Complexity: O(N) to store frequencies and the bucket array.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Construct Binary Tree from Preorder and Inorder Traversal",
        "category": "Trees",
        "difficulty": "Medium",
        "explanation": """Given two integer arrays `preorder` and `inorder`, construct and return the binary tree.

**Pattern:** Tree Traversal Properties. The first element of `preorder` is always the root. We locate this root in `inorder` to determine the boundary between the left and right subtrees. Then, we recursively build the left and right branches.""",
        "diagram": """flowchart TD
    A["Preorder: [Root, Left..., Right...]"] --> B["Inorder: [Left..., Root, Right...]"]
    B --> C["Root is Preorder[0]"]
    C --> D["Find Root in Inorder (mid)"]
    D --> E["Left tree = Inorder[:mid]"]
    D --> F["Right tree = Inorder[mid+1:]"]""",
        "test_cases": [{'input': 'preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]', 'output': '[3,9,20,null,null,15,7]'}, {'input': 'preorder = [-1], inorder = [-1]', 'output': '[-1]'}],
        "js_code": """function buildTree(preorder, inorder) {
    if (!preorder.length || !inorder.length) return null;
    
    const root = new ListNode(preorder[0]);
    const mid = inorder.indexOf(preorder[0]);
    
    root.left = buildTree(
        preorder.slice(1, mid + 1),
        inorder.slice(0, mid)
    );
    root.right = buildTree(
        preorder.slice(mid + 1),
        inorder.slice(mid + 1)
    );
    
    return root;
}""",
        "py_code": """def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
        
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    
    root.left = buildTree(
        preorder[1:mid + 1], 
        inorder[:mid]
    )
    root.right = buildTree(
        preorder[mid + 1:], 
        inorder[mid + 1:]
    )
    
    return root""",
        "solution_explanation": "Time Complexity: O(N^2) normally due to `.indexOf()` inside recursion, but can be optimized to O(N) by using a hash map to store inorder indices. Space Complexity: O(N) to store the result and call stack.",
        "js_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
        "py_walkthrough": "1. <strong>Base Case:</strong> Check if the current node is `null`. If so, return immediately (usually 0 or null).<br>2. <strong>Recursive Calls:</strong> Call the function recursively on `node.left` and `node.right`.<br>3. <strong>Process Node:</strong> Perform logic on the current node using the results from the left and right subtrees (Bottom-Up) or pass values down (Top-Down).<br>4. <strong>Return Value:</strong> Return the aggregated result up the recursive call stack.",
    },
    {
        "title": "Clone Graph",
        "category": "Graphs",
        "difficulty": "Medium",
        "explanation": """Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

**Pattern:** Hash Map + DFS/BFS. We use a hash map to map original nodes to their cloned counterparts. During traversal (DFS or BFS), if a node hasn't been cloned, we clone it, put it in the map, and recursively clone its neighbors. If it has been cloned, we simply append the cloned node from the map to the current node's neighbors list.""",
        "diagram": """flowchart TD
    A["Original Node"] --> B{"Is in Map?"}
    B -->|Yes| C["Return Map[Node]"]
    B -->|No| D["Clone = new Node(val)"]
    D --> E["Map[Node] = Clone"]
    E --> F["For neighbor in neighbors:"]
    F --> G["Clone.neighbors.push(DFS(neighbor))"]
    G --> F""",
        "test_cases": [{'input': 'adjList = [[2,4],[1,3],[2,4],[1,3]]', 'output': '[[2,4],[1,3],[2,4],[1,3]]'}, {'input': 'adjList = [[]]', 'output': '[[]]'}],
        "js_code": """function cloneGraph(node) {
    if (!node) return null;
    const map = new Map();
    
    function dfs(node) {
        if (map.has(node)) return map.get(node);
        
        const clone = new _Node(node.val);
        map.set(node, clone);
        
        for (const neighbor of node.neighbors) {
            clone.neighbors.push(dfs(neighbor));
        }
        
        return clone;
    }
    
    return dfs(node);
}""",
        "py_code": """def cloneGraph(node):
    if not node:
        return None
        
    oldToNew = {}
    
    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]
            
        copy = Node(node.val)
        oldToNew[node] = copy
        
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
            
        return copy
        
    return dfs(node)""",
        "solution_explanation": "Time Complexity: O(V + E) where V is vertices and E is edges, as we visit each node and edge exactly once. Space Complexity: O(V) for the hash map and the recursion stack.",
        "js_walkthrough": "1. <strong>Adjacency List:</strong> Build a graph representation using a Map or Array of lists.<br>2. <strong>Visited Set:</strong> Initialize a `visited` Set to avoid cycles and infinite loops.<br>3. <strong>Traversal (BFS/DFS):</strong> Use a Queue for BFS (level-by-level) or Recursion/Stack for DFS (deep exploration).<br>4. <strong>Neighbor Exploration:</strong> For the current node, iterate through all its neighbors. If unvisited, mark them and add them to the queue/stack.<br>5. <strong>Result:</strong> Accumulate the path, count components, or return true if a target is reached.",
        "py_walkthrough": "1. <strong>Adjacency List:</strong> Build a graph representation using a Map or Array of lists.<br>2. <strong>Visited Set:</strong> Initialize a `visited` Set to avoid cycles and infinite loops.<br>3. <strong>Traversal (BFS/DFS):</strong> Use a Queue for BFS (level-by-level) or Recursion/Stack for DFS (deep exploration).<br>4. <strong>Neighbor Exploration:</strong> For the current node, iterate through all its neighbors. If unvisited, mark them and add them to the queue/stack.<br>5. <strong>Result:</strong> Accumulate the path, count components, or return true if a target is reached.",
    },
    {
        "title": "Course Schedule",
        "category": "Graphs",
        "difficulty": "Medium",
        "explanation": """There are `numCourses` courses. You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must take course `b` first if you want to take course `a`. Return true if you can finish all courses.

**Pattern:** Topological Sort / Cycle Detection. We can model this as a directed graph. The problem boils down to detecting if there is a cycle in the graph. We can use DFS with a `visited` set to track the current path. If we see a node already in our current path set, a cycle exists.""",
        "diagram": """flowchart LR
    A["Course 0"] --> B["Course 1"]
    B --> C["Course 2"]
    C -.->|"Cycle Detected!"| A
    
    D["DFS State"] --> E["0 = Unvisited"]
    D --> F["1 = Visiting (In Current Path)"]
    D --> G["2 = Visited (Fully Processed)"]""",
        "test_cases": [{'input': 'numCourses = 2, prerequisites = [[1,0]]', 'output': 'true'}, {'input': 'numCourses = 2, prerequisites = [[1,0],[0,1]]', 'output': 'false'}],
        "js_code": """function canFinish(numCourses, prerequisites) {
    const preMap = new Map();
    for (let i = 0; i < numCourses; i++) {
        preMap.set(i, []);
    }
    for (const [crs, pre] of prerequisites) {
        preMap.get(crs).push(pre);
    }
    
    const visitSet = new Set();
    
    function dfs(crs) {
        if (visitSet.has(crs)) return false;
        if (preMap.get(crs).length === 0) return true;
        
        visitSet.add(crs);
        for (const pre of preMap.get(crs)) {
            if (!dfs(pre)) return false;
        }
        visitSet.delete(crs);
        preMap.set(crs, []); // optimization
        return true;
    }
    
    for (let i = 0; i < numCourses; i++) {
        if (!dfs(i)) return false;
    }
    return true;
}""",
        "py_code": """def canFinish(numCourses, prerequisites):
    preMap = {i: [] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)
        
    visitSet = set()
    
    def dfs(crs):
        if crs in visitSet:
            return False
        if preMap[crs] == []:
            return True
            
        visitSet.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre): return False
        visitSet.remove(crs)
        preMap[crs] = [] # optimization
        return True
        
    for crs in range(numCourses):
        if not dfs(crs): return False
    return True""",
        "solution_explanation": "Time Complexity: O(V + E) where V is the number of courses and E is the number of prerequisites. Space Complexity: O(V + E) to build the adjacency list and for the DFS stack/visited set.",
        "js_walkthrough": "1. <strong>Adjacency List:</strong> Build a graph representation using a Map or Array of lists.<br>2. <strong>Visited Set:</strong> Initialize a `visited` Set to avoid cycles and infinite loops.<br>3. <strong>Traversal (BFS/DFS):</strong> Use a Queue for BFS (level-by-level) or Recursion/Stack for DFS (deep exploration).<br>4. <strong>Neighbor Exploration:</strong> For the current node, iterate through all its neighbors. If unvisited, mark them and add them to the queue/stack.<br>5. <strong>Result:</strong> Accumulate the path, count components, or return true if a target is reached.",
        "py_walkthrough": "1. <strong>Adjacency List:</strong> Build a graph representation using a Map or Array of lists.<br>2. <strong>Visited Set:</strong> Initialize a `visited` Set to avoid cycles and infinite loops.<br>3. <strong>Traversal (BFS/DFS):</strong> Use a Queue for BFS (level-by-level) or Recursion/Stack for DFS (deep exploration).<br>4. <strong>Neighbor Exploration:</strong> For the current node, iterate through all its neighbors. If unvisited, mark them and add them to the queue/stack.<br>5. <strong>Result:</strong> Accumulate the path, count components, or return true if a target is reached.",
    },
    {
        "title": "Pacific Atlantic Water Flow",
        "category": "Graphs / Matrix",
        "difficulty": "Medium",
        "explanation": """Given an `m x n` grid of heights, water can flow to neighboring cells if their height is less than or equal to the current cell's height. Find all cells that can flow to BOTH the Pacific (top/left) and Atlantic (bottom/right) oceans.

**Pattern:** Reverse DFS/BFS. Instead of starting from every cell and checking if it reaches both oceans (which is slow), start from the ocean borders and flow water *uphill* (checking if neighbor height >= current height). Run DFS from the Pacific edge to build a reachable set, and another from the Atlantic edge. The intersection of the two sets is the answer.""",
        "diagram": """flowchart TD
    A["Pacific Border (Top/Left)"] --> B["DFS Uphill (pacSet)"]
    C["Atlantic Border (Bottom/Right)"] --> D["DFS Uphill (atlSet)"]
    B --> E["Find Intersection"]
    D --> E
    E --> F["Return [r, c] pairs"]""",
        "test_cases": [{'input': 'heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]', 'output': '[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]'}, {'input': 'heights = [[1]]', 'output': '[[0,0]]'}],
        "js_code": """function pacificAtlantic(heights) {
    if (!heights || heights.length === 0) return [];
    
    const ROWS = heights.length, COLS = heights[0].length;
    const pac = new Set(), atl = new Set();
    
    function dfs(r, c, visit, prevHeight) {
        const key = r + ',' + c;
        if (r < 0 || c < 0 || r === ROWS || c === COLS || 
            visit.has(key) || heights[r][c] < prevHeight) {
            return;
        }
        
        visit.add(key);
        dfs(r + 1, c, visit, heights[r][c]);
        dfs(r - 1, c, visit, heights[r][c]);
        dfs(r, c + 1, visit, heights[r][c]);
        dfs(r, c - 1, visit, heights[r][c]);
    }
    
    for (let c = 0; c < COLS; c++) {
        dfs(0, c, pac, heights[0][c]);
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]);
    }
    for (let r = 0; r < ROWS; r++) {
        dfs(r, 0, pac, heights[r][0]);
        dfs(r, COLS - 1, atl, heights[r][COLS - 1]);
    }
    
    const res = [];
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (pac.has(r + ',' + c) && atl.has(r + ',' + c)) {
                res.push([r, c]);
            }
        }
    }
    return res;
}""",
        "py_code": """def pacificAtlantic(heights):
    if not heights: return []
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()
    
    def dfs(r, c, visit, prevHeight):
        if (r < 0 or c < 0 or r == ROWS or c == COLS or
            (r, c) in visit or heights[r][c] < prevHeight):
            return
        visit.add((r, c))
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])
        
    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
    res = []
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])
    return res""",
        "solution_explanation": "Time Complexity: O(M * N) where M is rows and N is columns. We run DFS from the borders, but the visited set ensures we process each cell at most once per ocean. Space Complexity: O(M * N) for the visited sets and recursion stack.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Number of Islands",
        "category": "Graphs / Matrix",
        "difficulty": "Medium",
        "explanation": """Given an `m x n` 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

**Pattern:** DFS / BFS on Grid. Iterate through every cell. When you encounter a '1', increment your island count, then run a DFS or BFS to mark that entire connected component of '1's as visited (e.g., by changing them to '0').""",
        "diagram": """flowchart TD
    A["Iterate grid"] --> B{"Is cell '1'?"}
    B -->|Yes| C["Island Count++"]
    C --> D["DFS: Sink Island ('1' -> '0')"]
    D --> E["Search neighbors (Up, Down, Left, Right)"]
    E --> D
    B -->|No| F["Continue"]""",
        "test_cases": [{'input': "grid = [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]", 'output': '3'}],
        "js_code": """function numIslands(grid) {
    if (!grid || grid.length === 0) return 0;
    
    let islands = 0;
    const ROWS = grid.length;
    const COLS = grid[0].length;
    
    function dfs(r, c) {
        if (r < 0 || c < 0 || r >= ROWS || c >= COLS || grid[r][c] === '0') {
            return;
        }
        
        grid[r][c] = '0'; // mark as visited
        
        dfs(r + 1, c);
        dfs(r - 1, c);
        dfs(r, c + 1);
        dfs(r, c - 1);
    }
    
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (grid[r][c] === '1') {
                islands++;
                dfs(r, c);
            }
        }
    }
    
    return islands;
}""",
        "py_code": """def numIslands(grid):
    if not grid:
        return 0
        
    islands = 0
    ROWS, COLS = len(grid), len(grid[0])
    
    def dfs(r, c):
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0':
            return
            
        grid[r][c] = '0' # mark visited
        
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)
                
    return islands""",
        "solution_explanation": "Time Complexity: O(M * N) since we visit every cell. The DFS also processes each cell at most once. Space Complexity: O(M * N) for the worst-case recursion stack (if the entire grid is one island).",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Longest Consecutive Sequence",
        "category": "Arrays / Hashing",
        "difficulty": "Medium",
        "explanation": """Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in `O(n)` time.

**Pattern:** HashSet. Throw all numbers into a HashSet. Then, iterate through the set. A number can only be the start of a sequence if `num - 1` does NOT exist in the set. If it is a start, keep checking if `num + 1, num + 2...` exist and track the max length.""",
        "diagram": """flowchart TD
    A["Convert nums to HashSet"] --> B["Iterate num in Set"]
    B --> C{"Does (num - 1) exist?"}
    C -->|Yes| D["Not a start, skip"]
    C -->|No| E["Start of sequence found"]
    E --> F["While (num + length) exists: length++"]
    F --> G["Update Max Length"]""",
        "test_cases": [{'input': 'nums = [100,4,200,1,3,2]', 'output': '4 (Sequence: 1, 2, 3, 4)'}, {'input': 'nums = [0,3,7,2,5,8,4,6,0,1]', 'output': '9'}],
        "js_code": """function longestConsecutive(nums) {
    const numSet = new Set(nums);
    let longest = 0;
    
    for (const num of numSet) {
        // Check if it's the start of a sequence
        if (!numSet.has(num - 1)) {
            let length = 1;
            
            while (numSet.has(num + length)) {
                length++;
            }
            
            longest = Math.max(longest, length);
        }
    }
    
    return longest;
}""",
        "py_code": """def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0
    
    for num in numSet:
        # Check if it's the start of a sequence
        if (num - 1) not in numSet:
            length = 1
            while (num + length) in numSet:
                length += 1
            longest = max(longest, length)
            
    return longest""",
        "solution_explanation": "Time Complexity: O(N). Although there's a while loop inside the for loop, the while loop only runs for the *start* of a sequence, meaning each number is visited at most twice. Space Complexity: O(N) for the HashSet.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Set Matrix Zeroes",
        "category": "Matrix",
        "difficulty": "Medium",
        "explanation": """Given an `m x n` integer matrix, if an element is 0, set its entire row and column to 0's. You must do it in place.

**Pattern:** O(1) Space In-Place Marker. Use the first row and first column of the matrix itself to keep track of which rows and columns need to be zeroed. Because `matrix[0][0]` overlaps for both the first row and first column, use an extra variable to track if the first row (or col) needs zeroing.""",
        "diagram": """flowchart TD
    A["Iterate Matrix"] --> B{"Is cell 0?"}
    B -->|Yes| C["Set first element of row to 0"]
    B -->|Yes| D["Set first element of col to 0"]
    C --> E["Iterate Matrix again (except first row/col)"]
    E --> F{"Is first of row or col 0?"}
    F -->|Yes| G["Set cell to 0"]
    G --> H["Zero out first row/col if needed"]""",
        "test_cases": [{'input': 'matrix = [[1,1,1],[1,0,1],[1,1,1]]', 'output': '[[1,0,1],[0,0,0],[1,0,1]]'}],
        "js_code": """function setZeroes(matrix) {
    const ROWS = matrix.length;
    const COLS = matrix[0].length;
    let rowZero = false;
    
    // Determine which rows/cols need to be zeroed
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (matrix[r][c] === 0) {
                matrix[0][c] = 0; // Mark Col
                if (r > 0) {
                    matrix[r][0] = 0; // Mark Row
                } else {
                    rowZero = true; // Mark First Row
                }
            }
        }
    }
    
    // Zero out inner cells based on markers
    for (let r = 1; r < ROWS; r++) {
        for (let c = 1; c < COLS; c++) {
            if (matrix[0][c] === 0 || matrix[r][0] === 0) {
                matrix[r][c] = 0;
            }
        }
    }
    
    // Zero out first column if needed
    if (matrix[0][0] === 0) {
        for (let r = 0; r < ROWS; r++) {
            matrix[r][0] = 0;
        }
    }
    
    // Zero out first row if needed
    if (rowZero) {
        for (let c = 0; c < COLS; c++) {
            matrix[0][c] = 0;
        }
    }
}""",
        "py_code": """def setZeroes(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    rowZero = False
    
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True
                    
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
                
    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0
            
    if rowZero:
        for c in range(COLS):
            matrix[0][c] = 0""",
        "solution_explanation": "Time Complexity: O(M * N) since we iterate through the matrix a couple of times. Space Complexity: O(1) as we do it in-place using the first row and column as markers.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Spiral Matrix",
        "category": "Matrix",
        "difficulty": "Medium",
        "explanation": """Given an `m x n` matrix, return all elements of the matrix in spiral order.

**Pattern:** 4 Boundaries. Maintain `left`, `right`, `top`, and `bottom` boundaries. We loop while `left < right` and `top < bottom`. In each iteration, we traverse top row (left to right), right column (top to bottom), bottom row (right to left), and left column (bottom to top), shrinking the boundaries as we go.""",
        "diagram": """flowchart TD
    A["Initialize Boundaries: left, right, top, bottom"] --> B{"left < right AND top < bottom?"}
    B -->|Yes| C["Traverse Top Row, top++"]
    C --> D["Traverse Right Col, right--"]
    D --> E{"Break if left >= right OR top >= bottom"}
    E --> F["Traverse Bottom Row, bottom--"]
    F --> G["Traverse Left Col, left++"]
    G --> B""",
        "test_cases": [{'input': 'matrix = [[1,2,3],[4,5,6],[7,8,9]]', 'output': '[1,2,3,6,9,8,7,4,5]'}, {'input': 'matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]', 'output': '[1,2,3,4,8,12,11,10,9,5,6,7]'}],
        "js_code": """function spiralOrder(matrix) {
    const res = [];
    let left = 0, right = matrix[0].length;
    let top = 0, bottom = matrix.length;
    
    while (left < right && top < bottom) {
        // get every i in the top row
        for (let i = left; i < right; i++) {
            res.push(matrix[top][i]);
        }
        top++;
        
        // get every i in the right col
        for (let i = top; i < bottom; i++) {
            res.push(matrix[i][right - 1]);
        }
        right--;
        
        if (!(left < right && top < bottom)) {
            break;
        }
        
        // get every i in the bottom row
        for (let i = right - 1; i >= left; i--) {
            res.push(matrix[bottom - 1][i]);
        }
        bottom--;
        
        // get every i in the left col
        for (let i = bottom - 1; i >= top; i--) {
            res.push(matrix[i][left]);
        }
        left++;
    }
    
    return res;
}""",
        "py_code": """def spiralOrder(matrix):
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    
    while left < right and top < bottom:
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1
        
        if not (left < right and top < bottom):
            break
            
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1
        
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
        
    return res""",
        "solution_explanation": "Time Complexity: O(M * N) as we visit every element exactly once. Space Complexity: O(1) not counting the output array.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Rotate Image",
        "category": "Matrix",
        "difficulty": "Medium",
        "explanation": """You are given an `n x n` 2D matrix representing an image, rotate the image by 90 degrees (clockwise). You have to rotate the image in-place.

**Pattern:** Transpose then Reverse OR 4-way Swap. A 90 degree clockwise rotation can be achieved by first transposing the matrix (swapping `matrix[i][j]` with `matrix[j][i]`), and then reversing each row. Alternatively, you can swap the 4 corners in a loop moving inward.""",
        "diagram": """flowchart LR
    A["Original Matrix"] -->|Transpose| B["Rows become Cols"]
    B -->|Reverse Rows| C["Rotated 90 Deg"]
    
    D["1 2 3"] -.-> E["1 4 7"] -.-> F["7 4 1"]
    G["4 5 6"] -.-> H["2 5 8"] -.-> I["8 5 2"]
    J["7 8 9"] -.-> K["3 6 9"] -.-> L["9 6 3"]""",
        "test_cases": [{'input': 'matrix = [[1,2,3],[4,5,6],[7,8,9]]', 'output': '[[7,4,1],[8,5,2],[9,6,3]]'}],
        "js_code": """function rotate(matrix) {
    const N = matrix.length;
    
    // Transpose
    for (let r = 0; r < N; r++) {
        for (let c = r; c < N; c++) {
            let temp = matrix[r][c];
            matrix[r][c] = matrix[c][r];
            matrix[c][r] = temp;
        }
    }
    
    // Reverse rows
    for (let r = 0; r < N; r++) {
        matrix[r].reverse();
    }
}""",
        "py_code": """def rotate(matrix):
    N = len(matrix)
    
    # Transpose
    for r in range(N):
        for c in range(r, N):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            
    # Reverse rows
    for r in range(N):
        matrix[r].reverse()""",
        "solution_explanation": "Time Complexity: O(N^2) where N is the length of one side of the matrix, as we visit each cell a constant number of times. Space Complexity: O(1) because we swap in-place.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Word Search",
        "category": "Matrix / Backtracking",
        "difficulty": "Medium",
        "explanation": """Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid. The word can be constructed from letters of sequentially adjacent cells (horizontal/vertical). The same cell may not be used more than once.

**Pattern:** DFS + Backtracking. Iterate through every cell. If it matches the first letter of the word, start a DFS. Pass the current index of the word we are looking for. Keep track of visited cells in the current DFS path to avoid reusing them. Backtrack by un-visiting cells when returning from DFS.""",
        "diagram": """flowchart TD
    A["Iterate through board"] --> B{"board[r][c] == word[0]?"}
    B -->|Yes| C["DFS(r, c, index=0)"]
    C --> D{"index == word.length?"}
    D -->|Yes| E["Return True"]
    D -->|No| F["Mark visited, DFS neighbors"]
    F --> G["Unmark visited (Backtrack)"]
    G --> C""",
        "test_cases": [{'input': "board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = 'ABCCED'", 'output': 'true'}, {'input': "board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = 'ABCB'", 'output': 'false'}],
        "js_code": """function exist(board, word) {
    const ROWS = board.length;
    const COLS = board[0].length;
    const path = new Set();
    
    function dfs(r, c, i) {
        if (i === word.length) return true;
        
        const key = r + ',' + c;
        if (r < 0 || c < 0 || r >= ROWS || c >= COLS || 
            word[i] !== board[r][c] || path.has(key)) {
            return false;
        }
        
        path.add(key);
        const res = (dfs(r + 1, c, i + 1) ||
                     dfs(r - 1, c, i + 1) ||
                     dfs(r, c + 1, i + 1) ||
                     dfs(r, c - 1, i + 1));
        path.delete(key);
        
        return res;
    }
    
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (dfs(r, c, 0)) return true;
        }
    }
    return false;
}""",
        "py_code": """def exist(board, word):
    ROWS, COLS = len(board), len(board[0])
    path = set()
    
    def dfs(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
            word[i] != board[r][c] or (r, c) in path):
            return False
            
        path.add((r, c))
        res = (dfs(r + 1, c, i + 1) or
               dfs(r - 1, c, i + 1) or
               dfs(r, c + 1, i + 1) or
               dfs(r, c - 1, i + 1))
        path.remove((r, c))
        
        return res
        
    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0): return True
    return False""",
        "solution_explanation": "Time Complexity: O(M * N * 4^L) where L is the length of the word, as we have 4 directions to explore for each step in the word. Space Complexity: O(L) for the recursion stack and path set.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Reverse Bits",
        "category": "Bit Manipulation",
        "difficulty": "Easy",
        "explanation": """Reverse bits of a given 32 bits unsigned integer.

**Pattern:** Bit Shifting. We can loop 32 times. In each iteration, extract the rightmost bit of the input number `(n & 1)`, shift the result to the left by 1, and add the extracted bit to the result. Then shift the input number to the right by 1 to process the next bit.""",
        "diagram": """flowchart TD
    A["Result = 0, Loop 32 times"] --> B["Bit = n & 1 (Get rightmost bit)"]
    B --> C["Result = Result << 1"]
    C --> D["Result = Result | Bit"]
    D --> E["n = n >> 1"]
    E --> A""",
        "test_cases": [{'input': 'n = 00000010100101000001111010011100', 'output': '964176192 (00111001011110000010100101000000)'}],
        "js_code": """function reverseBits(n) {
    let res = 0;
    
    for (let i = 0; i < 32; i++) {
        // Get the rightmost bit
        let bit = (n >> i) & 1;
        // Shift it to its new reversed position and add it
        // Use >>> to force unsigned bit shift in JS
        res = res | (bit << (31 - i));
    }
    
    // JS bitwise ops operate on 32-bit signed integers. 
    // Return unsigned equivalent
    return res >>> 0; 
}""",
        "py_code": """def reverseBits(n):
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res = res | (bit << (31 - i))
    return res""",
        "solution_explanation": "Time Complexity: O(1) because we always loop exactly 32 times. Space Complexity: O(1).",
        "js_walkthrough": "1. <strong>Bitwise Operators:</strong> Utilize operators like XOR (`^`), AND (`&`), or shifts (`<<`, `>>`).<br>2. <strong>XOR Logic:</strong> Remember `a ^ a = 0` and `a ^ 0 = a` (useful for finding missing/single numbers).<br>3. <strong>AND Logic:</strong> `n & (n - 1)` removes the lowest set bit (useful for counting 1s or checking powers of 2).<br>4. <strong>Iteration:</strong> Process the number bit by bit using a loop (up to 32 times for integers).<br>5. <strong>Result:</strong> Accumulate the bits into a final integer return value.",
        "py_walkthrough": "1. <strong>Bitwise Operators:</strong> Utilize operators like XOR (`^`), AND (`&`), or shifts (`<<`, `>>`).<br>2. <strong>XOR Logic:</strong> Remember `a ^ a = 0` and `a ^ 0 = a` (useful for finding missing/single numbers).<br>3. <strong>AND Logic:</strong> `n & (n - 1)` removes the lowest set bit (useful for counting 1s or checking powers of 2).<br>4. <strong>Iteration:</strong> Process the number bit by bit using a loop (up to 32 times for integers).<br>5. <strong>Result:</strong> Accumulate the bits into a final integer return value.",
    },
    {
        "title": "Number of 1 Bits",
        "category": "Bit Manipulation",
        "difficulty": "Easy",
        "explanation": """Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

**Pattern:** Bit Manipulation Trick: `n & (n-1)`. The expression `n & (n-1)` flips the least significant '1' bit of `n` to '0'. By repeatedly applying this operation and counting until the number becomes 0, we can efficiently find the number of 1s without looking at every 0.""",
        "diagram": """flowchart LR
    A["Count = 0"] --> B{"n != 0?"}
    B -->|Yes| C["n = n & (n - 1)"]
    C --> D["Count++"]
    D --> B
    B -->|No| E["Return Count"]""",
        "test_cases": [{'input': 'n = 00000000000000000000000000001011', 'output': '3'}, {'input': 'n = 00000000000000000000000010000000', 'output': '1'}],
        "js_code": """function hammingWeight(n) {
    let res = 0;
    
    while (n !== 0) {
        n = n & (n - 1);
        res++;
    }
    
    return res;
}""",
        "py_code": """def hammingWeight(n):
    res = 0
    while n:
        n &= (n - 1)
        res += 1
    return res""",
        "solution_explanation": "Time Complexity: O(1) mathematically, or O(K) where K is the number of '1' bits, which is bound by 32. Space Complexity: O(1).",
        "js_walkthrough": "1. <strong>Bitwise Operators:</strong> Utilize operators like XOR (`^`), AND (`&`), or shifts (`<<`, `>>`).<br>2. <strong>XOR Logic:</strong> Remember `a ^ a = 0` and `a ^ 0 = a` (useful for finding missing/single numbers).<br>3. <strong>AND Logic:</strong> `n & (n - 1)` removes the lowest set bit (useful for counting 1s or checking powers of 2).<br>4. <strong>Iteration:</strong> Process the number bit by bit using a loop (up to 32 times for integers).<br>5. <strong>Result:</strong> Accumulate the bits into a final integer return value.",
        "py_walkthrough": "1. <strong>Bitwise Operators:</strong> Utilize operators like XOR (`^`), AND (`&`), or shifts (`<<`, `>>`).<br>2. <strong>XOR Logic:</strong> Remember `a ^ a = 0` and `a ^ 0 = a` (useful for finding missing/single numbers).<br>3. <strong>AND Logic:</strong> `n & (n - 1)` removes the lowest set bit (useful for counting 1s or checking powers of 2).<br>4. <strong>Iteration:</strong> Process the number bit by bit using a loop (up to 32 times for integers).<br>5. <strong>Result:</strong> Accumulate the bits into a final integer return value.",
    },
    {
        "title": "Counting Bits",
        "category": "Bit Manipulation / DP",
        "difficulty": "Easy",
        "explanation": """Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (0 <= i <= n), `ans[i]` is the number of `1`'s in the binary representation of `i`.

**Pattern:** Dynamic Programming. Notice the pattern in binary: the number of 1s in `N` is the same as the number of 1s in `N / 2` (right shifted by 1), plus `1` if `N` is odd. `dp[i] = dp[i >> 1] + (i & 1)`.""",
        "diagram": """flowchart TD
    A["Initialize DP array of size n+1"] --> B["dp[0] = 0"]
    B --> C["Loop i from 1 to n"]
    C --> D["dp[i] = dp[i >> 1] + (i & 1)"]
    D --> C""",
        "test_cases": [{'input': 'n = 2', 'output': '[0,1,1]'}, {'input': 'n = 5', 'output': '[0,1,1,2,1,2]'}],
        "js_code": """function countBits(n) {
    const dp = new Array(n + 1).fill(0);
    
    let offset = 1;
    for (let i = 1; i <= n; i++) {
        if (offset * 2 === i) {
            offset = i;
        }
        dp[i] = 1 + dp[i - offset];
    }
    
    // Alternatively: dp[i] = dp[i >> 1] + (i & 1);
    
    return dp;
}""",
        "py_code": """def countBits(n):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # i >> 1 is i // 2
        # i & 1 is i % 2
        dp[i] = dp[i >> 1] + (i & 1)
        
    return dp""",
        "solution_explanation": "Time Complexity: O(N) as we compute each number in O(1) time using previously computed results. Space Complexity: O(N) for the DP array.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Missing Number",
        "category": "Bit Manipulation / Math",
        "difficulty": "Easy",
        "explanation": """Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

**Pattern:** XOR or Math. Math approach: The expected sum of numbers from 0 to N is `N * (N + 1) / 2`. Subtract the actual sum of the array to find the missing number. XOR approach: `XOR`ing a number with itself gives 0. `XOR` the array index and values together; the missing number won't cancel out.""",
        "diagram": """flowchart TD
    A["Expected Sum = N * (N+1) / 2"] --> B["Actual Sum = Sum(nums)"]
    B --> C["Missing = Expected - Actual"]""",
        "test_cases": [{'input': 'nums = [3,0,1]', 'output': '2'}, {'input': 'nums = [9,6,4,2,3,5,7,0,1]', 'output': '8'}],
        "js_code": """function missingNumber(nums) {
    // XOR Approach
    let res = nums.length;
    
    for (let i = 0; i < nums.length; i++) {
        // XOR the index and the value
        res ^= i ^ nums[i];
    }
    
    return res;
    
    /* Math Approach:
    const expected = (nums.length * (nums.length + 1)) / 2;
    const actual = nums.reduce((a, b) => a + b, 0);
    return expected - actual;
    */
}""",
        "py_code": """def missingNumber(nums):
    res = len(nums)
    
    for i in range(len(nums)):
        res ^= i ^ nums[i]
        
    return res""",
        "solution_explanation": "Time Complexity: O(N) for either computing the sum or doing XOR across all elements. Space Complexity: O(1) since we only use a few variables.",
        "js_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
        "py_walkthrough": "1. <strong>Initialization:</strong> Set up necessary data structures and state variables.<br>2. <strong>Iteration/Recursion:</strong> Traverse the input space.<br>3. <strong>Logic Evaluation:</strong> Apply the core algorithmic condition.<br>4. <strong>State Update:</strong> Update variables based on the evaluation.<br>5. <strong>Result:</strong> Return the final computed value.",
    },
    {
        "title": "Sum of Two Integers",
        "category": "Bit Manipulation",
        "difficulty": "Medium",
        "explanation": """Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.

**Pattern:** Bitwise XOR and AND. `XOR` acts as addition without carrying over. `AND` followed by a left shift `<< 1` finds where the carries happen. We repeat `a = a ^ b` and `b = carry << 1` until there are no more carries (`b == 0`).""",
        "diagram": """flowchart LR
    A["While b != 0"] --> B["tmp = (a AND b) << 1"]
    B --> C["a = a XOR b"]
    C --> D["b = tmp"]
    D --> A
    A -->|Done| E["Return a"]""",
        "test_cases": [{'input': 'a = 1, b = 2', 'output': '3'}, {'input': 'a = 2, b = 3', 'output': '5'}],
        "js_code": """function getSum(a, b) {
    while (b !== 0) {
        // Carry contains common set bits of a and b
        let carry = (a & b) << 1;
        
        // Sum of bits of a and b where at least one of the bits is not set
        a = a ^ b;
        
        b = carry;
    }
    return a;
}""",
        "py_code": """def getSum(a, b):
    # In Python, integers have arbitrary precision.
    # We must restrict to 32 bits manually using a mask.
    mask = 0xffffffff
    
    while (b & mask) > 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
        
    # Handle negative numbers
    return (a & mask) if b > 0 else a""",
        "solution_explanation": "Time Complexity: O(1) bounded by 32 bits, as the carry will shift out of 32-bit limits in at most 32 operations. Space Complexity: O(1).",
        "js_walkthrough": "1. <strong>Bitwise Operators:</strong> Utilize operators like XOR (`^`), AND (`&`), or shifts (`<<`, `>>`).<br>2. <strong>XOR Logic:</strong> Remember `a ^ a = 0` and `a ^ 0 = a` (useful for finding missing/single numbers).<br>3. <strong>AND Logic:</strong> `n & (n - 1)` removes the lowest set bit (useful for counting 1s or checking powers of 2).<br>4. <strong>Iteration:</strong> Process the number bit by bit using a loop (up to 32 times for integers).<br>5. <strong>Result:</strong> Accumulate the bits into a final integer return value.",
        "py_walkthrough": "1. <strong>Bitwise Operators:</strong> Utilize operators like XOR (`^`), AND (`&`), or shifts (`<<`, `>>`).<br>2. <strong>XOR Logic:</strong> Remember `a ^ a = 0` and `a ^ 0 = a` (useful for finding missing/single numbers).<br>3. <strong>AND Logic:</strong> `n & (n - 1)` removes the lowest set bit (useful for counting 1s or checking powers of 2).<br>4. <strong>Iteration:</strong> Process the number bit by bit using a loop (up to 32 times for integers).<br>5. <strong>Result:</strong> Accumulate the bits into a final integer return value.",
    },
    {
        "title": "Graph Valid Tree",
        "category": "Graphs",
        "difficulty": "Medium",
        "explanation": """You have a graph of `n` nodes. You are given an integer n and an array of `edges`. Return `true` if the edges make up a valid tree, and `false` otherwise.

**Pattern:** DFS / Cycle Detection. A valid tree must satisfy two conditions: 1. It must be fully connected (all nodes reachable). 2. It must contain NO cycles. We run DFS from node 0. If we encounter a visited node that isn't our immediate parent, we found a cycle. Afterward, we verify `visited.size === n` to ensure it's fully connected.""",
        "diagram": """flowchart TD
    A["Build Adjacency List"] --> B["DFS from node 0"]
    B --> C{"Neighbor visited AND not parent?"}
    C -->|Yes| D["Cycle Found (Return False)"]
    C -->|No| E["Continue DFS"]
    E --> F{"Are all nodes visited?"}
    F -->|Yes| G["True"]
    F -->|No| H["False (Disconnected)"]""",
        "test_cases": [{'input': 'n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]', 'output': 'true'}, {'input': 'n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]', 'output': 'false'}],
        "js_code": """function validTree(n, edges) {
    if (!n) return true;
    
    const adj = new Map();
    for (let i = 0; i < n; i++) adj.set(i, []);
    for (const [n1, n2] of edges) {
        adj.get(n1).push(n2);
        adj.get(n2).push(n1);
    }
    
    const visit = new Set();
    
    function dfs(i, prev) {
        if (visit.has(i)) return false; // Cycle detected
        
        visit.add(i);
        for (const j of adj.get(i)) {
            if (j === prev) continue;
            if (!dfs(j, i)) return false;
        }
        return true;
    }
    
    return dfs(0, -1) && visit.size === n;
}""",
        "py_code": """def validTree(n, edges):
    if not n: return True
    
    adj = {i: [] for i in range(n)}
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)
        
    visit = set()
    
    def dfs(i, prev):
        if i in visit:
            return False
            
        visit.add(i)
        for j in adj[i]:
            if j == prev:
                continue
            if not dfs(j, i):
                return False
        return True
        
    return dfs(0, -1) and len(visit) == n""",
        "solution_explanation": "Time Complexity: O(V + E). Space Complexity: O(V + E) to store adjacency list and visited set.",
        "js_walkthrough": "1. <strong>Adjacency List:</strong> Build a graph representation using a Map or Array of lists.<br>2. <strong>Visited Set:</strong> Initialize a `visited` Set to avoid cycles and infinite loops.<br>3. <strong>Traversal (BFS/DFS):</strong> Use a Queue for BFS (level-by-level) or Recursion/Stack for DFS (deep exploration).<br>4. <strong>Neighbor Exploration:</strong> For the current node, iterate through all its neighbors. If unvisited, mark them and add them to the queue/stack.<br>5. <strong>Result:</strong> Accumulate the path, count components, or return true if a target is reached.",
        "py_walkthrough": "1. <strong>Adjacency List:</strong> Build a graph representation using a Map or Array of lists.<br>2. <strong>Visited Set:</strong> Initialize a `visited` Set to avoid cycles and infinite loops.<br>3. <strong>Traversal (BFS/DFS):</strong> Use a Queue for BFS (level-by-level) or Recursion/Stack for DFS (deep exploration).<br>4. <strong>Neighbor Exploration:</strong> For the current node, iterate through all its neighbors. If unvisited, mark them and add them to the queue/stack.<br>5. <strong>Result:</strong> Accumulate the path, count components, or return true if a target is reached.",
    },
    {
        "title": "Climbing Stairs",
        "category": "1D Dynamic Programming",
        "difficulty": "Easy",
        "explanation": """You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Pattern:** Fibonacci Sequence / Bottom-Up DP. To reach step `i`, you must have come from either step `i-1` or step `i-2`. Therefore, the number of ways to reach step `i` is the sum of the ways to reach step `i-1` and `i-2`. We can compute this iteratively using two variables to save space.""",
        "diagram": """flowchart TD
    A["Step N"] --> B["Step N-1"]
    A --> C["Step N-2"]
    B --> D["..."]
    C --> E["..."]
    
    F["Base Cases:"] -.-> G["Step 1 = 1 way"]
    F -.-> H["Step 2 = 2 ways"]""",
        "test_cases": [{'input': 'n = 2', 'output': '2 (1+1, 2)'}, {'input': 'n = 3', 'output': '3 (1+1+1, 1+2, 2+1)'}],
        "js_code": """function climbStairs(n) {
    // Base cases for small stairs
    if (n <= 3) return n;
    
    // one represents ways to reach (i-1)
    // two represents ways to reach (i-2)
    let one = 2; 
    let two = 1;
    
    for (let i = 3; i < n; i++) {
        // Current step ways is sum of previous two
        const temp = one + two;
        two = one;
        one = temp;
    }
    
    return one + two;
}""",
        "py_code": """def climbStairs(n):
    # Base cases for small stairs
    if n <= 3:
        return n
        
    # one represents ways to reach (i-1)
    # two represents ways to reach (i-2)
    one, two = 2, 1
    
    for i in range(3, n):
        # Current step ways is sum of previous two
        temp = one + two
        two = one
        one = temp
        
    return one + two""",
        "js_walkthrough": "1. <strong>Base Cases:</strong> We first handle small inputs `n <= 3` where the answer is just `n`.<br>2. <strong>Variables:</strong> We initialize `one` to 2 (ways to reach step 2) and `two` to 1 (ways to reach step 1).<br>3. <strong>Loop:</strong> We loop from step 3 up to `n - 1`. In each iteration, we calculate `temp` as the sum of `one` and `two`.<br>4. <strong>Shift:</strong> We then shift our window forward: `two` becomes the old `one`, and `one` becomes `temp`.<br>5. <strong>Result:</strong> Finally, we return the sum of the last two calculated steps.",
        "py_walkthrough": "1. <strong>Base Cases:</strong> We first handle small inputs `n <= 3` where the answer is just `n`.<br>2. <strong>Variables:</strong> We initialize `one` to 2 (ways to reach step 2) and `two` to 1 (ways to reach step 1).<br>3. <strong>Loop:</strong> We use a `for` loop starting from 3 up to `n - 1`. We calculate the current step as `one + two`.<br>4. <strong>Shift:</strong> We shift our variables forward to prepare for the next step.<br>5. <strong>Result:</strong> We return `one + two` which represents the total ways to reach the top.",
        "solution_explanation": "Time Complexity: O(N) since we loop through `n` steps. Space Complexity: O(1) as we only use two variables instead of a full DP array.",
    },
    {
        "title": "Coin Change",
        "category": "1D Dynamic Programming",
        "difficulty": "Medium",
        "explanation": """You are given an integer array `coins` and an integer `amount`. Return the fewest number of coins that you need to make up that amount. If it cannot be made, return `-1`.

**Pattern:** Bottom-Up DP. Create an array `dp` of size `amount + 1` initialized to `amount + 1` (acting as infinity). `dp[i]` represents the minimum coins needed to make amount `i`. For each amount from 1 to `amount`, we try subtracting each coin and see if it takes fewer coins than our current best.""",
        "diagram": """flowchart LR
    A["dp array initialized to Infinity"] --> B["dp[0] = 0"]
    B --> C["For a in 1..amount:"]
    C --> D["For c in coins:"]
    D --> E{"a - c >= 0?"}
    E -->|Yes| F["dp[a] = min(dp[a], 1 + dp[a - c])"]
    E -->|No| D""",
        "test_cases": [{'input': 'coins = [1,2,5], amount = 11', 'output': '3 (5 + 5 + 1)'}, {'input': 'coins = [2], amount = 3', 'output': '-1'}],
        "js_code": """function coinChange(coins, amount) {
    // Initialize DP array with 'Infinity' (amount + 1 is safe)
    const dp = new Array(amount + 1).fill(amount + 1);
    
    // 0 coins needed to make amount 0
    dp[0] = 0;
    
    // Iterate through all amounts from 1 to amount
    for (let a = 1; a <= amount; a++) {
        for (const c of coins) {
            // If coin can be used
            if (a - c >= 0) {
                dp[a] = Math.min(dp[a], 1 + dp[a - c]);
            }
        }
    }
    
    // If dp[amount] wasn't changed, return -1
    return dp[amount] !== amount + 1 ? dp[amount] : -1;
}""",
        "py_code": """def coinChange(coins, amount):
    # Initialize DP array with 'Infinity' (amount + 1 is safe)
    dp = [amount + 1] * (amount + 1)
    
    # 0 coins needed to make amount 0
    dp[0] = 0
    
    # Iterate through all amounts from 1 to amount
    for a in range(1, amount + 1):
        for c in coins:
            # If coin can be used
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
                
    # If dp[amount] wasn't changed, return -1
    return dp[amount] if dp[amount] != amount + 1 else -1""",
        "js_walkthrough": "1. <strong>DP Array Initialization:</strong> We create an array `dp` of size `amount + 1` and fill it with `amount + 1`. This value acts as infinity because the max possible coins is `amount` (if all are 1).<br>2. <strong>Base Case:</strong> `dp[0] = 0` since it takes 0 coins to make amount 0.<br>3. <strong>Iterate Amounts:</strong> We loop `a` from 1 up to `amount`.<br>4. <strong>Iterate Coins:</strong> For each amount `a`, we loop through every coin. If `a - c >= 0`, we check if taking this coin (`1 + dp[a - c]`) gives a smaller total coin count than the current `dp[a]`.<br>5. <strong>Return:</strong> We return `dp[amount]` unless it remains at infinity, in which case we return `-1`.",
        "py_walkthrough": "1. <strong>DP Array Initialization:</strong> We initialize a list `dp` of size `amount + 1` with a dummy max value (`amount + 1`).<br>2. <strong>Base Case:</strong> We set `dp[0] = 0`.<br>3. <strong>Iterate Amounts:</strong> We use an outer loop for `a` from 1 to `amount`.<br>4. <strong>Iterate Coins:</strong> We use an inner loop for each coin `c`. If the coin doesn't exceed the amount (`a - c >= 0`), we update `dp[a]` with `min(dp[a], 1 + dp[a - c])`.<br>5. <strong>Return:</strong> If `dp[amount]` is still the initialized max value, the amount cannot be made, so we return `-1`. Otherwise, we return `dp[amount]`.",
        "solution_explanation": "Time Complexity: O(amount * len(coins)). We solve for every sub-amount from 1 to amount, and for each sub-amount, we iterate through the coins array. Space Complexity: O(amount) to store the DP array.",
    },
    {
        "title": "Longest Increasing Subsequence",
        "category": "1D Dynamic Programming",
        "difficulty": "Medium",
        "explanation": """Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

**Pattern:** Bottom-Up DP. Initialize a DP array of 1s (since each number is a subsequence of length 1 by itself). For each number at index `i`, we look back at all previous numbers at index `j`. If `nums[i] > nums[j]`, we can append `nums[i]` to the subsequence ending at `j`.""",
        "diagram": """flowchart TD
    A["dp = [1, 1, 1...]"] --> B["For i from 1 to n:"]
    B --> C["For j from 0 to i:"]
    C --> D{"nums[i] > nums[j]?"}
    D -->|Yes| E["dp[i] = max(dp[i], 1 + dp[j])"]
    D -->|No| C
    E --> C""",
        "test_cases": [{'input': 'nums = [10,9,2,5,3,7,101,18]', 'output': '4 ([2,3,7,101])'}, {'input': 'nums = [7,7,7,7,7,7,7]', 'output': '1'}],
        "js_code": """function lengthOfLIS(nums) {
    if (nums.length === 0) return 0;
    
    // Every element is an increasing subsequence of length 1
    const dp = new Array(nums.length).fill(1);
    let maxLIS = 1;
    
    for (let i = 1; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            // If current element is larger than previous
            if (nums[i] > nums[j]) {
                // Update max length at i
                dp[i] = Math.max(dp[i], 1 + dp[j]);
            }
        }
        // Track the global maximum length
        maxLIS = Math.max(maxLIS, dp[i]);
    }
    
    return maxLIS;
}""",
        "py_code": """def lengthOfLIS(nums):
    if not nums: return 0
    
    # Every element is an increasing subsequence of length 1
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            # If current element is larger than previous
            if nums[i] > nums[j]:
                # Update max length at i
                dp[i] = max(dp[i], 1 + dp[j])
                
    # Return the global maximum length
    return max(dp)""",
        "js_walkthrough": "1. <strong>DP Array:</strong> We create a `dp` array filled with `1`s because every individual element forms a valid subsequence of length 1.<br>2. <strong>Outer Loop:</strong> We iterate `i` starting from 1 up to the end of the array.<br>3. <strong>Inner Loop:</strong> For each `i`, we look back at all previous elements `j` from 0 to `i-1`.<br>4. <strong>Condition:</strong> If `nums[i] > nums[j]`, it means `nums[i]` can legally extend the subsequence ending at `j`. We update `dp[i] = Math.max(dp[i], 1 + dp[j])`.<br>5. <strong>Result:</strong> We keep track of the maximum value found in the `dp` array and return it.",
        "py_walkthrough": "1. <strong>DP Array:</strong> We initialize a list `dp` where each element is `1`, representing the minimum LIS length for any single item.<br>2. <strong>Outer Loop:</strong> We use an outer loop `i` traversing from 1 to the end.<br>3. <strong>Inner Loop:</strong> The inner loop `j` checks every index before `i`.<br>4. <strong>Condition:</strong> If `nums[i] > nums[j]`, we know `nums[i]` can strictly increase the sequence that ended at `j`. We update `dp[i]` to be the max of its current value or `1 + dp[j]`.<br>5. <strong>Result:</strong> Finally, we return the maximum value contained anywhere within the `dp` array using `max(dp)`.",
        "solution_explanation": "Time Complexity: O(N^2) due to the nested loops checking all previous elements. Note: an O(N log N) solution exists using Binary Search. Space Complexity: O(N) to store the DP array.",
    },
    {
        "title": "Longest Common Subsequence",
        "category": "2D Dynamic Programming",
        "difficulty": "Medium",
        "explanation": """Given two strings `text1` and `text2`, return the length of their longest common subsequence.

**Pattern:** 2D DP Grid. Create a 2D grid of size `(len1+1) x (len2+1)`. We iterate backwards (or forwards). If characters match, `dp[i][j] = 1 + dp[i+1][j+1]`. If they do not match, we take the max of skipping a character from text1 or text2: `dp[i][j] = max(dp[i+1][j], dp[i][j+1])`.""",
        "diagram": """flowchart TD
    A["Iterate 2D grid backward"] --> B{"text1[i] == text2[j]?"}
    B -->|Yes| C["dp[i][j] = 1 + dp[i+1][j+1] (Diagonal)"]
    B -->|No| D["dp[i][j] = max(dp[i+1][j], dp[i][j+1]) (Right or Down)"]""",
        "test_cases": [{'input': "text1 = 'abcde', text2 = 'ace'", 'output': "3 ('ace')"}, {'input': "text1 = 'abc', text2 = 'def'", 'output': '0'}],
        "js_code": """function longestCommonSubsequence(text1, text2) {
    const dp = Array.from({ length: text1.length + 1 }, () => 
        new Array(text2.length + 1).fill(0)
    );
    
    // Iterate backwards
    for (let i = text1.length - 1; i >= 0; i--) {
        for (let j = text2.length - 1; j >= 0; j--) {
            if (text1[i] === text2[j]) {
                // Match: take diagonal + 1
                dp[i][j] = 1 + dp[i + 1][j + 1];
            } else {
                // No match: max of right or bottom cell
                dp[i][j] = Math.max(dp[i + 1][j], dp[i][j + 1]);
            }
        }
    }
    
    return dp[0][0];
}""",
        "py_code": """def longestCommonSubsequence(text1, text2):
    # Create 2D grid with extra row and col for base cases (out of bounds = 0)
    dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
    
    # Iterate backwards
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                # Match: take diagonal + 1
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                # No match: max of right or bottom cell
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                
    return dp[0][0]""",
        "js_walkthrough": "1. <strong>2D Array Setup:</strong> We create a 2D array `dp` with an extra row and column filled with `0`s to handle out-of-bounds boundary conditions easily.<br>2. <strong>Reverse Iteration:</strong> We iterate backwards through both strings starting from the last characters.<br>3. <strong>Match Condition:</strong> If `text1[i] === text2[j]`, we add `1` to the result of the remaining strings (which is stored diagonally at `dp[i+1][j+1]`).<br>4. <strong>Mismatch Condition:</strong> If they don't match, we must skip a character in either `text1` or `text2`. We take the maximum of skipping in `text1` (`dp[i+1][j]`) or skipping in `text2` (`dp[i][j+1]`).<br>5. <strong>Result:</strong> After the loops, `dp[0][0]` will contain the maximum length considering both full strings.",
        "py_walkthrough": "1. <strong>2D Array Setup:</strong> We use list comprehension to create a 2D list `dp` filled with `0`s. The dimensions are `len(text1)+1` by `len(text2)+1`.<br>2. <strong>Reverse Iteration:</strong> We loop backwards (`range(n-1, -1, -1)`). Working backwards allows us to build the solution bottom-up.<br>3. <strong>Match Condition:</strong> If `text1[i] == text2[j]`, the characters match. We look diagonally down-right (`dp[i+1][j+1]`) and add 1.<br>4. <strong>Mismatch Condition:</strong> If they don't match, we carry over the maximum subsequence found so far by checking the cell to the right or the cell below.<br>5. <strong>Result:</strong> The answer propagates all the way back to the top-left cell, so we return `dp[0][0]`.",
        "solution_explanation": "Time Complexity: O(M * N) where M and N are the lengths of the strings. Space Complexity: O(M * N) to store the 2D DP grid.",
    },
    {
        "title": "Word Break",
        "category": "1D Dynamic Programming",
        "difficulty": "Medium",
        "explanation": """Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of dictionary words.

**Pattern:** Bottom-Up DP. Initialize a DP array of boolean values where `dp[i]` represents if the string *starting from index i* can be segmented. Iterate backwards. If the current substring matches a word in the dict, `dp[i] = dp[i + len(word)]`.""",
        "diagram": """flowchart TD
    A["Initialize dp[len(s)] = True"] --> B["Iterate i backward from len(s)-1"]
    B --> C["For word in wordDict:"]
    C --> D{"Substring matches word?"}
    D -->|Yes| E["dp[i] = dp[i + word.length]"]
    E --> F{"dp[i] == True?"}
    F -->|Yes| B
    F -->|No| C""",
        "test_cases": [{'input': "s = 'leetcode', wordDict = ['leet','code']", 'output': 'true'}, {'input': "s = 'catsandog', wordDict = ['cats','dog','sand','and','cat']", 'output': 'false'}],
        "js_code": """function wordBreak(s, wordDict) {
    const dp = new Array(s.length + 1).fill(false);
    dp[s.length] = true; // Base case: end of string is 'matched'
    
    for (let i = s.length - 1; i >= 0; i--) {
        for (const w of wordDict) {
            // If there's enough space for the word and it matches
            if (i + w.length <= s.length && 
                s.slice(i, i + w.length) === w) {
                
                dp[i] = dp[i + w.length];
            }
            
            // Optimization: if we already found a valid break, move to next i
            if (dp[i]) {
                break;
            }
        }
    }
    
    return dp[0];
}""",
        "py_code": """def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True # Base case
    
    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            # If there's enough space and it matches
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
                
            # Optimization: break if we found a valid path
            if dp[i]:
                break
                
    return dp[0]""",
        "js_walkthrough": "1. <strong>DP Initialization:</strong> We create a `dp` array of booleans. `dp[s.length] = true` is our base case indicating that an empty substring is technically valid.<br>2. <strong>Reverse Loop:</strong> We iterate backwards through the string `s`.<br>3. <strong>Word Check:</strong> For each index `i`, we check every word in `wordDict`. We slice the string from `i` to `i + w.length` and compare it to the word.<br>4. <strong>DP Update:</strong> If it matches, we set `dp[i]` equal to `dp[i + w.length]`. This means if the *rest* of the string was valid, then this current position is also valid.<br>5. <strong>Return:</strong> `dp[0]` will ultimately tell us if the entire string starting from index 0 is valid.",
        "py_walkthrough": "1. <strong>DP Initialization:</strong> We create a list `dp` of `False`. We set the very last element (index `len(s)`) to `True` to act as our base case anchor.<br>2. <strong>Reverse Loop:</strong> We loop backwards over the string index `i`.<br>3. <strong>Word Check:</strong> Inside the loop, we iterate through the dictionary words. We check if the string slice `s[i : i + len(w)]` exactly matches the word `w`.<br>4. <strong>DP Update:</strong> If we find a match, `dp[i]` inherits the truth value of the index immediately following the word (`dp[i + len(w)]`). We `break` early if `dp[i]` becomes `True` to save time.<br>5. <strong>Return:</strong> Returning `dp[0]` evaluates the entire string.",
        "solution_explanation": "Time Complexity: O(N * M * L) where N is string length, M is number of words, and L is max length of a word (for string slicing). Space Complexity: O(N) for the DP array.",
    },
    {
        "title": "Merge Intervals",
        "category": "Intervals",
        "difficulty": "Medium",
        "explanation": """Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals.

**Pattern:** Sorting. Sort the intervals based on the starting value. Create a result array. Iterate through the sorted intervals. If the current interval's start is less than or equal to the previous interval's end, they overlap. We merge them by updating the previous interval's end to be the max of both ends.""",
        "diagram": """flowchart LR
    A["Sort intervals by start"] --> B["Add first interval to Result"]
    B --> C["Iterate intervals"]
    C --> D{"curr.start <= last.end?"}
    D -->|Yes (Overlap)| E["last.end = max(last.end, curr.end)"]
    D -->|No| F["Result.push(curr)"]
    E --> C
    F --> C""",
        "test_cases": [{'input': 'intervals = [[1,3],[2,6],[8,10],[15,18]]', 'output': '[[1,6],[8,10],[15,18]]'}, {'input': 'intervals = [[1,4],[4,5]]', 'output': '[[1,5]]'}],
        "js_code": """function merge(intervals) {
    if (intervals.length <= 1) return intervals;
    
    // Sort intervals by their start value
    intervals.sort((a, b) => a[0] - b[0]);
    
    const res = [intervals[0]];
    
    for (let i = 1; i < intervals.length; i++) {
        const lastMerged = res[res.length - 1];
        const current = intervals[i];
        
        // If they overlap (curr start <= last end)
        if (current[0] <= lastMerged[1]) {
            // Update the end of the last merged interval
            lastMerged[1] = Math.max(lastMerged[1], current[1]);
        } else {
            // No overlap, push to result
            res.push(current);
        }
    }
    
    return res;
}""",
        "py_code": """def merge(intervals):
    if len(intervals) <= 1:
        return intervals
        
    # Sort intervals by their start value
    intervals.sort(key=lambda i: i[0])
    
    res = [intervals[0]]
    
    for start, end in intervals[1:]:
        lastEnd = res[-1][1]
        
        # If they overlap (curr start <= last end)
        if start <= lastEnd:
            # Update the end of the last merged interval
            res[-1][1] = max(lastEnd, end)
        else:
            # No overlap, push to result
            res.append([start, end])
            
    return res""",
        "js_walkthrough": "1. <strong>Edge Case:</strong> Return early if the array has 1 or fewer intervals.<br>2. <strong>Sorting:</strong> We sort the array using `a[0] - b[0]` to ensure intervals are ordered by their start times.<br>3. <strong>Initialization:</strong> We push the very first interval into our `res` (result) array.<br>4. <strong>Iteration:</strong> We loop through the remaining intervals. We compare the current interval's start `current[0]` with the end of the last interval pushed to `res`.<br>5. <strong>Merge Logic:</strong> If `current[0] <= lastMerged[1]`, we merge them by extending `lastMerged[1]` to the maximum of both ends. If there's no overlap, we simply push `current` to `res` as a distinct new interval.",
        "py_walkthrough": "1. <strong>Edge Case:</strong> Return early if the list is small.<br>2. <strong>Sorting:</strong> We sort the list using a lambda function targeting the first element (`i[0]`).<br>3. <strong>Initialization:</strong> We start our `res` list by appending the first interval from the sorted list.<br>4. <strong>Iteration:</strong> We iterate over the remaining intervals, unpacking them into `start` and `end`.<br>5. <strong>Merge Logic:</strong> We fetch `lastEnd` from `res[-1][1]`. If `start <= lastEnd`, they overlap. We mutate the last interval in `res` to take the `max()` of both ends. Otherwise, we append the new interval to `res`.",
        "solution_explanation": "Time Complexity: O(N log N) dominated by the sorting step. The iteration itself is O(N). Space Complexity: O(N) to store the result array (or O(1) auxiliary space if not counting output).",
    },
    {
        "title": "Non-overlapping Intervals",
        "category": "Intervals",
        "difficulty": "Medium",
        "explanation": """Given an array of intervals, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

**Pattern:** Greedy / Sorting. Sort intervals by start time. Iterate through. If we find an overlap, we must remove an interval. Greedily, we should remove the interval that ends *later*, because it has a higher chance of overlapping with future intervals. We simulate removal by updating the `prevEnd` pointer to the smaller of the two ends.""",
        "diagram": """flowchart TD
    A["Sort intervals by start"] --> B["prevEnd = intervals[0].end"]
    B --> C["Iterate remaining intervals"]
    C --> D{"curr.start >= prevEnd?"}
    D -->|Yes (No overlap)| E["prevEnd = curr.end"]
    D -->|No (Overlap)| F["res++ (remove one)"]
    F --> G["prevEnd = min(prevEnd, curr.end)"]
    E --> C
    G --> C""",
        "test_cases": [{'input': 'intervals = [[1,2],[2,3],[3,4],[1,3]]', 'output': '1 (Remove [1,3])'}, {'input': 'intervals = [[1,2],[1,2],[1,2]]', 'output': '2'}],
        "js_code": """function eraseOverlapIntervals(intervals) {
    if (intervals.length === 0) return 0;
    
    intervals.sort((a, b) => a[0] - b[0]);
    let res = 0;
    let prevEnd = intervals[0][1];
    
    for (let i = 1; i < intervals.length; i++) {
        const start = intervals[i][0];
        const end = intervals[i][1];
        
        if (start >= prevEnd) {
            // No overlap
            prevEnd = end;
        } else {
            // Overlap: remove the one that ends later
            res++;
            prevEnd = Math.min(prevEnd, end);
        }
    }
    
    return res;
}""",
        "py_code": """def eraseOverlapIntervals(intervals):
    if not intervals: return 0
    
    intervals.sort(key=lambda i: i[0])
    res = 0
    prevEnd = intervals[0][1]
    
    for start, end in intervals[1:]:
        if start >= prevEnd:
            # No overlap
            prevEnd = end
        else:
            # Overlap: remove the one that ends later
            res += 1
            prevEnd = min(prevEnd, end)
            
    return res""",
        "js_walkthrough": "1. <strong>Sorting:</strong> Sort the intervals by their start values.<br>2. <strong>State Variables:</strong> Initialize `res` to 0 (counter for removals) and `prevEnd` to the end time of the first interval.<br>3. <strong>Loop:</strong> Iterate from the second interval onward.<br>4. <strong>No Overlap:</strong> If `start >= prevEnd`, there's no conflict. We safely update `prevEnd` to the current interval's `end`.<br>5. <strong>Overlap Resolution:</strong> If they overlap, we increment our removal counter `res`. We simulate deleting the \"longer\" interval by setting `prevEnd` to `Math.min(prevEnd, end)`. This minimizes future conflicts.",
        "py_walkthrough": "1. <strong>Sorting:</strong> Sort the list of intervals by the start value using `lambda i: i[0]`.<br>2. <strong>State Variables:</strong> We set `res = 0` and grab the end time of the first interval as `prevEnd`.<br>3. <strong>Loop:</strong> We loop through unpacked `start, end` variables for the remaining intervals.<br>4. <strong>No Overlap:</strong> If the current `start` is after or exactly at `prevEnd`, we just update `prevEnd = end`.<br>5. <strong>Overlap Resolution:</strong> If they overlap, we must \"remove\" one. We add 1 to `res`. We retain the interval that ends sooner to greedily free up space, so we update `prevEnd = min(prevEnd, end)`.",
        "solution_explanation": "Time Complexity: O(N log N) because of the sorting step. Space Complexity: O(1) or O(N) depending on the sorting algorithm implementation.",
    },
    {
        "title": "House Robber",
        "category": "1D Dynamic Programming",
        "difficulty": "Medium",
        "explanation": """You are a professional robber planning to rob houses. Each house has a certain amount of money. You cannot rob adjacent houses. Return the maximum amount of money you can rob tonight.

**Pattern:** 1D DP. For each house, we have two choices: rob it (and add its money to the max from `house-2`), or don't rob it (and keep the max from `house-1`). We only need to store the previous two maximums (`rob1` and `rob2`) to calculate the current maximum.""",
        "diagram": """flowchart LR
    A["nums = [1, 2, 3, 1]"] --> B["rob1=0, rob2=0"]
    B --> C["House 1: max(1+0, 0) = 1"]
    C --> D["House 2: max(2+0, 1) = 2"]
    D --> E["House 3: max(3+1, 2) = 4"]
    E --> F["House 4: max(1+2, 4) = 4"]""",
        "test_cases": [{'input': 'nums = [1,2,3,1]', 'output': '4 (Rob house 1 and 3)'}, {'input': 'nums = [2,7,9,3,1]', 'output': '12 (Rob 1, 3, 5)'}],
        "js_code": """function rob(nums) {
    let rob1 = 0;
    let rob2 = 0;
    
    // [rob1, rob2, n, n+1, ...]
    for (const n of nums) {
        const temp = Math.max(n + rob1, rob2);
        rob1 = rob2;
        rob2 = temp;
    }
    
    return rob2;
}""",
        "py_code": """def rob(nums):
    rob1, rob2 = 0, 0
    
    # [rob1, rob2, n, n+1, ...]
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
        
    return rob2""",
        "js_walkthrough": "1. <strong>Variables:</strong> We initialize `rob1` and `rob2` to 0. Think of them as the max profit `i-2` and `i-1` steps ago.<br>2. <strong>Loop:</strong> We iterate over each house `n` in `nums`.<br>3. <strong>Max Logic:</strong> For the current house, the max we can rob is `Math.max(n + rob1, rob2)`. This represents picking current house + money from 2 houses ago, vs. keeping the money from the previous house.<br>4. <strong>Shift Pointers:</strong> We update `rob1 = rob2` and `rob2 = temp` to move our rolling window forward.<br>5. <strong>Result:</strong> `rob2` holds the absolute maximum money by the end.",
        "py_walkthrough": "1. <strong>Variables:</strong> `rob1` and `rob2` are initialized to 0, representing the maximum money up to two houses ago and one house ago.<br>2. <strong>Loop:</strong> We iterate through every house `n` in the array `nums`.<br>3. <strong>Max Logic:</strong> We compute `temp = max(n + rob1, rob2)`. We either rob the current house `n` (and add `rob1`) or skip it (and keep `rob2`).<br>4. <strong>Shift Pointers:</strong> `rob1` becomes `rob2`, and `rob2` takes the new max `temp`.<br>5. <strong>Result:</strong> Return `rob2`.",
        "solution_explanation": "Time Complexity: O(N) as we make one pass. Space Complexity: O(1) as we only use two variables instead of a full array.",
    },
    {
        "title": "House Robber II",
        "category": "1D Dynamic Programming",
        "difficulty": "Medium",
        "explanation": """Similar to House Robber, but the houses are arranged in a **circle**. This means the first house and the last house are adjacent.

**Pattern:** Re-use House Robber 1. Since the first and last houses are connected, we can't rob both. The answer is simply the maximum of two scenarios: Robbing from house 1 to n-1, OR robbing from house 2 to n. We run the standard `rob` helper on both sub-arrays.""",
        "diagram": """flowchart TD
    A["nums = [1, 2, 3, 1]"] --> B["Scenario 1: Skip Last House"]
    A --> C["Scenario 2: Skip First House"]
    B --> D["rob([1, 2, 3]) = 4"]
    C --> E["rob([2, 3, 1]) = 3"]
    D --> F["max(4, 3) = 4"]
    E --> F""",
        "test_cases": [{'input': 'nums = [2,3,2]', 'output': '3'}, {'input': 'nums = [1,2,3,1]', 'output': '4'}],
        "js_code": """function rob(nums) {
    if (nums.length === 1) return nums[0];
    
    // Helper is exactly House Robber I
    function robHelper(arr) {
        let rob1 = 0, rob2 = 0;
        for (const n of arr) {
            const temp = Math.max(n + rob1, rob2);
            rob1 = rob2;
            rob2 = temp;
        }
        return rob2;
    }
    
    // Max of (skip last house) vs (skip first house)
    return Math.max(
        robHelper(nums.slice(0, nums.length - 1)),
        robHelper(nums.slice(1))
    );
}""",
        "py_code": """def rob(nums):
    if len(nums) == 1:
        return nums[0]
        
    def rob_helper(arr):
        rob1, rob2 = 0, 0
        for n in arr:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        
    # Max of (skip last house) vs (skip first house)
    return max(
        rob_helper(nums[:-1]),
        rob_helper(nums[1:])
    )""",
        "js_walkthrough": "1. <strong>Edge Case:</strong> If there's only 1 house, return `nums[0]` immediately, as array slicing might empty the array otherwise.<br>2. <strong>Helper Function:</strong> We write `robHelper(arr)`, which is the exact same standard DP logic from House Robber I.<br>3. <strong>Two Scenarios:</strong> Because the street is circular, the first and last houses touch. We compute the max profit of the array excluding the last house `nums.slice(0, nums.length - 1)` and the array excluding the first house `nums.slice(1)`.<br>4. <strong>Result:</strong> We return `Math.max()` of the two scenarios.",
        "py_walkthrough": "1. <strong>Edge Case:</strong> Return `nums[0]` if length is 1 to prevent empty lists during slicing.<br>2. <strong>Helper Function:</strong> `rob_helper` executes standard House Robber 1 logic using `rob1` and `rob2`.<br>3. <strong>Two Scenarios:</strong> To bypass the circular adjacent problem, we just pretend there are two separate streets. One street excludes the last house (`nums[:-1]`), and the other excludes the first house (`nums[1:]`).<br>4. <strong>Result:</strong> Return `max()` of the two paths.",
        "solution_explanation": "Time Complexity: O(N). We run the O(N) helper twice. Space Complexity: O(N) because of array slicing, but can be optimized to O(1) if passing index pointers instead.",
    },
    {
        "title": "Decode Ways",
        "category": "1D Dynamic Programming",
        "difficulty": "Medium",
        "explanation": """A message containing letters from A-Z is encoded into numbers (A=1 ... Z=26). Given a string `s` of digits, return the number of ways to decode it.

**Pattern:** DP String parsing. We can initialize a DP array or use two variables. At step `i`, we can parse a single digit (if it's not '0'). We can also parse two digits (if they form a number between 10 and 26). We add the valid combinations.""",
        "diagram": """flowchart TD
    A["s = '226'"] --> B["dp[len] = 1"]
    B --> C["i=2 ('6'): dp[2] = dp[3] = 1"]
    C --> D["i=1 ('2'): dp[1] = dp[2] ('2') + dp[3] ('26') = 2"]
    D --> E["i=0 ('2'): dp[0] = dp[1] ('2') + dp[2] ('22') = 3"]""",
        "test_cases": [{'input': "s = '12'", 'output': "2 ('AB' or 'L')"}, {'input': "s = '226'", 'output': "3 ('BZ', 'VF', 'BBF')"}, {'input': "s = '06'", 'output': '0'}],
        "js_code": """function numDecodings(s) {
    // Edge case: string starts with 0
    if (s[0] === '0') return 0;
    
    const dp = new Array(s.length + 1).fill(0);
    // Base cases
    dp[s.length] = 1;
    
    for (let i = s.length - 1; i >= 0; i--) {
        if (s[i] === '0') {
            dp[i] = 0; // '0' is invalid on its own
            continue;
        }
        
        // Single digit parsing
        dp[i] = dp[i + 1];
        
        // Double digit parsing
        if (i + 1 < s.length && 
            (s[i] === '1' || (s[i] === '2' && '0123456'.includes(s[i+1])))) {
            dp[i] += dp[i + 2];
        }
    }
    
    return dp[0];
}""",
        "py_code": """def numDecodings(s):
    if not s or s[0] == '0': return 0
    
    dp = {len(s): 1}
    
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
            dp[i] = 0
            continue
            
        # Single digit
        dp[i] = dp[i + 1]
        
        # Double digit (10-26)
        if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
            dp[i] += dp[i + 2]
            
    return dp[0]""",
        "js_walkthrough": "1. <strong>Edge Case:</strong> If the string starts with '0', it's invalid, return 0 immediately.<br>2. <strong>DP Array:</strong> Create `dp` filled with 0s. Set `dp[s.length] = 1` as the base case empty suffix.<br>3. <strong>Reverse Iteration:</strong> Loop backwards from the end.<br>4. <strong>Zero Check:</strong> If `s[i]` is '0', it cannot be decoded standalone, so `dp[i] = 0`.<br>5. <strong>Single Digit:</strong> Otherwise, taking `s[i]` as a single letter adds `dp[i+1]` to our total ways.<br>6. <strong>Double Digit:</strong> We also check if `s[i]` and `s[i+1]` form a number between 10 and 26. If so, we add `dp[i+2]` ways to `dp[i]`.<br>7. <strong>Return:</strong> Return `dp[0]`.",
        "py_walkthrough": "1. <strong>Edge Case:</strong> Return 0 if the string starts with '0'.<br>2. <strong>DP Hash Map:</strong> We use a dictionary `dp` for caching, setting `dp[len(s)] = 1` as the base case.<br>3. <strong>Reverse Loop:</strong> We iterate backward. If `s[i] == '0'`, `dp[i]` is 0.<br>4. <strong>Single Digit:</strong> A valid non-zero digit at `i` gives us at least `dp[i+1]` ways.<br>5. <strong>Double Digit Check:</strong> If the current digit is '1', OR the current digit is '2' and the next is between '0'-'6', it forms a valid 2-digit number (10-26). We add `dp[i+2]` to our total.<br>6. <strong>Result:</strong> `dp[0]` yields the final distinct decodings.",
        "solution_explanation": "Time Complexity: O(N) since we process each character once. Space Complexity: O(N) for the DP array (can be O(1) using two variables).",
    },
    {
        "title": "Unique Paths",
        "category": "2D Dynamic Programming",
        "difficulty": "Medium",
        "explanation": """A robot is located at the top-left corner of an `m x n` grid. It can only move either down or right at any point in time. Return the number of unique paths to reach the bottom-right corner.

**Pattern:** 2D DP. Start by initializing the bottom row to 1s. Then build upward. For any cell `dp[r][c]`, the number of ways to reach the end is `dp[r+1][c]` (going down) plus `dp[r][c+1]` (going right). We can optimize space by only keeping the previous row.""",
        "diagram": """flowchart TD
    A["Initialize row = [1, 1, 1...]"] --> B["For each row r above bottom:"]
    B --> C["newRow = [1, 1, 1...]"]
    C --> D["For col c right to left:"]
    D --> E["newRow[c] = newRow[c+1] + row[c]"]
    E --> F["row = newRow"]""",
        "test_cases": [{'input': 'm = 3, n = 7', 'output': '28'}, {'input': 'm = 3, n = 2', 'output': '3'}],
        "js_code": """function uniquePaths(m, n) {
    // Keep track of the row below us
    let row = new Array(n).fill(1);
    
    // Go from second-to-last row up to the top
    for (let i = 0; i < m - 1; i++) {
        const newRow = new Array(n).fill(1);
        
        // Go from second-to-last column to the left
        for (let j = n - 2; j >= 0; j--) {
            // Right cell + Bottom cell
            newRow[j] = newRow[j + 1] + row[j];
        }
        row = newRow;
    }
    
    return row[0];
}""",
        "py_code": """def uniquePaths(m, n):
    # The bottom row is all 1s
    row = [1] * n
    
    # Iterate through all other rows bottom-up
    for i in range(m - 1):
        newRow = [1] * n
        
        # Calculate from right to left
        for j in range(n - 2, -1, -1):
            # Right + Down
            newRow[j] = newRow[j + 1] + row[j]
            
        row = newRow
        
    return row[0]""",
        "js_walkthrough": "1. <strong>Initialize Row:</strong> We create an array `row` filled with `1`s representing the bottom-most row of the grid. It only has 1 way to reach the target (keep moving right).<br>2. <strong>Row Iteration:</strong> We loop `m - 1` times to build the grid upwards row by row.<br>3. <strong>Column Iteration:</strong> Inside, we create `newRow` and loop backwards from `n - 2` down to 0.<br>4. <strong>DP Relation:</strong> The value at `newRow[j]` is the cell to its right `newRow[j+1]` plus the cell directly below it `row[j]`.<br>5. <strong>Shift:</strong> We set `row = newRow` to move up to the next row.<br>6. <strong>Result:</strong> `row[0]` is the top-left cell's value.",
        "py_walkthrough": "1. <strong>Initialize Row:</strong> `row = [1] * n` acts as our bottom boundary. <br>2. <strong>Row Loop:</strong> We iterate `m - 1` times to generate the rows above it, starting from the second-to-bottom.<br>3. <strong>Column Loop:</strong> We create `newRow` and compute values backwards (`range(n - 2, -1, -1)`).<br>4. <strong>DP Relation:</strong> `newRow[j]` is the sum of moving right (`newRow[j + 1]`) and moving down (`row[j]`).<br>5. <strong>Shift:</strong> We replace `row` with `newRow` for the next vertical iteration.<br>6. <strong>Result:</strong> Finally, `row[0]` holds the result for the starting cell.",
        "solution_explanation": "Time Complexity: O(M * N) since we visit every cell in the grid. Space Complexity: O(N) because we only keep track of a single row of size N, rather than the entire M*N grid.",
    },
    {
        "title": "Jump Game",
        "category": "Greedy",
        "difficulty": "Medium",
        "explanation": """You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return `true` if you can reach the last index.

**Pattern:** Greedy. We shift the `goal` post backwards from the end of the array. At each index `i`, we check if `i + nums[i] >= goal`. If it is, we can reach the goal from `i`, so we update `goal = i`.""",
        "diagram": """flowchart LR
    A["Goal = len(nums) - 1"] --> B["Iterate backwards"]
    B --> C{"i + nums[i] >= Goal?"}
    C -->|Yes| D["Goal = i"]
    C -->|No| B
    D --> E{"Goal == 0?"}""",
        "test_cases": [{'input': 'nums = [2,3,1,1,4]', 'output': 'true'}, {'input': 'nums = [3,2,1,0,4]', 'output': 'false'}],
        "js_code": """function canJump(nums) {
    let goal = nums.length - 1;
    
    // Iterate backwards
    for (let i = nums.length - 2; i >= 0; i--) {
        // If we can reach the goal from current position
        if (i + nums[i] >= goal) {
            goal = i; // Move goalpost closer to start
        }
    }
    
    // True if goal reaches index 0
    return goal === 0;
}""",
        "py_code": """def canJump(nums):
    goal = len(nums) - 1
    
    # Iterate backwards
    for i in range(len(nums) - 2, -1, -1):
        # If we can reach the goal from current position
        if i + nums[i] >= goal:
            goal = i # Move goalpost closer to start
            
    # True if goal reaches index 0
    return goal == 0""",
        "js_walkthrough": "1. <strong>Goal Variable:</strong> We set `goal` to the very last index of the array.<br>2. <strong>Reverse Iteration:</strong> We loop backward from the second-to-last element (`length - 2`) down to `0`.<br>3. <strong>Reachability Check:</strong> We check if the current index `i` plus the jump distance `nums[i]` is greater than or equal to the `goal`.<br>4. <strong>Update Goal:</strong> If it is, it means from index `i`, we can leap to the `goal` (or past it). Thus, `i` becomes our new `goal`.<br>5. <strong>Result:</strong> If the `goal` successfully shifts all the way back to `0`, we return `true`.",
        "py_walkthrough": "1. <strong>Goal Post:</strong> Set `goal` equal to `len(nums) - 1`.<br>2. <strong>Reverse Loop:</strong> Traverse the list in reverse from `len(nums) - 2` down to `0`.<br>3. <strong>Check Reach:</strong> For each step `i`, `i + nums[i]` calculates the furthest index we can jump to. If this is `>= goal`, the path is valid.<br>4. <strong>Shift Goal:</strong> If valid, we shift the `goal` to `i`. We now only need to prove we can reach `i` from earlier steps.<br>5. <strong>Result:</strong> Return `goal == 0` at the end.",
        "solution_explanation": "Time Complexity: O(N) as we do a single pass backward. Space Complexity: O(1) as we only use a single pointer.",
    },
    {
        "title": "Combination Sum",
        "category": "Backtracking",
        "difficulty": "Medium",
        "explanation": """Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations where the chosen numbers sum to `target`. You may use the same number an unlimited number of times.

**Pattern:** Backtracking / DFS. We define a recursive function that keeps track of the current combination array, current sum, and current index. At each step, we can either: 1) add the current candidate and stay at the same index (unlimited usage), or 2) skip the candidate and move to the next index.""",
        "diagram": """flowchart TD
    A["dfs(i, currentPath, currentSum)"] --> B{"currentSum == target?"}
    B -->|Yes| C["Add to Result"]
    B -->|No| D{"currentSum > target or i >= len?"}
    D -->|Yes| E["Return (Backtrack)"]
    D -->|No| F["Branch 1: include candidates[i]"]
    D -->|No| G["Branch 2: skip candidates[i]"]
    F --> H["dfs(i, path + c[i], sum + c[i])"]
    G --> I["dfs(i + 1, path, sum)"]""",
        "test_cases": [{'input': 'candidates = [2,3,6,7], target = 7', 'output': '[[2,2,3],[7]]'}, {'input': 'candidates = [2,3,5], target = 8', 'output': '[[2,2,2,2],[2,3,3],[3,5]]'}],
        "js_code": """function combinationSum(candidates, target) {
    const res = [];
    
    function dfs(i, currentCombination, currentSum) {
        if (currentSum === target) {
            res.push([...currentCombination]);
            return;
        }
        if (i >= candidates.length || currentSum > target) {
            return;
        }
        
        // Decision 1: Include current candidate (stay at same index i)
        currentCombination.push(candidates[i]);
        dfs(i, currentCombination, currentSum + candidates[i]);
        
        // Decision 2: Don't include, move to next candidate (i + 1)
        currentCombination.pop(); // backtrack
        dfs(i + 1, currentCombination, currentSum);
    }
    
    dfs(0, [], 0);
    return res;
}""",
        "py_code": """def combinationSum(candidates, target):
    res = []
    
    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return
            
        # Decision 1: Include current candidate (stay at same index i)
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        
        # Decision 2: Don't include, move to next candidate (i + 1)
        cur.pop() # backtrack
        dfs(i + 1, cur, total)
        
    dfs(0, [], 0)
    return res""",
        "js_walkthrough": "1. <strong>Setup:</strong> Initialize `res` array. Create a `dfs` recursive function.<br>2. <strong>Base Case (Success):</strong> If `currentSum === target`, we found a combination. Push a *copy* of `currentCombination` to `res` and return.<br>3. <strong>Base Case (Fail):</strong> If `currentSum > target` or we run out of elements (`i >= candidates.length`), we return immediately to kill this invalid branch.<br>4. <strong>Branch 1 (Include):</strong> We push `candidates[i]` to our array and call `dfs` again with `i` (so we can use it again) and an increased sum.<br>5. <strong>Branch 2 (Skip):</strong> We `.pop()` the item we just added (this is the backtracking step) and call `dfs` with `i + 1` to skip to the next number.",
        "py_walkthrough": "1. <strong>Setup:</strong> Create `res` list. Define nested `dfs` function to track index `i`, path list `cur`, and running sum `total`.<br>2. <strong>Base Case (Success):</strong> If `total == target`, append `cur.copy()` to `res`. We must copy, otherwise future pops will mutate the saved answer.<br>3. <strong>Base Case (Fail):</strong> If `total > target` or index is out of bounds, stop this branch.<br>4. <strong>Branch 1 (Include):</strong> Append the current number, then recurse. Keep index `i` the same because we can reuse numbers.<br>5. <strong>Branch 2 (Skip):</strong> Remove the number via `cur.pop()`, then recurse on `i + 1` without adding anything to total.",
        "solution_explanation": "Time Complexity: O(2^T) where T is the target, as in the worst case (e.g. target 10, candidates=[1]) the tree is deep. Space Complexity: O(T) for the recursion stack.",
    },
    {
        "title": "Meeting Rooms II",
        "category": "Intervals",
        "difficulty": "Medium",
        "explanation": """Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]`, find the minimum number of conference rooms required.

**Pattern:** Array / Two Pointers. Instead of standard sorting of intervals, extract all `start` times and all `end` times into two separate sorted arrays. Use two pointers (`s` and `e`) to iterate. If a meeting starts before the previous one ends, we need a new room. If it starts after, a room just freed up.""",
        "diagram": """flowchart TD
    A["Sort starts: [0, 5, 15]"] --> B["Sort ends: [10, 20, 30]"]
    B --> C["s = 0, e = 0, count = 0, max = 0"]
    C --> D{"starts[s] < ends[e]?"}
    D -->|Yes (Meeting starts)| E["count++, s++"]
    D -->|No (Meeting ends)| F["count--, e++"]
    E --> G["max = Math.max(max, count)"]
    F --> G""",
        "test_cases": [{'input': 'intervals = [[0,30],[5,10],[15,20]]', 'output': '2'}, {'input': 'intervals = [[7,10],[2,4]]', 'output': '1'}],
        "js_code": """function minMeetingRooms(intervals) {
    if (intervals.length === 0) return 0;
    
    // Separate and sort start and end times
    const starts = intervals.map(i => i[0]).sort((a, b) => a - b);
    const ends = intervals.map(i => i[1]).sort((a, b) => a - b);
    
    let res = 0, count = 0;
    let s = 0, e = 0;
    
    while (s < intervals.length) {
        if (starts[s] < ends[e]) {
            // A meeting starts before the earliest ending meeting
            count++;
            s++;
        } else {
            // A meeting ends
            count--;
            e++;
        }
        res = Math.max(res, count);
    }
    
    return res;
}""",
        "py_code": """def minMeetingRooms(intervals):
    if not intervals: return 0
    
    # Separate and sort start and end times
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    
    res, count = 0, 0
    s, e = 0, 0
    
    while s < len(intervals):
        if starts[s] < ends[e]:
            # A meeting starts before earliest ending meeting
            count += 1
            s += 1
        else:
            # A meeting ends
            count -= 1
            e += 1
            
        res = max(res, count)
        
    return res""",
        "js_walkthrough": "1. <strong>Extract & Sort:</strong> Create two flat arrays: `starts` and `ends`. Sort them both in ascending order.<br>2. <strong>Pointers:</strong> Initialize pointer `s` for starts array, and `e` for ends array. Set `count` (current rooms) and `res` (max rooms) to 0.<br>3. <strong>Iteration:</strong> Loop while `s` is less than total meetings.<br>4. <strong>Start Check:</strong> If `starts[s] < ends[e]`, it means the next chronological event is a meeting starting. We increment `count` and move `s`.<br>5. <strong>End Check:</strong> Otherwise, a meeting ends. We decrement `count` and move `e`.<br>6. <strong>Track Max:</strong> Update `res = Math.max(res, count)` at each step.",
        "py_walkthrough": "1. <strong>Extract & Sort:</strong> Use list comprehensions to create a list of `starts` and a list of `ends`. `sorted()` handles the numerical sorting.<br>2. <strong>Pointers:</strong> Use `s` and `e` pointers initialized to 0. `count` tracks active rooms, `res` tracks the peak number of rooms.<br>3. <strong>Iteration:</strong> Use a `while` loop that runs until we've processed all start times.<br>4. <strong>Start vs End Check:</strong> If `starts[s] < ends[e]`, a new meeting is starting before any current meeting ends. We add 1 room. If it's `>=` a meeting ends, freeing a room.<br>5. <strong>Track Max:</strong> Record the maximum concurrent rooms in `res`.",
        "solution_explanation": "Time Complexity: O(N log N) because sorting both arrays is the dominant operation. Space Complexity: O(N) to store the starts and ends arrays.",
    },
    {
        "title": "Insert Interval",
        "category": "Intervals",
        "difficulty": "Medium",
        "explanation": """You are given an array of non-overlapping intervals sorted by their start time, and a `newInterval`. Insert `newInterval` such that the intervals are still sorted and non-overlapping (merge if necessary).

**Pattern:** Iteration. Since intervals are sorted, we can iterate through them and place the `newInterval` in exactly one of three states: 1) Before the current interval, 2) After the current interval, 3) Overlapping with the current interval (so we merge them into `newInterval`).""",
        "diagram": """flowchart TD
    A["Iterate intervals"] --> B{"new.end < curr.start?"}
    B -->|Yes| C["Push new, then push rest, Return"]
    B -->|No| D{"new.start > curr.end?"}
    D -->|Yes| E["Push curr"]
    D -->|No (Overlap)| F["new = [min(start), max(end)]"]
    F --> A""",
        "test_cases": [{'input': 'intervals = [[1,3],[6,9]], newInterval = [2,5]', 'output': '[[1,5],[6,9]]'}, {'input': 'intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]', 'output': '[[1,2],[3,10],[12,16]]'}],
        "js_code": """function insert(intervals, newInterval) {
    const res = [];
    
    for (let i = 0; i < intervals.length; i++) {
        const curr = intervals[i];
        
        // Case 1: newInterval comes BEFORE curr interval
        if (newInterval[1] < curr[0]) {
            res.push(newInterval);
            return res.concat(intervals.slice(i));
        }
        // Case 2: newInterval comes AFTER curr interval
        else if (newInterval[0] > curr[1]) {
            res.push(curr);
        }
        // Case 3: Overlap, merge them into newInterval
        else {
            newInterval = [
                Math.min(newInterval[0], curr[0]),
                Math.max(newInterval[1], curr[1])
            ];
        }
    }
    
    res.push(newInterval);
    return res;
}""",
        "py_code": """def insert(intervals, newInterval):
    res = []
    
    for i in range(len(intervals)):
        curr = intervals[i]
        
        # Case 1: newInterval comes BEFORE curr interval
        if newInterval[1] < curr[0]:
            res.append(newInterval)
            return res + intervals[i:]
            
        # Case 2: newInterval comes AFTER curr interval
        elif newInterval[0] > curr[1]:
            res.append(curr)
            
        # Case 3: Overlap, merge them into newInterval
        else:
            newInterval = [
                min(newInterval[0], curr[0]),
                max(newInterval[1], curr[1])
            ]
            
    res.append(newInterval)
    return res""",
        "js_walkthrough": "1. <strong>Setup:</strong> We initialize an empty result array `res`.<br>2. <strong>Iteration:</strong> We loop through each interval `curr`.<br>3. <strong>Case 1 (Before):</strong> If `newInterval` ends before `curr` starts, it belongs exactly here without overlap. We push it, concat the rest of the array, and return immediately.<br>4. <strong>Case 2 (After):</strong> If `newInterval` starts after `curr` ends, `curr` is safe. Push `curr` and continue.<br>5. <strong>Case 3 (Overlap):</strong> The intervals intersect. We mutate `newInterval` to engulf both, expanding its start and end bounds.<br>6. <strong>Final Step:</strong> If the loop finishes without hitting Case 1, `newInterval` goes at the very end.",
        "py_walkthrough": "1. <strong>Setup:</strong> Initialize `res` list.<br>2. <strong>Iteration:</strong> Use a `for` loop to check each `curr` interval.<br>3. <strong>Case 1 (Before):</strong> `newInterval[1] < curr[0]`. The new interval sits entirely to the left. Append it, and return the `res` plus the remaining `intervals[i:]` list.<br>4. <strong>Case 2 (After):</strong> `newInterval[0] > curr[1]`. The new interval sits to the right. Append `curr` to the result.<br>5. <strong>Case 3 (Overlap):</strong> They clash. Redefine `newInterval` taking `min` of starts and `max` of ends.<br>6. <strong>Final Step:</strong> If we never triggered Case 1, `newInterval` is the rightmost element. Append it manually at the end.",
        "solution_explanation": "Time Complexity: O(N) as we do a single linear scan of the intervals. Space Complexity: O(N) to store the newly created output array.",
    }
,
{'title': 'Missing Number', 'category': 'Bit Manipulation', 'difficulty': 'Easy', 'explanation': "Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.\n\n**Pattern:** Gauss' Formula or XOR. The sum of numbers from 0 to n is `n * (n + 1) / 2`. If we subtract the sum of our array from this expected sum, the result is the missing number. Alternatively, XOR-ing all indices and array values leaves only the missing number.", 'diagram': 'flowchart LR\n    A["nums = [3,0,1], n = 3"] --> B["Expected sum = 3 * 4 / 2 = 6"]\n    B --> C["Actual sum = 3 + 0 + 1 = 4"]\n    C --> D["Missing = 6 - 4 = 2"]', 'test_cases': [{'input': 'nums = [3,0,1]', 'output': '2'}, {'input': 'nums = [0,1]', 'output': '2'}], 'js_code': 'function missingNumber(nums) {\n    const n = nums.length;\n    let expectedSum = (n * (n + 1)) / 2;\n    let actualSum = 0;\n    \n    for (let i = 0; i < n; i++) {\n        actualSum += nums[i];\n    }\n    \n    return expectedSum - actualSum;\n}', 'py_code': 'def missingNumber(nums):\n    n = len(nums)\n    expected_sum = n * (n + 1) // 2\n    actual_sum = sum(nums)\n    \n    return expected_sum - actual_sum', 'js_walkthrough': "1. <strong>Array Length:</strong> Get `n`, the length of the array.<br>2. <strong>Expected Sum:</strong> Calculate the sum of `1...n` using Gauss's formula `(n * (n + 1)) / 2`.<br>3. <strong>Actual Sum:</strong> Loop through the array to sum up all the numbers present.<br>4. <strong>Result:</strong> Subtract the `actualSum` from the `expectedSum` to find exactly which number is missing.", 'py_walkthrough': "1. <strong>Array Length:</strong> Store the length of the array in `n`.<br>2. <strong>Expected Sum:</strong> Calculate the mathematical sum of the series `0...n` using `n * (n + 1) // 2`.<br>3. <strong>Actual Sum:</strong> Use Python's built-in `sum()` function to get the total of the list.<br>4. <strong>Result:</strong> The missing number is simply `expected_sum - actual_sum`.", 'solution_explanation': 'Time Complexity: O(N) to sum the array. Space Complexity: O(1) as we only use variables.'},
{'title': 'Counting Bits', 'category': 'Bit Manipulation', 'difficulty': 'Easy', 'explanation': "Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (0 <= i <= n), `ans[i]` is the number of `1`'s in the binary representation of `i`.\n\n**Pattern:** Dynamic Programming / Bit Manipulation. The number of 1s in a number `i` is the same as the number of 1s in `i / 2` (bit shifted right by 1) plus `i % 2` (the least significant bit). So, `dp[i] = dp[i >> 1] + (i & 1)`.", 'diagram': 'flowchart TD\n    A["dp = [0]"] --> B["i=1: dp[1] = dp[0] + (1&1) = 1"]\n    B --> C["i=2: dp[2] = dp[1] + (2&1) = 1"]\n    C --> D["i=3: dp[3] = dp[1] + (3&1) = 2"]\n    D --> E["i=4: dp[4] = dp[2] + (4&1) = 1"]', 'test_cases': [{'input': 'n = 2', 'output': '[0,1,1]'}, {'input': 'n = 5', 'output': '[0,1,1,2,1,2]'}], 'js_code': 'function countBits(n) {\n    const dp = new Array(n + 1).fill(0);\n    \n    for (let i = 1; i <= n; i++) {\n        // Shift right by 1 (i >> 1) and add LSB (i & 1)\n        dp[i] = dp[i >> 1] + (i & 1);\n    }\n    \n    return dp;\n}', 'py_code': 'def countBits(n):\n    dp = [0] * (n + 1)\n    \n    for i in range(1, n + 1):\n        # Shift right by 1 (i >> 1) and add LSB (i & 1)\n        dp[i] = dp[i >> 1] + (i & 1)\n        \n    return dp', 'js_walkthrough': "1. <strong>DP Array:</strong> Create a `dp` array of length `n + 1` filled with `0`. `dp[0] = 0` since 0 has zero 1-bits.<br>2. <strong>Iteration:</strong> Loop from 1 up to `n`.<br>3. <strong>Bit Shift Math:</strong> For any number `i`, shifting it right by 1 bit (`i >> 1`) is equivalent to floor division by 2. We already know the bit count for `i >> 1` because it's earlier in our `dp` array.<br>4. <strong>LSB check:</strong> The only missing bit is the least significant bit, which we check with `i & 1`.<br>5. <strong>Result:</strong> Assign the sum to `dp[i]` and return the array at the end.", 'py_walkthrough': "1. <strong>DP Array:</strong> Initialize a list `dp` of zeros of size `n + 1`.<br>2. <strong>Loop:</strong> Iterate `i` from 1 to `n`.<br>3. <strong>Bit Math:</strong> A number's bits are identical to its half (`i >> 1`), plus whether it is odd or even (`i & 1`).<br>4. <strong>DP Cache:</strong> We set `dp[i] = dp[i >> 1] + (i & 1)`, looking up the bit count of the halved number from our cache.<br>5. <strong>Result:</strong> Return `dp`.", 'solution_explanation': 'Time Complexity: O(N) as we do one pass. Space Complexity: O(N) for the resulting array.'},
{'title': 'Reverse Bits', 'category': 'Bit Manipulation', 'difficulty': 'Easy', 'explanation': 'Reverse bits of a given 32 bits unsigned integer.\n\n**Pattern:** Bitwise Iteration. Create a result variable. Iterate 32 times. At each step, shift the result left by 1 to make room. Extract the rightmost bit of the input number using `n & 1`. Add that bit to the result using bitwise OR `|`. Finally, shift the input number right by 1.', 'diagram': 'flowchart TD\n    A["res = 0"] --> B["Loop 32 times:"]\n    B --> C["bit = n & 1"]\n    C --> D["res = (res << 1) | bit"]\n    D --> E["n = n >> 1"]\n    E --> B', 'test_cases': [{'input': 'n = 00000010100101000001111010011100', 'output': '964176192 (00111001011110000010100101000000)'}], 'js_code': 'function reverseBits(n) {\n    let res = 0;\n    \n    for (let i = 0; i < 32; i++) {\n        // Shift res to the left to make room\n        res = res * 2; // In JS, bitwise shift can have sign issues, *2 is safer for unsigned\n        \n        // Add the rightmost bit of n\n        res += (n & 1);\n        \n        // Logical right shift n by 1 (unsigned)\n        n = n >>> 1;\n    }\n    \n    return res;\n}', 'py_code': 'def reverseBits(n):\n    res = 0\n    \n    for i in range(32):\n        # Get rightmost bit\n        bit = (n >> i) & 1\n        \n        # Place it in its reversed position\n        res = res | (bit << (31 - i))\n        \n    return res', 'js_walkthrough': "1. <strong>Initialization:</strong> Set `res = 0`.<br>2. <strong>Iteration:</strong> Loop 32 times since it's a 32-bit integer.<br>3. <strong>Shift Res:</strong> Multiply `res` by 2 (equivalent to `res << 1` but avoids JS 32-bit signed overflow issues).<br>4. <strong>Extract Bit:</strong> Add `(n & 1)` to `res`. This pulls the least significant bit from `n`.<br>5. <strong>Shift N:</strong> Use the unsigned right shift operator `n >>> 1` to move the next bit to the LSB spot.<br>6. <strong>Result:</strong> Return `res`.", 'py_walkthrough': '1. <strong>Initialization:</strong> Set `res = 0`.<br>2. <strong>Iteration:</strong> Loop `i` from 0 to 31.<br>3. <strong>Extract Bit:</strong> We shift `n` right by `i` positions and bitwise AND with `1` to isolate the `i`th bit.<br>4. <strong>Place Bit:</strong> We then shift that bit left by `(31 - i)` positions, putting it in its mirror position on the other side.<br>5. <strong>Accumulate:</strong> We use bitwise OR `|` to merge it into `res`.<br>6. <strong>Result:</strong> Return `res`.', 'solution_explanation': 'Time Complexity: O(1) since the loop always runs exactly 32 times. Space Complexity: O(1).'},
{'title': 'Set Matrix Zeroes', 'category': 'Matrix', 'difficulty': 'Medium', 'explanation': "Given an `m x n` integer matrix, if an element is 0, set its entire row and column to 0's in-place.\n\n**Pattern:** Matrix Markers. Instead of using O(M*N) extra space to track zeros, use the first row and first column of the matrix itself to store flags. If `matrix[r][c] == 0`, mark `matrix[r][0] = 0` and `matrix[0][c] = 0`. Since the first row and column overlap at `[0][0]`, use an extra variable for the first row's flag.", 'diagram': 'flowchart TD\n    A["Iterate Matrix"] --> B{"Cell == 0?"}\n    B -->|Yes| C["Mark first element of its row and col as 0"]\n    B -->|No| A\n    C --> D["Iterate skipping first row/col"]\n    D --> E{"Is row flag or col flag 0?"}\n    E -->|Yes| F["Set Cell to 0"]\n    F --> G["Zero out first row/col if their markers demand it"]', 'test_cases': [{'input': 'matrix = [[1,1,1],[1,0,1],[1,1,1]]', 'output': '[[1,0,1],[0,0,0],[1,0,1]]'}, {'input': 'matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]', 'output': '[[0,0,0,0],[0,4,5,0],[0,3,1,0]]'}], 'js_code': 'function setZeroes(matrix) {\n    const rows = matrix.length;\n    const cols = matrix[0].length;\n    let rowZero = false; // Flag for first row\n    \n    // Pass 1: Mark zeros\n    for (let r = 0; r < rows; r++) {\n        for (let c = 0; c < cols; c++) {\n            if (matrix[r][c] === 0) {\n                matrix[0][c] = 0; // Mark column\n                if (r > 0) matrix[r][0] = 0; // Mark row\n                else rowZero = true; // Mark first row separately\n            }\n        }\n    }\n    \n    // Pass 2: Zero out based on marks (skip first row and col)\n    for (let r = 1; r < rows; r++) {\n        for (let c = 1; c < cols; c++) {\n            if (matrix[0][c] === 0 || matrix[r][0] === 0) {\n                matrix[r][c] = 0;\n            }\n        }\n    }\n    \n    // Pass 3: Zero out first col if needed\n    if (matrix[0][0] === 0) {\n        for (let r = 0; r < rows; r++) matrix[r][0] = 0;\n    }\n    \n    // Pass 4: Zero out first row if needed\n    if (rowZero) {\n        for (let c = 0; c < cols; c++) matrix[0][c] = 0;\n    }\n}', 'py_code': 'def setZeroes(matrix):\n    rows, cols = len(matrix), len(matrix[0])\n    rowZero = False # Flag for first row\n    \n    # Pass 1: Mark zeros\n    for r in range(rows):\n        for c in range(cols):\n            if matrix[r][c] == 0:\n                matrix[0][c] = 0 # Mark col\n                if r > 0:\n                    matrix[r][0] = 0 # Mark row\n                else:\n                    rowZero = True\n                    \n    # Pass 2: Zero out based on marks\n    for r in range(1, rows):\n        for c in range(1, cols):\n            if matrix[0][c] == 0 or matrix[r][0] == 0:\n                matrix[r][c] = 0\n                \n    # Pass 3: Zero out first col\n    if matrix[0][0] == 0:\n        for r in range(rows):\n            matrix[r][0] = 0\n            \n    # Pass 4: Zero out first row\n    if rowZero:\n        for c in range(cols):\n            matrix[0][c] = 0', 'js_walkthrough': '1. <strong>Flags setup:</strong> We use the first row and column of the matrix itself to store whether a whole row or column needs to be zeroed. Because `matrix[0][0]` overlaps, we use `rowZero` to explicitly track the 0th row.<br>2. <strong>Pass 1:</strong> Iterate the matrix. If a cell is 0, set its corresponding top-most and left-most cell to 0.<br>3. <strong>Pass 2:</strong> Iterate again, starting from index 1. If the top cell or left cell is 0, make the current cell 0.<br>4. <strong>Pass 3 & 4:</strong> Check `matrix[0][0]` to see if the first column needs zeroing. Check `rowZero` to see if the first row needs zeroing. This completes the in-place replacement.', 'py_walkthrough': "1. <strong>Flags setup:</strong> We dedicate the first row and first column to act as markers for zeroing out lines. We use a boolean `rowZero` exclusively for the first row.<br>2. <strong>Pass 1:</strong> For every `0` found, we project it to the borders (`matrix[0][c] = 0` and `matrix[r][0] = 0`).<br>3. <strong>Pass 2:</strong> Loop from `r=1` and `c=1`. We check the border markers. If either the row's marker or col's marker is `0`, we zero out the cell.<br>4. <strong>Borders:</strong> Finally, we resolve the first column depending on `matrix[0][0]`, and the first row depending on `rowZero`.", 'solution_explanation': 'Time Complexity: O(M * N) since we do two passes. Space Complexity: O(1) strictly constant in-place space.'},
{'title': 'Spiral Matrix', 'category': 'Matrix', 'difficulty': 'Medium', 'explanation': 'Given an `m x n` matrix, return all elements of the matrix in spiral order.\n\n**Pattern:** Four Pointers. Keep track of four boundaries: `left`, `right`, `top`, `bottom`. Use a loop to iterate left-to-right (top row), top-to-bottom (right col), right-to-left (bottom row), and bottom-to-top (left col). After traversing a boundary, shrink it.', 'diagram': 'flowchart TD\n    A["Initialize top, bottom, left, right boundaries"] --> B["While left < right AND top < bottom"]\n    B --> C["Traverse top row, top++"]\n    C --> D["Traverse right col, right--"]\n    D --> E{"Condition check (avoid duplicates)"}\n    E --> F["Traverse bottom row, bottom--"]\n    F --> G["Traverse left col, left++"]\n    G --> B', 'test_cases': [{'input': 'matrix = [[1,2,3],[4,5,6],[7,8,9]]', 'output': '[1,2,3,6,9,8,7,4,5]'}, {'input': 'matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]', 'output': '[1,2,3,4,8,12,11,10,9,5,6,7]'}], 'js_code': 'function spiralOrder(matrix) {\n    const res = [];\n    let left = 0, right = matrix[0].length;\n    let top = 0, bottom = matrix.length;\n    \n    while (left < right && top < bottom) {\n        // Get every i in the top row\n        for (let i = left; i < right; i++) res.push(matrix[top][i]);\n        top++;\n        \n        // Get every i in the right col\n        for (let i = top; i < bottom; i++) res.push(matrix[i][right - 1]);\n        right--;\n        \n        // Check if matrix is 1D (prevents duplicate reverse traversal)\n        if (!(left < right && top < bottom)) break;\n        \n        // Get every i in the bottom row\n        for (let i = right - 1; i >= left; i--) res.push(matrix[bottom - 1][i]);\n        bottom--;\n        \n        // Get every i in the left col\n        for (let i = bottom - 1; i >= top; i--) res.push(matrix[i][left]);\n        left++;\n    }\n    \n    return res;\n}', 'py_code': 'def spiralOrder(matrix):\n    res = []\n    left, right = 0, len(matrix[0])\n    top, bottom = 0, len(matrix)\n    \n    while left < right and top < bottom:\n        # Get every i in the top row\n        for i in range(left, right):\n            res.append(matrix[top][i])\n        top += 1\n        \n        # Get every i in the right col\n        for i in range(top, bottom):\n            res.append(matrix[i][right - 1])\n        right -= 1\n        \n        # Break out if boundaries crossed\n        if not (left < right and top < bottom):\n            break\n            \n        # Get every i in the bottom row\n        for i in range(right - 1, left - 1, -1):\n            res.append(matrix[bottom - 1][i])\n        bottom -= 1\n        \n        # Get every i in the left col\n        for i in range(bottom - 1, top - 1, -1):\n            res.append(matrix[i][left])\n        left += 1\n        \n    return res', 'js_walkthrough': "1. <strong>Boundaries:</strong> Define `left`, `right`, `top`, and `bottom`. Note `right` and `bottom` are set to `length` (out of bounds).<br>2. <strong>Loop:</strong> Run while boundaries haven't crossed.<br>3. <strong>Top Row:</strong> Loop `i` from `left` to `right-1`. Push cells from `matrix[top]`. Increment `top`.<br>4. <strong>Right Col:</strong> Loop `i` from `top` to `bottom-1`. Push cells from `matrix[...][right-1]`. Decrement `right`.<br>5. <strong>Safety Break:</strong> If `left >= right` or `top >= bottom` after shifting, `break` early to avoid parsing the same row/col backward.<br>6. <strong>Bottom Row & Left Col:</strong> Same looping logic backwards, adjusting `bottom` and `left` inward.", 'py_walkthrough': '1. <strong>Boundaries:</strong> `left` and `top` are 0. `right` is columns count, `bottom` is rows count.<br>2. <strong>Loop:</strong> Run while `left < right` and `top < bottom`.<br>3. <strong>Top Row:</strong> Loop left to right. Append `matrix[top][i]`. Increment `top`.<br>4. <strong>Right Col:</strong> Loop top to bottom. Append `matrix[i][right-1]`. Decrement `right`.<br>5. <strong>Safety Break:</strong> Check if boundaries crossed after shrinking. If so, `break`.<br>6. <strong>Bottom Row & Left Col:</strong> Loop right to left, decrement `bottom`. Loop bottom to top, increment `left`.', 'solution_explanation': 'Time Complexity: O(M * N) since we visit every cell exactly once. Space Complexity: O(M * N) to store the result, or O(1) auxiliary.'}
]
