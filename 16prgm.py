fruits={'apple':2,'orange':14,'pinapple':31,'grapes':10,'watermelon':61}
l=list(fruits.items())
l.sort()
print('Ascending order is:',l)
l=list(fruits.items())
l.sort(reverse=True)
print('desending order is:',l)