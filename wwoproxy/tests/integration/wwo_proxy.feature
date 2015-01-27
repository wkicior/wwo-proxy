Feature: WWO proxy integration test
  Scenario: Get the forecast
    Given Flask app is running
    When We request a forecast
    Then We get a forecast
