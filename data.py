# Objective: Read mat7.3 datasets using h5py

# Import packages
import h5py
import numpy as np

file = h5py.File('../testfile1.mat', 'r')

print(list(file)) # List file structure
print( type(list(file)) )

# 'file/data'
    # print(list(file['data'])) # List structure of 'data'

## Print Numbers
int8 = np.array(file['data/int8_'])
int8 = int8.flatten()                   # Remove array nesting, extract data
    # print(int8[0])

uint16 = np.array(file['data/uint16_'])
uint16 = uint16.flatten()
    # print(uint16[0])

single = np.array(file['data/single_'])
single = single.flatten()
    # print(single[0])

double = np.array(file['data/double_'])
double = double.flatten()
    # print(double[0])

## Print Char
char = np.array(file['data/char_'])
char = (char.flatten())[0]
    # print(chr(char))

## Print Bool
boole = np.array(file['data/bool_'])
boole = boole.flatten()
    # print(boole[0])                         # print(bool(boole)) -- convert to bool

## Print Float Array
floatArr = np.array(file['data/arr_float'])
    # print(list(floatArr))

## Print Missing --> None
missing = file.get('data/missing_/Full')
    # print(missing)
missing = file.get('data/missing_/WL')
    # print(missing)

## Print Complex Number
comPlex = file.get('data/complex_')
    # print(comPlex.dtype)                    # Get numpy data type
comPlex = (np.array(comPlex)).flatten()
    # print(complex(comPlex[0][0], comPlex[0][1]))

## Print Complex Array
comArr = (np.array(file.get('data/complex3_'))).flatten()
    # print(comArr[0][0] + 1j*comArr[0][1])

## Print Cell Char
num = 3
cellChar = file['data/cell_char_']
    # print(cellChar)
cellChar = (np.array(cellChar)).flatten()
    # print(cellChar[num])                          # This prints out the reference, we need to get
st = cellChar[num]                            # The HDF5 object
str1 = (np.array(file[st])).flatten()       # Get the object, Un-nest the array, (*0)
str1 = ''.join(chr(i) for i in str1)
    # print(str1)

## Print 'string'
str2 = file['data/string_']
str2 = (np.array(str2)).flatten()
str2 = ''.join(chr(i) for i in str2)
    # print(str2)

## Print 'struct_'
struct = file.get('data/struct_')
    # print(list(struct))                             # Get structure of matlab struct
    # print((np.array(struct['test'])).flatten())     # Get contents of struct

## Print 'struct2_'
struct_2 = file.get('data/struct2_')
    # print(list(struct_2))

### Print 'struct2_/type'
num = 1
tYpe = struct_2['type']
    # print(tYpe[num][0])                                     # The second index un-nests the object
big = (np.array(file[tYpe[num][0]])).flatten()           # out of the array
big = ''.join(chr(i) for i in big)
    # print(big)

### Print 'struct2_/color'
    # print(list(struct_2['color']))
color = struct_2['color']
color0 = struct_2['color'][1][0]
    # print(color0)
    # print(file[color0])
color0 = (np.array(file[color0]).flatten())
str3 = ''.join(chr(i) for i in color0)
    # print(str3)

### Print 'struct2_/x'
    # print(list(file['data/struct2_/x']))
    # print(len( list(file['data/struct2_/x']) )  )
arr = file['data/struct2_/x']
xArr = file[arr[1][0]]
    # print(np.transpose(xArr))                               # Matrix now follows the shape shown in matlab
    # print(np.array(file[struct_2['x'][0][0]]))
    # print(np.array(file[struct_2['x'][1][0]]))


# 'file/keys'

## Convert int array to char array to string
#print(file['keys'])                    # Char array
str0 = np.array(file['keys'])           # Turn hdf5 char array to numpy array
str0 = str0.flatten()                   # turn array to 1 row instead of an array of array of an int
str0 = ''.join(chr(i) for i in str0)    # turn num array to char array
# print(f"key char array: {str0}")



# 'file/secondvar'




# Comments:
# •••••••••••••••••••••••••••••••••••••••••••••••••••
# •••••••••••••••••••••••••••••••••••••••••••••••••••
# •••••••••••••••••••••••••••••••••••••••••••••••••••
# print(file.keys()) # List keys
# print(list(file['data/arr_bool/'][0]))
# print(file['data/arr_bool/']) # Access groups in datasets
                                # Get data from structures in datasets


# (*0)
"""
Nested Array: [ [0], [1], [2], [3] ]
Un-nested Array: [0, 1, 2, 3]           -- This makes it to where
                                           we loop over one dimension
                                           instead of 2
"""
