#!/usr/bin/python3

from brownie import *
from scripts.utils.helpers import *
import json


def main():

    deployer = get_deployer()

    # TODO change poolAddress, for your pool address which you can find printed on your console
    with open('contrat_addresses.json', "r") as f:
        contract_addresses = json.load(f)

    stakingPoolAddress = contract_addresses["stakingPool_addr"]
    lsdETHaddress = contract_addresses["lsdETH_addr"]

    stakingPool = StakingPool.at(stakingPoolAddress)
    lsdETH = LSDETH.at(lsdETHaddress)

    print("unStaking...")
    lsdETH.approve(stakingPool.address, 0.001 * 10 ** 18, {'from': deployer})
    stakingPool.unStake(0.001 * 10 ** 18, {'from': deployer})
