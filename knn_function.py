import math
def distance(vector1,vector2):
        if len(vector1)!=len(vector2):
            print('you must input vectors with same length')
        else:
            length=len(vector1)
            sum=0
            for x in range(length):
                sum+=(vector2[x]-vector1[x])**2
            return math.sqrt(sum)

def norm(list):
    length=len(list)
    max_num=max(list)
    min_num=min(list)
    for x in range(length):
        num=(list[x]-min_num)/(max_num-min_num)
        list[x]=num
    return list

def norm_test(list1,list2):
    length=len(list1)
    max_num=max(list2)
    min_num=min(list2)
    for x in range(length):
        num=(list1[x]-min_num)/(max_num-min_num)
        list1[x]=num
    return list1

def vector_combine(list):
    length=len(list[0])
    vector_list=[]
    for x in range(length):
        vector=[]
        for y in range(len(list)):
            vector.append(list[y][x])
        vector_list.append(vector)
    return vector_list

def classfication_result(k,vector,group_list,distance_list):
    neighbour1 = distance_list.copy()
    neighbour1.sort()
    neighbour1 = neighbour1[:k]
    nei_index=[]
    for x in range(k):
        nei_index.append(distance_list.index(neighbour1[x]))
    result_dic={}
    for index in nei_index:
        if group_list[index] in result_dic:
            result_dic[group_list[index]]+=1
        else:
            result_dic[group_list[index]]=1
    result_dic_sort=sorted(result_dic.items(),key=lambda x:x[1],reverse=True)
    return result_dic_sort[0][0]







