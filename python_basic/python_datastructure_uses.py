"""
Python Data Structures: A Comprehensive Guide

LISTS:
- Ordered, mutable collection of items
- When to use: When you need to store multiple items in a specific order and modify them
- Why: Lists support indexing, slicing, and allow easy insertion/deletion
- Where: Storing sequences, stacks, queues (with deque for efficiency)
- Characteristics: Slower lookups O(n), fast appends O(1), dynamic sizing

TUPLES:
- Ordered, immutable collection of items
- When to use: When you need unchangeable collections or dictionary keys
- Why: Immutability provides safety and allows use as dict keys/set elements
- Where: Function return values, fixed collections, hashable requirements
- Characteristics: Memory efficient, slightly faster than lists, prevents accidental modification

DICTIONARIES:
- Unordered (3.7+ maintains insertion order), mutable key-value pairs
- When to use: When you need fast lookups by key or mapping relationships
- Why: O(1) average lookup time, intuitive key-value associations
- Where: Caching, counting occurrences, representing objects/records
- Characteristics: Keys must be hashable, highly efficient for lookups

SETS:
- Unordered, mutable collection of unique items
- When to use: When you need to store unique values or perform set operations
- Why: O(1) average lookup, automatic uniqueness, fast membership testing
- Where: Removing duplicates, finding common elements, membership testing
- Characteristics: No indexing, immutable items only, excellent for mathematical operations

COMPARISON:
- Speed: Dict/Set O(1) lookups > List O(n) > Tuple O(n)
- Memory: Tuple < List < Set < Dict
- Mutability: Lists/Dicts/Sets (mutable) vs Tuples/frozen sets (immutable)
- Use Dict for fast lookups, Set for uniqueness, List for order, Tuple for safety
"""