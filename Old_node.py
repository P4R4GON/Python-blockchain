from uuid import uuid4

from blockchain import Blockchain
from utils.verification import Verification
from wallet import Wallet

class Node :

    def __init__(self):
        # self.wallet.public_key = st
        self.wallet = Wallet()                
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)

    def get_transaction_value(self):
        
        tx_recipient = input ('Enter The Recipient Of the Transaction ')

        tx_amount = float(input('Your Transaction Amount Please:'))
        return (tx_recipient, tx_amount)

    def get_user_choice(self):
        user_input = input('Your Choice :')
        return user_input

    def print_blockchain_elements(self):
        for block in self.blockchain.chain:
            print ('Outputting The Block')
            print(block)



    def listen_for_input(self):

        waiting_for_input = True 

        while waiting_for_input:
            print('Please Choose')
            print ('1: Add a New Transaction Value ')
            print ('2: Mine a new Block ')
            print ('3: Output the Blockchain Blocks')
            print ('4: Check Transaction Validity')
            print ('5: Create Wallet')
            print ('6: Load Wallet')
            print ('7: Save Keys')
            print ('q: Quit')
            
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data 
                
                signature = self.wallet.sign_transaction(self.wallet.public_key, recipient, amount)

                if self.blockchain.add_transaction(recipient, self.wallet.public_key, signature, amount = amount):
                    print('Added Transaction!')
                else :
                    print('Transaction Failed')
                print(self.blockchain.get_open_transactions())
            elif user_choice == '2' :
                if not self.blockchain.mine_block():
                    print('Mining Failed, Got No Wallet?')

            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('All Transactions are Valid')
                else :
                    print('There are Invalid Transactions')
            elif user_choice == '5':
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '6':
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '7':
                self.wallet.save_keys()
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print ('Input was Invalid , Please Pick a Value From the List ')
            
            if not Verification.verify_chain(self.blockchain.chain):
                self.print_blockchain_elements()
                print('Invalid Blockchain !')
                break
            print('Balance of {} : {:6.2f}'.format(self.wallet.public_key, self.blockchain.get_balance())) 
        else :
            print('User Left !')    

if __name__ == '__main__':
        node = Node()
        node.listen_for_input()
