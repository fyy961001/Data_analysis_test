import pandas as pd
import list_practice.knn_function as kf
# read file and save it in dataframe
train_file=pd.read_csv('https://raw.githubusercontent.com/fyy961001/Data_analysis_test/master/train.csv')
test_file=pd.read_csv('https://raw.githubusercontent.com/fyy961001/Data_analysis_test/master/test.csv')
# read data and save it into list
key_list=train_file.keys()
key_list_test=test_file.keys()
group_list=train_file[key_list[1]].values.tolist()
vector1_list=train_file[key_list[2]].values.tolist()
vector1_list_norm=kf.norm(vector1_list.copy())
vector2_list=train_file[key_list[3]].values.tolist()
vector2_list_norm=kf.norm(vector2_list.copy())
vector_list=kf.vector_combine([vector1_list_norm,vector2_list_norm])

vector1_list_test=test_file[key_list_test[1]].values.tolist()
vector1_list_norm_test=kf.norm_test(vector1_list_test,vector1_list)
vector2_list_test=test_file[key_list_test[2]].values.tolist()
vector2_list_norm_test=kf.norm_test(vector2_list_test,vector2_list)
vector_list_test=kf.vector_combine([vector1_list_norm_test,vector2_list_norm_test])

k_value=3
distance1=[]
for x in range(len(vector_list)):
    distance1.append(kf.distance(vector_list_test[0],vector_list[x]))


