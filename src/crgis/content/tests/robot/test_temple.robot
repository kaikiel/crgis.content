# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s crgis.content -t test_temple.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src crgis.content.testing.CRGIS_CONTENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_temple.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Temple
  Given a logged-in site administrator
    and an add temple form
   When I type 'My Temple' into the title field
    and I submit the form
   Then a temple with the title 'My Temple' has been created

Scenario: As a site administrator I can view a Temple
  Given a logged-in site administrator
    and a temple 'My Temple'
   When I go to the temple view
   Then I can see the temple title 'My Temple'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add temple form
  Go To  ${PLONE_URL}/++add++Temple

a temple 'My Temple'
  Create content  type=Temple  id=my-temple  title=My Temple


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the temple view
  Go To  ${PLONE_URL}/my-temple
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a temple with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the temple title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
