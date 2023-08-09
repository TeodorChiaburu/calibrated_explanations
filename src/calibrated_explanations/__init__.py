# flake8: noqa: E501
"""
Calibrated Explanations (calibrated_explanations)

is a Python package for explaining black-box models.

It is based on the paper "Calibrated Explanations: with Uncertainty Information and Counterfactuals" 
by Helena Löfström et al.
"""
from lime.discretize import EntropyDiscretizer, QuartileDiscretizer, DecileDiscretizer
from .core import CalibratedExplainer, __version__
from .wrappers import CalibratedAsLimeTabularExplainer, CalibratedAsShapExplainer
from ._discretizers import BinaryDiscretizer, BinaryEntropyDiscretizer
from ._explanations import CalibratedExplanation
from .VennAbers import VennAbers
