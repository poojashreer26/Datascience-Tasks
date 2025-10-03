-- 1. Find customers born after the year 1990.
-- SELECT * FROM SH.customers WHERE CUST_YEAR_OF_BIRTH > 1990;

-- 2. List all male customers (`CUST_GENDER = 'M'`)
-- SELECT CUST_GENDER FROM SH.customers WHERE CUST_GENDER = 'M'

-- 3. Retrieve all female customers (`CUST_GENDER = 'F'`) living in Sydney
-- SELECT  CUST_GENDER , CUST_CITY FROM SH.CUSTOMERS WHERE CUST_GENDER = 'F' AND CUST_CITY = 'Sydney' ;

-- 4. Find customers with income level `"G: 130,000 - 149,999"`.
-- SELECT CUST_INCOME_LEVEL FROM SH.CUSTOMERS WHERE CUST_INCOME_LEVEL='G: 130,000 - 149,999';

--5. Get all customers with a credit limit above 10,000.
-- SELECT CUST_CREDIT_LIMIT FROM SH.CUSTOMERS WHERE CUST_CREDIT_LIMIT > 10000;

-- 6. Retrieve customers from the state "California".
-- SELECT CUST_STATE_PROVINCE FROM SH.CUSTOMERS WHERE CUST_STATE_PROVINCE = 'California' ;

-- 7. Find customers who have provided an email address.
-- SELECT CUST_ID,CUST_EMAIL FROM SH.CUSTOMERS WHERE CUST_EMAIL IS NOT NULL

--8. List customers with missing marital status.
--  SELECT CUST_MARITAL_STATUS FROM SH.CUSTOMERS WHERE CUST_MARITAL_STATUS = NULL

--9. Find customers whose postal code starts with "53".
-- SELECT CUST_POSTAL_CODE FROM SH.CUSTOMERS WHERE CUST_POSTAL_CODE LIKE '53%' ;

--10. Get customers born before 1980 with a credit limit above 5,000.
--SELECT CUST_ID,CUST_YEAR_OF_BIRTH,CUST_CREDIT_LIMIT FROM SH.customers WHERE CUST_YEAR_OF_BIRTH < 1980 AND CUST_CREDIT_LIMIT > 5000

--11. Retrieve customers from Almere or Amersfoort.
--SELECT CUST_ID,CUST_CITY FROM SH.CUSTOMERS WHERE CUST_CITY = 'Almere' OR CUST_CITY = 'Amersfoort'

--12. Find customers who do not have a credit limit
--SELECT CUST_ID,CUST_CREDIT_LIMIT FROM SH.CUSTOMERS WHERE CUST_CREDIT_LIMIT IS  NULL

--13. List customers whose phone number starts with "487".
-- SELECT CUST_MAIN_PHONE_NUMBER FROM SH.CUSTOMERS WHERE CUST_MAIN_PHONE_NUMBER LIKE '487%' 

--14. Find married customers with income level `"Medium"`.
-- SELECT CUST_MARITAL_STATUS,CUST_INCOME_LEVEL FROM SH.CUSTOMERS WHERE CUST_INCOME_LEVEL = 'Medium'

--15. Get customers whose last name starts with "G".
--SELECT CUST_ID, CUST_LAST_NAME FROM SH.CUSTOMERS WHERE CUST_LAST_NAME LIKE 'G%'


--16. Find customers with city_id = 51057.
--SELECT CUST_CITY_ID FROM SH.CUSTOMERS WHERE CUST_CITY_ID = '51057'

--17.Retrieve all customers who are valid (`CUST_VALID = 'A'`).
--SELECT CUST_ID,CUST_VALID FROM SH.CUSTOMERS WHERE CUST_VALID = 'A'

--18. Find customers whose effective start date (`CUST_EFF_FROM`) is after 2020.
--SELECT CUST_ID,CUST_EFF_FROM FROM SH.CUSTOMERS --WHERE CUST_EFF_FROM > year '2020'

--19. Retrieve customers whose effective end date (`CUST_EFF_TO`) is before 2021.
--SELECT CUST_ID,CUST_EFF_TO FROM SH.CUSTOMERS WHERE CUST_EFF_TO < DATE '2021';

--20. Find customers with credit limit between 5,000 and 9,000.
--SELECT CUST_ID,CUST_CREDIT_LIMIT FROM SH.CUSTOMERS WHERE CUST_CREDIT_LIMIT BETWEEN 5000 and 9000

--21. Get all customers from country_id = 101.
--SELECT CUST_ID,COUNTRY_ID FROM SH.CUSTOMERS WHERE COUNTRY_ID = '101'

--22. Find customers whose email ends with `"@company.example.com"`.
--SELECT CUST_ID,CUST_EMAIL FROM SH.CUSTOMERS WHERE CUST_EMAIL LIKE '%@company.example.com'

--23. List customers with `CUST_TOTAL_ID = 52772`.
--SELECT CUST_ID,CUST_TOTAL_ID FROM SH.CUSTOMERS WHERE CUST_TOTAL_ID = '52772'

--24. Find customers with `CUST_SRC_ID` in (10, 20, 30).
--SELECT CUST_ID,CUST_SRC_ID FROM SH.CUSTOMERS WHERE CUST_SRC_ID in (10, 20, 30)

--25. Retrieve customers who either do not have email or do not have a credit limit.
-- SELECT CUST_ID,CUST_EMAIL,CUST_CREDIT_LIMIT FROM SH.CUSTOMERS WHERE CUST_EMAIL IS NULL AND CUST_CREDIT_LIMIT IS NULL