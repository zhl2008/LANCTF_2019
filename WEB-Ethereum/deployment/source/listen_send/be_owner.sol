pragma solidity ^0.4.24;
contract be_owner{
    
   
    address public hacker = 0x0000128775Ae1206901CdF2A44Bef379b1E76905;
    address public owner;
    
    event SendFlag(string);
    
    
    modifier OnlyOwner {
        require (msg.sender == owner, "OnlyOwner methods called by non-owner.");
        _;
    }
    
    modifier OnlyHacker {
        require (msg.sender == hacker, "OnlyOwner methods called by non-hacker.");
        _;
    }
    
    constructor () public{
        owner = msg.sender;
    }
    
    function GetFlag(string email) OnlyOwner payable public{
        if(msg.value >= 0.1 ether){
        emit SendFlag(email);
        }
    }
    
    function paolu() OnlyHacker public{
        selfdestruct(hacker);
    }

}
