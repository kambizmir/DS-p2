import hashlib
import time


class Block:

    def __init__(self, timestamp, data, previous_hash, index, next):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.index = index
        self.next = next


    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class Blockchain():

    def __init__(self):
        self.genesis = None
        self.last = None
    def add(self, data):
        if not self.genesis:
            self.genesis = Block(time.gmtime() , data , 0, 0, None)
            self.last = self.genesis
        else:
            new_block = Block(time.gmtime(), data, self.last.hash, self.last.index + 1, None)
            self.last.next = new_block
            self.last = new_block
    def traverse(self):
        block = self.genesis
        while block:
            print(f'index={block.index} \nts={block.timestamp} \ndata={block.data} \nhash={block.hash} \nprev_hash={block.previous_hash} ', "\n")
            block = block.next


bc1 = Blockchain()
bc1.add("5")
bc1.add("10")
bc1.add("15")
bc1.add("20")

bc1.traverse() 

print("---------------")


bc2 = Blockchain()
bc2.add("this")
bc2.add("is")
bc2.add("a")
bc2.add("simple")
bc2.add("blockchain")

bc2.traverse() 


