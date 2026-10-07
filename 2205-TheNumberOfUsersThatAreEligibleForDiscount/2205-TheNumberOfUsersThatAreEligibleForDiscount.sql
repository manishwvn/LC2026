-- Last updated: 10/7/2026, 2:50:22 PM
CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
BEGIN
  RETURN (
      SELECT
        COUNT(DISTINCT USER_ID) AS user_cnt
      FROM
        PURCHASES P
      WHERE
        (time_stamp BETWEEN startDate AND endDate)
        AND
        AMOUNT >= minAmount
      
  );
END