nums = [2,7,11,15]
target = 9
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        no_i_list=[num for num in nums]
        no_i_list.remove(nums[i])
        for j in range(len(no_i_list)):
            sum=nums[i]+no_i_list[j]
            if sum==target:
                second_num=nums.index(no_i_list[j])
                break
        return [i,second_num]
l1=[2,4,3]
l2=[5,6,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Initialize the dummy head of the result list
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    # Traverse both lists
    while l1 is not None or l2 is not None:
        # Get the values from the current nodes, defaulting to 0 if the node is None
        x = l1.val if l1 is not None else 0
        y = l2.val if l2 is not None else 0

        # Calculate the sum and the carry
        sum_val = carry + x + y
        carry = sum_val // 10
        current.next = ListNode(sum_val % 10)
        
        # Move to the next nodes
        current = current.next
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    # If there's a carry left after the final addition, add a new node with that carry
    if carry > 0:
        current.next = ListNode(carry)

    return dummy_head.next

def lengthOfLongestSubstring(s: str) -> int:
    char_index_map = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            left = char_index_map[s[right]] + 1
        char_index_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# Test cases
# print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
# print(lengthOfLongestSubstring("bbbbb"))     # Output: 1
# print(lengthOfLongestSubstring("pwwkew"))    # Output: 3
# Explanation:
# Initialization:

# char_index_map: A dictionary to store the latest index of each character.
# left: The left pointer of the sliding window, initially set to 0.
# max_length: Variable to keep track of the maximum length of the substring found so far.
# Sliding Window Loop:

# Iterate over the string with the right pointer (right).
# If the character at the right pointer is already in the char_index_map and its index is greater than or equal to left (indicating it is within the current window), update left to be one position right of the last occurrence of this character. This effectively moves the window past the repeated character.
# Update the char_index_map with the current index of the character at the right pointer.
# Calculate the length of the current window (right - left + 1) and update max_length if the current window length is greater.
# Detailed Steps:
# Iterate through each character in the string with the right pointer.
# Check if the character is already in the char_index_map and if it is within the bounds of the current window (left to right). If it is, move the left pointer just past the last occurrence of the character to ensure no duplicates in the current window.
# Update the character's latest index in the char_index_map.
# Calculate the length of the current window and update max_length if necessary.
# After the loop ends, return max_length which contains the length of the longest substring without repeating characters.
# This solution efficiently finds the length of the longest substring without repeating characters with a time complexity of O(n), where n is the length of the string, and a space complexity of O(min(n, m)), where m is the size of the character set.

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        sortednums=nums1+nums2
        sortednums.sort()
        length=len(sortednums)
        if length%2==0:
            return (sortednums[length//2]+sortednums[length//2-1])/2
        else:
            return sortednums[len(sortednums)//2]
print(findMedianSortedArrays([1,2,3,4],[2,5,6]))

s='stringabba'

def longestPalindrome(s: str) -> str:
        palindrome_list=[]
        substring_list=[]
        lengthlist=[]
        def is_palindrome(word: str)->bool:
            m=0
            for i in range(len(word)):
                if word[i]!=word[len(word)-i-1]:
                    m+=1
            if m==0:
                return True
            else: return False
        for i in range(len(s)):
            substring=s[i:]
            for j in range(len(substring)):
                subsubstring=substring[:j+1]
                substring_list.append(subsubstring)
        for k in substring_list:
            if is_palindrome(k):
                palindrome_list.append(k)
                lengthlist.append(len(k))
        return palindrome_list[lengthlist.index(max(lengthlist))]
print(longestPalindrome(s))