class solution(object):

def lettercombinations (self,digits):

if len(digits) - 0:

return()

characters (2:"abc",3:"def",4:"ghi",5:"jk1",6:"no",7:"pqrs", 8: "tuv", 9:"wxyz")

result =[]

self.solve(digits, characters, result)

return (result)

def solve(self, digits, characters, result, current_strings="", current level -0):

if current level len (digits): result.append(current_string)

obl

return()

for i in characters[int(digits[current_level])]:

self.solve(digits, characters, result, current_string+1, current level+1)

pri

obl =solution()

m =(input("enter the numbers"))

print(obl. lettercombinations (m))
