#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Luminance :math:`Y`
===================

Defines *luminance* :math:`Y` computation objects.

The following methods are available:

-   :func:`luminance_newhall1943`: *luminance* :math:`Y` computation of given
    *Munsell* value :math:`V` using *Newhall, Nickerson, and Judd (1943)*
    method.
-   :func:`luminance_1976`: *luminance* :math:`Y` computation of given
    *Lightness* :math:`L^*` as per *CIE Lab* implementation.
-   :func:`luminance_ASTM_D1535_08`: *luminance* :math:`Y` computation of given
    *Munsell* value :math:`V` using *ASTM D1535-08e1 (2008)* method.
"""

from __future__ import unicode_literals

from colour.constants import CIE_E, CIE_K

__author__ = "Colour Developers"
__copyright__ = "Copyright (C) 2013 - 2014 - Colour Developers"
__license__ = "New BSD License - http://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-science@googlegroups.com"
__status__ = "Production"

__all__ = ["luminance_newhall1943",
           "luminance_1976",
           "luminance_ASTM_D1535_08",
           "LUMINANCE_FUNCTIONS",
           "get_luminance"]


def luminance_newhall1943(V):
    """
    Returns the *luminance* :math:`Y` of given *Munsell* value :math:`V` using
    *Newhall, Nickerson, and Judd (1943)* method.

    Parameters
    ----------
    V : float
        *Munsell* value :math:`V`.

    Returns
    -------
    float
        *luminance* :math:`Y`.

    Notes
    -----
    -   Input *Munsell* value :math:`V` is in domain [0, 10].
    -   Output *luminance* :math:`Y` is in domain [0, 100].

    References
    ----------
    .. [1]  http://en.wikipedia.org/wiki/Lightness
            (Last accessed 13 April 2014)

    Examples
    --------
    >>> luminance_newhall1943(3.74629715382)
    10.4089874577
    """

    Y = 1.2219 * V - 0.23111 * (V * V) + 0.23951 * (V ** 3) - 0.021009 * (
        V ** 4) + 0.0008404 * (V ** 5)

    return Y


def luminance_1976(L, Yn=100.):
    """
    Returns the *luminance* :math:`Y` of given *Lightness* :math:`L^*` with
    given reference white *luminance* :math:`Y_n`.

    Parameters
    ----------
    L : float
        *Lightness* :math:`L^*`
    Yn : float
        White reference *luminance* :math:`Y_n`.

    Returns
    -------
    float
        *luminance* :math:`Y`.

    Notes
    -----
    -   Input *Lightness* :math:`L^*` is in domain [0, 100].
    -   Output *luminance* :math:`Y` is in domain [0, 100].

    References
    ----------
    .. [2]  http://www.poynton.com/PDFs/GammaFAQ.pdf
            (Last accessed 12 April 2014)

    Examples
    --------
    >>> luminance_1976(37.9856290977)
    10.08
    """

    Y = ((((L + 16.) / 116.) ** 3.) * Yn
         if L > CIE_K * CIE_E else
         (L / CIE_K) * Yn)

    return Y


def luminance_ASTM_D1535_08(V):
    """
    Returns the *luminance* :math:`Y` of given *Munsell* value :math:`V` using
    *ASTM D1535-08e1 (2008)* method.

    Parameters
    ----------
    V : float
        *Munsell* value :math:`V`.

    Returns
    -------
    float
        *luminance* :math:`Y`.

    Notes
    -----
    -   Input *Munsell* value :math:`V` is in domain [0, 10].
    -   Output *luminance* :math:`Y` is in domain [0, 100].

    References
    ----------
    -  http://www.scribd.com/doc/89648322/ASTM-D1535-08e1-Standard-Practice-for-Specifying-Color-by-the-Munsell-System

    Examples
    --------
    >>> luminance_ASTM_D1535_08(3.74629715382)
    10.1488096782
    """

    Y = 1.1914 * V - 0.22533 * (V * V) + 0.23352 * (V ** 3) - 0.020484 * (
        V ** 4) + 0.00081939 * (V ** 5)

    return Y


LUMINANCE_FUNCTIONS = {"Luminance Newhall 1943": luminance_newhall1943,
                       "Luminance 1976": luminance_1976,
                       "Luminance ASTM D1535-08": luminance_ASTM_D1535_08}
"""
Supported *luminance* computations methods.

LUMINANCE_FUNCTIONS : dict
    ("Luminance Newhall 1943", "Luminance 1976", "Luminance ASTM D1535-08")
"""

def get_luminance(LV, Yn=100., method="Luminance 1976"):
    """
    Returns the *luminance* :math:`Y` of given *Lightness* :math:`L^*` or given
    *Munsell* value :math:`V`.

    Parameters
    ----------
    LV : float
        *Lightness* :math:`L^*` or *Munsell* value :math:`V`.
    Yn : float, optional
        White reference *luminance* :math:`Y_n`.
    method : unicode, optional
        ("Luminance Newhall 1943", "Luminance 1976", "Luminance ASTM D1535-08")
        Computation method.

    Returns
    -------
    float
        *luminance* :math:`Y`.

    Notes
    -----
    -   Input *LV* is in domain [0, 100] or [0, 10] and *luminance* :math:`Y_n`
        is in domain [0, 100].
    -   Output *luminance* :math:`Y` is in domain [0, 100].

    Examples
    --------
    >>> get_luminance(3.74629715382)
    37.9856290977
    """

    if Yn is None or method is not None:
        return LUMINANCE_FUNCTIONS.get(method)(LV)
    else:
        return luminance_1976(LV, Yn)