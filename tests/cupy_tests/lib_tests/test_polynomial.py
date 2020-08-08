import unittest

import pytest
import numpy

import cupy
import cupyx
from cupy import testing


@testing.parameterize(
    {'variable': None},
    {'variable': 'y'},
)
@testing.gpu
class TestPoly1dInit(unittest.TestCase):

    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_array_equal()
    def test_poly1d_numpy_array(self, xp, dtype):
        a = numpy.arange(5, dtype=dtype)
        with cupyx.allow_synchronize(False):
            out = xp.poly1d(a, variable=self.variable)
        assert out.variable == (self.variable or 'x')
        return out

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_poly1d_cupy_array(self, xp, dtype):
        a = testing.shaped_arange((5,), xp, dtype)
        with cupyx.allow_synchronize(False):
            out = xp.poly1d(a, variable=self.variable)
        assert out.variable == (self.variable or 'x')
        return out

    @testing.numpy_cupy_array_equal()
    def test_poly1d_list(self, xp):
        with cupyx.allow_synchronize(False):
            out = xp.poly1d([1, 2, 3, 4], variable=self.variable)
        assert out.variable == (self.variable or 'x')
        return out

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_poly1d_numpy_poly1d(self, xp, dtype):
        array = testing.shaped_arange((5,), numpy, dtype)
        a = numpy.poly1d(array)
        with cupyx.allow_synchronize(False):
            out = xp.poly1d(a, variable=self.variable)
        assert out.variable == (self.variable or 'x')
        return out

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_poly1d_numpy_poly1d_variable(self, xp, dtype):
        array = testing.shaped_arange((5,), numpy, dtype)
        a = numpy.poly1d(array, variable='z')
        with cupyx.allow_synchronize(False):
            out = xp.poly1d(a, variable=self.variable)
        assert out.variable == (self.variable or 'z')
        return out

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_poly1d_cupy_poly1d(self, xp, dtype):
        array = testing.shaped_arange((5,), xp, dtype)
        a = xp.poly1d(array)
        out = xp.poly1d(a, variable=self.variable)
        assert out.variable == (self.variable or 'x')
        return out

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_poly1d_cupy_poly1d_variable(self, xp, dtype):
        array = testing.shaped_arange((5,), xp, dtype)
        a = xp.poly1d(array, variable='z')
        out = xp.poly1d(a, variable=self.variable)
        assert out.variable == (self.variable or 'z')
        return out

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_poly1d_zero_dim(self, xp, dtype):
        a = testing.shaped_arange((), xp, dtype)
        with cupyx.allow_synchronize(False):
            out = xp.poly1d(a, variable=self.variable)
        assert out.variable == (self.variable or 'x')
        return out

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_poly1d_zero_size(self, xp, dtype):
        a = testing.shaped_arange((0,), xp, dtype)
        with cupyx.allow_synchronize(False):
            out = xp.poly1d(a, variable=self.variable)
        assert out.variable == (self.variable or 'x')
        return out


