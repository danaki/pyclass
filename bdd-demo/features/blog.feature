Feature: As a website owner, I want to create posts

  Scenario: Successfuly create blog record
    Given flaskr is setup
      And I login with "admin" and "default"
      When I create a post with title "My Title" and body "Post Body"
      Then I should see created post with title "My Title"
