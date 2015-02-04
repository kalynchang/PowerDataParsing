def dict_converter(file):
    f = open(file)
    name_list = []
    data = {}
    
    for line in f:
        s = line.strip().split(',')
        if s[0] == '# timestamp':
            for v in s:
                name_list.append(v)
                data[v] = []
            break
        
    for line in f:
        s = line.strip().split(',')
        ind = 0
        for v in s:
            data[name_list[ind]].append(v)
            ind += 1
    
    for i in range(1, len(name_list)):
         for j in range(0, len(data[name_list[i]])):
            num = data[name_list[i]][j]
            if num == '+0.000000+0.000000j':
                num = num[1:9]
                num = float(num)
                data[name_list[i]][j] = num
            else:
                num = num[1:12]
                num = float(num)
                data[name_list[i]][j] = num
    
    for i in range(1, len(name_list)):
        avg = 0
        for j in range(0, len(data[name_list[i]])):
            num = data[name_list[i]][j] 
            avg += num
        avg = avg / len(data[name_list[i]])
        data[name_list[i]] = avg
    
    return data
    
A = dict_converter('primary_node_voltage_A.csv')
B = dict_converter('primary_node_voltage_B.csv')
C = dict_converter('primary_node_voltage_C.csv')

print A
print B
print C

import json
json_data = open('gldRunDef.json')
data = json.load(json_data)

# print data['TX_H8345Y_B']['from']
# print data['switch_P5010422-1_15452$P5010422-1_T_-1']['from']

# get transformer names
# find from nodes for each transformer
# find the from node in each dictionary (A, B, C)
# average the three values of the from nodes
# put new value into a new dictionary with transformer as the key 

def dict_writer(file, dict1, dict2, dict3):
    f = open(file)
    name_list = []
    new_data = {}
    
    for line in f: 
        s = line.strip()
        key = data[s]['name']
        # print key
        name_list.append(key)
        # print name_list
        # print name_list[0]
        # find the node in each dictionary
        new_data[key] = []
        # print new_data
    
    # now find node name in each dictionary, average the values, and set as 
    # value for corresponding node in new_data
    for node in name_list:
        if node in dict1:
            a = dict1[node]
        if node in dict2:
            b = dict2[node]
        if node in dict3:
            c = dict3[node]
        avg = 0
        div = 0
        if a != 0.0:
            avg += a
            div += 1
        if b != 0.0:
            avg += b
            div += 1
        if c != 0.0:
            avg += c
            div += 1
        avg = avg / div
        print avg
        new_data[node] = avg
        
    return new_data
        
        
# D is the final dictionary with node names as keys and the average value
# of the voltages at each node as the value 
D = dict_writer('nodesInOrder.csv', A, B, C)
print D 