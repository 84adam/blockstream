# blockstream
A python 3 wrapper class for blockstream.info's Bitcoin block explorer API

Written in Python 3

Docs: https://github.com/pasquantonio/blockstream/blob/master/docs.md

Block explorer: https://blockstream.info

API Reference: https://github.com/Blockstream/esplora/blob/master/API.md

## Install
```
pip install blockstream
```

if not in a python3 virtualenv make sure to use python3
```
pip3 install blockstream
```

## Run standalone "Ten Blocks" script

`git clone https://github.com/84adam/blockstream.git ; cd blockstream/ ; chmod +x tenblocks.py`
`./tenblocks.py`

EXAMPLE OUTPUT FROM 'tenblocks.py':

```
HEADER   HASH                                                               TIME (UTC)             
593282 - 00000000000000000008a7cc8e38b24c91df803147be280896a0580f06acc404 - 2019/09/05 01:04:00
593281 - 00000000000000000002f80eb0d566456d78c0bc005c38be9fb0f5cd8e8f401f - 2019/09/05 00:52:30
593280 - 0000000000000000000db45da1a64794dfe1e7992a115d5a67621d9c4d419067 - 2019/09/05 00:49:03
593279 - 00000000000000000008ee8e1a554c42baa15d6aa23b7cd15a6e2ad95e6cf522 - 2019/09/05 00:47:26
593278 - 0000000000000000000ccb89ad8fb6c8bdf740141077a2cdccc232d3e973c04a - 2019/09/05 00:43:22
593277 - 0000000000000000001571b16e468b696360e14098ef8268c3ebddb1b3af6d82 - 2019/09/05 00:24:07
593276 - 000000000000000000070fa45b3e3fc1f669498bb3f18991db33c6d2b94af5f0 - 2019/09/05 00:12:39
593275 - 00000000000000000019a023954abcc049a34e9cc1cca025c933e2003c66e6fd - 2019/09/05 00:07:55
593274 - 0000000000000000001a02b38c821a5a8713c2a40d34ef753780bd561482df0b - 2019/09/04 23:54:16
593273 - 000000000000000000199363b99e0ab2a4e3231b0fde369af9fc328093eba617 - 2019/09/04 23:53:50
```

## Usage
```python
from blockstream import blockexplorer

# get transaction by id
tx_id = '56a5b477182cddb6edb460b39135a3dc785eaf7ea88a572052a761d6983e26a2'
tx = blockexplorer.get_transaction(tx_id)

# get address data
address = '3ADPkym6mQ2HyP7uASh5g3VYauhCWZpczF'
addr_info = blockexplorer.get_address(address)
```

## Examples
Reference examples.py to see each method in use

## Issues
the `scripthash` endpoint seems to be broken, however you can get data about a scripthash address by calling the `address` endpoint. I have decided to remove the functions to hit the `scripthash` endpoint for now.
