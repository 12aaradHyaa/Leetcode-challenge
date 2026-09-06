SELECT ROUND(SUM(tiv_2016),2) as tiv_2016
FROM Insurance
WHERE tiv_2015 IN(
    select tiv_2015
    from Insurance
    group by tiv_2015
    having count(*)>1
) AND (lat,lon) IN(
    select lat, lon
    from Insurance
    group by lat, lon
    having count(*)=1
)