/*  BASIC COUNTING  */
/*  COUNT() | DISTINCT  */

-- count the total number of records in a table
SELECT COUNT(*) AS column_alias
FROM table_name;

-- count multiple fields in a table
SELECT COUNT(language) AS count_languages, COUNT(country) AS count_countries
FROM tbl_films;

-- return the unique number of countries in the table
SELECT COUNT (DISTINCT country) AS count_distinct_countries
FROM tbl_films;



/*  BASIC FILTERING  */
/*     WHERE  */

-- Count the records with at least 100,000 votes
SELECT COUNT(*) AS films_over_100K_votes
FROM reviews
WHERE num_votes >= 100000;

-- Count the Spanish-language films
SELECT COUNT(language) AS count_spanish
FROM films
WHERE language = 'Spanish';



/* FILTERING: LOGICAL OPERATORS  */
/*  AND | OR | NOT  */

-- title and release_year of films released in 1990 or 1999, 
-- which were in English or Spanish and took in more 
-- than $2,000,000 gross
SELECT title, release_year
FROM films
WHERE (release_year = 1990 OR release_year = 1999)
	AND (language = 'English' OR language = 'Spanish')
	AND gross > 2000000

-- title and release_year of all Spanish-language films 
-- released between 1990 and 2000 (inclusive) with budgets over $100 million.
SELECT title, release_year
FROM films
WHERE release_year BETWEEN 1990 AND 2000
	AND budget > 100000000
	AND (language = 'Spanish' OR language = 'French')


/*  FILTERING: LIKE, WHERE IN, AND WILDCARDS  */

-- Select the names that start with B
SELECT name
FROM people
WHERE name LIKE 'B%';

-- Select the names that have "r" as the second letter
SELECT name
FROM people
WHERE name LIKE '_r%';

-- Select names that don't start with A
SELECT name
FROM people
WHERE name NOT LIKE 'A%';