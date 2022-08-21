import h5py
import numpy as np

file = h5py.File('../testfile1.mat', 'r')   # Read in file

# Get structure of dataset
    # print(list(file))



# file['data']
    # print(type(file['data']))                   # datatype: <class 'h5py._hl.group.Group'>
    # print(list(file['data']))


## file['data/arr_bool']
    # print(file['data/arr_bool'].dtype)          # datatype: uint8
    # print(file['data/arr_char'].dtype)          # datatype: uint16

count = 0
arr = list(file['data'])


'''
# List properties of data in datasets
for item in arr:
    # print(f"{count}, {item}: {file['data'][item].dtype}")
    print(f"{count}, {item}: {file['data'][item]}")
    count += 1
'''


## file['data/cell_']
cellArr = np.array(file['data']['cell_'])
cellArr = cellArr.flatten()
for item in cellArr:
    pass
    # print(file[item])

### Convert char array to string
num = 5
item = file['data/cell_/'][num][0]
charArr = (np.array(file[item])).flatten()
charArr = str(np.array(charArr, dtype=np.int8).tobytes().decode("utf-8"))
    # print(charArr)


### Item 6
num = 6
num1 = 0
item = file['data/cell_/'][num][0]
item0 = list(file[item])[num1] 
charArr2 = (np.array(file[item0[0]])).flatten()
charArr2 = str(np.array(charArr2, dtype=np.int8).tobytes().decode("utf-8"))
    # print(charArr2)


## file['data/string_']
string = file['data/string_']
string = (np.array(string)).flatten()
string = str(np.array(string, dtype=np.int8).tobytes().decode("utf-8"))
    # print(string)
# -------------------------------------------------------------------------------- 

## file['data/struct_']
    # print( file['data/struct_'] )
    # print( list(file['data/struct_']) )                 # Output: ['test']
    # print( file['data/struct_/test'] )
test = (np.array(file['data/struct_/test'] )).flatten()
    # print(test) 

## file['data/struct2_']; type, color
num3 = 1
    # print(file['data/struct2_'])
test2 = list( file['data/struct2_'] )
    # print(test2)                                            # Print items in struct
str2 = list(file['data/struct2_']['color'])[num3][0]
str2 = (np.array(file[str2])).flatten()
str2 = (np.array(str2, dtype=np.int8).tobytes().decode("utf-8"))
    # print(str2)

## file['data/struct2_']; x
x = file['data/struct2_/x']
x0 = x[0][0]
x0 = np.array(file[x0])
    # print(np.transpose(x0))
x1 = x[1][0]
x1 = np.array(file[x1])
    # print(np.transpose(x1))

## file['data/structarr_']
strArr = file['data/structarr_']
strArrList = np.array(strArr)
f1 = file['data/structarr_'][strArrList[0]]
f2 = file['data/structarr_'][strArrList[1]]
f1Objs = np.array(f1)
f2Objs = np.array(f2)
### f1-->text
f1Text = file[f1Objs[0][0]]
f1Text = (np.array(f1Text)).flatten()
f1Text = (np.array(f1Text, dtype=np.int8).tobytes().decode("utf-8"))
    # print(f1Text)
### f1-->int_array
f1numArr = file[f1Objs[0][1]]
f1numArr = (np.array(f1numArr)).flatten()
    #print(f1numArr)

### f1-->int_matrix
f1numMat = file[f1Objs[0][2]]
f1numMat = np.array(f1numMat)
    # print(np.transpose(f1numMat))

###f2-->text
f2Text = file[f2Objs[0][0]]
f2Text = (np.array(f2Text)).flatten()
f2Text = (np.array(f2Text, dtype=np.int8).tobytes().decode("utf-8"))
print(f2Text)





# print(file['data'][arr[22]].dtype)
# item = str(list(file['data'])[0])
# print(file['data'][item].dtype)
