//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LSDETH is ERC20, Ownable {
  address public minter;
  uint256 public sharePrice = 1e18;

  // ICommon immutable CommonContract;
  constructor() ERC20("LSDETH", "lsdETH") {
    minter = msg.sender;
  }

  function mint(address recipient, uint256 amount) external onlyOwner {
    _mint(recipient, amount);
  }

  function changeSharePrice(uint256 new_price) external onlyOwner {
    sharePrice = new_price;
  }
}
