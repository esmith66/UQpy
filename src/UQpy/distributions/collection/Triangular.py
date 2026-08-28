from typing import Union
import scipy.stats as stats
from beartype import beartype
from UQpy.distributions.baseclass import DistributionContinuous1D


class Triangular(DistributionContinuous1D):
    @beartype
    def __init__(
        self, 
        c: Union[None, float, int] = 0.5,
        loc: Union[None, float, int] = 0.0,
        scale: Union[None, float, int] = 1.0
    ):
        """
        Initialize a triangular distribution.

        :param c: The shape parameter, which determines the location of the peak.
        :param loc: The location parameter.
        :param scale: The scale parameter.
        """
        super().__init__(loc=loc, scale=scale, ordered_parameters=("c", "loc", "scale"))
        self._construct_from_scipy(scipy_name=stats.triang)

