# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from crgis.content.testing import CRGIS_CONTENT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that crgis.content is properly installed."""

    layer = CRGIS_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if crgis.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'crgis.content'))

    def test_browserlayer(self):
        """Test that ICrgisContentLayer is registered."""
        from crgis.content.interfaces import (
            ICrgisContentLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICrgisContentLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = CRGIS_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['crgis.content'])

    def test_product_uninstalled(self):
        """Test if crgis.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'crgis.content'))

    def test_browserlayer_removed(self):
        """Test that ICrgisContentLayer is removed."""
        from crgis.content.interfaces import \
            ICrgisContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           ICrgisContentLayer,
           utils.registered_layers())
