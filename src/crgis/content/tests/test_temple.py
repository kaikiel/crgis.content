# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from crgis.content.interfaces import ITemple
from crgis.content.testing import CRGIS_CONTENT_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class TempleIntegrationTest(unittest.TestCase):

    layer = CRGIS_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Temple')
        schema = fti.lookupSchema()
        self.assertEqual(ITemple, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Temple')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Temple')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(ITemple.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='Temple',
            id='Temple',
        )
        self.assertTrue(ITemple.providedBy(obj))
