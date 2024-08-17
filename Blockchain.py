class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.currentTransactions = []

    def new_block(self):
        # Function that creates a new block and add to the chain
        pass

    def new_transaction(self):
        # Function that creates a new transaction and adds it to the list of transaction
        pass

    @staticmethod
    def hash(block):
        # Hashes a block
        pass

    @property
    def last_block(self):
        # Returns the last block in a chain
        pass

