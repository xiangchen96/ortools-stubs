# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from ortools.util.optional_boolean_pb2 import (
    OptionalBooleanValue as ortools___util___optional_boolean_pb2___OptionalBooleanValue,
)

from typing import (
    Iterable as typing___Iterable,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    NewType as typing___NewType,
    Optional as typing___Optional,
    Text as typing___Text,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

MPSolverResponseStatusValue = typing___NewType('MPSolverResponseStatusValue', builtin___int)
type___MPSolverResponseStatusValue = MPSolverResponseStatusValue
MPSolverResponseStatus: _MPSolverResponseStatus
class _MPSolverResponseStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MPSolverResponseStatusValue]):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    MPSOLVER_OPTIMAL = typing___cast(MPSolverResponseStatusValue, 0)
    MPSOLVER_FEASIBLE = typing___cast(MPSolverResponseStatusValue, 1)
    MPSOLVER_INFEASIBLE = typing___cast(MPSolverResponseStatusValue, 2)
    MPSOLVER_UNBOUNDED = typing___cast(MPSolverResponseStatusValue, 3)
    MPSOLVER_ABNORMAL = typing___cast(MPSolverResponseStatusValue, 4)
    MPSOLVER_NOT_SOLVED = typing___cast(MPSolverResponseStatusValue, 6)
    MPSOLVER_MODEL_IS_VALID = typing___cast(MPSolverResponseStatusValue, 97)
    MPSOLVER_UNKNOWN_STATUS = typing___cast(MPSolverResponseStatusValue, 99)
    MPSOLVER_MODEL_INVALID = typing___cast(MPSolverResponseStatusValue, 5)
    MPSOLVER_MODEL_INVALID_SOLUTION_HINT = typing___cast(MPSolverResponseStatusValue, 84)
    MPSOLVER_MODEL_INVALID_SOLVER_PARAMETERS = typing___cast(MPSolverResponseStatusValue, 85)
    MPSOLVER_SOLVER_TYPE_UNAVAILABLE = typing___cast(MPSolverResponseStatusValue, 7)
MPSOLVER_OPTIMAL = typing___cast(MPSolverResponseStatusValue, 0)
MPSOLVER_FEASIBLE = typing___cast(MPSolverResponseStatusValue, 1)
MPSOLVER_INFEASIBLE = typing___cast(MPSolverResponseStatusValue, 2)
MPSOLVER_UNBOUNDED = typing___cast(MPSolverResponseStatusValue, 3)
MPSOLVER_ABNORMAL = typing___cast(MPSolverResponseStatusValue, 4)
MPSOLVER_NOT_SOLVED = typing___cast(MPSolverResponseStatusValue, 6)
MPSOLVER_MODEL_IS_VALID = typing___cast(MPSolverResponseStatusValue, 97)
MPSOLVER_UNKNOWN_STATUS = typing___cast(MPSolverResponseStatusValue, 99)
MPSOLVER_MODEL_INVALID = typing___cast(MPSolverResponseStatusValue, 5)
MPSOLVER_MODEL_INVALID_SOLUTION_HINT = typing___cast(MPSolverResponseStatusValue, 84)
MPSOLVER_MODEL_INVALID_SOLVER_PARAMETERS = typing___cast(MPSolverResponseStatusValue, 85)
MPSOLVER_SOLVER_TYPE_UNAVAILABLE = typing___cast(MPSolverResponseStatusValue, 7)
type___MPSolverResponseStatus = MPSolverResponseStatus

class MPVariableProto(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    lower_bound: builtin___float = ...
    upper_bound: builtin___float = ...
    objective_coefficient: builtin___float = ...
    is_integer: builtin___bool = ...
    name: typing___Text = ...
    branching_priority: builtin___int = ...

    def __init__(self,
        *,
        lower_bound : typing___Optional[builtin___float] = None,
        upper_bound : typing___Optional[builtin___float] = None,
        objective_coefficient : typing___Optional[builtin___float] = None,
        is_integer : typing___Optional[builtin___bool] = None,
        name : typing___Optional[typing___Text] = None,
        branching_priority : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"branching_priority",b"branching_priority",u"is_integer",b"is_integer",u"lower_bound",b"lower_bound",u"name",b"name",u"objective_coefficient",b"objective_coefficient",u"upper_bound",b"upper_bound"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"branching_priority",b"branching_priority",u"is_integer",b"is_integer",u"lower_bound",b"lower_bound",u"name",b"name",u"objective_coefficient",b"objective_coefficient",u"upper_bound",b"upper_bound"]) -> None: ...
