import unittest2 as unittest
from plone.formwidget.dateinput.testing import PFWDT_INTEGRATION_TESTING
from Products.CMFCore.utils import getToolByName


class DatetimeTest(unittest.TestCase):
    layer = PFWDT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_portal_js(self):
        # this plugin is disabled by default. let's check if it's now enabled'
        js_id = "++resource++plone.app.jquerytools.dateinput.js"
        p_js = getToolByName(self.portal,'portal_javascripts')
        self.failUnless(p_js.getResource(js_id).getEnabled())


    def test_portal_css(self):
        # this stylesheet is disabled by default. let's check if it's now enabled
        css_id = "++resource++plone.app.jquerytools.dateinput.css"
        p_css = getToolByName(self.portal,'portal_css')
        self.failUnless(p_css.getResource(css_id).getEnabled())