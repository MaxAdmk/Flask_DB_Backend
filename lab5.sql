USE iot_db;

-- Створення таблиці VideoMessage
CREATE TABLE VideoMessage (
    id INT PRIMARY KEY AUTO_INCREMENT,
    video_message_path VARCHAR(400),
    sender INT,
    text_chat_id INT,
    CONSTRAINT fk_sender FOREIGN KEY (sender) REFERENCES iot_db.user(id),
    CONSTRAINT fk_text_chat FOREIGN KEY (text_chat_id) REFERENCES iot_db.text_chat(id)
);

DELIMITER //

CREATE TRIGGER before_insert_VideoMessage
BEFORE INSERT ON VideoMessage
FOR EACH ROW
BEGIN
    IF NEW.text_chat_id IS NOT NULL AND NOT EXISTS (SELECT 1 FROM text_chat WHERE id = NEW.text_chat_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Foreign key constraint failed: text_chat_id does not exist';
    END IF;
END;

//

DELIMITER ;

INSERT INTO VideoMessage(video_message_path, sender, text_chat_id)
VALUES ('./.', 2, 6)

DELIMITER //

-- Створення процедури для вставки значень у таблицю VideoMessage
CREATE PROCEDURE InsertVideoMessage(
    IN p_video_message_path VARCHAR(400),
    IN p_sender INT,
    IN p_text_chat_id INT
)
BEGIN
    -- Вставка нового запису
    INSERT INTO VideoMessage (video_message_path, sender, text_chat_id)
    VALUES (p_video_message_path, p_sender, p_text_chat_id);
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE InsertMultipleVideoMessages()
BEGIN
    DECLARE counter INT DEFAULT 1;

    WHILE counter <= 10 DO
        SET @video_message_path = CONCAT('Noname', counter);

        INSERT INTO VideoMessage (video_message_path, sender, text_chat_id)
        VALUES (@video_message_path, 1, 1);
        SET counter = counter + 1;
    END WHILE;
END //

DELIMITER ;

CALL InsertMultipleVideoMessages();

-- Створення користувацької функції
DELIMITER //

CREATE FUNCTION CalculateChannelStats(
    columnName VARCHAR(255),
    aggregateType VARCHAR(10)
)
RETURNS DOUBLE
NO SQL
BEGIN
    DECLARE result DOUBLE;

    CASE aggregateType
        WHEN 'MAX' THEN
            SELECT MAX(columnName) INTO result FROM iot_db.channel;
        WHEN 'MIN' THEN
            SELECT MIN(columnName) INTO result FROM iot_db.channel;
        WHEN 'SUM' THEN
            SELECT SUM(columnName) INTO result FROM iot_db.channel;
        WHEN 'AVG' THEN
            SELECT AVG(columnName) INTO result FROM iot_db.channel;
        ELSE
            SET result = 0; 
    END CASE;

    RETURN result;
END //

DELIMITER ;

SELECT CalculateChannelStats('members', 'MAX') AS max_members;
SELECT CalculateChannelStats('members', 'MIN') AS min_members;
SELECT CalculateChannelStats('members', 'SUM') AS sum_members;
SELECT CalculateChannelStats('members', 'AVG') AS avg_members;

DELIMITER //

CREATE PROCEDURE CopyDataWithTimestamp()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE tableName1 VARCHAR(255);
    DECLARE tableName2 VARCHAR(255);
    DECLARE cursorTable CURSOR FOR SELECT table_name FROM information_schema.tables WHERE table_schema = 'iot_db' AND table_type = 'BASE TABLE';
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cursorTable;

    read_loop: LOOP
        FETCH cursorTable INTO tableName1;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SET tableName2 = CONCAT(tableName1, '_', DATE_FORMAT(NOW(), '%Y%m%d%H%i%s'));

        SET @createTableQuery = CONCAT('CREATE TABLE ', tableName2, ' LIKE ', tableName1);
        PREPARE stmt FROM @createTableQuery;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

        SET @copyDataQuery = CONCAT('INSERT INTO ', tableName2, ' SELECT * FROM ', tableName1, ' ORDER BY RAND() LIMIT 1');
        PREPARE stmt FROM @copyDataQuery;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;

    CLOSE cursorTable;
END //

DELIMITER ;



CALL CopyDataWithTimestamp();

DELIMITER //

CREATE TRIGGER check_username
BEFORE INSERT ON user
FOR EACH ROW
BEGIN
    IF NEW.username NOT IN ('Svitlana', 'Petro', 'Olha', 'Taras') THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid username. Allowed values are: Svitlana, Petro, Olha, Taras';
    END IF;
END;

//

DELIMITER ;

DELIMITER //

CREATE TRIGGER check_email_suffix
BEFORE INSERT ON user
FOR EACH ROW
BEGIN
    IF NEW.email LIKE '%00' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid email suffix. It cannot end with two zeros.';
    END IF;
END;

//

DELIMITER ;

INSERT INTO iot_db.user (`username`, `email`)
VALUES
    ('llll', 'john@mail.com00');

DELIMITER //

CREATE TRIGGER prevent_delete_user_rows
BEFORE DELETE ON user
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deletion of rows from the user table is not allowed.';
END;

//

DELIMITER ;



