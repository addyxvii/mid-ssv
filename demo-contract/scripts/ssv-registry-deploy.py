#!/usr/bin/python3

from brownie import *
from scripts.utils.helpers import *
import json


def main():

    deployer = get_deployer()

    # # TODO OPTIONAL update these values
    # whitelist = "0x0000536dbD99d918092249Ef4eDe4a69A35CccCa"
    # withdrawal_creds = "0x0000536dbD99d918092249Ef4eDe4a69A35CccCa"
    # operator_ids = [1, 2, 9, 42]

    # deposit_contract = "0xff50ed3d0ec03ac01d4c79aad74928bff48a7b2b"
    # ssv_network_contract = "0xb9e155e65B5c4D66df28Da8E9a0957f06F11Bc04"
    # ssv_token_address = "0x3a9f01091C446bdE031E39ea8354647AFef091E7"

    print("Deploying ssvRegistryFactory...")
    lsdETH = LSDETH.deploy({'from': deployer})
    # print('lsdETH deployed to: ', lsdETH.address)

    print("deploying staking Pool...")
    stakingPool = StakingPool.deploy(whitelist, deposit_contract, withdrawal_creds,
                                     ssv_network_contract, ssv_token_address, lsdETH.address, operator_ids, {'from': deployer})
    # print("staking pool deployed to:", stakingPool.address)

    print("trasferring minting ownership...")
    lsdETH.transferOwnership(stakingPool.address, {'from': deployer})

    print("staking...")
    stakingPool.stake({'value': 0.001 * 10 ** 18, 'from': deployer})

    print("unStaking...")
    lsdETH.approve(stakingPool.address, 0.001 * 10 ** 18, {'from': deployer})
    stakingPool.unStake(0.001 * 10 ** 18, {'from': deployer})

    with open('contrat_addresses.json', "r") as f:
        data = json.load(f)

    data["stakingPool_addr"] = stakingPool.address
    data["lsdETH_addr"] = lsdETH.address

    with open('contrat_addresses.json', 'w') as f:
        json.dump(data, f)

    print("addresses written")
