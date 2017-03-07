ASCII

BDD
$section_renders =
  A loading animation should run (min timeout 1 sec for proper feedback)
  And the products should render an additional grid of 20 items
  And should be followed by an ad that is random and unique
  And should be responsive at 1170(5up), 970(4up), and 750(2up + padding)
  And should quietly fetch the next set of results

$date_renders =
  A date field for when the product was added
  And should show a relative date if it was added less than a week ago
  But should show a actual date if it was added more than a week ago

Feature: Products display in a grid that renders 20 items and an ad

    Scenario: When the grid page renders
      Given The JSON has loaded with no errors
        And there are more items to load
      When the page loads
      Then $section_renders

    Scenario: When the grid page DOES NOT renders
      Given the JSON has loaded with errors
      Then a warning message is render to the shopper

    Scenario: When an item renders
      Given the JSON has loaded with no errors
        And is has finished loading the section
      Then the ASCIIs should be displayed within its boundaries
        And should be at the correct size
        And should display a size field in pixels
        And should display a price field in cents
        And should display a $date_renders

    Scenario: When the grid page is scrolled
      Given the previous 20 items have loaded
        And there are more items to load
      When the shopper scrolls
      Then $section_renders

    Scenario: When the grid page is scrolled
      Given the previous 20 items have loaded
        And there are NO more items to load
      When the shopper scrolls
      Then the a "end of catalogue" message is rendered

  Feature: Product grid is sortable

  Feature: Product grid is searchable
