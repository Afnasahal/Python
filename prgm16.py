fruits={'apple':2,'orange':4,'pinapple':31,'watermelon':61,'grapes':10}
l=list(fruits.items())
l.sort()
print('ascending order is:',l)
l=list(fruits.items())
l.sort(reverse=True)
print('descending order is:',l)