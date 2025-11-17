from solcx import compile_standard, install_solc, get_installable_solc_versions
import json

# Install Solidity compiler
install_solc("0.8.0")

# Load Solidity code
with open("TransferContract.sol", "r") as file:
    contract_source_code = file.read()
# Compile the contract
compiled_contract = compile_standard({
    "language": "Solidity",
    "sources": {"TransferContract.sol": {"content": contract_source_code}},
    "settings": {
        "outputSelection": {
            "*": {"*": ["abi", "evm.bytecode.object"]}
        }
    }
})

abi = compiled_contract["contracts"]["TransferContract.sol"]["TransferContract"]["abi"]
bytecode = compiled_contract["contracts"]["TransferContract.sol"]["TransferContract"]["evm"]["bytecode"]["object"]
print(bytecode)
# Save ABI and bytecode for later use
with open("TransferContract_abi.json", "w") as abi_file:
    json.dump(abi, abi_file)