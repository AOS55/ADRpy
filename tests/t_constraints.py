#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""t_constraints.py:
Unit tests for the constraints module
"""
import math
import unittest
from ADRpy import constraintanalysis as ca
from ADRpy import atmospheres as at

class TestUM(unittest.TestCase):
    """Unit tests for the constraints module."""

    def setUp(self):
        pass

    def test_take_off(self):
        """Tests the take-off constraint calculation"""

        print("Take-off constraint test.")

        designbrief = {'rwyelevation_m':1000, 'groundrun_m':1200}
        designdefinition = {'aspectratio':7.3, 'bpr':3.9, 'tr':1.05}
        designperformance = {'CDTO':0.04, 'CLTO':0.9, 'CLmaxTO':1.6, 'mu_R':0.02}

        wingloadinglist_pa = [2000, 3000, 4000, 5000]

        atm = at.Atmosphere()
        concept = ca.AircraftConcept(designbrief, designdefinition, designperformance, atm)

        tw_sl, liftoffspeed_mpstas, _ = concept.twrequired_to(wingloadinglist_pa)

        self.assertEqual(round(10000 * tw_sl[0]), round(10000 * 0.19397876))
        self.assertEqual(round(10000 * liftoffspeed_mpstas[0]), round(10000 * 52.16511207))

        self.assertEqual(round(10000 * tw_sl[3]), round(10000 * 0.41110154))
        self.assertEqual(round(10000 * liftoffspeed_mpstas[3]), round(10000 * 82.48028428))

    def test_wig(self):
        """Tests the wing in ground effect factor calculation"""

        print("WIG factor test.")

        designdef = {'aspectratio':8}
        wingarea_m2 = 10
        wingspan_m = math.sqrt(designdef['aspectratio'] * wingarea_m2)

        for wingheight_m in [0.6, 0.8, 1.0]:
            designdef['wingheightratio'] = wingheight_m / wingspan_m
            aircraft = ca.AircraftConcept({}, designdef, {}, {})

        self.assertEqual(round(10000 * aircraft.wigfactor()),
                         round(10000 * 0.7619047))


if __name__ == '__main__':
    unittest.main()
