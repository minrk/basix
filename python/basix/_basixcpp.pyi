from typing import Any, ClassVar

import nanobind

cell_facet_jacobians: nanobind.nb_func
cell_facet_normals: nanobind.nb_func
cell_facet_orientations: nanobind.nb_func
cell_facet_outward_normals: nanobind.nb_func
cell_facet_reference_volumes: nanobind.nb_func
cell_volume: nanobind.nb_func
compute_interpolation_operator: nanobind.nb_func
create_custom_element_float32: nanobind.nb_func
create_custom_element_float64: nanobind.nb_func
create_element: nanobind.nb_func
create_lattice: nanobind.nb_func
create_tp_element: nanobind.nb_func
geometry: nanobind.nb_func
index: nanobind.nb_func
make_quadrature: nanobind.nb_func
polynomials_dim: nanobind.nb_func
restriction: nanobind.nb_func
sobolev_space_intersection: nanobind.nb_func
sub_entity_connectivity: nanobind.nb_func
sub_entity_geometry: nanobind.nb_func
superset: nanobind.nb_func
tabulate_polynomial_set: nanobind.nb_func
tabulate_polynomials: nanobind.nb_func
topology: nanobind.nb_func
tp_factors: nanobind.nb_func
tp_dof_ordering: nanobind.nb_func
__version__: str

class CellType:
    __entries__: ClassVar[dict] = ...
    hexahedron: ClassVar[CellType] = ...
    interval: ClassVar[CellType] = ...
    point: ClassVar[CellType] = ...
    prism: ClassVar[CellType] = ...
    pyramid: ClassVar[CellType] = ...
    quadrilateral: ClassVar[CellType] = ...
    tetrahedron: ClassVar[CellType] = ...
    triangle: ClassVar[CellType] = ...
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    @property
    def name(self) -> str: ...

class DPCVariant:
    __entries__: ClassVar[dict] = ...
    diagonal_equispaced: ClassVar[DPCVariant] = ...
    diagonal_gll: ClassVar[DPCVariant] = ...
    horizontal_equispaced: ClassVar[DPCVariant] = ...
    horizontal_gll: ClassVar[DPCVariant] = ...
    legendre: ClassVar[DPCVariant] = ...
    simplex_equispaced: ClassVar[DPCVariant] = ...
    simplex_gll: ClassVar[DPCVariant] = ...
    unset: ClassVar[DPCVariant] = ...
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    @property
    def name(self) -> str: ...

class ElementFamily:
    __entries__: ClassVar[dict] = ...
    BDM: ClassVar[ElementFamily] = ...
    CR: ClassVar[ElementFamily] = ...
    DPC: ClassVar[ElementFamily] = ...
    HHJ: ClassVar[ElementFamily] = ...
    Hermite: ClassVar[ElementFamily] = ...
    N1E: ClassVar[ElementFamily] = ...
    N2E: ClassVar[ElementFamily] = ...
    P: ClassVar[ElementFamily] = ...
    RT: ClassVar[ElementFamily] = ...
    Regge: ClassVar[ElementFamily] = ...
    bubble: ClassVar[ElementFamily] = ...
    custom: ClassVar[ElementFamily] = ...
    iso: ClassVar[ElementFamily] = ...
    serendipity: ClassVar[ElementFamily] = ...
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    @property
    def name(self) -> str: ...

