class Printable:
    def __repr__(self):
        return str(self.__dict__)
        # return 'Index: {}, Previous Hash: {}, Proof: {}, Transactions: {}'.format(self.index, self.previous_hash, self.proof, self.transactions 
        # )