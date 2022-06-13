# SplitLibrary
The SplitLibrary is a library to split an array to an array of array suitably sized for delivery to a system which has some limits.

### How to install?

```
python setup.py bdist_wheel
python -m pip install dist/split*.whl
```


### How to use?
```
import splitlib as sl
s = sl.Splitter().splitLib(['Helsinki', 'Paris', 'this is a long string' 'Rome', 'Barcelona',
         'Tehran', 'Lisbon', 'this is another long string', 'Stokholm', 'Amesterdam'])
print(s)		 
```