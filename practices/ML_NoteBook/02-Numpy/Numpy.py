# %%


# %%
import numpy as np

# %%
myList = [1,2,3]

# %%
type(myList)

# %%
np.array(myList)

# %%
myMatrix = [[1,2,4],[5,6,7],[8,9,10],[11,12,13]]

# %%
myMat = np.array(myMatrix)

# %%
myMat

# %%
np.zeros(5)

# %%
np.zeros((5,6))

# %%
np.ones((4,3))

# %%
np.linspace(0,10,3)

# %%
np.eye(5)

# %%
np.random.rand((3,3))

# %%
np.random.rand(3,3)

# %%
np.random.rand()

# %%
np.random.rand(1)

# %%
np.random.randn(3,3)

# %%
np.random.randn()

# %%
np.random.randn(2)

# %%
np.random.randomn(5,5)

# %%
np.random.randint

# %%
np.random.randint(5,5)

# %%
np.random.randint(0,100,size=(5,5))

# %%
np.random.seed(42)
np.random.rand(4)

# %%
np.random.rand(4)

# %%
np.random.seed(42)
np.random.rand(4)

# %%
np.random.seed(13)
np.random.randn(5,5)

# %%
np.random.seed(13)
np.random.randn(5,5)

# %%
np.array(0,10,3)

# %%
np.array(0,4)

# %%
np.arange(0,24, 3)

# %%
np.arange(0,24,3.2,float)

# %%
np.linspace(0,10,3)

# %%
np.arange(0,25,5)

# %%
np.random.seed(23)
np.arange(0,25)

# %%
np.arange(0,25)

# %%
arr = np.arange(0,25)

# %%
arr

# %%
arr.reshape(5,6)

# %%
arr.reshape(6,6)

# %%
arr.reshape(5,5)

# %%
ranarr = np.random.randint(0,201,20)

# %%
ranarr

# %%
ranarr.max()

# %%
ranarr.argmax()

# %%
ranarr.min()
ranarr.argmin()

# %%
ranarr.dtype()

# %%
ranarr.dtype

# %%
import numpy as np

# %%
ranarr = np.random.rand(0,25,4)

# %%
ranarr

# %%
ranarr = np.random.rand(3,3)

# %%
ranarr


# %%
ranarr.dtype

# %%
ranarr = np.random.randint(0,25,(3,3))

# %%
ranarr

# %%
ranarr.dtype

# %%
arr

# %%
ranarr.shape

# %%
ranarr.reshape(3,4)

# %%
ranarr.reshape(9)

# %%
ranarr.reshape(1,9)

# %%
ranarr.reshape(9,1)

# %%
np.arange(0,15)

# %%
arr = np.arange(0,20)

# %%
arr[8]

# %%
arr[ : 5]

# %%
arr[11:16]

# %%
arr[7:]

# %%
arr[0:8] = 27

# %%
arr

# %%
slice_of_arr = arr[0:11]

# %%
slice_of_arr[0:8] = 29

# %%
slice_of_arr

# %%
arr

# %%
arr_copy = arr.copy()

# %%
arr_copy[0:7] = 76

# %%
arr_copy

# %%
arr

# %%
arr.reshape(5,4)

# %%
arr_2d = arr.reshape(5,4)

# %%
arr_2d

# %%
arr_2d[0]

# %%
arr_2d[2,3]

# %%
arr[,3]

# %%
arr_2d[:2]

# %%
arr_2d[:2,1:]

# %%
arr_2d[:2,2:]

# %%
arr = np.arange(1,11)

# %%
arr

# %%
arr > 4

# %%
bool_arr = arr > 4

# %%
bool_arr

# %%
arr(bool_arr)

# %%
arr[bool_arr]

# %%
arr[arr<7]

# %%
dice_rolls = np.array([3, 1, 5, 2, 5, 1, 1, 5, 1, 4, 2, 1, 4, 5, 3, 4, 5, 2, 4, 2, 6, 6, 3, 6, 2, 3, 5, 6, 5])

# %%
condition = dice_rolls[dice_rolls>2].shape

# %%
condition

# %%
x = condition[0]

# %%
x

# %%
arr = np.arange[0,10]

# %%
arr

# %%
arr = np.arange(0,10)

# %%
arr = arr + 5

# %%
arr

# %%
arr - 2

# %%
arr

# %%
arr + arr

# %%
arr-arr

# %%
arr / arr

# %%
1/arr

# %%
arr = np.arange(0,10)

# %%
arr

# %%
arr / arr

# %%
1 / arr

# %%
np.sqrt(arr)

# %%
np.log(arr)

# %%
np.sin(arr)

# %%
np.tan(arr)

# %%
np.cot(arr)

# %%
np.tanh(arr)

# %%
arr.var()

# %%
arr.std()

# %%
arr2D = np.arange(1,26).reshape(5,5)

# %%
arr2D

# %%
arr2D.sum()

# %%
arr[0:].sum()

# %%
arr2D.sum(axis=0)

# %%
arr2D.sum(axis=1)

# %%
arr = np.random.randn()

# %%
arr

# %%
np.random.randn(10)

# %%
arr = np.random.randn(3,3)

# %%
arr

# %%
arr.std()

# %%
arr.var()

# %%
import numpy as np

# %%
arr = np.array([1,2,3,4,5])

# %%
arr

# %%
np.arange(0,25,4,dtype=float)

# %%
arr = np.arange(1,26)

# %%
arr

# %%
arr.reshape(5,5)

# %%
arr.argmax()

# %%
arr.std()

# %%
arr.var()

# %%
arr2 = np.random.rand()

# %%
arr2

# %%
arr2 = np.random.rand(16)

# %%
arr2

# %%
arr2.reshape(4,4)

# %%
arr3 = np.random.rand(16)

# %%
arr2 = arr2.reshape(4,4)
arr3 = arr3.reshape(4,4)

# %%
arr2
arr3

# %%
arr2

# %%
arr3

# %%
arr4 = arr2 + arr3

# %%
arr4

# %%
np.linspace(0,100,0.01)


