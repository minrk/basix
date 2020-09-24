// Copyright (c) 2020 Chris Richardson
// FEniCS Project
// SPDX-License-Identifier:    MIT

#include "cell.h"
#include "finite-element.h"

#pragma once

class RaviartThomas : public FiniteElement
{
  /// Raviart-Thomas element of given dimension (2 or 3) and degree k .
public:
  RaviartThomas(Cell::Type celltype, int k);

  Eigen::Array<double, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>
  tabulate_basis(const Eigen::Array<double, Eigen::Dynamic, Eigen::Dynamic,
                                    Eigen::RowMajor>& pts) const;
};
