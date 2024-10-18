-- Create a function SafeDiv to divide two numbers safely
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
    RETURN IF(b = 0, 0, a / b);
END//

DELIMITER ;
