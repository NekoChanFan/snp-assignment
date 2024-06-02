def sort_list(l:list):
  if(len(l) == 0):
    return []
  minInL = min(l)
  maxInL = max(l)

  for i in range(len(l)):
    if l[i] == minInL:
      l[i] = maxInL
      continue
    if l[i] == maxInL:
      l[i] = minInL
  l.append(minInL)
  return l

if __name__ == "__main__":
    print(sort_list([]))
    print(sort_list([2,4,6,8]))
    print(sort_list([1]))
    print(sort_list([1,2,1,3]))