type___MPVariableProto = MPVariableProto

class MPConstraintProto(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    var_index: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    coefficient: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    lower_bound: builtin___float = ...
    upper_bound: builtin___float = ...
    name: typing___Text = ...
    is_lazy: builtin___bool = ...

    def __init__(self,
        *,
        var_index : typing___Optional[typing___Iterable[builtin___int]] = None,
        coefficient : typing___Optional[typing___Iterable[builtin___float]] = None,
        lower_bound : typing___Optional[builtin___float] = None,
        upper_bound : typing___Optional[builtin___float] = None,
        name : typing___Optional[typing___Text] = None,
        is_lazy : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"is_lazy",b"is_lazy",u"lower_bound",b"lower_bound",u"name",b"name",u"upper_bound",b"upper_bound"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"coefficient",b"coefficient",u"is_lazy",b"is_lazy",u"lower_bound",b"lower_bound",u"name",b"name",u"upper_bound",b"upper_bound",u"var_index",b"var_index"]) -> None: ...
type___MPConstraintProto = MPConstraintProto

class MPGeneralConstraintProto(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...

    @property
    def indicator_constraint(self) -> type___MPIndicatorConstraint: ...

    @property
    def sos_constraint(self) -> type___MPSosConstraint: ...

    @property
    def quadratic_constraint(self) -> type___MPQuadraticConstraint: ...

    @property
    def abs_constraint(self) -> type___MPAbsConstraint: ...

    @property
    def and_constraint(self) -> type___MPArrayConstraint: ...

    @property
    def or_constraint(self) -> type___MPArrayConstraint: ...

    @property
    def min_constraint(self) -> type___MPArrayWithConstantConstraint: ...

    @property
    def max_constraint(self) -> type___MPArrayWithConstantConstraint: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        indicator_constraint : typing___Optional[type___MPIndicatorConstraint] = None,
        sos_constraint : typing___Optional[type___MPSosConstraint] = None,
        quadratic_constraint : typing___Optional[type___MPQuadraticConstraint] = None,
        abs_constraint : typing___Optional[type___MPAbsConstraint] = None,
        and_constraint : typing___Optional[type___MPArrayConstraint] = None,
        or_constraint : typing___Optional[type___MPArrayConstraint] = None,
        min_constraint : typing___Optional[type___MPArrayWithConstantConstraint] = None,
        max_constraint : typing___Optional[type___MPArrayWithConstantConstraint] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"abs_constraint",b"abs_constraint",u"and_constraint",b"and_constraint",u"general_constraint",b"general_constraint",u"indicator_constraint",b"indicator_constraint",u"max_constraint",b"max_constraint",u"min_constraint",b"min_constraint",u"name",b"name",u"or_constraint",b"or_constraint",u"quadratic_constraint",b"quadratic_constraint",u"sos_constraint",b"sos_constraint"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"abs_constraint",b"abs_constraint",u"and_constraint",b"and_constraint",u"general_constraint",b"general_constraint",u"indicator_constraint",b"indicator_constraint",u"max_constraint",b"max_constraint",u"min_constraint",b"min_constraint",u"name",b"name",u"or_constraint",b"or_constraint",u"quadratic_constraint",b"quadratic_constraint",u"sos_constraint",b"sos_constraint"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"general_constraint",b"general_constraint"]) -> typing_extensions___Literal["indicator_constraint","sos_constraint","quadratic_constraint","abs_constraint","and_constraint","or_constraint","min_constraint","max_constraint"]: ...
type___MPGeneralConstraintProto = MPGeneralConstraintProto

