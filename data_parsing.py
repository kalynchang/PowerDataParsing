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

print data['TX_H8345Y_B']['from']
print data['P5010422']['from']

# get transformer names
# find from nodes for each transformer
# find the from node in each dictionary (A, B, C)
# average the three values of the from nodes
# put new value into a new dictionary with transformer as the key 

def dict_writer(file):
    f = open(file)
    trans_list = []
    new_data = {}
    
    for line in f: 
        s = line.strip()
        # trans = data[s]['from']
        
dict_writer('idsinorder.csv')
