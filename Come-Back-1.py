def binary_search_recursive(my_list, item):
  L=sorted(my_list)
  found=False
  first =0
  last=len(L)-1
  mid=(first+last)//2
  if(len(L)==1):
    if(L[0]!=item):
      found=False
    else:
      found=True
  else:
    while first<=last and found==False:
      if(L[mid]==item):
        found=True
      elif(L[mid]<item):
        first=mid+1
      else:
        last=mid-1
  return found
# Testing the function
print(binary_search_recursive([1, 3, 5, 7, 9], 5))
print(binary_search_recursive([1, 3, 5, 7, 9], 6))