class MPIndicatorConstraint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    var_index: builtin___int = ...
    var_value: builtin___int = ...

    @property
    def constraint(self) -> type___MPConstraintProto: ...

    def __init__(self,
        *,
        var_index : typing___Optional[builtin___int] = None,
        var_value : typing___Optional[builtin___int] = None,
        constraint : typing___Optional[type___MPConstraintProto] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"constraint",b"constraint",u"var_index",b"var_index",u"var_value",b"var_value"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"constraint",b"constraint",u"var_index",b"var_index",u"var_value",b"var_value"]) -> None: ...
type___MPIndicatorConstraint = MPIndicatorConstraint

class MPSosConstraint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    TypeValue = typing___NewType('TypeValue', builtin___int)
    type___TypeValue = TypeValue
    Type: _Type
    class _Type(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MPSosConstraint.TypeValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        SOS1_DEFAULT = typing___cast(MPSosConstraint.TypeValue, 0)
        SOS2 = typing___cast(MPSosConstraint.TypeValue, 1)
    SOS1_DEFAULT = typing___cast(MPSosConstraint.TypeValue, 0)
    SOS2 = typing___cast(MPSosConstraint.TypeValue, 1)
    type___Type = Type

    type: type___MPSosConstraint.TypeValue = ...
    var_index: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    weight: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...

    def __init__(self,
        *,
        type : typing___Optional[type___MPSosConstraint.TypeValue] = None,
        var_index : typing___Optional[typing___Iterable[builtin___int]] = None,
        weight : typing___Optional[typing___Iterable[builtin___float]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"type",b"type"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"type",b"type",u"var_index",b"var_index",u"weight",b"weight"]) -> None: ...
type___MPSosConstraint = MPSosConstraint

class MPQuadraticConstraint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    var_index: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    coefficient: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    qvar1_index: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    qvar2_index: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    qcoefficient: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    lower_bound: builtin___float = ...
    upper_bound: builtin___float = ...

    def __init__(self,
        *,
        var_index : typing___Optional[typing___Iterable[builtin___int]] = None,
        coefficient : typing___Optional[typing___Iterable[builtin___float]] = None,
        qvar1_index : typing___Optional[typing___Iterable[builtin___int]] = None,
        qvar2_index : typing___Optional[typing___Iterable[builtin___int]] = None,
        qcoefficient : typing___Optional[typing___Iterable[builtin___float]] = None,
        lower_bound : typing___Optional[builtin___float] = None,
        upper_bound : typing___Optional[builtin___float] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"lower_bound",b"lower_bound",u"upper_bound",b"upper_bound"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"coefficient",b"coefficient",u"lower_bound",b"lower_bound",u"qcoefficient",b"qcoefficient",u"qvar1_index",b"qvar1_index",u"qvar2_index",b"qvar2_index",u"upper_bound",b"upper_bound",u"var_index",b"var_index"]) -> None: ...
type___MPQuadraticConstraint = MPQuadraticConstraint

class MPAbsConstraint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    var_index: builtin___int = ...
    resultant_var_index: builtin___int = ...

    def __init__(self,
        *,
        var_index : typing___Optional[builtin___int] = None,
        resultant_var_index : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"resultant_var_index",b"resultant_var_index",u"var_index",b"var_index"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"resultant_var_index",b"resultant_var_index",u"var_index",b"var_index"]) -> None: ...
type___MPAbsConstraint = MPAbsConstraint

class MPArrayConstraint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    var_index: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    resultant_var_index: builtin___int = ...

    def __init__(self,
        *,
        var_index : typing___Optional[typing___Iterable[builtin___int]] = None,
        resultant_var_index : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"resultant_var_index",b"resultant_var_index"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"resultant_var_index",b"resultant_var_index",u"var_index",b"var_index"]) -> None: ...
type___MPArrayConstraint = MPArrayConstraint

class MPArrayWithConstantConstraint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    var_index: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    constant: builtin___float = ...
    resultant_var_index: builtin___int = ...

    def __init__(self,
        *,
        var_index : typing___Optional[typing___Iterable[builtin___int]] = None,
        constant : typing___Optional[builtin___float] = None,
        resultant_var_index : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"constant",b"constant",u"resultant_var_index",b"resultant_var_index"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"constant",b"constant",u"resultant_var_index",b"resultant_var_index",u"var_index",b"var_index"]) -> None: ...
