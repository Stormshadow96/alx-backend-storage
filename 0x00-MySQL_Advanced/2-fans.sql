-- Selects and ranks bands country origins, ordered by total number of fans.
-- L2: Selects 'origin' column and calculates sum of 'fans' for each country.
-- L3: Groups results by country origin.
-- L4: Orders results by total number of fans in descending order.
SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;
