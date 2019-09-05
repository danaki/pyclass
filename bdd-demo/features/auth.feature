Feature: As a website owner, I want to secure my website

  Scenario: Successfuly login
    Given flaskr is setup
      When I login with "admin" and "default"
      Then I should see the alert "You were logged in"

  Scenario: Can't login with incorrect username
    Given flaskr is setup
      When I login with "monty" and "default"
      Then I should see the alert "Invalid username"

  Scenario: Can't login with incorrect password
    Given flaskr is setup
      When I login with "admin" and "python"
      Then I should see the alert "Invalid password"

  Scenario: Successfuly logout
    Given flaskr is setup
      And I login with "admin" and "default"
      When I logout
      Then I should see the alert "You were logged out"