type___MPArrayWithConstantConstraint = MPArrayWithConstantConstraint

class MPQuadraticObjective(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    qvar1_index: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    qvar2_index: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    coefficient: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...

    def __init__(self,
        *,
        qvar1_index : typing___Optional[typing___Iterable[builtin___int]] = None,
        qvar2_index : typing___Optional[typing___Iterable[builtin___int]] = None,
        coefficient : typing___Optional[typing___Iterable[builtin___float]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"coefficient",b"coefficient",u"qvar1_index",b"qvar1_index",u"qvar2_index",b"qvar2_index"]) -> None: ...
type___MPQuadraticObjective = MPQuadraticObjective

class PartialVariableAssignment(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    var_index: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    var_value: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...

    def __init__(self,
        *,
        var_index : typing___Optional[typing___Iterable[builtin___int]] = None,
        var_value : typing___Optional[typing___Iterable[builtin___float]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"var_index",b"var_index",u"var_value",b"var_value"]) -> None: ...
type___PartialVariableAssignment = PartialVariableAssignment

class MPModelProto(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    maximize: builtin___bool = ...
    objective_offset: builtin___float = ...
    name: typing___Text = ...

    @property
    def variable(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___MPVariableProto]: ...

    @property
    def constraint(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___MPConstraintProto]: ...

    @property
    def general_constraint(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___MPGeneralConstraintProto]: ...

    @property
    def quadratic_objective(self) -> type___MPQuadraticObjective: ...

    @property
    def solution_hint(self) -> type___PartialVariableAssignment: ...

    def __init__(self,
        *,
        variable : typing___Optional[typing___Iterable[type___MPVariableProto]] = None,
        constraint : typing___Optional[typing___Iterable[type___MPConstraintProto]] = None,
        general_constraint : typing___Optional[typing___Iterable[type___MPGeneralConstraintProto]] = None,
        maximize : typing___Optional[builtin___bool] = None,
        objective_offset : typing___Optional[builtin___float] = None,
        quadratic_objective : typing___Optional[type___MPQuadraticObjective] = None,
        name : typing___Optional[typing___Text] = None,
        solution_hint : typing___Optional[type___PartialVariableAssignment] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"maximize",b"maximize",u"name",b"name",u"objective_offset",b"objective_offset",u"quadratic_objective",b"quadratic_objective",u"solution_hint",b"solution_hint"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"constraint",b"constraint",u"general_constraint",b"general_constraint",u"maximize",b"maximize",u"name",b"name",u"objective_offset",b"objective_offset",u"quadratic_objective",b"quadratic_objective",u"solution_hint",b"solution_hint",u"variable",b"variable"]) -> None: ...
type___MPModelProto = MPModelProto

class OptionalDouble(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    value: builtin___float = ...

    def __init__(self,
        *,
        value : typing___Optional[builtin___float] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> None: ...
type___OptionalDouble = OptionalDouble

class MPSolverCommonParameters(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    LPAlgorithmValuesValue = typing___NewType('LPAlgorithmValuesValue', builtin___int)
    type___LPAlgorithmValuesValue = LPAlgorithmValuesValue
    LPAlgorithmValues: _LPAlgorithmValues
    class _LPAlgorithmValues(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MPSolverCommonParameters.LPAlgorithmValuesValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        LP_ALGO_UNSPECIFIED = typing___cast(MPSolverCommonParameters.LPAlgorithmValuesValue, 0)
        LP_ALGO_DUAL = typing___cast(MPSolverCommonParameters.LPAlgorithmValuesValue, 1)
        LP_ALGO_PRIMAL = typing___cast(MPSolverCommonParameters.LPAlgorithmValuesValue, 2)
        LP_ALGO_BARRIER = typing___cast(MPSolverCommonParameters.LPAlgorithmValuesValue, 3)
    LP_ALGO_UNSPECIFIED = typing___cast(MPSolverCommonParameters.LPAlgorithmValuesValue, 0)
    LP_ALGO_DUAL = typing___cast(MPSolverCommonParameters.LPAlgorithmValuesValue, 1)
    LP_ALGO_PRIMAL = typing___cast(MPSolverCommonParameters.LPAlgorithmValuesValue, 2)
    LP_ALGO_BARRIER = typing___cast(MPSolverCommonParameters.LPAlgorithmValuesValue, 3)
    type___LPAlgorithmValues = LPAlgorithmValues

    lp_algorithm: type___MPSolverCommonParameters.LPAlgorithmValuesValue = ...
    presolve: ortools___util___optional_boolean_pb2___OptionalBooleanValue = ...
    scaling: ortools___util___optional_boolean_pb2___OptionalBooleanValue = ...

    @property
    def relative_mip_gap(self) -> type___OptionalDouble: ...

    @property
    def primal_tolerance(self) -> type___OptionalDouble: ...

    @property
    def dual_tolerance(self) -> type___OptionalDouble: ...

    def __init__(self,
        *,
        relative_mip_gap : typing___Optional[type___OptionalDouble] = None,
        primal_tolerance : typing___Optional[type___OptionalDouble] = None,
        dual_tolerance : typing___Optional[type___OptionalDouble] = None,
        lp_algorithm : typing___Optional[type___MPSolverCommonParameters.LPAlgorithmValuesValue] = None,
        presolve : typing___Optional[ortools___util___optional_boolean_pb2___OptionalBooleanValue] = None,
        scaling : typing___Optional[ortools___util___optional_boolean_pb2___OptionalBooleanValue] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"dual_tolerance",b"dual_tolerance",u"lp_algorithm",b"lp_algorithm",u"presolve",b"presolve",u"primal_tolerance",b"primal_tolerance",u"relative_mip_gap",b"relative_mip_gap",u"scaling",b"scaling"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dual_tolerance",b"dual_tolerance",u"lp_algorithm",b"lp_algorithm",u"presolve",b"presolve",u"primal_tolerance",b"primal_tolerance",u"relative_mip_gap",b"relative_mip_gap",u"scaling",b"scaling"]) -> None: ...
type___MPSolverCommonParameters = MPSolverCommonParameters

class MPModelDeltaProto(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class VariableOverridesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: builtin___int = ...

        @property
        def value(self) -> type___MPVariableProto: ...

        def __init__(self,
            *,
            key : typing___Optional[builtin___int] = None,
            value : typing___Optional[type___MPVariableProto] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___VariableOverridesEntry = VariableOverridesEntry

    class ConstraintOverridesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: builtin___int = ...

        @property
        def value(self) -> type___MPConstraintProto: ...

        def __init__(self,
            *,
            key : typing___Optional[builtin___int] = None,
            value : typing___Optional[type___MPConstraintProto] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___ConstraintOverridesEntry = ConstraintOverridesEntry

    baseline_model_file_path: typing___Text = ...

    @property
    def variable_overrides(self) -> typing___MutableMapping[builtin___int, type___MPVariableProto]: ...

    @property
    def constraint_overrides(self) -> typing___MutableMapping[builtin___int, type___MPConstraintProto]: ...

    def __init__(self,
        *,
        baseline_model_file_path : typing___Optional[typing___Text] = None,
        variable_overrides : typing___Optional[typing___Mapping[builtin___int, type___MPVariableProto]] = None,
        constraint_overrides : typing___Optional[typing___Mapping[builtin___int, type___MPConstraintProto]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"baseline_model_file_path",b"baseline_model_file_path"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"baseline_model_file_path",b"baseline_model_file_path",u"constraint_overrides",b"constraint_overrides",u"variable_overrides",b"variable_overrides"]) -> None: ...
type___MPModelDeltaProto = MPModelDeltaProto

class MPModelRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    SolverTypeValue = typing___NewType('SolverTypeValue', builtin___int)
    type___SolverTypeValue = SolverTypeValue
    SolverType: _SolverType
    class _SolverType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MPModelRequest.SolverTypeValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        GLOP_LINEAR_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 2)
        CLP_LINEAR_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 0)
        GLPK_LINEAR_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 1)
        GUROBI_LINEAR_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 6)
        XPRESS_LINEAR_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 101)
        CPLEX_LINEAR_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 10)
        SCIP_MIXED_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 3)
        GLPK_MIXED_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 4)
        CBC_MIXED_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 5)
        GUROBI_MIXED_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 7)
        XPRESS_MIXED_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 102)
        CPLEX_MIXED_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 11)
        BOP_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 12)
        SAT_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 14)
        KNAPSACK_MIXED_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 13)
    GLOP_LINEAR_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 2)
    CLP_LINEAR_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 0)
    GLPK_LINEAR_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 1)
    GUROBI_LINEAR_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 6)
    XPRESS_LINEAR_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 101)
    CPLEX_LINEAR_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 10)
    SCIP_MIXED_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 3)
    GLPK_MIXED_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 4)
    CBC_MIXED_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 5)
    GUROBI_MIXED_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 7)
    XPRESS_MIXED_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 102)
    CPLEX_MIXED_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 11)
    BOP_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 12)
    SAT_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 14)
    KNAPSACK_MIXED_INTEGER_PROGRAMMING = typing___cast(MPModelRequest.SolverTypeValue, 13)
    type___SolverType = SolverType

    solver_type: type___MPModelRequest.SolverTypeValue = ...
    solver_time_limit_seconds: builtin___float = ...
    enable_internal_solver_output: builtin___bool = ...
    solver_specific_parameters: typing___Text = ...

    @property
    def model(self) -> type___MPModelProto: ...

    @property
    def model_delta(self) -> type___MPModelDeltaProto: ...

    def __init__(self,
        *,
        model : typing___Optional[type___MPModelProto] = None,
        solver_type : typing___Optional[type___MPModelRequest.SolverTypeValue] = None,
        solver_time_limit_seconds : typing___Optional[builtin___float] = None,
        enable_internal_solver_output : typing___Optional[builtin___bool] = None,
        solver_specific_parameters : typing___Optional[typing___Text] = None,
        model_delta : typing___Optional[type___MPModelDeltaProto] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"enable_internal_solver_output",b"enable_internal_solver_output",u"model",b"model",u"model_delta",b"model_delta",u"solver_specific_parameters",b"solver_specific_parameters",u"solver_time_limit_seconds",b"solver_time_limit_seconds",u"solver_type",b"solver_type"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"enable_internal_solver_output",b"enable_internal_solver_output",u"model",b"model",u"model_delta",b"model_delta",u"solver_specific_parameters",b"solver_specific_parameters",u"solver_time_limit_seconds",b"solver_time_limit_seconds",u"solver_type",b"solver_type"]) -> None: ...
