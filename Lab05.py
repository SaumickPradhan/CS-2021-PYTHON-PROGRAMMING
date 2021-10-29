## Lab 5: Required Questions - Dictionaries  ##

# RQ1
def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

    >>> new =  merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    >>> new == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    True
    """
    "*** YOUR CODE HERE ***"
    dict_ans={}
    for i in dict1:
      dict_ans[i]=dict1[i]
    for i in dict2:
      dict_ans[i]=dict2[i]
    return dict_ans




# RQ2
def counter(message):
    """ Returns a dictionary where the keys are the words in the message, and each
    key is mapped (has associated value) equal 
    to the number of times the word appears in the message.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    "*** YOUR CODE HERE ***"
    dict_ans={}
    for i in message.split():
      if i not in dict_ans:
        dict_ans[i]=1
      else:
        dict_ans[i] +=1
    return dict_ans


# RQ3
def replace_all(d, x, y):
    """ Returns a dictionary where the key/value pairs are the same as d, 
    except when a value is equal to x, then it should be replaced by y.
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    "*** YOUR CODE HERE ***"
    for i in d:
      if (d[i]==x):
        d[i]=y
    # return d -  the doctests given in the question do not expect us to return the dictionary. If we wanted to, we write the following statement

# RQ4
def sumdicts(lst):
   """ 
   Takes a list of dictionaries and returns a single dictionary which contains all the keys/value pairs found in list. And 
   if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned 
   as the value mapped for that key
   >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
   >>> d == {'b': 88, 'c': 100, 'a': 140, 'd': 19}
   True
   """
   "*** YOUR CODE HERE ***"
   dict_ans={}
   for i in lst:
     for j in i:
       if j not in dict_ans:
         dict_ans[j]=i[j]
       else:
         dict_ans[j]+=i[j]
   return dict_ans


def construct_tweet(word, table): 
  import random
  result = ' '
  while word not in ['.', '!', '?']:
    result += word + ' '
    word = random.choice(table[word])
  return result + word
    
def random_tweet(table):
    import random
    return construct_tweet(random.choice(table['.']), table)

def build_successors_table(tokens):
 
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
          table[prev] = []
        table[prev] += [word]    
        prev = word
    return table

#RQ5
def middle_tweet(table):
    """ Calls the function random_tweet() 5 times (see Interactive Worksheet) and 
    returns the one string which has length in middle value of the 5.
    Returns a string that is a random sentence of average length starting with word, and choosing successors from table.
    """
    "*** YOUR CODE HERE ***"
    dict_ans={}
    l=0
    size=[]
    from statistics import median
    for i in range(5):
      s=random_tweet(table)
      l=len(s)
      size+=[l]
      dict_ans[l]=s
    median_length=(median(size))
    return (dict_ans[median_length])
    


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
