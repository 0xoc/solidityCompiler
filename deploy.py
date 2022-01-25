import json
from solcx import compile_standard, install_solc


install_solc("0.6.0")

with open("SimpleStorage.sol") as file:
    simple_storage_file_content = file.read()

    print(simple_storage_file_content)

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file_content}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)

with open("compiled.json", "w") as file:
    json.dump(compiled_sol, file)


bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

address = "0x8eB7CCD9E806286241634DC6e1f0460A28E8f4Bb"
