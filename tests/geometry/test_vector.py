# LICENSE HEADER MANAGED BY add-license-header
#
# Copyright 2018 Kornia Team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import pytest
import torch

from kornia.geometry.vector import Scalar, Vector2, Vector3

from testing.base import BaseTester


class TestVector3(BaseTester):
    def test_smoke(self, device, dtype):
        vec = Vector3.random(device=device, dtype=dtype)
        assert vec.shape == (3,)
        assert vec.x is not None
        assert vec.y is not None
        assert vec.z is not None

    @pytest.mark.parametrize("batch_size", (1, 2, 5))
    def test_getitem(self, device, dtype, batch_size):
        xyz = torch.rand((batch_size, 3), device=device, dtype=dtype)
        vec = Vector3(xyz)
        for i in range(batch_size):
            v = vec[i]
            self.assert_close(v.data, xyz[i, ...])

    @pytest.mark.parametrize("shape", ((), (1,), (2, 4)))
    def test_cardinality(self, device, dtype, shape):
        vec = Vector3.random(shape, device, dtype)
        assert vec.shape[:-1] == shape
        assert vec.x.shape == shape
        assert vec.y.shape == shape
        assert vec.z.shape == shape

    def test_from_coords(self):
        vec = Vector3.from_coords(0.0, 1.0, 0.0)
        assert vec.shape == (3,)
        assert vec.x == 0.0
        assert vec.y == 1.0
        assert vec.z == 0.0

    @pytest.mark.parametrize("shape", ((), (1,), (2, 4)))
    def test_from_coords_tensor(self, device, dtype, shape):
        xyz = torch.rand((*shape, 3), device=device, dtype=dtype)
        vec = Vector3.from_coords(xyz[..., 0], xyz[..., 1], xyz[..., 2])
        assert vec.shape[:-1] == shape
        assert vec.x.shape == shape
        assert vec.y.shape == shape
        assert vec.z.shape == shape

    @pytest.mark.parametrize("shape", (None, (1,), (2, 1)))
    def test_dot(self, device, dtype, shape):
        p0 = Vector3.random(shape, device, dtype)
        n0 = Vector3.random(shape, device, dtype).normalized()
        res: Scalar = p0.dot(n0)
        assert res.shape == () if shape is None else shape
        expected = torch.ones(shape or (), device=device, dtype=dtype)
        self.assert_close(n0.dot(n0), expected)

    @pytest.mark.parametrize("shape", (None, (1,), (2, 1)))
    def test_squared_norm(self, device, dtype, shape):
        p0 = Vector3.random(shape, device, dtype)
        res: Scalar = p0.squared_norm()
        assert res.shape == () if shape is None else shape

    @pytest.mark.skip(reason="not implemented yet")
    def test_jit(self, device, dtype):
        pass

    @pytest.mark.skip(reason="not implemented yet")
    def test_exception(self, device, dtype):
        pass

    @pytest.mark.skip(reason="not implemented yet")
    def test_module(self, device, dtype):
        pass

    @pytest.mark.skip(reason="not implemented yet")
    def test_gradcheck(self, device):
        pass


class TestVector2(BaseTester):
    def test_smoke(self, device, dtype):
        vec = Vector2.random(device=device, dtype=dtype)
        assert vec.shape == (2,)
        assert vec.x is not None
        assert vec.y is not None

    @pytest.mark.parametrize("batch_size", (1, 2, 5))
    def test_getitem(self, device, dtype, batch_size):
        xy = torch.rand((batch_size, 2), device=device, dtype=dtype)
        vec = Vector2(xy)
        for i in range(batch_size):
            v = vec[i]
            self.assert_close(v.data, xy[i, ...])

    @pytest.mark.parametrize("shape", ((), (1,), (2, 4)))
    def test_cardinality(self, device, dtype, shape):
        vec = Vector2.random(shape, device, dtype)
        assert vec.shape[:-1] == shape
        assert vec.x.shape == shape
        assert vec.y.shape == shape

    def test_from_coords(self):
        vec = Vector2.from_coords(0.0, 1.0)
        assert vec.shape == (2,)
        assert vec.x == 0.0
        assert vec.y == 1.0

    @pytest.mark.parametrize("shape", ((), (1,), (2, 4)))
    def test_from_coords_tensor(self, device, dtype, shape):
        xy = torch.rand((*shape, 2), device=device, dtype=dtype)
        vec = Vector2.from_coords(xy[..., 0], xy[..., 1])
        assert vec.shape[:-1] == shape
        assert vec.x.shape == shape
        assert vec.y.shape == shape

    @pytest.mark.parametrize("shape", (None, (1,), (2, 1)))
    def test_dot(self, device, dtype, shape):
        p0 = Vector2.random(shape, device, dtype)
        n0 = Vector2.random(shape, device, dtype).normalized()
        res: Scalar = p0.dot(n0)
        assert res.shape == () if shape is None else shape
        expected = torch.ones(shape or (), device=device, dtype=dtype)
        self.assert_close(n0.dot(n0), expected)

    @pytest.mark.parametrize("shape", (None, (1,), (2, 1)))
    def test_squared_norm(self, device, dtype, shape):
        p0 = Vector2.random(shape, device, dtype)
        res: Scalar = p0.squared_norm()
        assert res.shape == () if shape is None else shape

    @pytest.mark.skip(reason="not implemented yet")
    def test_jit(self, device, dtype):
        pass

    @pytest.mark.skip(reason="not implemented yet")
    def test_exception(self, device, dtype):
        pass

    @pytest.mark.skip(reason="not implemented yet")
    def test_module(self, device, dtype):
        pass

    @pytest.mark.skip(reason="not implemented yet")
    def test_gradcheck(self, device):
        pass
