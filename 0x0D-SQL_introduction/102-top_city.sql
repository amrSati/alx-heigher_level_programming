-- Displays the top 3 of cities temperature during july and august
-- ordered by temperature
CREATE TABLE IF NOT EXIST jul_aug
	SELECT *
	FROM temperatures
	WHERE month = 7 OR month = 8;

SELECT city, AVG(value) AS avg_temp
FROM jul_aug
GROUP BY city
ORDER BY avg_tmp DESC
LIMIT 3;
