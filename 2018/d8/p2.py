file_read = None
with open("input.txt" , "r") as fp:
    file_read = fp.read()

parsed = [int(x) for x in file_read.split()]
    
class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

index=0
def parse_node():
    global index
    num_child_nodes,num_meta_nodes = parsed[index:index+2]
    index+=2
    children = []
    for _ in range(num_child_nodes):
        children.append(parse_node())
    meta_data = parsed[index:index+num_meta_nodes]
    index+=num_meta_nodes
    
    return Node(children,meta_data)
    
def sum_node_values(node):
    s = 0
    if(len(node.children) == 0):
        return sum(node.metadata)
    
    for i in node.metadata:
        if (i != 0 and i < len(node.children)+1):
            s+=sum_node_values(node.children[i-1])
    
    return s
    
root = parse_node()

print(sum_node_values(root))

