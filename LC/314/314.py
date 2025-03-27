null = None # needed to be able to use the example vectors directly in Python

# First version, O(n^2) and many code paths (lower maintainability)
def verticaltraversal(root):
  if 0==len(root):
    return []
  # initialize raw results, key-value pairs of column, elements. 
  # It's a kvp so that we can add cols with negative indices
  r = {}
  r[0] = [root[0]] 
  # Initialize column indices for this level 
  ix = [0] 
  iix = 1
  # loop over the elements in root. We need a while because the length of root can change
  i = 1
  while i < len(root):
    # If we need a new level, generate indices
    if len(ix) <= iix:
      oldix = ix
      ix = []
      for j in range(len(oldix)):
        ix.append(oldix[j]-1)
        ix.append(oldix[j]+1)
      iix = 0
    # If we come across a null, "de-optimize" the tree representation to make it a complete tree
    # then continue to the next iteration without adding the node to the results
    if root[i] is None:      
      if 1+(i*2) < len(root):
        root = root[:1+(i*2)]+[None, None]+root[1+(i*2):]
      iix += 1
      i += 1
      continue
    # Upsert the appropriate list
    if not ix[iix] in r:
      r[ix[iix]] = [root[i]]
    else:
      r[ix[iix]].append(root[i])
    # next iteration
    iix += 1
    i += 1
  # Convert raw results to list of lists
  rr = []
  for k in sorted(r.keys()):
    rr.append(r[k])
  return rr

# We need to process *incomplete* trees, see example 3. Rebuild the tree as complete. O(n)
def complete(root):
  if 0 == len(root):
    return []
  r = [root[0]]
  for i in range(1, len(root)):
    if r[i//2-1] is None:
      r += [None, None]
    r.append(root[i])
  return r

def vt(root):
  if 0==len(root):
    return []
  # initialize raw results, key-value pairs of column, elements. 
  # It's a kvp so that we can add cols with negative indices
  r = {}
  r[0] = [root[0]] 
  # Initialize column indices for this level 
  ix = [0] 
  iix = 1
  cr = complete(root)
  mincol = 0
  maxcol = 0
  for i in range(1, len(cr)):
    # If we need a new level, generate indices
    if len(ix) <= iix:
      oldix = ix
      ix = []
      for j in range(len(oldix)): # This is O(2^log(n)), done n times, complexity is O(n * 2^log(n))
        ix.append(oldix[j]-1)
        ix.append(oldix[j]+1)
      iix = 0
    # Upsert the appropriate list
    col = ix[iix]
    iix += 1
    if cr[i] is not null:
      if not col in r:
        if col < mincol:
          mincol = col
        if col > maxcol:
          maxcol = col
        r[col] = [cr[i]]
      else:
        r[col].append(cr[i])
  # Convert raw results to list of lists
  rr = []
  for k in range(mincol, maxcol+1):
    rr.append(r[k])
  return rr