class FiniteElement_float32:
    def __init__(self, *args, **kwargs) -> None: ...
    def base_transformations(self, *args, **kwargs) -> Any: ...
    def entity_transformations(self) -> dict: ...
    def get_tensor_product_representation(self) -> list[list[FiniteElement_float32]]: ...
    def Tt_apply(self, *args, **kwargs) -> Any: ...
    def T_apply(self, *args, **kwargs) -> Any: ...
    def Tt_inv_apply(self, *args, **kwargs) -> Any: ...
    def Tt_apply_right(self, *args, **kwargs) -> Any: ...
    def pull_back(self, *args, **kwargs) -> Any: ...
    def push_forward(self, *args, **kwargs) -> Any: ...
    def tabulate(self, *args, **kwargs) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def hash(self) -> int: ...
    @property
    def M(self) -> Any: ...
    @property
    def cell_type(self) -> CellType: ...
    @property
    def coefficient_matrix(self) -> Any: ...
    @property
    def degree(self) -> int: ...
    @property
    def dim(self) -> int: ...
    @property
    def discontinuous(self) -> bool: ...
    @property
    def dof_ordering(self) -> list[int]: ...
    @property
    def dof_transformations_are_identity(self) -> bool: ...
    @property
    def dof_transformations_are_permutations(self) -> bool: ...
    @property
    def dpc_variant(self) -> DPCVariant: ...
    @property
    def dtype(self) -> str: ...
    @property
    def dual_matrix(self) -> Any: ...
    @property
    def embedded_subdegree(self) -> int: ...
    @property
    def embedded_superdegree(self) -> int: ...
    @property
    def entity_closure_dofs(self) -> list[list[list[int]]]: ...
    @property
    def entity_dofs(self) -> list[list[list[int]]]: ...
    @property
    def family(self) -> ElementFamily: ...
    @property
    def has_tensor_product_factorisation(self) -> bool: ...
    @property
    def interpolation_is_identity(self) -> bool: ...
    @property
    def interpolation_matrix(self) -> Any: ...
    @property
    def interpolation_nderivs(self) -> int: ...
    @property
    def lagrange_variant(self) -> LagrangeVariant: ...
    @property
    def map_type(self) -> MapType: ...
    @property
    def num_entity_closure_dofs(self) -> list[list[int]]: ...
    @property
    def num_entity_dofs(self) -> list[list[int]]: ...
    @property
    def points(self) -> Any: ...
    @property
    def polyset_type(self) -> PolysetType: ...
    @property
    def sobolev_space(self) -> SobolevSpace: ...
    @property
    def value_shape(self) -> list[int]: ...
    @property
    def value_size(self) -> int: ...
    @property
    def wcoeffs(self) -> Any: ...
    @property
    def x(self) -> Any: ...

class FiniteElement_float64:
    def __init__(self, *args, **kwargs) -> None: ...
    def base_transformations(self, *args, **kwargs) -> Any: ...
    def entity_transformations(self) -> dict: ...
    def get_tensor_product_representation(self) -> list[list[FiniteElement_float64]]: ...
    def Tt_apply(self, *args, **kwargs) -> Any: ...
    def T_apply(self, *args, **kwargs) -> Any: ...
    def Tt_inv_apply(self, *args, **kwargs) -> Any: ...
    def Tt_apply_right(self, *args, **kwargs) -> Any: ...
    def pull_back(self, *args, **kwargs) -> Any: ...
    def push_forward(self, *args, **kwargs) -> Any: ...
    def tabulate(self, *args, **kwargs) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def hash(self) -> int: ...
    @property
    def M(self) -> Any: ...
    @property
    def cell_type(self) -> CellType: ...
    @property
    def coefficient_matrix(self) -> Any: ...
    @property
    def degree(self) -> int: ...
    @property
    def dim(self) -> int: ...
    @property
    def discontinuous(self) -> bool: ...
    @property
    def dof_ordering(self) -> list[int]: ...
    @property
    def dof_transformations_are_identity(self) -> bool: ...
    @property
    def dof_transformations_are_permutations(self) -> bool: ...
    @property
    def dpc_variant(self) -> DPCVariant: ...
    @property
    def dtype(self) -> str: ...
    @property
    def dual_matrix(self) -> Any: ...
    @property
    def embedded_subdegree(self) -> int: ...
    @property
    def embedded_superdegree(self) -> int: ...
    @property
    def entity_closure_dofs(self) -> list[list[list[int]]]: ...
    @property
    def entity_dofs(self) -> list[list[list[int]]]: ...
    @property
    def family(self) -> ElementFamily: ...
    @property
    def has_tensor_product_factorisation(self) -> bool: ...
    @property
    def interpolation_is_identity(self) -> bool: ...
    @property
    def interpolation_matrix(self) -> Any: ...
    @property
    def interpolation_nderivs(self) -> int: ...
    @property
    def lagrange_variant(self) -> LagrangeVariant: ...
    @property
    def map_type(self) -> MapType: ...
    @property
    def num_entity_closure_dofs(self) -> list[list[int]]: ...
    @property
    def num_entity_dofs(self) -> list[list[int]]: ...
    @property
    def points(self) -> Any: ...
    @property
    def polyset_type(self) -> PolysetType: ...
    @property
    def sobolev_space(self) -> SobolevSpace: ...
    @property
    def value_shape(self) -> list[int]: ...
    @property
    def value_size(self) -> int: ...
    @property
    def wcoeffs(self) -> Any: ...
    @property
    def x(self) -> Any: ...

