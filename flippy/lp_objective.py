from typing import Optional, Mapping, Union
from flippy.lp_variable import LpVariable
from flippy.lp_expression import LpExpression
from flippy.utils import Numeric


class Minimize:
    """ A class representing a minimization problem """


class Maximize:
    """ A class representing a maximization problem """


ObjectiveType = Union[Minimize, Maximize]


class LpObjective(LpExpression):
    """ A class representing an objective function """

    def __init__(self, name: str = '', expression: Optional[Mapping[LpVariable, Numeric]] = None, constant: Numeric = 0,
                 sense: ObjectiveType = Minimize) -> None:
        """ Initialize the objective

        Parameters
        ----------
        name:
            The name of the objective
        expression:
            Dictionary representing variables and their coefficients
        constant:
            The constant term of the objective
        sense:
            Whether to minimize or maximize the objective
        """
        super(LpObjective, self).__init__(name, expression, constant)
        self._sense = None

        self.sense = sense

    @property
    def sense(self) -> ObjectiveType:
        """ Getter for the sense of the objective

        Returns
        -------
        flippy.lp_objective.ObjectiveType
        """
        return self._sense

    @sense.setter
    def sense(self, sense: ObjectiveType) -> None:
        """ Setter for the sens eof the objective. Raises error if not valid sense.

        Parameters
        ----------
        sense: flippy.lp_objective.Minimize or flippy.lp_objective.Maximize
        """
        if sense not in [Minimize, Maximize]:
            raise ValueError("Sense must be one of %s, %s not %s" % (Minimize, Maximize, sense))
        self._sense = sense
