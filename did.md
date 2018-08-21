## Fri 17th August

Back from Nigeria!

* Worked out how I should process the MTO/ATO/MTS malarky!
    
    Each order will go onto a work queue, and be passed through the system by way of moving a form along.
    I think I'll assume that, when forms are passed along, the car and its current state are also transported as far as they need to
    without any mistakes. This could be improved in later versions of the model; passing information correctly doesn't imply
    there aren't physical errors!
    
    There are two kinds of message: An order_anticipated and an order_placed. For every anticipated order, there's a placed order too.
    Say an anticipated ATO order is placed and arrives at the shop floor.
    Because we're working with ATO, the shop floor pauses production on this order and places it into Storage.
    Shop floor then waits for a matching placed order to also arrive on its work queue.
    It takes the previous order out of Storage, and processes the message, passing it back through the queue until the complete.
    
    Note that we only use Storage for ATO and MTS.
    
    Note that QA will sometimes push orders *back through the system* when they're found to be improperly done.
    This is sorted already in our model, because what's pushed back through isn't an order_anticipated but an order_placed, so it's done first.
    order_placed should get priority over order_anticipated, so the work queue needs to be a priority queue, sorted by type and then by time.
    
    [Queue.PriorityQueue](https://docs.python.org/2/library/queue.html#module-Queue) will sort queue entries giving the *smallest* of them priority.
    I'll make my entries into the work queue take the form ((order_type, order_number), order_object), so that we sort by type, then by age
    (giving smaller order numbers priority means we do things chronologically)
    
* Put together a `SimulationAgent` class that does most of the heavy lifting for the above, and helps to interact properly with Theatre.
    
    

## Mon 23rd July

* Began the domain model again with the rethought connections and functionality from the weekend
* Logged some potential variance options in the readme.txt