class LagrangeVariant:
    __entries__: ClassVar[dict] = ...
    bernstein: ClassVar[LagrangeVariant] = ...
    chebyshev_centroid: ClassVar[LagrangeVariant] = ...
    chebyshev_isaac: ClassVar[LagrangeVariant] = ...
    chebyshev_warped: ClassVar[LagrangeVariant] = ...
    equispaced: ClassVar[LagrangeVariant] = ...
    gl_centroid: ClassVar[LagrangeVariant] = ...
    gl_isaac: ClassVar[LagrangeVariant] = ...
    gl_warped: ClassVar[LagrangeVariant] = ...
    gll_centroid: ClassVar[LagrangeVariant] = ...
    gll_isaac: ClassVar[LagrangeVariant] = ...
    gll_warped: ClassVar[LagrangeVariant] = ...
    legendre: ClassVar[LagrangeVariant] = ...
    unset: ClassVar[LagrangeVariant] = ...
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    @property
    def name(self) -> str: ...

class LatticeSimplexMethod:
    __entries__: ClassVar[dict] = ...
    centroid: ClassVar[LatticeSimplexMethod] = ...
    isaac: ClassVar[LatticeSimplexMethod] = ...
    none: ClassVar[LatticeSimplexMethod] = ...
    warp: ClassVar[LatticeSimplexMethod] = ...
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    @property
    def name(self) -> str: ...

class LatticeType:
    __entries__: ClassVar[dict] = ...
    chebyshev: ClassVar[LatticeType] = ...
    equispaced: ClassVar[LatticeType] = ...
    gl: ClassVar[LatticeType] = ...
    gll: ClassVar[LatticeType] = ...
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    @property
    def name(self) -> str: ...

class MapType:
    __entries__: ClassVar[dict] = ...
    L2Piola: ClassVar[MapType] = ...
    contravariantPiola: ClassVar[MapType] = ...
    covariantPiola: ClassVar[MapType] = ...
    doubleContravariantPiola: ClassVar[MapType] = ...
    doubleCovariantPiola: ClassVar[MapType] = ...
    identity: ClassVar[MapType] = ...
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    @property
    def name(self) -> str: ...

class PolynomialType:
    __entries__: ClassVar[dict] = ...
    bernstein: ClassVar[PolynomialType] = ...
    legendre: ClassVar[PolynomialType] = ...
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    @property
    def name(self) -> str: ...

class PolysetType:
    __entries__: ClassVar[dict] = ...
    macroedge: ClassVar[PolysetType] = ...
    standard: ClassVar[PolysetType] = ...
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    @property
    def name(self) -> str: ...

class QuadratureType:
    __entries__: ClassVar[dict] = ...
    Default: ClassVar[QuadratureType] = ...
    gauss_jacobi: ClassVar[QuadratureType] = ...
    gll: ClassVar[QuadratureType] = ...
    xiao_gimbutas: ClassVar[QuadratureType] = ...
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    @property
    def name(self) -> str: ...

class SobolevSpace:
    __entries__: ClassVar[dict] = ...
    H1: ClassVar[SobolevSpace] = ...
    H2: ClassVar[SobolevSpace] = ...
    H3: ClassVar[SobolevSpace] = ...
    HCurl: ClassVar[SobolevSpace] = ...
    HDiv: ClassVar[SobolevSpace] = ...
    HDivDiv: ClassVar[SobolevSpace] = ...
    HEin: ClassVar[SobolevSpace] = ...
    HInf: ClassVar[SobolevSpace] = ...
    L2: ClassVar[SobolevSpace] = ...
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    @property
    def name(self) -> str: ...
