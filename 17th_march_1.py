"""
Write a Python program to select a string from a given list of strings with the most unique characters. Go to the editor
Input:
['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
Output:
abcdefhijklmnop
Input:
['Green', 'Red', 'Orange', 'Yellow', '', 'White']
Output:
Orange
"""
def test(strs):
    return max(strs, key=lambda x: len(set(x)))
strs = ['cat', 'catatatatctsansondosdniubniuhybuybdwub', 'abcdefhi', '124259239185125', '', 'foo', 'unique']
print("Original list:")
print(strs)
print("Select a string from the said list of strings with the most unique characters:")
print(test(strs))
strs = ['Green', 'Red', 'Orange', 'Yellow', '', 'White']
print("\nOriginal list:")
print(strs)
print("Select a string from the said list of strings with the most unique characters:")
print(test(strs))