// Copyright (c) 2020 Chris Richardson
// FEniCS Project
// SPDX-License-Identifier:    MIT

#include "finite-element.h"
#include <iostream>

//-----------------------------------------------------------------------------
FiniteElement::FiniteElement(Cell::Type cell_type, int degree)
    : _cell_type(cell_type), _degree(degree)
{
  // Do nothing in base class
}
//-----------------------------------------------------------------------------
void FiniteElement::apply_dualmat_to_basis(
    const Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic,
                        Eigen::RowMajor>& coeffs,
    const Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic,
                        Eigen::RowMajor>& dualmat)
{
  auto A = coeffs * dualmat.transpose();

  _new_coeffs.resize(coeffs.rows(), coeffs.cols());

  // auto Ainv = A.inverse();
  //  new_coeffs = Ainv * coeffs;
  // faster to use solve()
  _new_coeffs = A.colPivHouseholderQr().solve(coeffs);

#ifndef NDEBUG
  std::cout << "Initial coeffs = \n[" << coeffs << "]\n";
  std::cout << "Dual matrix = \n[" << dualmat << "]\n";
  std::cout << "New coeffs = \n[" << _new_coeffs << "]\n";
#endif
}
//-----------------------------------------------------------------------------
