# Copyright (c) 2020 Chris Richardson
# FEniCS Project
# SPDX-License-Identifier: MIT

import numpy as np
import pytest

import basix


@pytest.mark.parametrize("order", [1, 2, 3])
def test_quad(order):
    Lpts, Lwts = basix.make_quadrature(basix.CellType.interval, 2*order + 1)
    Qwts = []
    Qpts = []
    for p, u in zip(Lpts, Lwts):
        for q, v in zip(Lpts, Lwts):
            Qpts.append([p[0], q[0]])
            Qwts.append(u * v)
    Qpts = np.array(Qpts)
    basis = basix._basixcpp.tabulate_polynomial_set(
        basix.CellType.quadrilateral, basix.PolysetType.standard, order, 0, Qpts)[0]
    ndofs = basis.shape[0]

    mat = np.zeros((ndofs, ndofs))
    for i in range(ndofs):
        for j in range(ndofs):
            mat[i, j] = sum(basis[i, :] * basis[j, :] * Qwts)

    assert np.allclose(mat, np.eye(ndofs))


@pytest.mark.parametrize("order", [1, 2, 3, 4])
def test_pyramid(order):
    Lpts, Lwts = basix.make_quadrature(basix.CellType.interval, 4*order + 2)
    Qwts = []
    Qpts = []
    for p, u in zip(Lpts, Lwts):
        for q, v in zip(Lpts, Lwts):
            for r, w in zip(Lpts, Lwts):
                sc = (1.0 - r[0])
                Qpts.append([p[0] * sc, q[0] * sc, r[0]])
                Qwts.append(u * v * sc * sc * w)
    Qpts = np.array(Qpts)
    basis = basix._basixcpp.tabulate_polynomial_set(
        basix.CellType.pyramid, basix.PolysetType.standard,  order, 0, Qpts)[0]
    ndofs = basis.shape[0]

    mat = np.zeros((ndofs, ndofs))
    for i in range(ndofs):
        for j in range(ndofs):
            mat[i, j] = sum(basis[i, :] * basis[j, :] * Qwts)

    assert np.allclose(mat, np.eye(ndofs))


@pytest.mark.parametrize("order", [1, 2, 3])
def test_hex(order):
    Lpts, Lwts = basix.make_quadrature(basix.CellType.interval, 2*order + 1)
    Qwts = []
    Qpts = []
    for p, u in zip(Lpts, Lwts):
        for q, v in zip(Lpts, Lwts):
            for r, w in zip(Lpts, Lwts):
                Qpts.append([p[0], q[0], r[0]])
                Qwts.append(u * v * w)
    Qpts = np.array(Qpts)
    basis = basix._basixcpp.tabulate_polynomial_set(
        basix.CellType.hexahedron, basix.PolysetType.standard, order, 0, Qpts)[0]
    ndofs = basis.shape[0]

    mat = np.zeros((ndofs, ndofs))
    for i in range(ndofs):
        for j in range(ndofs):
            mat[i, j] = sum(basis[i, :] * basis[j, :] * Qwts)

    assert np.allclose(mat, np.eye(ndofs))


@pytest.mark.parametrize("order", [1, 2, 3])
def test_prism(order):
    Tpts, Twts = basix.make_quadrature(basix.CellType.triangle, 2*order + 1)
    Lpts, Lwts = basix.make_quadrature(basix.CellType.interval, 2*order + 1)
    Qwts = []
    Qpts = []
    for p, u in zip(Tpts, Twts):
        for q, v in zip(Lpts, Lwts):
            Qpts.append([p[0], p[1], q[0]])
            Qwts.append(u * v)
    Qpts = np.array(Qpts)
    basis = basix._basixcpp.tabulate_polynomial_set(
        basix.CellType.prism, basix.PolysetType.standard, order, 0, Qpts)[0]
    ndofs = basis.shape[0]

    mat = np.zeros((ndofs, ndofs))
    for i in range(ndofs):
        for j in range(ndofs):
            mat[i, j] = sum(basis[i, :] * basis[j, :] * Qwts)

    assert np.allclose(mat, np.eye(ndofs))


@pytest.mark.parametrize("cell_type", [
    basix.CellType.interval,
    basix.CellType.triangle,
    basix.CellType.quadrilateral,
    basix.CellType.tetrahedron,
    basix.CellType.hexahedron,
    basix.CellType.prism,
])
@pytest.mark.parametrize("order", [0, 1, 2, 3, 4])
def test_standard(cell_type, order):
    Qpts, Qwts = basix.make_quadrature(cell_type, 2*order + 1)
    basis = basix._basixcpp.tabulate_polynomial_set(
        cell_type, basix.PolysetType.standard, order, 0, Qpts)[0]

    ndofs = basis.shape[0]
    mat = np.zeros((ndofs, ndofs))
    for i in range(ndofs):
        for j in range(ndofs):
            mat[i, j] = sum(basis[i, :] * basis[j, :] * Qwts)

    assert np.allclose(mat, np.eye(ndofs))


@pytest.mark.parametrize("cell_type", [
    basix.CellType.interval,
    basix.CellType.triangle,
    basix.CellType.tetrahedron,
    basix.CellType.quadrilateral,
    basix.CellType.hexahedron,
])
@pytest.mark.parametrize("order", [0, 1, 2, 3, 4])
def test_macroedge(cell_type, order):
    if cell_type == basix.CellType.triangle and order > 2:
        pytest.xfail("Degree > 2 edge macro polysets not implemented on triangles.")
    if cell_type == basix.CellType.tetrahedron and order > 1:
        pytest.xfail("Degree > 1 edge macro polysets not implemented on tetrahedra.")

    Qpts, Qwts = basix.make_quadrature(cell_type, 2*order + 1, polyset_type=basix.PolysetType.macroedge)
    basis = basix._basixcpp.tabulate_polynomial_set(
        cell_type, basix.PolysetType.macroedge, order, 0, Qpts)[0]

    ndofs = basis.shape[0]
    mat = np.zeros((ndofs, ndofs))
    for i in range(ndofs):
        for j in range(ndofs):
            mat[i, j] = sum(basis[i, :] * basis[j, :] * Qwts)
    assert np.allclose(mat, np.eye(ndofs))