@testing.gpu
class TestPoly1d(unittest.TestCase):

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_poly1d_leading_zeros(self, xp, dtype):
        a = xp.array([0, 0, 1, 2, 3], dtype)
        return xp.poly1d(a).coeffs

    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_array_equal()
    def test_poly1d_neg(self, xp, dtype):
        a = testing.shaped_arange((5,), xp, dtype)
        return -xp.poly1d(a)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_equal()
    def test_poly1d_order(self, xp, dtype):
        a = testing.shaped_arange((10,), xp, dtype)
        return xp.poly1d(a).order

    @testing.for_all_dtypes()
    @testing.numpy_cupy_equal()
    def test_poly1d_order_leading_zeros(self, xp, dtype):
        a = xp.array([0, 0, 1, 2, 3, 0], dtype)
        return xp.poly1d(a).order

    @testing.for_all_dtypes()
    @testing.numpy_cupy_equal()
    def test_poly1d_getitem1(self, xp, dtype):
        a = testing.shaped_arange((10,), xp, dtype)
        with cupyx.allow_synchronize(False):
            return xp.poly1d(a)[-1]

    @testing.for_all_dtypes()
    @testing.numpy_cupy_equal()
    def test_poly1d_getitem2(self, xp, dtype):
        a = testing.shaped_arange((10,), xp, dtype)
        with cupyx.allow_synchronize(False):
            return xp.poly1d(a)[5]

    @testing.for_all_dtypes()
    @testing.numpy_cupy_equal()
    def test_poly1d_getitem3(self, xp, dtype):
        a = testing.shaped_arange((10,), xp, dtype)
        with cupyx.allow_synchronize(False):
            return xp.poly1d(a)[100]

    @testing.for_all_dtypes()
    @testing.numpy_cupy_equal()
    def test_poly1d_getitem4(self, xp, dtype):
        a = xp.array([0, 0, 1, 2, 3, 0], dtype)
        with cupyx.allow_synchronize(False):
            return xp.poly1d(a)[2]

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_poly1d_setitem(self, xp, dtype):
        a = testing.shaped_arange((10,), xp, dtype)
        b = xp.poly1d(a)
        with cupyx.allow_synchronize(False):
            b[100] = 20
        return b

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_poly1d_setitem_leading_zeros(self, xp, dtype):
        a = xp.array([0, 0, 0, 2, 3, 0], dtype)
        b = xp.poly1d(a)
        with cupyx.allow_synchronize(False):
            b[1] = 10
        return b

    @testing.for_all_dtypes()
    def test_poly1d_setitem_neg(self, dtype):
        for xp in (numpy, cupy):
            a = testing.shaped_arange((10,), xp, dtype)
            b = xp.poly1d(a)
            with pytest.raises(ValueError):
                b[-1] = 20

    @testing.for_all_dtypes()
    def test_poly1d_get1(self, dtype):
        a1 = testing.shaped_arange((10,), cupy, dtype)
        a2 = testing.shaped_arange((10,), numpy, dtype)
        b1 = cupy.poly1d(a1, variable='z').get()
        b2 = numpy.poly1d(a2, variable='z')
        assert b1 == b2

    @testing.for_all_dtypes()
    def test_poly1d_get2(self, dtype):
        a1 = testing.shaped_arange((), cupy, dtype)
        a2 = testing.shaped_arange((), numpy, dtype)
        b1 = cupy.poly1d(a1).get()
        b2 = numpy.poly1d(a2)
        assert b1 == b2

    @testing.for_all_dtypes(no_bool=True)
    def test_poly1d_set(self, dtype):
        arr1 = testing.shaped_arange((10,), cupy, dtype)
        arr2 = numpy.ones(10, dtype=dtype)
        a = cupy.poly1d(arr1)
        b = numpy.poly1d(arr2, variable='z')
        a.set(b)
        assert a.variable == b.variable
        testing.assert_array_equal(a.coeffs, b.coeffs)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_equal()
    def test_poly1d_repr(self, xp, dtype):
        a = testing.shaped_arange((5,), xp, dtype)
        return repr(xp.poly1d(a))

    @testing.for_all_dtypes()
    @testing.numpy_cupy_equal()
    def test_poly1d_str(self, xp, dtype):
        a = testing.shaped_arange((5,), xp, dtype)
        return str(xp.poly1d(a))


class Poly1dTestBase(unittest.TestCase):

    def _get_input(self, xp, in_type, dtype):
        if in_type == 'poly1d':
            return xp.poly1d(testing.shaped_arange((10,), xp, dtype) + 1)
        if in_type == 'ndarray':
            return testing.shaped_arange((10,), xp, dtype)
        if in_type == 'python_scalar':
            return dtype(5).item()
        if in_type == 'numpy_scalar':
            return dtype(5)
        assert False


@testing.gpu
@testing.parameterize(*testing.product({
    'func': [
        lambda x, y: x + y,
        lambda x, y: x - y,
        lambda x, y: x * y,
    ],
    'type_l': ['poly1d', 'python_scalar'],
    'type_r': ['poly1d', 'ndarray', 'python_scalar', 'numpy_scalar'],
}))
class TestPoly1dArithmetic(Poly1dTestBase):

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose(rtol=1e-4, accept_error=TypeError)
    def test_poly1d_arithmetic(self, xp, dtype):
        a1 = self._get_input(xp, self.type_l, dtype)
        a2 = self._get_input(xp, self.type_r, dtype)
        return self.func(a1, a2)


@testing.gpu
@testing.parameterize(*testing.product({
    'func': [
        lambda x, y: x + y,
        lambda x, y: x - y,
        lambda x, y: x * y,
    ],
    'type_l': ['ndarray', 'numpy_scalar'],
    'type_r': ['poly1d'],
}))
class TestPoly1dArithmeticInvalid(Poly1dTestBase):

    @testing.for_all_dtypes()
    def test_poly1d_arithmetic_invalid(self, dtype):
        # CuPy does not support them because device-to-host synchronization is
        # needed to convert the return value to cupy.ndarray type.
        n1 = self._get_input(numpy, self.type_l, dtype)
        n2 = self._get_input(numpy, self.type_r, dtype)
        assert type(self.func(n1, n2)) is numpy.ndarray

        c1 = self._get_input(cupy, self.type_l, dtype)
        c2 = self._get_input(cupy, self.type_r, dtype)
        with pytest.raises(TypeError):
            self.func(c1, c2)


