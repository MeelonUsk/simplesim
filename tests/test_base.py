"""Test cases for base module.

This module contains tests for the base module.
"""

# Standard library imports
import unittest

# Local application imports
from simplesim import base


class TestObserver(unittest.TestCase):
    """Test the Observer class.

    """
    # pylint: disable=no-self-use
    def test_update(self):
        """Tests the observer update method.

        :return: None
        """
        observer = base.Observer()
        observer.update()


class TestObservable(unittest.TestCase):
    """Test the Observable class.

    """
    def test_init(self):
        """Tests that Observable class initializes properly.

        :return: None
        """
        observable = base.Observable()
        self.assertEqual(observable.observers, [])

    def test_add_observer(self):
        """Tests the add observer method.

        :return: None
        """
        observable = base.Observable()
        observer1 = base.Observer()
        observer2 = base.Observer()
        test_observers = [observer1, observer2]

        observable.add_observer(observer1)
        observable.add_observer(observer2)

        for test_obs, ret_obs in zip(test_observers, observable.observers):
            self.assertIs(test_obs, ret_obs)

    def test_remove_observer(self):
        """Tests the remove observer method.

        :return: None
        """
        observable = base.Observable()
        observer = base.Observer()

        observable.add_observer(observer)
        self.assertTrue(observable.observers)
        self.assertIs(observable.observers[0], observer)

        observable.remove_observer(observer)
        self.assertFalse(observable.observers)

    # pylint: disable=no-self-use
    def test_notify(self):
        """Tests the notify method.

        :return: None
        """
        observable = base.Observable()
        observer1 = base.Observer()
        observer2 = base.Observer()

        observable.add_observer(observer1)
        observable.add_observer(observer2)

        observable.notify()


if __name__ == '__main__':
    unittest.main()
