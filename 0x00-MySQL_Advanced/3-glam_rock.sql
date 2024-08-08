-- Lists all bands with Glam rock as their main style, ranked by their longevity.
-- Selects band_name and calculates their lifespan by subtracting year formed
-- *** from the year of their split (if exists) or the current year.
-- L6: Uses IFNULL to handle NULL values in 'split' column, defaulting
-- *** to '2022'.
-- L7: Filters bands with 'Glam rock' as one of their styles.
-- L8: Orders the result by lifespan in descending order.
SELECT band_name, (IFNULL(split, '2022') - formed) AS lifespan
    FROM metal_bands
    WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
    ORDER BY lifespan DESC;
