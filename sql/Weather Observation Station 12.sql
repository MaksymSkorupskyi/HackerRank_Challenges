# Weather Observation Station 12
# Query the list of CITY names from STATION that do not start with vowels and do not end with vowels.
# Your result cannot contain duplicates.
SELECT
  DISTINCT city
FROM
  station
WHERE
  LEFT(city, 1) NOT IN ('a','e','i','o','u')
  AND RIGHT(city, 1) NOT IN ('a','e','i','o','u')