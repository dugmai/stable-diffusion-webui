import types

import pytest
import torch

from modules.torch_utils import get_param


@pytest.mark.parametrize("wrapped", [True, False])
def test_get_param(wrapped):
    mod = torch.nn.Linear(1, 1)
    cpu = torch.device("cpu")
    mod.to(dtype=torch.float16, device=cpu)
    if wrapped:
        # more or less how spandrel wraps a thing
        mod = types.SimpleNamespace(model=mod)
    p = get_param(mod)
    assert p.dtype == torch.float16
    assert p.device == cpu
