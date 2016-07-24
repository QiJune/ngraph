# ----------------------------------------------------------------------------
# Copyright 2016 Nervana Systems Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------
from __future__ import division
from builtins import object, str
import abc

import weakref
import numbers

import numpy as np

import geon.backends.graph.nodes as nodes
from geon.backends.graph.environment import get_current_environment, get_current_ops, captured_ops
from geon.backends.graph.arrayaxes import get_batch_axes, TensorDescription, \
    AxisIDTuple, Axes, AxesAxis


class AbstractVisitor(nodes.AbstractVisitor):

    @abc.abstractmethod
    def visit_op(self, op):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_tensor(self, tensor):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_allocation(self, allocation):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_computation(self, computation):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_container(self, container):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_RNG(self, rng):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_rngop(self, rngop, rng):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_normal(self, normal, loc, scale, rng):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_uniform(self, uniform, low, high, rng):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_void(self, void):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_set_item(self, set_item, tensor, item, val):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_doall(self, doall, *args):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_elementwise(self, elementwise):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_all_reduce(self, all_reduce, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_placheolder(self, placeholder):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_fill(self, fill, const):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_constant(self, constant, const):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_numpy_tensor(self, numpy_tensor, nptensor):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_broadcast(self, broadcast, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_absolute(self, absolute, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_add(self, add, x, y):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_argmax(self, argmax, max_axes, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_argmin(self, argmin, min_axes, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_cos(self, cos, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_divide(self, divide, x, y):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_dot(self, dot, reduction_axes, out_axes, x, y):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_elementwise_boolean(self, elementwise_boolean):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_equal(self, equal, x, y):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_not_equal(self, not_equal, x, y):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_greater(self, greater, x, y):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_less(self, less, x, y):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_greater_equal(self, greater_equal, x, y):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_less_equal(self, less_equal, x, y):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_onehot(self, onehot, x, axis):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_softmax(self, softmax, x, sx):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_sum(self, sum, reduction_axes, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_variable(self, variable):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_temporary(self, temporary):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_exp(self, exp, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_log(self, log, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_safelog(self, safelog, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_max(self, max, x, y):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_maximum(self, maximum, x, y):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_min(self, min, x, y):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_minimum(self, minimum, x, y):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_multiply(self, multiply, x, y):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_negative(self, negative, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_power(self, power, x, y):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_reciprocal(self, reciprocal, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_reduction(self, reduction, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_sgn(self, sgn, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_sig(self, sig, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_sin(self, sin, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_sqrt(self, sqrt, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_square(self, square, x):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_subtract(self, subtract, x, y):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_tanh(self, tanh, x):
        raise NotImplementedError()


class Visitor(nodes.Visitor):

    def visit_op(self, op):
        return self.visit_node(op)

    def visit_tensor(self, tensor):
        return self.visit_op(tensor)

    def visit_allocation(self, allocation):
        return self.visit_tensor(allocation)

    def visit_computation(self, computation):
        return self.visit_tensor(computation)

    def visit_container(self, container):
        return self.visit_computation(container)

    def visit_RNG(self, rng):
        return self.visit_allocation(rng)

    def visit_rngop(self, rngop, rng):
        return self.visit_computation(rngop)

    def visit_normal(self, normal, loc, scale, rng):
        return self.visit_rngop(normal, rng)

    def visit_uniform(self, uniform, low, high, rng):
        return self.visit_rngop(uniform, rng)

    def visit_void(self, void):
        return self.visit_computation(void)

    def visit_set_item(self, set_item, tensor, item, val):
        return self.visit_void(set_item)

    def visit_doall(self, doall, *args):
        return self.visit_void(doall)

    def visit_elementwise(self, elementwise):
        return self.visit_computation(elementwise)

    def visit_all_reduce(self, all_reduce, x):
        return self.visit_elemenwise(all_reduce)

    def visit_placeholder(self, placeholder):
        return self.visit_allocation(placeholder)

    def visit_fill(self, fill, const):
        return self.visit_void(fill)

    def visit_constant(self, constant, const):
        return self.visit_allocation(constant)

    def visit_numpy_tensor(self, numpy_tensor, nptensor):
        return self.visit_allocation(numpy_tensor)

    def visit_broadcast(self, broadcast, x):
        return self.visit_tensor(broadcast)

    def visit_absolute(self, absolute, x):
        return self.visit_elementwise(absolute)

    def visit_add(self, add, x, y):
        return self.visit_elementwise(add)

    def visit_argmax(self, argmax, max_axes, x):
        return self.visit_elementwise(argmax)

    def visit_argmin(self, argmin, min_axes, x):
        return self.visit_elementwise(argmin)

    def visit_cos(self, cos, x):
        return self.visit_elementwise(cos)

    def visit_divide(self, divide, x, y):
        return self.visit_elementwise(divide)

    def visit_dot(self, dot, reduction_axes, out_axes, x, y):
        return self.visit_elementwise(dot)

    def visit_elementwise_boolean(self, elementwise_boolean):
        return self.visit_elementwise(elementwise_boolean)

    def visit_equal(self, equal, x, y):
        return self.visit_elementwise_boolean(equal)

    def visit_not_equal(self, not_equal, x, y):
        return self.visit_elementwise_boolean(not_equal)

    def visit_greater(self, greater, x, y):
        return self.visit_elementwise_boolean(greater)

    def visit_less(self, less, x, y):
        return self.visit_elementwise_boolean(less)

    def visit_greater_equal(self, greater_equal, x, y):
        return self.visit_elementwise_boolean(greater_equal)

    def visit_less_equal(self, less_equal, x, y):
        return self.visit_elementwise_boolean(less_equal)

    def visit_onehot(self, onehot, x, index):
        return self.visit_computation(onehot)

    def visit_reduction(self, reduction, x):
        return self.visit_computation(reduction)

    def visit_softmax(self, softmax, x, sx):
        return self.visit_computation(softmax)

    def visit_sum(self, sum, reduction_axes, x):
        return self.visit_reduction(sum)

    def visit_variable(self, variable):
        return self.visit_allocation(variable)

    def visit_temporary(self, temporary):
        return self.visit_allocation(temporary)

    def visit_exp(self, exp, x):
        return self.visit_elementwise(exp)

    def visit_log(self, log, x):
        return self.visit_elementwise(log)

    def visit_safelog(self, safelog, x):
        return self.visit_log(safelog, x)

    def visit_max(self, max, x, y):
        return self.visit_reduction(max)

    def visit_maximum(self, maximum, x, y):
        return self.visit_elementwise(maximum)

    def visit_min(self, min, x, y):
        return self.visit_reduction(min)

    def visit_minimum(self, minimum, x, y):
        return self.visit_elementwise(minimum)

    def visit_multiply(self, multiply, x, y):
        return self.visit_elementwise(multiply)

    def visit_negative(self, negative, x):
        return self.visit_elementwise(negative)

    def visit_power(self, power, x, y):
        return self.visit_elementwise(power)

    def visit_reciprocal(self, reciprocal, x):
        return self.visit_elementwise(reciprocal)

    def visit_sgn(self, sgn, x):
        return self.visit_elementwise(sgn)

    def visit_sig(self, sig, x):
        return self.visit_container(sig)

    def visit_sin(self, sin, x):
        return self.visit_elementwise(sin)

    def visit_sqrt(self, sqrt, x):
        return self.visit_elementwise(sqrt)

    def visit_square(self, square, x):
        return self.visit_elementwise(square)

    def visit_subtract(self, subtract, x, y):
        return self.visit_elementwise(subtract)

    def visit_tanh(self, tanh, x):
        return self.visit_elementwise(tanh)


class SimplePrune(Visitor):

    def __init__(self, results):
        self.results = results
        self.reps = []

    def init(self):
        self.reps = []

    def add_rep(self, op, replacement):
        # Can't replace op if its being returned
        if op not in self.results:
            self.reps.append((op, replacement))

    def visit_negative(self, negative, x):
        if isinstance(x, Constant):
            self.add_rep(negative, Constant(-x.const))

    def visit_multiply(self, multiply, x, y):
        rep = None
        if isinstance(x, Constant):
            if x.const == 0:
                rep = x
            elif x.const == 1:
                rep = y
            elif x.const == -1:
                rep = negative(y)
        elif isinstance(y, Constant):
            if y.const == 0:
                rep = y
            elif y.const == 1:
                rep = x
            elif y.const == -1:
                rep = negative(x)
        if rep is not None:
            self.add_rep(multiply, rep)

    def visit_add(self, add, x, y):
        rep = None
        if isinstance(x, Constant):
            if x.const == 0:
                rep = y
        elif isinstance(y, Constant):
            if y.const == 0:
                rep = x
        if rep is not None:
            self.add_rep(add, rep)

    def visit_sum(self, sum, reduction_axes, x):
        if isinstance(x, Constant):
            val = x.const * reduction_axes.size
            self.add_rep(sum, Constant(val))

    def visit_log(self, log, x):
        if isinstance(x, Container):
            args = x.args
            if len(args) == 1:
                x = args[0]
        if isinstance(x, divide):
            num, denom = x.args
            if isinstance(num, exp):
                exp_x, = num.args
                self.add_rep(log, exp_x - type(log)(denom))
        elif isinstance(x, exp):
            exp_x, = x.args
            self.add_rep(log, exp_x)

    def do_replacements(self):
        for old, rep in self.reps:
            old_users = set(old.users)
            for user in old_users:
                user.replace_arg(old, rep)
        return len(self.reps) > 0


class Op(nodes.Node):
    """Any operation that can be in an AST"""

    def __init__(self, initializers=None, **kwds):
        super(Op, self).__init__(**kwds)
        self._adjoints = None
        self.initializers = initializers or []
        ops = get_current_ops()
        if ops is not None:
            ops.append(self)
        self.transform_hook = None

    def parameters(self):
        """Return all parameters used in computing this node"""
        params = []
        visited = set()
        unvisited = [self]

        while unvisited:
            node = unvisited.pop()
            visited.add(node)
            if isinstance(node, Variable):
                params.append(node)
            unvisited.extend(node.args)

        return set(params)

    def visit(self, visitor, **kargs):
        return visitor.visit_op(self, **kargs)

    @staticmethod
    def get_ordered_ops(op, ordered_ops):
        """
        Get dependent ops ordered for autodiff.
        """
        nodes.Node.visit_input_closure([op], lambda o: ordered_ops.append(o))

    def adjoints(self):
        if self._adjoints is not None:
            return self._adjoints

        if len(self.axes.value) == 0:
            initial_adjoint = Constant(1)
        else:
            initial_adjoint = placeholder(axes=self.axes)
        self.initial_adjoint = initial_adjoint

        self._adjoints = dict()
        ordered_ops = []
        Op.get_ordered_ops(self, ordered_ops)
        self._adjoints[self] = self.initial_adjoint
        for o in list(reversed(ordered_ops)):
            if o in self._adjoints:
                scale = o.scale
                adjoint = self._adjoints[o]
                if scale is not None:
                    adjoint = adjoint * scale
                o.generate_adjoints(self._adjoints, adjoint, *o.args)
        return self._adjoints

    @staticmethod
    def ordered_ops(results):
        ordered_ops = []
        nodes.Node.visit_input_closure(
            results, lambda o: ordered_ops.append(o))
        return ordered_ops

    @staticmethod
    def analyze_liveness(results, ordered_ops):
        liveness = [set() for _ in ordered_ops]
        i = len(liveness) - 1
        for result in results:
            liveness[i].add(result)
        while i > 0:
            op = ordered_ops[i]
            prealive = liveness[i - 1]
            alive = set(liveness[i])
            if isinstance(op, Tensor):
                alive.discard(op)
                for arg in op.args:
                    alive.add(arg)
                prealive |= alive
            i = i - 1
        return liveness

    def as_node(self, x):
        return Op.as_op(x)

    @staticmethod
    def as_op(x):
        if isinstance(x, Tensor):
            return x

        return Constant(x)

    @property
    def ops(self):
        return []

    @staticmethod
    def simple_prune(results):
        pruner = SimplePrune(results)

        has_work = True
        while has_work:
            pruner.init()
            for op in Op.ordered_ops(results):
                op.visit(pruner)
            has_work = pruner.do_replacements()

    def transform(self, transformer, *args):
        """Process op"""
        pass

    def sync(self, transformer):
        """Make sure transformer has local changes"""
        pass

    def __str__(self):
        return '<{cl}:{id}>'.format(cl=self.__class__.__name__, id=id(self))


class TensorAxesInfo(object):
    """Information about a use of a tensor with axes"""

    def __init__(
            self,
            axes,
            alloc=None,
            read_only=False,
            tags=(),
            dtype=np.float32,
            **kargs):
        super(TensorAxesInfo, self).__init__(**kargs)
        axes = Axes(*axes)
        self.axes = axes
        self.views = weakref.WeakValueDictionary()
        self.alloc = alloc
        self.buffer = None
        self.read_only = read_only
        self.dtype = np.dtype(dtype)
        self.tags = set(tags)
        self.__tensor_description = None
        self.initializer = None
        self.initialized = False
        self.views[self.axes] = self

    @property
    def tensor_description(self):
        if self.__tensor_description is None:
            self.__tensor_description = TensorDescription(
                axes=self.axes, dtype=self.dtype)
        return self.__tensor_description

    @property
    def shapes(self):
        return self.tensor_description.shape

    @property
    def value(self):
        return self.tensor_description.value

    def set_tensor(self, transformer, tensor):
        self.tensor_description.value = tensor
        self.update_views(transformer, True)

    def update_views(self, transformer, force):
        for view in list(self.views.values()):
            if view.tensor_description is self.tensor_description:
                continue
            view.update_tensor(transformer, force)

    def allocate(self, transformer):
        if self.tensor_description.value is None:
            if self.alloc is not None:
                tensor = self.alloc(transformer, self.tensor_description)
            else:
                tensor = transformer.empty(self.tensor_description)
            self.set_tensor(transformer, tensor)
        else:
            self.update_views(transformer, False)

    def get_or_default(self, axes, default_function):
        if axes in self.views:
            return self.views[axes]
        result = default_function()
        self.views[axes] = result
        return result

    def reaxe(self, reaxe):
        return self.get_or_default(Axes(*reaxe),
                                   lambda: TensorReaxeViewInfo(
                                       tensor_axes_info=self,
                                       reaxes=reaxe,
                                       idx=len(self.views)))

    def dot_reaxe_left(self, red_axis_ids):
        return self.get_or_default(red_axis_ids,
                                   lambda: DotLeftViewInfo(
                                       tensor_axes_info=self,
                                       red_axis_ids=red_axis_ids,
                                       idx=len(self.views)))

    def dot_reaxe_right(self, red_axis_ids):
        return self.get_or_default(red_axis_ids,
                                   lambda: DotRightViewInfo(
                                       tensor_axes_info=self,
                                       red_axis_ids=red_axis_ids,
                                       idx=len(self.views)))


class TensorViewInfo(object):
    """The use of a view of a tensor with axes"""

    def __init__(self, tensor_axes_info, idx, **kargs):
        super(TensorViewInfo, self).__init__(**kargs)
        self.tensor_axes_info = tensor_axes_info
        self.idx = idx

    def allocate(self, transformer):
        if self.tensor_description.value is None:
            tensor = transformer.empty(self.tensor_description)
            self.tensor_description.value = tensor

    @property
    def value(self):
        return self.tensor_description.value

    def update_tensor(self, transformer, force):
        tensor_description = self.tensor_description
        if force or tensor_description.value is None:
            tensor_description.value = transformer.tensor_view(
                tensor_description)


class TensorReaxeViewInfo(TensorViewInfo):
    """The use of a reaxe view of a tensor with axes"""

    def __init__(self, reaxes, **kargs):
        super(TensorReaxeViewInfo, self).__init__(**kargs)
        self.reaxes = Axes(*reaxes)
        self.__tensor_description = None

    @property
    def tensor_description(self):
        if self.__tensor_description is None:
            self.__tensor_description = self.tensor_axes_info.tensor_description.reaxe(
                self.reaxes)
        return self.__tensor_description


class DotLeftViewInfo(TensorViewInfo):

    def __init__(self, red_axis_ids, **kargs):
        super(DotLeftViewInfo, self).__init__(**kargs)
        self.red_axis_ids = red_axis_ids
        self.__tensor_description = None

    @property
    def tensor_description(self):
        if self.__tensor_description is None:
            self.__tensor_description = self.tensor_axes_info. \
                tensor_description.dot_reaxe_left(self.red_axis_ids)
        return self.__tensor_description


class DotRightViewInfo(TensorViewInfo):

    def __init__(self, red_axis_ids, **kargs):
        super(DotRightViewInfo, self).__init__(**kargs)
        self.red_axis_ids = red_axis_ids
        self.__tensor_description = None

    @property
    def tensor_description(self):
        if self.__tensor_description is None:
            self.__tensor_description = self.tensor_axes_info. \
                tensor_description.dot_reaxe_right(self.red_axis_ids)
        return self.__tensor_description


class AxesComp(object):
    """A Computation for computing axes"""

    def __init__(self, axes=None, **kargs):
        super(AxesComp, self).__init__(**kargs)
        self.__axes__ = axes

    @staticmethod
    def as_axes(axes, **kargs):
        if isinstance(axes, AxesComp):
            return axes
        elif axes is None:
            return None
        else:
            return LiteralAxesComp(axes=Axes(*axes), **kargs)

    @property
    def value(self):
        if self.__axes__ is None:
            self.__axes__ = self.resolve()
        return self.__axes__

    def resolve(self):
        raise NotImplementedError()

    def __add__(self, x):
        return AxesAppendComp(self, AxesComp.as_axes(x))

    def __radd__(self, x):
        return AxesAppendComp(AxesComp.as_axes(x), self)

    def __sub__(self, x):
        return AxesSubComp(self, AxesComp.as_axes(x))

    def __rsub__(self, x):
        return AxesSubComp(AxesComp.as_axes(x), self)

    def __mul__(self, x):
        return AxesIntersectComp(self, AxesComp.as_axes(x))

    def __rmul__(self, x):
        return AxesIntersectComp(AxesComp.as_axes(x), self)


def sample_axes(x, **kargs):
    return AxesSubComp(AxesComp.as_axes(x, **kargs), get_batch_axes())


def tensor_sample_axes(x, **kargs):
    return sample_axes(x.axes, **kargs)


def tensor_batch_axes(x, **kargs):
    return batch_axes(x.axes, **kargs)


def batch_axes(x, **kargs):
    return AxesIntersectComp(AxesComp.as_axes(x, **kargs), get_batch_axes())


def linear_map_axesa(in_axes, out_axes):
    return AxesSubComp(AxesAppendComp(in_axes, out_axes),
                       AxesIntersectComp(in_axes, out_axes))


def linear_map_axes(in_axes, out_axes):
    return AxesSubComp(AxesAppendComp(out_axes, in_axes),
                       AxesIntersectComp(in_axes, out_axes))


class LiteralAxesComp(AxesComp):
    """Actual axes are provided"""

    def __init__(self, **kargs):
        super(LiteralAxesComp, self).__init__(**kargs)


class ValueAxesComp(AxesComp):
    """Determine axes from value computed by x"""

    def __init__(self, x, **kargs):
        super(ValueAxesComp, self).__init__(**kargs)
        self.x = x

    def resolve(self):
        return self.x.axes.value


class AxesSubComp(AxesComp):
    """Result will be removal of axes in y from those in x"""

    def __init__(self, x, y, **kargs):
        super(AxesSubComp, self).__init__(**kargs)
        self.x = AxesComp.as_axes(x)
        self.y = AxesComp.as_axes(y)

    def resolve(self):
        x_axes = self.x.value
        y_axes = self.y.value
        return AxisIDTuple.sub(x_axes, y_axes).as_axes()


class AxesIntersectComp(AxesComp):

    def __init__(self, x, y, **kargs):
        super(AxesIntersectComp, self).__init__(**kargs)
        self.x = AxesComp.as_axes(x)
        self.y = AxesComp.as_axes(y)

    def resolve(self):
        x_axes = self.x.value
        y_axes = self.y.value
        return AxisIDTuple.intersect(x_axes, y_axes).as_axes()


class AxesAppendComp(AxesComp):

    def __init__(self, x, y, allow_repeated=False, **kargs):
        super(AxesAppendComp, self).__init__(**kargs)
        self.x = AxesComp.as_axes(x)
        self.y = AxesComp.as_axes(y)
        self.allow_repeated = allow_repeated

    def resolve(self):
        x_axes = self.x.value
        y_axes = self.y.value
        if self.allow_repeated:
            return x_axes + y_axes
        else:
            return AxisIDTuple.append(x_axes, y_axes).as_axes()


class AxesSliceComp(AxesComp):

    def __init__(self, x, lower=0, upper=None, **kargs):
        super(AxesSliceComp, self).__init__(**kargs)
        self.x = AxesComp.as_axes(x)
        self.lower = lower
        self.upper = upper

    def resolve(self):
        x_axes = self.x.value
        if self.upper:
            return x_axes[self.lower:self.upper]
        else:
            return Axes(x_axes[self.lower])


class Tensor(Op):

    def __init__(self, dtype=None, axes=None, scale=None, **kwds):
        super(Tensor, self).__init__(**kwds)
        if dtype is None:
            dtype = np.dtype(np.float32)
        self.dtype = dtype
        if axes is None:
            axes = ValueAxesComp(self)
        else:
            axes = AxesComp.as_axes(axes)
        self.__axes = axes
        self.__tensor_axes_info = None
        self.__call_info = None

        # Derivative will be scaled by this
        self.scale = scale

    def visit(self, visitor, **kargs):
        return visitor.visit_tensor(self, **kargs)

    @property
    def output(self):
        return self

    @property
    def axes(self):
        return self.__axes

    def generate_add_delta(self, adjoints, delta):
        delta_axes = delta.axes.value
        self_axes = self.axes.value
        reduction_axes = AxisIDTuple.sub(delta_axes, self_axes).as_axes()
        if reduction_axes:
            delta = sum(delta, reduction_axes=reduction_axes)

        if self not in adjoints:
            adjoints[self] = delta
        else:
            adjoints[self] = delta + adjoints[self]

    # Magic methods for builtin operations we want to use for creating nodes
    def __neg__(self):
        return negative(self)

    def __pos__(self):
        return self

    def __abs__(self):
        return absolute(self)

    def __add__(self, val):
        return add(self, val)

    def __radd__(self, val):
        return add(val, self)

    def __sub__(self, val):
        return subtract(self, val)

    def __rsub__(self, val):
        return subtract(val, self)

    def __mul__(self, val):
        return multiply(self, val)

    def __rmul__(self, val):
        return multiply(val, self)

    def __truediv__(self, val):
        return divide(self, val)

    def __rtruediv__(self, val):
        return divide(val, self)

    def __rdiv__(self, val):
        return divide(val, self)

    def __pow__(self, val):
        return power(self, val)

    def __rpow__(self, val):
        return power(val, self)

    # Python always uses eq for comparing keys, so if we override __eq__ we
    # cannot have sets of tensors, or using them as dictionary keys.  So,
    # we must use Equal explicitly in transfrom.  defmod and define __eq__
    # if it can ensure that its nodes do not need to be used as keys.
    # def __eq__(self, val):
    #    return equal(self, val)

    # def __ne__(self, val):
    #    return not_equal(self, val)

    def __lt__(self, val):
        return less(self, val)

    def __gt__(self, val):
        return greater(self, val)

    def __le__(self, val):
        return less_equal(self, val)

    def __ge__(self, val):
        return greater_equal(self, val)

    # Only works when capturing ops
    def __setitem__(self, key, val):
        return SetItem(self, key, val)

    # Only works when capturing ops
    def __iadd__(self, val):
        return SetItem(self, slice(None, None, None), self + val)

    # Only works when capturing ops
    def __isub__(self, val):
        return SetItem(self, slice(None, None, None), self - val)

    # Only works when capturing ops
    def __imul__(self, val):
        return SetItem(self, slice(None, None, None), self * val)

    # Only works when capturing ops
    def __idiv__(self, val):
        return SetItem(self, slice(None, None, None), self / val)

    def __axes__(self):
        return self.axes

    @property
    def value(self):
        return self.tensor_axes_info.tensor_description.value

    @property
    def tensor_axes_info(self):
        if self.__tensor_axes_info is None:
            self.__tensor_axes_info = self.compute_tensor_axes_info()
        return self.__tensor_axes_info

    def compute_tensor_axes_info(self):
        dtype = np.float32
        if self.dtype is not None:
            dtype = self.dtype
        return TensorAxesInfo(self.axes.value, dtype=dtype, tags=self.tags)

    @property
    def call_info(self):
        if self.__call_info is None:
            self.__call_info = self.compute_call_info()
        return self.__call_info

    def compute_call_info(self):
        return [self.reaxe(self.axes.value)]

    def transform_call_info(self, transformer, *args):
        call_args = [arg.value for arg in args]
        self.transform(transformer, *call_args)

    @property
    def resolved_axes(self):
        return self.tensor_axes_info.axes

    def reaxe(self, reaxe):
        return self.tensor_axes_info.reaxe(reaxe)

    def dot_reaxe_left(self, red_axis_ids):
        return self.tensor_axes_info.dot_reaxe_left(red_axis_ids)

    def dot_reaxe_right(self, red_axis_ids):
        return self.tensor_axes_info.dot_reaxe_right(red_axis_ids)

    # Required for parameter initializers
    @property
    def shape(self):
        return self.__axes__()

    def mean(self, out_axes=(), **kargs):
        return mean(self, out_axes=out_axes, **kargs)


class Broadcast(Tensor):
    """
    Used to add additional axes for a returned derivative.

    """

    def __init__(self, x, **kargs):
        super(Broadcast, self).__init__(args=(x,), **kargs)

    def compute_tensor_axes_info(self):
        x, = self.args
        return x.tensor_axes_info

    def visit(self, visitor):
        x, = self.args
        return visitor.visit_broadcast(self, x)


class AllocationOp(Tensor):

    def __init__(
            self,
            init=None,
            initial_value=None,
            initializers=[],
            **kargs):
        super(AllocationOp, self).__init__(**kargs)
        if init is not None:
            with captured_ops(self.initializers):
                init.fill(self)
        elif callable(initial_value):
            self.initializers.append(assign(self, initial_value()))
        elif initial_value is not None:
            self.initializers.append(assign(self, initial_value))

    def visit(self, visitor):
        return visitor.visit_allocation(self)


class ComputationOp(Tensor):
    """
    An TensorOp is the result of some sort of operation.
    """

    def __init__(self, out=None, dtype=np.float32, batch_axes=None, **kargs):
        super(ComputationOp, self).__init__(**kargs)
        self.dtype = dtype
        self.defs = {self}

        for arg in self.args:
            arg.users.add(self)

        if batch_axes is None:
            batch_axes = get_batch_axes()

        self.batch_axes = AxesComp.as_axes(batch_axes)

    @property
    def graph_label(self):
        return self.__class__.__name__ + '[' + self.name + ']'

    def visit(self, visitor):
        return visitor.visit_computation(self)


class Container(ComputationOp):
    """
    Implemented in terms of a subgraph, but stays in the graph.
    """

    def compute_tensor_axes_info(self):
        x, = self.args
        return x.tensor_axes_info

    def visit(self, visitor):
        return visitor.visit_container(self)


class RNG(AllocationOp):

    def __init__(self, seed=None, **kargs):
        super(RNG, self).__init__(args=(), **kargs)
        self.seed = seed

    def visit(self, visitor):
        return visitor.visit_RNG(self)

    def compute_tensor_axes_info(self):
        tensor_axes_info = super(RNG, self).compute_tensor_axes_info()
        tensor_axes_info.alloc = lambda transformer, tensor_description: transformer.rng(
            seed=self.seed)
        return tensor_axes_info

    @property
    def axes(self):
        return AxesComp.as_axes(())

    def uniform(self, low=0.0, high=1.0, size=None, **kargs):
        return Uniform(rng=self, low=low, high=high, size=size, **kargs)

    def normal(self, loc, scale, size, **kargs):
        return Normal(rng=self, loc=loc, scale=scale, size=size, **kargs)


class RNGOp(AllocationOp):

    def __init__(self, rng, axes, **kargs):
        self.__axes = axes
        super(RNGOp, self).__init__(args=(rng,), **kargs)

    @property
    def axes(self):
        return self.__axes

    def visit(self, visitor):
        return visitor.visit_rngop(self, *self.args)

    def compute_call_info(self):
        rng, = self.args
        return [rng.reaxe(rng.axes.value)]


class Normal(RNGOp):

    def __init__(self, loc=0.0, scale=1.0, size=None, **kargs):
        super(Normal, self).__init__(axes=size, **kargs)
        self.loc = loc
        self.scale = scale

        def allocator(transformer, tensor_description):
            rng, = self.call_info
            return transformer.rng_normal_tensor(
                rng.value, tensor_description, loc, scale)

        self.tensor_axes_info.alloc = allocator

    def visit(self, visitor):
        return visitor.visit_uniform(self, self.loc, self.scale, *self.args)


class Uniform(RNGOp):

    def __init__(self, low=0.0, high=1.0, size=None, **kargs):
        super(Uniform, self).__init__(axes=size, **kargs)
        self.low = low
        self.high = high

        def allocator(transformer, tensor_description):
            rng, = self.call_info
            return transformer.rng_uniform_tensor(
                rng.value, tensor_description, low, high)

        self.tensor_axes_info.alloc = allocator

    def visit(self, visitor):
        return visitor.visit_uniform(self, self.low, self.high, *self.args)


class VoidOp(ComputationOp):

    def __init__(self, **kargs):
        super(VoidOp, self).__init__(**kargs)
        self.__axes = AxesComp.as_axes(())

    def visit(self, visitor):
        return visitor.visit_void(self)

    @property
    def axes(self):
        return self.__axes

    def compute_call_info(self):
        # No out
        return []


class SetItem(VoidOp):

    def __init__(self, tensor, item, val, **kargs):
        super(SetItem, self).__init__(args=(tensor, val), out=tensor, **kargs)
        self.item = item

    def visit(self, visitor):
        tensor, val = self.args
        return visitor.visit_set_item(self, tensor, self.item, val)

    def compute_call_info(self):
        tensor, val = self.args
        call_info = super(SetItem, self).compute_call_info()
        call_info.append(tensor.reaxe(tensor.axes.value))
        call_info.append(val.reaxe(tensor.axes.value))
        return call_info

    def transform(self, transformer, tensor, val):
        transformer.set_item(tensor, self.item, val)


class doall(VoidOp):

    def __init__(self, all, **kargs):
        super(doall, self).__init__(args=all, out=all[-1], **kargs)

    def visit(self, visitor):
        return visitor.visit_doall(self, *self.args)


class ElementWise(ComputationOp):

    def __init__(self, **kargs):
        super(ElementWise, self).__init__(**kargs)

    def visit(self, visitor):
        return visitor.visit_elementwise(self)

    @property
    def axes(self):
        inputs = self.args
        result = self.args[0].axes
        for input in inputs[1:]:
            result = AxesAppendComp(result, input.axes)
        return result

    def compute_call_info(self):
        ci = super(ElementWise, self).compute_call_info()
        for arg in self.args:
            ci.append(arg.reaxe(self.axes.value))
        return ci


class AllReduce(ElementWise):

    def __init__(self, x, **kargs):
        super(AllReduce, self).__init__(args=(x,), **kargs)

    def visit(self, visitor):
        return visitor.visit_all_reduce(self, *self.args)

    def transform(self, transformer, out, x):
        return transformer.allreduce(x, out)


class placeholder(AllocationOp):
    """
    Can be set externally.
    """

    def __init__(self, **kargs):
        super(placeholder, self).__init__(**kargs)
        self.__axes = ValueAxesComp(self)
        self.tensor_axes_info.read_only = True

    def __axes__(self):
        return self.__axes

    def visit(self, visitor):
        return visitor.visit_placeholder(self)

    def generate_adjoints(self, tape, delta):
        pass

    @property
    def value(self):
        return get_current_environment()[self]

    @value.setter
    def value(self, value):
        get_current_environment()[self] = value

    def sync(self, transformer):
        value = self.value
        if isinstance(value, numbers.Real):
            transformer.fill(
                self.tensor_axes_info.tensor_description.value, value)
        else:
            transformer.set_value(self, value)


class Fill(VoidOp):

    def __init__(self, tensor, const, **kargs):
        super(Fill, self).__init__(args=(tensor,), **kargs)
        self.const = const

    def visit(self, visitor):
        return visitor.visit_fill(self, self.const)

    def compute_call_info(self):
        tensor, = self.args
        call_info = super(Fill, self).compute_call_info()
        call_info.append(tensor.reaxe(tensor.axes.value))
        return call_info

    def transform(self, transformer, tensor):
        transformer.fill(tensor, self.const)


class Constant(AllocationOp):
    """
    A scalar constant that appears in a graph.
    """

    def __init__(self, const, **kargs):
        self.const = const
        super(Constant, self).__init__(
            axes=(), dtype=np.dtype(np.float32), **kargs)
        self.initializers.append(Fill(self, const))

    def visit(self, visitor):
        return visitor.visit_constant(self, self.const)

    def generate_adjoints(self, adjoints, delta):
        pass

    @property
    def graph_label(self):
        shapes = self.tensor_axes_info.shapes
        if not shapes or max(shapes) <= 2:
            return str(self.const)
        if self.name == self.id:
            return 'Constant'
        return self.name

    @property
    def axes(self):
        return AxesComp.as_axes((()))

    def __str__(self):
        return '<{cl} ({const})>'.format(
            cl=self.__class__.__name__, const=self.const)


class NumPyTensor(AllocationOp):
    """
    A NumPy tensor with attached axes information
    """

    def __init__(self, nptensor, **kargs):
        self.nptensor = nptensor
        super(NumPyTensor, self).__init__(dtype=nptensor.dtype, **kargs)

        def allocator(transformer, tensor_description):
            out, = self.call_info
            return transformer.nparray(tensor_description, nptensor)

        self.tensor_axes_info.alloc = allocator

    @property
    def graph_label(self):
        return str(self.nptensor.shape)

    def visit(self, visitor):
        return visitor.visit_numpy_tensor(self, self.nptensor)

    def generate_adjoints(self, adjoints, delta):
        pass

    def __str__(self):
        return '<{cl} ({const})>'.format(
            cl=self.__class__.__name__, const=self.nptensor)


class absolute(ElementWise):

    def __init__(self, x, **kargs):
        super(absolute, self).__init__(args=(x,), **kargs)

    def visit(self, visitor):
        return visitor.visit_absolute(self, *self.args)

    def transform(self, transformer, out, x):
        transformer.absolute(x, out)

    def generate_adjoints(self, adjoints, delta, x):
        x.generate_add_delta(adjoints, sgn(x) * delta)


class add(ElementWise):

    def __init__(self, x, y, **kargs):
        super(add, self).__init__(args=(x, y), **kargs)

    def visit(self, visitor):
        return visitor.visit_add(self, *self.args)

    def transform(self, transformer, out, x, y):
        transformer.add(x, y, out)

    def generate_adjoints(self, adjoints, delta, x, y):
        x.generate_add_delta(adjoints, delta)
        y.generate_add_delta(adjoints, delta)


class argmax(ComputationOp):

    def __init__(self, x, max_axes=None, **kargs):
        if max_axes is None:
            max_axes = tensor_sample_axes(x)
        self.max_axes = AxesComp.as_axes(max_axes)
        super(argmax, self).__init__(args=(x,), dtype=np.int64, **kargs)

    def visit(self, visitor):
        return visitor.visit_argmax(self, self.max_axes, *self.args)

    def compute_call_info(self):
        x, = self.args
        return [self.reaxe([self.axes.value]), x.reaxe(
            [self.max_axes.value, self.axes.value])]

    def transform(self, transformer, out, x):
        transformer.argmax(x, out)

    @property
    def axes(self):
        x, = self.args
        return AxesSubComp(x.axes, self.max_axes)


class argmin(ComputationOp):

    def __init__(self, x, min_axes=None, **kargs):
        if min_axes is None:
            min_axes = tensor_sample_axes
        self.min_axes = AxesComp.as_axes(min_axes)
        super(argmin, self).__init__(args=(x,), dtype=np.int64, **kargs)

    def visit(self, visitor):
        return visitor.visit_argmin(self, self.min_axes, *self.args)

    def compute_call_info(self):
        x, = self.args
        return [self.reaxe([self.axes.value]), x.reaxe(
            [self.min_axes.value, self.axes.value])]

    def transform(self, transformer, out, x):
        transformer.argmin(x, out)

    @property
    def axes(self):
        x, = self.args
        return AxesSubComp(x.axes, self.min_axes)


class cos(ElementWise):

    def __init__(self, x, **kargs):
        super(cos, self).__init__(args=(x,), **kargs)

    def visit(self, visitor):
        return visitor.visit_cos(self, *self.args)

    def generate_adjoints(self, adjoints, delta, x):
        x.generate_add_delta(adjoints, delta * sin(x))

    def transform(self, transformer, out, x):
        transformer.cos(x, out)


class divide(ElementWise):

    def __init__(self, x, y, **kargs):
        super(divide, self).__init__(args=(x, y), **kargs)

    def visit(self, visitor):
        return visitor.visit_divide(self, *self.args)

    def transform(self, transformer, out, x, y):
        transformer.divide(x, y, out)

    def generate_adjoints(self, adjoints, delta, x, y):
        x.generate_add_delta(adjoints, delta * self / x)
        y.generate_add_delta(adjoints, -delta * self / y)


class dot(ComputationOp):

    def __init__(self, x, y, reduction_axes=None, out_axes=None,
                 numpy_matching=False, **kargs):
        self.numpy_matching = numpy_matching

        if numpy_matching:
            self.out_axes = AxesAppendComp(
                AxesAppendComp(
                    AxesSliceComp(x.axes, 0, -1),
                    AxesSliceComp(y.axes, 0, -2),
                    allow_repeated=True
                ),
                AxesSliceComp(y.axes, -1),
                allow_repeated=True
            )
            self.reduction_axes = AxesSliceComp(x.axes, -1, -1)
            self.multiply = False
        else:
            self.out_axes = AxesComp.as_axes(out_axes)
            if reduction_axes is None:
                self.reduction_axes = AxesIntersectComp(x.axes, y.axes)
            else:
                self.reduction_axes = AxesComp.as_axes(reduction_axes)

            if out_axes is not None:
                self.reduction_axes = AxesSubComp(
                    self.reduction_axes, self.out_axes)

            self.multiply = False

        super(dot, self).__init__(args=(x, y), **kargs)

    def visit(self, visitor):
        return visitor.visit_dot(
            self,
            self.reduction_axes,
            self.out_axes,
            *self.args)

    def compute_call_info(self):
        x, y = self.args
        if self.numpy_matching:
            o, a, b = self.reaxe(self.axes.value),\
                x.reaxe(x.axes.value), y.reaxe(y.axes.value)
        else:
            red_axis_ids = self.reduction_axes.value.as_axis_ids()
            a, b = x.dot_reaxe_left(red_axis_ids),\
                y.dot_reaxe_right(red_axis_ids)
            a_axes, b_axes = a.tensor_description.axes,\
                b.tensor_description.axes

            o_axes = (
                a_axes.as_axis_ids()[:-1] +
                b_axes.as_axis_ids()[1:]
            ).as_axes()
            o = self.reaxe(o_axes)
        return [o, a, b]

    def transform(self, transformer, out, x, y):
        if self.multiply:
            transformer.multiply(x, y, out)
        else:
            transformer.dot(x, y, out)

    @property
    def axes(self):
        if self.out_axes:
            return self.out_axes
        else:
            x, y = self.args
            return AxesAppendComp(AxesSubComp(x.axes, self.reduction_axes),
                                  AxesSubComp(y.axes, self.reduction_axes))

    def generate_adjoints(self, adjoints, delta, x, y):
        x.generate_add_delta(adjoints, dot(delta, y, out_axes=x.axes))
        y.generate_add_delta(adjoints, dot(x, delta, out_axes=y.axes))


class ElementWiseBoolean(ElementWise):

    def __init__(self, x, y, dtype=np.dtype(bool), **kargs):
        super(ElementWiseBoolean, self).__init__(
            args=(x, y), dtype=dtype, **kargs)

    def visit(self, visitor):
        return visitor.visit_elementwise_boolean(self)


class equal(ElementWiseBoolean):

    def visit(self, visitor):
        return visitor.visit_equal(self, *self.args)

    def transform(self, transformer, out, x, y):
        transformer.equal(x, y, out)


class not_equal(ElementWiseBoolean):

    def transform(self, transformer, out, x, y):
        transformer.not_equal(x, y, out)

    def visit(self, visitor):
        return visitor.visit_not_equal(self, *self.args)


class greater(ElementWiseBoolean):

    def transform(self, transformer, out, x, y):
        transformer.greater(x, y, out)

    def visit(self, visitor):
        return visitor.visit_greater(self, *self.args)


class less(ElementWiseBoolean):

    def transform(self, transformer, out, x, y):
        transformer.less(x, y, out)

    def visit(self, visitor):
        return visitor.visit_less(self, *self.args)


class greater_equal(ElementWiseBoolean):

    def transform(self, transformer, out, x, y):
        transformer.greater_equal(x, y, out)

    def visit(self, visitor):
        return visitor.visit_greater_equal(self, *self.args)


class less_equal(ElementWiseBoolean):

    def transform(self, transformer, out, x, y):
        transformer.less_equal(x, y, out)

    def visit(self, visitor):
        return visitor.visit_less_equal(self, *self.args)


class softmax(Container):

    def __init__(self, x, softmax_axes=None, **kargs):
        if softmax_axes is None:
            softmax_axes = tensor_sample_axes(x, **kargs)
        self.softmax_axes = softmax_axes
        self.x = x
        exps = exp(x - max(x, reduction_axes=softmax_axes))
        self.z = sum(exps, reduction_axes=softmax_axes)
        super(softmax, self).__init__(args=(exps / self.z,), **kargs)

    @property
    def axes(self):
        return self.args[0].axes

    def visit(self, visitor):
        return visitor.visit_softmax(self, self.x, *self.args)

    def generate_adjoints(self, adjoints, delta, x):
        z = delta * self
        zs = sum(z, reduction_axes=AxesSubComp(self.x.axes, self.batch_axes))
        self.x.generate_add_delta(adjoints, (z - zs * self))


class ReductionOp(ComputationOp):

    def __init__(self, x, reduction_axes=None, out_axes=None, **kargs):
        self.out_axes = AxesComp.as_axes(out_axes)
        if reduction_axes is None:
            if out_axes is None:
                self.reduction_axes = sample_axes(x.axes)
            else:
                self.reduction_axes = AxesSubComp(x.axes, self.out_axes)
        else:
            self.reduction_axes = AxesComp.as_axes(reduction_axes)
        super(ReductionOp, self).__init__(args=(x,), **kargs)
        self.mode = None

    def compute_call_info(self):
        x, = self.args
        reduction_axes = self.reduction_axes.value

        if len(reduction_axes) == 0:
            # TODO do this as a reaxe to 1d or something
            xr = x.reaxe(self.axes.value)
            self.mode = 'copy'
            return [self.reaxe(self.axes.value), xr]
        else:
            np_out_axes = self.axes.value
            red_axes = [AxesAxis(reduction_axes)]
            red_axes.extend(np_out_axes)
            red_axes = Axes(*red_axes)
            self.mode = 0
            return [self.reaxe(np_out_axes), x.reaxe(red_axes)]

    @property
    def axes(self):
        if self.out_axes is not None:
            return self.out_axes
        return AxesSubComp(self.args[0].axes, self.reduction_axes)


class max(ReductionOp):

    def __init__(self, x, **kargs):
        super(max, self).__init__(x, **kargs)

    def visit(self, visitor):
        return visitor.visit_sum(self, self.reduction_axes.value, *self.args)

    def transform(self, transformer, out, x):
        if self.mode is 'copy':
            # TODO Change this to a node replace
            transformer.set_item(out, (), x)
        else:
            transformer.max(x, self.mode, out)

    def generate_adjoints(self, adjoints, delta, x):
        x.generate_add_delta(adjoints, equal(x, self) * delta)


class min(ReductionOp):

    def __init__(self, x, **kargs):
        super(min, self).__init__(x, **kargs)

    def visit(self, visitor):
        return visitor.visit_sum(self, self.reduction_axes.value, *self.args)

    def transform(self, transformer, out, x):
        if self.mode is 'copy':
            # TODO Change this to a node replace
            transformer.set_item(out, (), x)
        else:
            transformer.min(x, self.mode, out)

    def generate_adjoints(self, adjoints, delta, x):
        x.generate_add_delta(adjoints, equal(x, self) * delta)


class sum(ReductionOp):

    def __init__(self, x, **kargs):
        super(sum, self).__init__(x, **kargs)

    def visit(self, visitor):
        return visitor.visit_sum(self, self.reduction_axes.value, *self.args)

    def transform(self, transformer, out, x):
        if self.mode is 'copy':
            # TODO Change this to a node replace
            transformer.set_item(out, (), x)
        else:
            transformer.sum(x, self.mode, out)

    def generate_adjoints(self, adjoints, delta, x):
        x.generate_add_delta(adjoints, delta)


def assign(lvalue, rvalue):
    return SetItem(lvalue, slice(None, None, None), rvalue)


class tensor_size(ComputationOp):

    def __init__(self, x, reduction_axes=None, out_axes=None, **kargs):
        self.out_axes = AxesComp.as_axes(out_axes)
        if reduction_axes is None:
            if out_axes is None:
                self.reduction_axes = sample_axes(x.axes)
            else:
                self.reduction_axes = AxesSubComp(x.axes, self.out_axes)
        else:
            self.reduction_axes = AxesComp.as_axes(reduction_axes)
        super(tensor_size, self).__init__(args=(x,), **kargs)

    def transform(self, transformer, out):
        resolved_reduction_axes = self.reduction_axes.value
        size = resolved_reduction_axes.size
        transformer.fill(out, size)

    @property
    def axes(self):
        return AxesComp.as_axes(())

    def generate_adjoints(self, adjoints, delta, x):
        pass


class Slice(ComputationOp):

    def __init__(self, slices, x, **kargs):
        super(Slice, self).__init__(args=(x,), **kargs)
        self.slices = slices


class Pad(ComputationOp):

    def __init__(self, axes, slice, x, **kargs):
        super(Pad, self).__init__(args=(x,), **kargs)
        self._axes = axes
        self.slice = slice

    @property
    def axes(self):
        return self._axes

    def transform(self, transformer, out, x):
        transformer.pad(x, self.slice, out)

    def generate_adjoints(self, adjoints, delta, x):
        pass


class Variable(AllocationOp):

    def __init__(self, **kargs):
        super(Variable, self).__init__(**kargs)
        self.tensor_axes_info.read_only = True

    def visit(self, visitor):
        return visitor.visit_variable(self)

    def generate_adjoints(self, adjoints, delta):
        pass


class Temporary(AllocationOp):

    def __init__(self, **kargs):
        super(Temporary, self).__init__(tags=['temp'], **kargs)

    def visit(self, visitor):
        return visitor.visit_temporary(self)

    def generate_adjoints(self, adjoints, delta):
        pass


class exp(ElementWise):

    def __init__(self, x, **kargs):
        super(exp, self).__init__(args=(x,), **kargs)

    def visit(self, visitor):
        return visitor.visit_exp(self, *self.args)

    def generate_adjoints(self, adjoints, delta, x):
        x.generate_add_delta(adjoints, delta * self)

    def transform(self, transformer, out, x):
        transformer.exp(x, out)


class log(ElementWise):

    def __init__(self, x, **kargs):
        super(log, self).__init__(args=(x,), **kargs)

    def visit(self, visitor):
        return visitor.visit_log(self, *self.args)

    def generate_adjoints(self, adjoints, delta, x):
        def do_adjoints(delta, x):

            if False and isinstance(x, softmax):
                x, = x.args

            if isinstance(x, divide):
                a, b = x.args
                do_adjoints(delta, a)
                do_adjoints(-delta, b)

            elif isinstance(x, exp):
                x.args[0].generate_add_delta(adjoints, delta)

            else:
                x.generate_add_delta(adjoints, delta / x)

        do_adjoints(delta, x)

    def transform(self, transformer, out, x):
        transformer.log(x, out)


class safelog(log):
    expm50 = np.exp(-50.)

    def visit(self, visitor):
        return visitor.visit_safelog(self, *self.args)

    def transform(self, transformer, out, x):
        transformer.maximum(x, safelog.expm50, out)
        transformer.log(out, out)


class maximum(ElementWise):

    def __init__(self, x, y, **kargs):
        super(maximum, self).__init__(args=(x, y), **kargs)

    def visit(self, visitor):
        return visitor.visit_maximum(self, *self.args)

    def transform(self, transformer, out, x, y):
        transformer.maximum(x, y, out=out)

    def generate_adjoints(self, adjoints, delta, x, y):
        x.generate_add_delta(adjoints, equal(self, x) * delta)
        y.generate_add_delta(adjoints, equal(self, y) * delta)


class minimum(ElementWise):

    def __init__(self, x, y, **kargs):
        super(minimum, self).__init__(args=(x, y), **kargs)

    def visit(self, visitor):
        return visitor.visit_minimum(self, *self.args)

    def transform(self, transformer, out, x, y):
        transformer.minimum(x, y, out=out)

    def generate_adjoints(self, adjoints, delta, x, y):
        x.generate_add_delta(adjoints, equal(self, x) * delta)
        y.generate_add_delta(adjoints, equal(self, y) * delta)


class multiply(ElementWise):

    def __init__(self, x, y, **kargs):
        super(multiply, self).__init__(args=(x, y), **kargs)

    def visit(self, visitor):
        return visitor.visit_multiply(self, *self.args)

    def generate_adjoints(self, adjoints, delta, x, y):
        x.generate_add_delta(adjoints, delta * y)
        y.generate_add_delta(adjoints, x * delta)

    def transform(self, transformer, out, x, y):
        transformer.multiply(x, y, out)


class negative(ElementWise):

    def __init__(self, x, **kargs):
        super(negative, self).__init__(args=(x,), **kargs)

    def visit(self, visitor):
        return visitor.visit_negative(self, *self.args)

    def generate_adjoints(self, adjoints, delta, x):
        x.generate_add_delta(adjoints, -delta)

    def transform(self, transformer, out, x):
        transformer.negative(x, out)


class onehot(ComputationOp):

    def __init__(self, x, axis=None, axes=None, **kargs):
        if axis is None:
            if axes is None:
                raise ValueError('Cannot determine one-hot axis.')
            axis = AxesSubComp(axes, x.axes)
        else:
            if axes is None:
                x_sample = sample_axes(x.axes)
                x_batch = batch_axes(x.axes)
                axes = AxesAppendComp(Axes(axis), AxesAppendComp(x_sample, x_batch))
        super(onehot, self).__init__(args=(x,), axes=axes, **kargs)
        self.axis = axis

    def visit(self, visitor):
        return visitor.visit_onehot(self, self.args[0], self.axis)

    def compute_call_info(self):
        x, = self.args
        ci = [self.reaxe(Axes(Axes(self.axis),
                              AxesSubComp(self.axes, Axes(self.axis)).value)),
              x.reaxe(Axes(x.axes.value))]
        return ci

    def transform(self, transformer, out, x):
        transformer.onehot(x, out)


class power(ElementWise):

    def __init__(self, x, y, **kargs):
        super(power, self).__init__(args=(x,), **kargs)

    def visit(self, visitor):
        return visitor.visit_power(self, *self.args)

    def transform(self, transformer, out, x, y):
        transformer.pow(x, y, out)

    def generate_adjoints(self, adjoints, delta, x, y):
        x.generate_add_delta(adjoints, delta * y * self / x)
        y.generate_add_delta(adjoints, delta * self * log(x))


class reciprocal(ElementWise):

    def __init__(self, x, **kargs):
        super(reciprocal, self).__init__(args=(x,), **kargs)

    def visit(self, visitor):
        return visitor.visit_reciprocal(self, *self.args)

    def generate_adjoints(self, adjoints, delta, x):
        x.generate_add_delta(adjoints, -self * self * delta)

    def transform(self, transformer, out, x):
        transformer.reciprocal(x, out)


class sgn(ElementWise):

    def __init__(self, x, **kargs):
        super(sgn, self).__init__(args=(x,), **kargs)

    def visit(self, visitor):
        return visitor.visit_sgn(self, *self.args)

    def generate_adjoints(self, adjoints, delta, x):
        # Zero
        pass

    def transform(self, transformer, out, x):
        transformer.sign(x, out)


class sig(Container, ElementWise):
    """Sigmoid"""

    def __init__(self, x, **kargs):
        self.x = x
        super(sig, self).__init__(args=(reciprocal(exp(-x) + 1),), axes=x.axes, **kargs)

    def visit(self, visitor):
        return visitor.visit_sig(self, *self.args)

    def generate_adjoints(self, adjoints, delta, x):
        self.x.generate_add_delta(adjoints, delta * self * (1.0 - self))


class sin(ElementWise):

    def __init__(self, x, **kargs):
        super(sin, self).__init__(args=(x,), **kargs)

    def visit(self, visitor):
        return visitor.visit_sin(self, *self.args)

    def generate_adjoints(self, adjoints, delta, x):
        x.generate_add_delta(adjoints, delta * cos(x))

    def transform(self, transformer, out, x):
        transformer.sin(x, out)


class sqrt(ElementWise):

    def __init__(self, x, **kargs):
        super(sqrt, self).__init__(args=(x,), **kargs)

    def visit(self, visitor):
        return visitor.visit_sqrt(self, *self.args)

    def generate_adjoints(self, adjoints, delta, x):
        x.generate_add_delta(adjoints, .5 * delta * self)

    def transform(self, transformer, out, x):
        transformer.sqrt(x, out)


class square(ElementWise):

    def __init__(self, x, **kargs):
        super(square, self).__init__(args=(x,), **kargs)

    def visit(self, visitor):
        return visitor.visit_square(self, *self.args)

    def generate_adjoints(self, adjoints, delta, x):
        x.generate_add_delta(adjoints, 2.0 * delta * x)

    def transform(self, transformer, out, x):
        transformer.square(x, out)


class subtract(ElementWise):

    def __init__(self, x, y, **kargs):
        super(subtract, self).__init__(args=(x, y), **kargs)

    def visit(self, visitor):
        return visitor.visit_subtract(self, *self.args)

    def generate_adjoints(self, adjoints, delta, x, y):
        x.generate_add_delta(adjoints, delta)
        y.generate_add_delta(adjoints, -delta)

    def transform(self, transformer, out, x, y):
        transformer.subtract(x, y, out)


class tanh(ElementWise):

    def __init__(self, x, **kargs):
        super(tanh, self).__init__(args=(x,), **kargs)

    def visit(self, visitor):
        return visitor.visit_tanh(self, *self.args)

    def generate_adjoints(self, adjoints, delta, x):
        x.generate_add_delta(adjoints, delta * (1.0 - self * self))

    def transform(self, transformer, out, x):
        transformer.tanh(x, out)


class Function(nodes.Node):

    def __init__(self, ops):
        super(Function, self).__init__()
        from geon.backends.graph.analysis import Digraph
        self.ops = Digraph(ops)
        args, defs = set(), set()
        for op in self.ops.topsort():
            # Kernel defines the def of each operation
            defs |= set([op])
            # Kernel uses the args of each operation
            # except whatever is being defined
            args |= set(op.args) - defs
        self.args = args
        self.defs = defs

    @property
    def inputs(self):
        return self.use


class Buffer(object):

    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.data = None


def mean(x, **kargs):
    return sum(x, **kargs) / tensor_size(x, **kargs)


def deriv(dep, indep):
    Op.simple_prune([dep, indep])
    adjoint = dep.adjoints()[indep]
    if adjoint.axes.value == indep.axes.value:
        return adjoint
    else:
        return Broadcast(adjoint, axes=indep.axes)


def cross_entropy_multi(y, t, usebits=False, out_axes=None):
    logscale = np.float(1. / np.log(2.0) if usebits else 1.)
    return -sum(safelog(y) * t, out_axes=out_axes) * logscale


class cross_entropy_binary_inner(Container, ElementWise):

    def __init__(self, y, t, **kargs):
        self.y = y
        self.t = t
        if isinstance(self.y, sig):
            cebi = (1 - t) * y.x - safelog(y)
        else:
            cebi = -(safelog(y) * t + safelog(1 - y) * (1 - t))
        super(cross_entropy_binary_inner, self).__init__(args=(cebi,), **kargs)

    def generate_adjoints(self, adjoints, delta, x):
        if isinstance(self.y, sig):
            # Shortcut derivative
            x = self.y.x
            x.generate_add_delta(adjoints, (self.y - self.t) * delta)
            self.t.generate_add_delta(adjoints, x * delta)
        else:
            self.args[0].generate_add_delta(adjoints, delta)


def cross_entropy_binary(y, t, out_axes=None):
    return sum(cross_entropy_binary_inner(y, t), out_axes=out_axes)


def set_break(op, name=None):
    def hook(transformer, op, transform_op):
        transform_op(op)
        # print(name)
        pass
    op.transform_hook = hook
    return op
