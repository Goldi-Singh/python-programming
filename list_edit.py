# edit =replace the elements

l=[100,200,300,400,500];
l[1:4]=[1,2,3,4,5];
print(l)
# append = add the elements at the end of the list
l.append(600);
print(l)
# extend = add the elements of another list at the end of the list
l.extend([700,800,900]);
print(l);
# insert = add the elements at the specified index
l.insert(2,250);
print(l)