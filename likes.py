"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function likes which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob 
"""



def likes(names):
   all = len(names)-2
   if  len(names)<1:
       return  ("no one likes this")
   elif len(names)==1:
       return  ("{} likes this".format(names[0]))
   elif len(names)==2:
       return  ("{} and {} like this".format(names[0],names[1]))
   elif len(names)==3:
       return  ("{}, {} and {} like this".format(names[0],names[1],names[2]))
   else:
       return  ("{}, {} and ".format(names[0],names[1]) +str(all)+" others like this")
# likes(["Jay","Kay","Em","Tee"])