@testing.gpu
@testing.parameterize(*testing.product({
    'fname': ['polyadd', 'polysub', 'polymul'],
    'type_l': ['poly1d', 'ndarray', 'python_scalar', 'numpy_scalar'],
    'type_r': ['poly1d', 'ndarray', 'python_scalar', 'numpy_scalar'],
}))
class TestPoly1dRoutines(Poly1dTestBase):

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose(rtol=1e-4, accept_error=TypeError)
    def test_poly1d_routine(self, xp, dtype):
        func = getattr(xp, self.fname)
        a1 = self._get_input(xp, self.type_l, dtype)
        a2 = self._get_input(xp, self.type_r, dtype)
        return func(a1, a2)


class UserDefinedArray:

    __array_priority__ = cupy.poly1d.__array_priority__ + 10

    def __init__(self):
        self.op_count = 0
        self.rop_count = 0

    def __add__(self, other):
        self.op_count += 1

    def __radd__(self, other):
        self.rop_count += 1

    def __sub__(self, other):
        self.op_count += 1

    def __rsub__(self, other):
        self.rop_count += 1

    def __mul__(self, other):
        self.op_count += 1

    def __rmul__(self, other):
        self.rop_count += 1


@testing.gpu
@testing.parameterize(*testing.product({
    'func': [
        lambda x, y: x + y,
        lambda x, y: x - y,
        lambda x, y: x * y,
    ],
}))
class TestPoly1dArrayPriority(Poly1dTestBase):

    def test_poly1d_array_priority_greator(self):
        a1 = self._get_input(cupy, 'poly1d', 'int64')
        a2 = UserDefinedArray()
        self.func(a1, a2)
        assert a2.op_count == 0
        assert a2.rop_count == 1
        self.func(a2, a1)
        assert a2.op_count == 1
        assert a2.rop_count == 1


@testing.gpu
class TestPoly1dEquality(unittest.TestCase):

    def make_poly1d1(self, xp, dtype):
        a1 = testing.shaped_arange((4,), xp, dtype)
        a2 = xp.zeros((4,), dtype)
        b1 = xp.poly1d(a1)
        b2 = xp.poly1d(a2)
        return b1, b2

    def make_poly1d2(self, xp, dtype):
        a1 = testing.shaped_arange((4,), xp, dtype)
        a2 = testing.shaped_arange((4,), xp, dtype)
        b1 = xp.poly1d(a1)
        b2 = xp.poly1d(a2)
        return b1, b2

    @testing.for_all_dtypes()
    @testing.numpy_cupy_equal()
    def test_poly1d_eq1(self, xp, dtype):
        a, b = self.make_poly1d1(xp, dtype)
        return a == b

    @testing.for_all_dtypes()
    @testing.numpy_cupy_equal()
    def test_poly1d_eq2(self, xp, dtype):
        a, b = self.make_poly1d2(xp, dtype)
        return a == b

    @testing.for_all_dtypes()
    @testing.numpy_cupy_equal()
    def test_poly1d_ne1(self, xp, dtype):
        a, b = self.make_poly1d1(xp, dtype)
        return a != b

    @testing.for_all_dtypes()
    @testing.numpy_cupy_equal()
    def test_poly1d_ne2(self, xp, dtype):
        a, b = self.make_poly1d2(xp, dtype)
        return a != b


@testing.gpu
@testing.parameterize(*testing.product({
    'fname': ['polyadd', 'polysub', 'polymul'],
    'shape1': [(), (0,), (3,), (5,)],
    'shape2': [(), (0,), (3,), (5,)],
}))
class TestPolyArithmeticShapeCombination(unittest.TestCase):

    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose(rtol=1e-5)
    def test_polyroutine(self, xp, dtype):
        func = getattr(xp, self.fname)
        a = testing.shaped_arange(self.shape1, xp, dtype)
        b = testing.shaped_arange(self.shape2, xp, dtype)
        return func(a, b)


