/*USE world

SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.code = languages.country_code
WHERE language = 'Slovene'
ORDER by languages.percentage DESC

SELECT countries.name, COUNT(cities.name) 
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP by countries.id
ORDER by COUNT (cities.name) DESC

SELECT cities.name, cities.population
FROM cities
JOIN countries ON cities.country_id = countries.id
WHERE countries.name = 'Mexico' and cities.population > 500000
ORDER by cities.population DESC

SELECT countries.name, languages.percentage
FROM countries
JOIN languages ON countries.code = languages.country_code
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC

SELECT name, surface_area, population
FROM countries
WHERE surface_area < 501 and population > 100000

SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE government_form = 'Constitutional Monarchy' and capital > 200 and life_expectancy > 75

SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina'
AND cities.district = 'Buenos Aires'
AND cities.population > 500000*/

SELECT countries.region, COUNT(countries.id)
FROM countries
GROUP by countries.region
ORDER by COUNT(countries.id) DESC