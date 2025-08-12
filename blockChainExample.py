import hashlib
import json
from time import time
from typing import List, Dict

class Block:
    def __init__(self, index: int, timestamp: float, transactions: List[Dict], previous_hash: str, nonce: int=0):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce

    def to_dict(self):
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }

    def hash(self):
        block_string = json.dumps(self.to_dict(), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain: List[Block] = []
        self.current_transactions: List[Dict] = []
        self.difficulty = difficulty
        # create genesis block
        genesis = Block(0, time(), [], "0", 0)
        self.chain.append(genesis)

    def new_transaction(self, sender: str, recipient: str, amount: float) -> int:
        self.current_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        })
        return self.last_block.index + 1

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    def proof_of_work(self, block: Block) -> int:
        block.nonce = 0
        target = "0" * self.difficulty
        while True:
            h = block.hash()
            if h.startswith(target):
                return block.nonce
            block.nonce += 1

    def add_block(self, nonce: int, previous_hash: str = None):
        block = Block(
            index=len(self.chain),
            timestamp=time(),
            transactions=self.current_transactions,
            previous_hash=previous_hash or self.last_block.hash(),
            nonce=nonce
        )
        self.current_transactions = []
        self.chain.append(block)
        return block

    def mine(self, miner_address: str):
        # reward
        self.new_transaction("0", miner_address, 1)
        block = Block(index=len(self.chain), timestamp=time(), transactions=self.current_transactions, previous_hash=self.last_block.hash())
        nonce = self.proof_of_work(block)
        mined = self.add_block(nonce)
        return mined

    def valid_chain(self, chain: List[Block]) -> bool:
        for i in range(1, len(chain)):
            prev = chain[i-1]
            curr = chain[i]
            if curr.previous_hash != prev.hash():
                return False
            if not curr.hash().startswith("0" * self.difficulty):
                return False
        return True

# contoh pakai
if __name__ == "__main__":
    bc = Blockchain(difficulty=3)  # difficulty kecil agar cepat
    bc.new_transaction("alice", "bob", 10)
    mined = bc.mine("miner1")
    print("Mined block index:", mined.index, "hash:", mined.hash())
    print("Chain length:", len(bc.chain))
