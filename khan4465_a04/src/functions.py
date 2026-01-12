"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Shamir Khan 
ID:      169094465
Email:   khan4465@mylaurier.ca
__updated__ = "2025-02-02"
-------------------------------------------------------
"""
# Imports

# Constants

from Queue_array import Queue 

from Priority_Queue_array import Priority_Queue

def queue_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source queues into the current target queue.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target = queue_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        target - a queue (Queue)
    -------------------------------------------------------
    """
    smaller_quque = 0
    bigger_quque = 0
    target = Queue()
    
    if(len(source1) < len(source2)):
        smaller_quque = source1
    else:
        smaller_quque = source2
        
    if(len(source1) > len(source2)):
        bigger_quque = source1
    else:
        bigger_quque = source2
    
    for x in range(len(smaller_quque)):
        target.insert(bigger_quque.remove())
        target.insert(smaller_quque.remove())
        
    for y in range(len(smaller_quque), len(bigger_quque)):
        target.insert(bigger_quque.remove())
    return target

def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    
    for x in range(len(source)):
        if( key > source.peek()):
            target1.insert(source.remove())
        else:
            target2.insert(source.remove())
    
    return target1, target2
    