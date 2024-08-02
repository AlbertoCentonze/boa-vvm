# Vyper Version Manager Plugin for Titanoboa

This plugin enables deployment and interaction with smart contracts written in legacy versions of Vyper.

## Usage

```python
import boa
import boa_vvm

vvm_deployer = boa.load_partial_vvm("Counter.sol")

vvm_contract = vvm_deployer.deploy()

# or attach to existing contract (useful when forking mainnet state)

vvm_contract = vvm_deployer.at(<addr>)
```