"""
    node.val 
    node.nxt
"""
def countTriplets(head,x):
    count = 0
    hashset = set()
    current = head 
    while current: 
        hashset.add(current.val)
        current = current.nxt
        
    current = head 
    while current: 
        num = current.val 
        node = current.nxt 
        while node:
            complement = x - (node.val + num)
            if complement < node.val and complement in hashset: 
                count += 1
            node = node.nxt 
        current = current.nxt
    return count