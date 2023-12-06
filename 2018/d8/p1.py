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
    
def sum_metadata_values(node):
    s = sum(node.metadata)
    if(len(node.children) == 0):
        return sum(node.metadata)
    for child in node.children:
        s+=sum_metadata_values(child)
    
    return s
    
root = parse_node()

print(sum_metadata_values(root))

