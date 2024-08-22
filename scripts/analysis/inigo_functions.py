def last_find(text,target):
    linenum = 0
    for line in text:
        if (line.find(target)) > -1 :
            last_line = linenum
        linenum += 1
    return last_line

def first_find(text,target):
   linenum = 0
   found = False
   for line in text:
      if not found:
        if (line.find(target)) > -1:
          found = True
        else:  
          linenum += 1
   return linenum

def all_find(text, target):
    dat = []
    linenum = 0
    dat_num = 0
    for line in text:
        if (line.find(target)) > -1:
            dat.append(text[linenum].split())
        linenum +=1
    return dat[:][:]

def all_after1(text, target):
    dat = []
    linenum = 0
    dat_num = 0
    for line in text:
        if (line.find(target)) > -1:
            dat.append(float(text[linenum + 1]))
        linenum +=1
    return dat[:][:]

def all_after1_split(text, target):
    dat = []
    linenum = 0
    dat_num = 0
    for line in text:
        if (line.find(target)) > -1:
            dat.append(float(text[linenum + 1].split()[0]))
        linenum +=1
    return dat[:][:]
