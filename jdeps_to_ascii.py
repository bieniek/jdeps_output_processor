import sys

def print_class(graph, class_name):
    print_class_r(graph, class_name, 1, [])

def print_class_r(graph, class_name, level, aggs):
    print(' '*level + "{}".format(class_name))
    if class_name in aggs:
        return
    else:
        aggs.append(class_name)

    if class_name in graph:
        package = class_name[:class_name.rindex('.'):]
        for line in graph[class_name]: 
            #if not (class_name in leafs or package in skip_packages) :
            print_class_r(graph, line, level+1, aggs)
    return

def strip_line(line):
    splitted = line.strip().split("->")
    return (splitted[0].strip(), splitted[1].strip())


def process(jdeps_output, clazz, prefix=None):    
    with open(jdeps_output) as f:
        my_lines = f.readlines()

    graph = {}
    for line in my_lines:
        (key, value) = strip_line(line)

        if prefix == None or (prefix <> None and key.startswith(prefix) and value.startswith(prefix)):            
            if key in graph:
                listOfValues = graph[key]
                listOfValues.append(value)
            else: 
                graph[key] = [value]
    print_class(graph, clazz) 

if len(sys.argv) > 2:    
    process(sys.argv[1], sys.argv[2], None if len(sys.argv) < 4 else sys.argv[3])
else:
    print('Please specify jdeps output, class name and optionally package prefix')
    

