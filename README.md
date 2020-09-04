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

- `git clone https://github.com/84adam/blockstream.git ; cd blockstream/ ; chmod +x tenblocks.py`
- `./tenblocks.py`

**EXAMPLE OUTPUT FROM 'tenblocks.py':**

PRINT:

`Please select: (1) Print last 10 blocks; (2) HTML format: 1`

```
HEIGHT   HASH                                                               TIME (UTC)             
593541 - 0000000000000000000f4047fed547074081a456591a05f7b8db93327f20bbf0 - 2019/09/06 14:38:00
593540 - 0000000000000000001592f74bdb97635d1dccebd1aef554d131f50d65c72e38 - 2019/09/06 14:33:04
593539 - 0000000000000000000999851ef12d154efb48ef9d36769665dbbcb1bea2288b - 2019/09/06 14:19:35
593538 - 0000000000000000000410a23ca333438201321d5fa3318525d630e8643a5806 - 2019/09/06 14:07:17
593537 - 0000000000000000000e02cef1877e14ea35d09a0ab649752dccc54cb23866a5 - 2019/09/06 13:45:17
593536 - 0000000000000000001926b0aa451de3e7485cdd468b94852283ada069898d3e - 2019/09/06 13:26:46
593535 - 0000000000000000000fca4ad171eea2a8d17831ac97bb91f21ceedd526cff15 - 2019/09/06 13:10:50
593534 - 00000000000000000001161b200e73732ee85ac24260cb97a0e5fd44b03fa59c - 2019/09/06 13:09:32
593533 - 0000000000000000000db7c6f64d52730ffa0a78900f2dd4dd6e8eb7fb6f544b - 2019/09/06 13:00:17
593532 - 00000000000000000016caf3cc539c784e8f94dfb033ed34ab27eed98d317bdd - 2019/09/06 12:50:52
```
HTML FORMAT:

`Please select: (1) Print last 10 blocks; (2) HTML format: 2`

```
<html><body><pre>
HEIGHT   HASH                                                               TIME (UTC)             
593542 - 0000000000000000001158f5ae1e66a991b47985dfeff9d72c7343068fec7eb2 - 2019/09/06 14:45:50
593541 - 0000000000000000000f4047fed547074081a456591a05f7b8db93327f20bbf0 - 2019/09/06 14:38:00
593540 - 0000000000000000001592f74bdb97635d1dccebd1aef554d131f50d65c72e38 - 2019/09/06 14:33:04
593539 - 0000000000000000000999851ef12d154efb48ef9d36769665dbbcb1bea2288b - 2019/09/06 14:19:35
593538 - 0000000000000000000410a23ca333438201321d5fa3318525d630e8643a5806 - 2019/09/06 14:07:17
593537 - 0000000000000000000e02cef1877e14ea35d09a0ab649752dccc54cb23866a5 - 2019/09/06 13:45:17
593536 - 0000000000000000001926b0aa451de3e7485cdd468b94852283ada069898d3e - 2019/09/06 13:26:46
593535 - 0000000000000000000fca4ad171eea2a8d17831ac97bb91f21ceedd526cff15 - 2019/09/06 13:10:50
593534 - 00000000000000000001161b200e73732ee85ac24260cb97a0e5fd44b03fa59c - 2019/09/06 13:09:32
593533 - 0000000000000000000db7c6f64d52730ffa0a78900f2dd4dd6e8eb7fb6f544b - 2019/09/06 13:00:17
</pre></body></html>
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
