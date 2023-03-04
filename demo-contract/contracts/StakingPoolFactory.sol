// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

//TODO CREATE A FACTORY BASED ON NEW ULTRA POOL
/// @notice Factory used to deploy new staking pool
contract StakingPoolFactory {
  event StakingPoolCreated(
    CollectionBuyCrowdfund crowdfund,
    CollectionBuyCrowdfund.CollectionBuyCrowdfundOptions opts
  );
  // Set the `Globals` contract.
  /// @notice Create a new crowdfund to purchase a specific NFT (i.e., with a
  ///         known token ID) listing for a known price.
  /// @param opts Options used to initialize the crowdfund. These are fixed
  ///             and cannot be changed later.
  /// @param createGateCallData Encoded calldata used by `createGate()` to
  ///                           create the crowdfund if one is specified in `opts`.
  //     function createStakingPool(
  //         BuyCrowdfund.BuyCrowdfundOptions memory opts,
  //         bytes memory createGateCallData
  //     ) public payable returns (BuyCrowdfund inst) {
  //         opts.gateKeeperId = _prepareGate(opts.gateKeeper, opts.gateKeeperId, createGateCallData);
  //         inst = BuyCrowdfund(
  //             payable(
  //                 new Proxy{ value: msg.value }(
  //                     _GLOBALS.getImplementation(LibGlobals.GLOBAL_BUY_CF_IMPL),
  //                     abi.encodeCall(BuyCrowdfund.initialize, (opts))
  //                 )
  //             )
  //         );
  //         emit StakingPoolCreated(crowdfund, opts);
  //     }
}
