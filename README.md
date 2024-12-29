# Ethereum Wallet Generator

This Python project demonstrates how to generate Ethereum wallets using the BIP-39 and BIP-44 standards. The script also checks the Ethereum balance of the generated wallet using the Web3 library.

## Features

- Generates a 12-word mnemonic using the BIP-39 word list.
- Derives Ethereum wallets using the BIP-44 standard.
- Fetches Ethereum wallet balances from the blockchain using Web3.
- Prints the private key of wallets with a non-zero balance.

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.8+** installed.
2. **Dependencies** listed in the `requirements.txt` file installed (see below).
3. An **Ethereum provider URL** (e.g., Infura) with access to the Ethereum blockchain.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ethereum-wallet-generator.git
   cd ethereum-wallet-generator
