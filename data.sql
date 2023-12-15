INSERT INTO iot_db.user (`username`, `email`)
VALUES
    ('John', 'john@mail.com'),
    ('Jane', 'jane@mail.com'),
    ('David', 'david@mail.com'),
    ('Emily', 'emily@mail.com'),
    ('Michael', 'michael@mail.com');

-- Insert data into `reservation`.`address` table
INSERT INTO iot_db.nitro_boost (`duration`, `user_id`)
VALUES
    ('2023-01-01 12:00:00', 1),
    ('2023-01-01 12:10:00', 2),
    ('2023-01-01 12:20:00', 3),
    ('2023-01-01 12:30:00', 4),
    ('2023-01-01 12:40:00', 5);

-- Insert data into `reservation`.`property_stats` table
INSERT INTO iot_db.channel (`name`, `members`)
VALUES
    ('name1', 10),
    ('name2', 15),
    ('name3', 20),
    ('name4', 25),
    ('name5', 30);

-- Insert data into `reservation`.`property` table
INSERT INTO iot_db.voice_chat (`name`, `channel_id`)
VALUES
    ('voice1', 1),
    ('voice2', 2),
    ('voice3', 3),
    ('voice4', 4),
    ('voice5', 5);

-- Insert data into `reservation`.`reviews` table
INSERT INTO iot_db.text_chat (`name`, `channel_id`)
VALUES
    ('Great property!',  1),
    ('Perfect stay!',  2),
    ('Nice place.', 3),
    ('Excellent service.', 4),
    ('Good experience.', 5);

-- Insert data into `reservation`.`people_photos` table
INSERT INTO iot_db.audio_message (`audio_message_path`, `sender`, `text_chat_id`)
VALUES
    ('src/music1.mp3', 1, 1),
    ('src/music2.mp3', 2, 2),
    ('src/music3.mp3', 3, 3),
    ('src/music4.mp3', 4, 4),
    ('src/music5.mp3', 5, 5);

-- Insert data into `reservation`.`reservation_time` table
INSERT INTO iot_db.photo_message (`photo_message_path`, `sender`, `text_chat_id`)
VALUES
    ('src/image1.jpeg', 1, 1),
    ('src/image2.jpeg', 2, 2),
    ('src/image3.jpeg', 3, 3),
    ('src/image4.jpeg', 4, 4),
    ('src/image5.jpeg', 5, 5);

-- Insert data into `reservation`.`reservations` table
INSERT INTO iot_db.text_message (`text`, `sender`, `text_chat_id`)
VALUES
    ('example 1 ', 1, 1),
    ('example 2', 2, 2),
    ('example 3', 3, 3),
    ('example 4', 4, 4),
    ('example 5', 5, 5);

-- Insert data into `reservation`.`bank_accounts` table
INSERT INTO iot_db.permission_list (`is_administrator`, `creating_roles_permission`, `voice_chat_editing_permission`,
                                      `text_chat_editing_permission`)
VALUES
    ( 1, 1, 1, 1),
    ( 0, 0, 0 , 0),
    ( 1, 0, 1 ,0),
    ( 1, 0, 1 ,0),
    ( 1, 1, 0, 0);

-- Insert data into `reservation`.`property_has_reservations` table
INSERT INTO iot_db.role (`name`, `channel_id`, `permission_list_id`, `user_id`)
VALUES
    ( 'role1', 1, 1, 1 ),
    ( 'role2', 2, 2, 2 ),
    ( 'role3', 3, 3, 3 ),
    ( 'role4', 4, 4, 4 ),
    ( 'role5', 5, 5, 5 );

