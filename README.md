# Vyper Version Manager Plugin for Titanoboa

This plugin enables deployment and interaction with smart contracts written in legacy versions of Vyper. Previously
compiler versions are installed through [Vyper Version Manager (vvm)](https://github.com/vyperlang/vvm)

## Usage

```python
import boa
import boa_vvm

vvm_deployer = boa.load_partial_vvm("Counter.sol")

vvm_contract = vvm_deployer.deploy()

# or attach to existing contract (useful when forking mainnet state)

vvm_contract = vvm_deployer.at(<addr>)
```

## Acknowledgments
Thanks to [z80dev](https://github.com/z80dev) for the solc plugin, from which this plugin is heavily inspired and to
the Vyper team for creating Vyper and VVM.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.