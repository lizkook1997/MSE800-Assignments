disct1 = {'a':1, 'b': 2, 'c': 3}
disct2 = {'d':4, 'e': 5, 'f': 6}

merged_dict = {**{k: v for k, v in disct1.items() if k in 'aeiou'},
               **{k: v for k, v in disct2.items() if k in 'aeiou'}}

# merged_dict = {**disct2, **disct1, }
print(merged_dict)
