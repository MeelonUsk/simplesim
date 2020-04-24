"""Test cases for simulation module.

This module contains tests for the simulation module.
"""

# Standard library imports
import unittest

# Local application imports
from simplesim import base
from simplesim import simulation


class TestSimulation(unittest.TestCase):
    """Test the Simulation class.

    """
    def test_init_default(self):
        """Tests that the Simulation class initializes properly.

        :return: None
        """
        sim = simulation.Simulation()

        self.assertEqual(sim.current_time, 0)
        self.assertEqual(sim.delta_time, 1)

    def test_init_custom(self):
        """Tests that Simulation class initializes with custom values.

        :return: None
        """
        sim = simulation.Simulation(1, 2)

        self.assertEqual(sim.current_time, 1)
        self.assertEqual(sim.delta_time, 2)

    def test_current_time_setter(self):
        """Tests the current time setter.

        :return: None
        """
        sim = simulation.Simulation()
        sim.current_time = 100

        self.assertEqual(sim.current_time, 100)

    def test_delta_time_setter(self):
        """Tests the delta time setter.

        :return: None
        """
        sim = simulation.Simulation()
        sim.delta_time = 100

        self.assertEqual(sim.delta_time, 100)

    def test_step(self):
        """Tests the step method.

        :return: None
        """
        observer = base.Observer()
        sim = simulation.Simulation()
        sim.add_observer(observer)
        sim.step()

        self.assertEqual(sim.current_time, 1)

    def test_run(self):
        """Tests the run method.

        :return: None
        """
        observer = base.Observer()
        sim = simulation.Simulation()
        sim.add_observer(observer)
        sim.run(10)

        self.assertEqual(sim.current_time, 10)


if __name__ == '__main__':
    unittest.main()
