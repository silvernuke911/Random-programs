import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define the comparison operators for the priority queue
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequency):
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_codes(node, prefix="", code_map={}):
    if node is not None:
        if node.char is not None:
            code_map[node.char] = prefix
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)
    return code_map

def huffman_encoding(data):
    if not data:
        return "", {}
    
    frequency = Counter(data)
    root = build_huffman_tree(frequency)
    huffman_code = generate_codes(root)
    
    encoded_data = ''.join(huffman_code[char] for char in data)
    return encoded_data, huffman_code

def huffman_decoding(encoded_data, huffman_code):
    reverse_code = {v: k for k, v in huffman_code.items()}
    current_code = ""
    decoded_output = []
    
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_code:
            character = reverse_code[current_code]
            decoded_output.append(character)
            current_code = ""
    
    return ''.join(decoded_output)

# Example usage
if __name__ == "__main__":
    data = "this is an example for huffman encoding"
    encoded_data, huffman_code = huffman_encoding(data)
    print("Encoded data:", encoded_data)
    print("Huffman Code:", huffman_code)
    
    decoded_data = huffman_decoding(encoded_data, huffman_code)
    print("Decoded data:", decoded_data)