@testing.gpu
@testing.parameterize(*testing.product({
    'fname': ['polyadd', 'polysub', 'polymul'],
}))
class TestPolyArithmeticDiffTypes(unittest.TestCase):

    @testing.for_all_dtypes_combination(names=['dtype1', 'dtype2'])
    @testing.numpy_cupy_allclose(rtol=1e-5, accept_error=TypeError)
    def test_polyroutine_diff_types_array(self, xp, dtype1, dtype2):
        func = getattr(xp, self.fname)
        a = testing.shaped_arange((10,), xp, dtype1)
        b = testing.shaped_arange((5,), xp, dtype2)
        return func(a, b)

    @testing.for_all_dtypes_combination(names=['dtype1', 'dtype2'])
    @testing.numpy_cupy_allclose(rtol=1e-5, accept_error=TypeError)
    def test_polyroutine_diff_types_poly1d(self, xp, dtype1, dtype2):
        func = getattr(xp, self.fname)
        a = testing.shaped_arange((10,), xp, dtype1)
        b = testing.shaped_arange((5,), xp, dtype2)
        a = xp.poly1d(a, variable='z')
        b = xp.poly1d(b, variable='y')
        out = func(a, b)
        assert out.variable == 'x'
        return out


@testing.gpu
@testing.parameterize(*testing.product({
    'fname': ['polyadd', 'polysub', 'polymul'],
}))
class TestPolyArithmeticNdim(unittest.TestCase):

    @testing.for_all_dtypes()
    def test_polyroutine_ndim(self, dtype):
        for xp in (numpy, cupy):
            func = getattr(xp, self.fname)
            a = testing.shaped_arange((2, 3, 4), xp, dtype)
            b = testing.shaped_arange((10, 5), xp, dtype)
            with pytest.raises(ValueError):
                func(a, b)


@testing.gpu
@testing.parameterize(*testing.product({
    'shape1': [(3,)],
    'shape2': [(3,), (3, 2)],
    'deg': [0, 3, 3.0, 3.5, 10],
    'rcond': [None, 0.5, 1e-15],
    'weighted': [True, False]
}))
class TestPolyfitParametersCombinations(unittest.TestCase):

    def _full_fit(self, xp, dtype):
        x = testing.shaped_arange(self.shape1, xp, dtype)
        y = testing.shaped_arange(self.shape2, xp, dtype)
        w = x if self.weighted else None
        return xp.polyfit(x, y, self.deg, self.rcond, True, w)

    @testing.for_all_dtypes(no_float16=True, no_bool=True)
    @testing.numpy_cupy_allclose(rtol=1e-6)
    def test_polyfit_default(self, xp, dtype):
        x = testing.shaped_arange(self.shape1, xp, dtype)
        y = testing.shaped_arange(self.shape2, xp, dtype)
        w = x if self.weighted else None
        return xp.polyfit(x, y, self.deg, self.rcond, w=w)

    @testing.for_all_dtypes(no_float16=True, no_bool=True, no_complex=True)
    def test_polyfit_full(self, dtype):
        cp_c, cp_resids, cp_rank, cp_s, cp_rcond = self._full_fit(cupy, dtype)
        np_c, np_resids, np_rank, np_s, np_rcond = self._full_fit(numpy, dtype)

        testing.assert_allclose(cp_c, np_c, rtol=1e-5)
        testing.assert_allclose(cp_resids, np_resids)
        testing.assert_allclose(cp_s, np_s)
        assert cp_rank == np_rank
        if self.rcond is not None:
            assert cp_rcond == np_rcond


@testing.gpu
@testing.parameterize(*testing.product({
    'shape': [(3,), (3, 2)],
    'deg': [0, 1],
    'rcond': [None, 1e-15],
    'weighted': [True, False],
    'cov': ['unscaled', True]
}))
class TestPolyfitCovMode(unittest.TestCase):

    def _cov_fit(self, xp, dtype):
        x = xp.array([0.008, 0.01, 0.015], dtype)
        y = testing.shaped_arange(self.shape, xp, dtype)
        w = x if self.weighted else None
        return xp.polyfit(x, y, self.deg, self.rcond, w=w, cov=self.cov)

    @testing.for_float_dtypes(no_float16=True)
    def test_polyfit_cov(self, dtype):
        cp_c, cp_cov = self._cov_fit(cupy, dtype)
        np_c, np_cov = self._cov_fit(numpy, dtype)
        testing.assert_allclose(cp_c, np_c, rtol=1e-5)
        testing.assert_allclose(cp_cov, np_cov, rtol=1e-3)


