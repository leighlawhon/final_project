BDD + Design
Users:
  • Shopper
  • ASCII artist
  • Advertiser

Components:
const $section_renders =
  Should load have data
  And should run a "loading"  animation for min 1 second
  And should preload when it has more data to load
    But should display "end of catalog" when it does not have more data to load
  And should display 20 items
  And should be responsive at 1170(5up), 970(4up), and 750(2up + padding)
  And should be followed by an ad that is random and unique

cons $item_render =
  Should be displayed within its boundaries
  And should be at the correct size
  And should display a size field in pixels
  And should display a price field in cents
  And should display a $date_renders

const $date_renders =
  Should add a date field for when the product was added
  And should show a relative date if it was added less than a week ago
  But should show a actual date if it was added more than a week ago

Feature: Products display in a grid that renders 20 items and an ad and adds more content as it scrolls

  Scenario: The grid page does not render
    Given the internet is functioning
    When the system returns an error
    Then should display a message that there is an error
      And should render what type of error
      And should render how to contact 

  Scenario: The grid page renders
    Given The JSON has loaded with no errors
      And there are more items to load
    When the section container is ready
    Then $section_renders
      But message "end of catalog" renders if there are no more items

  Scenario: An item renders
    Given the JSON has loaded with no errors
      And is has finished loading the section
    When the item container is ready
    Then $item_render

  Scenario: When the grid page is scrolled
    Given the previous 20 items have loaded
    When the shopper scrolls
    Then $section_renders if there are more items in the catalog
      But message "end of catalog" renders if there are no more items
