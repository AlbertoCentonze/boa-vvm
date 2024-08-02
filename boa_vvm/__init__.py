from pathlib import Path

from .vvm_deployer import VVMDeployer
import boa
import vvm


def load_partial_vvm(filename: str, version: str):
    vvm.install_vyper(version=version)
    compiled_src = vvm.compile_files([filename])
    abi = compiled_src[filename]["abi"]
    bytecode = compiled_src[filename]["bytecode"]
    bytecode = bytes.fromhex(bytecode[2:])
    return VVMDeployer(abi, bytecode, filename=filename)


boa.load_partial_vvm = load_partial_vvm

if __name__ == "__main__":
    contract_deployer = boa.load_partial_vvm("foo.vy", "0.3.10")
    contract = contract_deployer.deploy()