type___MPModelRequest = MPModelRequest

class MPSolutionResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    status: type___MPSolverResponseStatusValue = ...
    status_str: typing___Text = ...
    objective_value: builtin___float = ...
    best_objective_bound: builtin___float = ...
    variable_value: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    dual_value: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    reduced_cost: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...

    def __init__(self,
        *,
        status : typing___Optional[type___MPSolverResponseStatusValue] = None,
        status_str : typing___Optional[typing___Text] = None,
        objective_value : typing___Optional[builtin___float] = None,
        best_objective_bound : typing___Optional[builtin___float] = None,
        variable_value : typing___Optional[typing___Iterable[builtin___float]] = None,
        dual_value : typing___Optional[typing___Iterable[builtin___float]] = None,
        reduced_cost : typing___Optional[typing___Iterable[builtin___float]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"best_objective_bound",b"best_objective_bound",u"objective_value",b"objective_value",u"status",b"status",u"status_str",b"status_str"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"best_objective_bound",b"best_objective_bound",u"dual_value",b"dual_value",u"objective_value",b"objective_value",u"reduced_cost",b"reduced_cost",u"status",b"status",u"status_str",b"status_str",u"variable_value",b"variable_value"]) -> None: ...
type___MPSolutionResponse = MPSolutionResponse
