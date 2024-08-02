import boa
import boa_vvm


def test_load_partial_vvm():
    contract_deployer = boa.load_partial_vvm("mocks/mock_3_10.vy", "0.3.10")
    contract = contract_deployer.deploy()
    assert contract.hello() == 42
