# generate all combinations of N items

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', '\
                 + str(self.weight) + '>'
        return result

def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book',
             'computer']
    vals = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items

def yieldAllCombos(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(2**N):
        combo = ""
        c1 = ""
        for j in xrange(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo += (items[j].__str__()+" ")
            else:
                c1 += (items[j].__str__()+" ")
        combo = str(combo[:])
        c1 = str(c1[:])
        yield combo,c1

items = buildItems()
combos = yieldAllCombos(items)

# count = 0
#for i in combos:
#    count +=1
#    if count == 2:
#        break
#    else:
#        print i