@testing.gpu
class TestPolyfit(unittest.TestCase):

    @testing.for_all_dtypes(no_float16=True)
    def test_polyfit(self, dtype):
        for xp in (numpy, cupy):
            x = testing.shaped_arange((5,), xp, dtype)
            y = testing.shaped_arange((5,), xp, dtype)
            with pytest.warns(numpy.RankWarning):
                xp.polyfit(x, y, 6)


@testing.gpu
@testing.parameterize(*testing.product({
    'shape': [(), (0,), (5, 3, 3)],
}))
class TestPolyfitInvalidShapes(unittest.TestCase):

    @testing.for_all_dtypes()
    def test_polyfit_x_invalid_shape(self, dtype):
        for xp in (numpy, cupy):
            x = testing.shaped_arange(self.shape, xp, dtype)
            y = testing.shaped_arange((5,), xp, dtype)
            with pytest.raises(TypeError):
                xp.polyfit(x, y, 5)

    @testing.for_all_dtypes()
    def test_polyfit_y_invalid_shape(self, dtype):
        for xp in (numpy, cupy):
            x = testing.shaped_arange((5,), xp, dtype)
            y = testing.shaped_arange(self.shape, xp, dtype)
            with pytest.raises(TypeError):
                xp.polyfit(x, y, 5)

    @testing.for_all_dtypes()
    def test_polyfit_w_invalid_shape(self, dtype):
        for xp in (numpy, cupy):
            x = testing.shaped_arange((5,), xp, dtype)
            w = testing.shaped_arange(self.shape, xp, dtype)
            with pytest.raises(TypeError):
                xp.polyfit(x, x, 5, w=w)


@testing.gpu
class TestPolyfitInvalid(unittest.TestCase):

    @testing.for_all_dtypes()
    def test_polyfit_neg_degree(self, dtype):
        for xp in (numpy, cupy):
            x = testing.shaped_arange((5,), xp, dtype)
            y = testing.shaped_arange((5,), xp, dtype)
            with pytest.raises(ValueError):
                xp.polyfit(x, y, -4)

    @testing.for_all_dtypes()
    def test_polyfit_complex_degree(self, dtype):
        for xp in (numpy, cupy):
            x = testing.shaped_arange((5,), xp, dtype)
            y = testing.shaped_arange((5,), xp, dtype)
            with pytest.raises(TypeError):
                xp.polyfit(x, y, 5j)

    @testing.for_all_dtypes()
    def test_polyfit_xy_mismatched_length(self, dtype):
        for xp in (numpy, cupy):
            x = testing.shaped_arange((10,), xp, dtype)
            y = testing.shaped_arange((5,), xp, dtype)
            with pytest.raises(TypeError):
                xp.polyfit(x, y, 5)

    @testing.for_all_dtypes()
    def test_polyfit_yw_mismatched_length(self, dtype):
        for xp in (numpy, cupy):
            y = testing.shaped_arange((10,), xp, dtype)
            w = testing.shaped_arange((5,), xp, dtype)
            with pytest.raises(TypeError):
                xp.polyfit(y, y, 5, w=w)

    @testing.for_all_dtypes(no_float16=True, no_bool=True)
    def test_polyfit_cov_invalid(self, dtype):
        for xp in (numpy, cupy):
            x = testing.shaped_arange((5,), xp, dtype)
            y = testing.shaped_arange((5,), xp, dtype)
            with pytest.raises(ValueError):
                xp.polyfit(x, y, 5, cov=True)


@testing.gpu
class TestPolyfitDiffTypes(unittest.TestCase):

    @testing.for_all_dtypes_combination(
        names=['dtype1', 'dtype2'], no_float16=True, no_bool=True)
    @testing.numpy_cupy_allclose()
    def test_polyfit_unweighted_diff_types(self, xp, dtype1, dtype2):
        x = testing.shaped_arange((5,), xp, dtype1)
        y = testing.shaped_arange((5,), xp, dtype2)
        return xp.polyfit(x, y, 5)

    @testing.for_all_dtypes_combination(
        names=['dtype1', 'dtype2', 'dtype3'],
        no_float16=True, no_bool=True, no_complex=True)
    @testing.numpy_cupy_allclose(rtol=1e-3)
    def test_polyfit_weighted_diff_types(self, xp, dtype1, dtype2, dtype3):
        x = testing.shaped_arange((5,), xp, dtype1)
        y = testing.shaped_arange((5,), xp, dtype2)
        w = testing.shaped_arange((5,), xp, dtype3) / dtype3(5)
        return xp.polyfit(x, y, 5, w=w)
