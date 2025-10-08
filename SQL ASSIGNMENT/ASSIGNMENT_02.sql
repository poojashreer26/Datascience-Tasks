-- By Using Groupby and having

-- 26. Count the number of customers in each city.
-- SELECT CUST_CITY,Count(Cust_Id) FROM sh.CUSTOMERS Group by CUST_CITY

-- 27. Find cities with more than 100 customers.
-- SELECT CUST_CITY,Count(*) FROM sh.CUSTOMERS Group by CUST_CITY HAVING count(*)>100

-- 28. Count the number of customers in each state.
-- SELECT CUST_STATE_PROVINCE,Count(*) FROM sh.CUSTOMERS Group by CUST_STATE_PROVINCE

-- 29. Find states with fewer than 50 customers.
-- SELECT CUST_STATE_PROVINCE,COUNT(*) FROM SH.CUSTOMERS Group by CUST_STATE_PROVINCE HAVING COUNT(*)<50

-- 30. Calculate the average credit limit of customers in each city.
-- SELECT CUST_CITY,AVG(Cust_credit_limit) from sh.CUSTOMERS group by CUST_CITY 

-- 31. Find cities with average credit limit greater than 8,000.
-- SELECT CUST_CITY,AVG(Cust_credit_limit) FROM SH.CUSTOMERS GROUP BY CUST_CITY HAVING AVG(Cust_credit_limit)>8000

-- 32. Count customers by marital status.
-- SELECT CUST_MARITAL_STATUS,COUNT(*) FROM SH.CUSTOMERS GROUP BY CUST_MARITAL_STATUS

-- 33. Find marital statuses with more than 200 customers.
-- SELECT CUST_MARITAL_STATUS,COUNT(*) FROM SH.CUSTOMERS Group by CUST_MARITAL_STATUS HAVING COUNT(*)>200

-- 34. Calculate the average year of birth grouped by gender.
-- SELECT CUST_GENDER,AVG(CUST_YEAR_OF_BIRTH)FROM SH.CUSTOMERS GROUP BY (CUST_GENDER)

-- 35. Find genders with average year of birth after 1990.
-- SELECT CUST_GENDER,AVG(CUST_YEAR_OF_BIRTH) FROM SH.CUSTOMERS GROUP BY CUST_GENDER HAVING AVG(CUST_YEAR_OF_BIRTH)>1990

-- 36. Count the number of customers in each country.
-- SELECT COUNTRY_ID,COUNT(*) FROM SH.CUSTOMERS GROUP BY COUNTRY_ID

-- 37. Find countries with more than 1,000 customers.
-- SELECT COUNTRY_ID,COUNT(*) FROM SH.CUSTOMERS GROUP BY COUNTRY_ID HAVING COUNT(*)>1000

-- 38. Calculate the total credit limit per state.
-- SELECT CUST_STATE_PROVINCE,SUM(Cust_credit_limit) FROM SH.CUSTOMERS GROUP BY (CUST_STATE_PROVINCE)

-- 39. Find states where the total credit limit exceeds 100,000.
-- SELECT CUST_STATE_PROVINCE,SUM(Cust_credit_limit) FROM SH.CUSTOMERS GROUP BY (CUST_STATE_PROVINCE) HAVING SUM(Cust_credit_limit)>100000

-- 40. Find the maximum credit limit for each income level.
-- SELECT CUST_INCOME_LEVEL,MAX(Cust_credit_limit) FROM SH.CUSTOMERS GROUP BY (CUST_INCOME_LEVEL)

-- 41. Find income levels where the maximum credit limit is greater than 15,000.
-- SELECT CUST_INCOME_LEVEL,MAX(Cust_credit_limit)FROM SH.CUSTOMERS GROUP BY CUST_INCOME_LEVEL HAVING MAX(CUST_CREDIT_LIMIT)>15000

-- 42. Count customers by year of birth.
-- SELECT CUST_YEAR_OF_BIRTH,COUNT(*)FROM SH.CUSTOMERS GROUP BY CUST_YEAR_OF_BIRTH

-- 43. Find years of birth with more than 50 customers.
-- SELECT CUST_YEAR_OF_BIRTH,COUNT(*)FROM SH.CUSTOMERS GROUP BY CUST_YEAR_OF_BIRTH HAVING COUNT(*)>50

-- 44. Calculate the average credit limit per marital status.
-- SELECT CUST_MARITAL_STATUS,AVG(Cust_credit_limit) FROM SH.CUSTOMERS GROUP BY CUST_MARITAL_STATUS

-- 45. Find marital statuses with average credit limit less than 5,000.
-- SELECT CUST_MARITAL_STATUS,AVG(Cust_credit_limit) FROM SH.CUSTOMERS GROUP BY CUST_MARITAL_STATUS HAVING AVG(Cust_credit_limit)>5000

-- 46. Count the number of customers by email domain (e.g., `company.example.com`).
-- SELECT CUST_EMAIL,COUNT(*) FROM SH.CUSTOMERS GROUP BY CUST_EMAIL

-- 47. Find email domains with more than 300 customers.
-- SELECT CUST_EMAIL,COUNT(*) FROM SH.CUSTOMERS GROUP BY CUST_EMAIL HAVING COUNT(*)>300

-- 48. Calculate the average credit limit by validity (`CUST_VALID`).
-- SELECT CUST_VALID,AVG(Cust_credit_limit)FROM SH.CUSTOMERS GROUP BY CUST_VALID

-- 49. Find validity groups where the average credit limit is greater than 7,000.
-- SELECT CUST_VALID,AVG(Cust_credit_limit)FROM SH.CUSTOMERS GROUP BY CUST_VALID HAVING AVG(Cust_credit_limit)>7000

-- 50. Count the number of customers per state and city combination where there are more than 50 customers.
-- SELECT CUST_STATE_PROVINCE,CUST_CITY,Count(*) FROM sh.CUSTOMERS Group by CUST_STATE_PROVINCE,CUST_CITY HAVING COUNT(*)>50