class Stack:

    def __init__(self, items = [], limit = 100):
        if (type(limit) == int): pass;
        else: raise Exception("limit must be a number!");
        if (len(items) > limit): raise Exception("too many items in the stack!");
        else:
            self.limit = limit;
            self.items = [];
            for i in range(len(items)):
                self.items.append(items[i]);

    def isEmpty(self):
        if (self.items == None): return True;
        else: return (len(self.items) < 1);

    def push(self, item):
        if (self.full()): return;#should be an error
        else: self.items.append(item);

    def pop(self):
        if (self.isEmpty()): return None;#should be an error
        else:
            val = self.items.pop();
            return val;

    def peek(self):
        if (self.isEmpty()): return None;#should be an error
        else: return self.items[self.size() - 1];
    
    def size(self):
        return len(self.items);

    def full(self):
        if (self.limit == None): return False;
        else: return (self.size() == self.limit or self.limit < self.size());

    def search(self, target):
        if (self.isEmpty()): return -1;#or error value
        elif (self.peek() == target): return 0;
        else:
            mremitems = [];
            while (self.peek() != target):
                mremitems.append(self.pop());
                #print(mremitems);
                sval = self.search(target);
                retval = self.search(target) + 1;
                for item in mremitems: self.push(item);
                if (sval < 0): return sval;
                else: return retval;
            return -1;#or error value
            
#mstack = Stack([5,6,7,8,9,10]);
#print(mstack.search(5));
#print(f"mstack.items = {mstack.items}");
#print(mstack.search(6));
#print(f"mstack.items = {mstack.items}");
#print(mstack.search(7));
#print(f"mstack.items = {mstack.items}");
#print(mstack.search(8));
#print(f"mstack.items = {mstack.items}");
#print(mstack.search(9));
#print(f"mstack.items = {mstack.items}");
#print(mstack.search(10));
#print(f"mstack.items = {mstack.items}");
#print(mstack.search(11));
#print(f"mstack.items = {mstack.items}");
