# goit-algo-hw-05
Algo homework 05

1. hastable.py -> Implementation of Hashtable, with "delete()" support
2. binary_search_float.py -> Implementation of binary search for float numbers
3. substring_search.py -> Test for text search algorithms
4. string_search_algos.py -> Implementation of text search algorithms

## Results of test for text text search:
    Testing text 1....
    Testing by substring 'кількість'....
    Result for KMP search algorithm is 0.00012947
    Result for Boyer-Moore search algorithm is 0.00005059
    Result for Rabin-Karp search algorithm is 0.00026199


    Testing by substring 'неіснуюча комбінація слов і літер'....
    Result for KMP search algorithm is 0.00115189
    Result for Boyer-Moore search algorithm is 0.00020652
    Result for Rabin-Karp search algorithm is 0.00262771





    Testing text 2....
    Testing by substring 'кількість'....
    Result for KMP search algorithm is 0.00025956
    Result for Boyer-Moore search algorithm is 0.00010970
    Result for Rabin-Karp search algorithm is 0.00058501


    Testing by substring 'неіснуюча комбінація слов і літер'....
    Result for KMP search algorithm is 0.00160664
    Result for Boyer-Moore search algorithm is 0.00028479
    Result for Rabin-Karp search algorithm is 0.00365348

Boyer-Moore search was the fastest for first text, for both existing and non-existing substrings.
The same result for second text as well. So we can see, that usually Boyer-Moore is the best algorithm for search in text.