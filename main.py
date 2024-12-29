from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
from eth_account import Account
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

# Infura or any Ethereum provider URL
INFURA_URL = os.getenv('INFURA_URL')

# Web3 instance connected to Ethereum mainnet
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Generate a valid 12-word mnemonic from the BIP-39 word list
def generate_valid_mnemonic():
    return Bip39MnemonicGenerator().FromWordsNumber(12)

# Function to generate Ethereum wallet from mnemonic
def generate_wallet(mnemonic):
    # Generate seed from mnemonic
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    
    # Generate the Ethereum wallet (BIP44 standard)
    bip44_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
    bip44_acc = bip44_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT)
    bip44_addr = bip44_acc.AddressIndex(0)
    
    # Get the wallet's public address and private key
    private_key = bip44_addr.PrivateKey().Raw().ToHex()
    eth_account = Account.from_key(private_key)
    
    return eth_account.address, private_key

# Function to check the balance of an Ethereum address
def get_eth_balance(address):
    try:
        balance_wei = web3.eth.get_balance(address)  # Balance in Wei (1 ETH = 10^18 Wei)
        balance_eth = web3.from_wei(balance_wei, 'ether')  # Convert to Ether
        return balance_eth
    except Exception as e:
        print(e)
        return 0

while True:
    # Generate a valid mnemonic
    mnemonic = generate_valid_mnemonic()
    print(f"Generated Mnemonic: {mnemonic}")

    # Generate wallet using the mnemonic
    wallet_address, wallet_private_key = generate_wallet(mnemonic)
    print(f"Wallet Address: {wallet_address}")

    # Get the Ethereum balance for the wallet
    balance = get_eth_balance(wallet_address)
    print(f"Balance: {balance} ETH")

    # If balance is greater than 0, print the private key
    if balance > 0:
        print(f"Private Key: {wallet_private_key}")
        break
    else:
        print("Wallet has no balance.")
