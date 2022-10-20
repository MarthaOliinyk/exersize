use exersize;

#role
SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE role;

SET FOREIGN_KEY_CHECKS = 1;

insert into role (name) value ('User');
insert into role (name) value ('Admin');
insert into role (name) value ('Trainer');

#user
SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE user;

SET FOREIGN_KEY_CHECKS = 1;

insert into user(email, password, username, registration_date, role_id) values ('dmytro.sliusarchuk.kn.2021@lpnu.ua','test1111','Dmytro Sliusarchuck','2022-08-26',1);
insert into user(email, password, username, registration_date, role_id) values ('denys.tykhonov.kn.2021@lpnu.ua','test2222','Denys Tykhonov','2022-07-05',1);
insert into user(email, password, username, registration_date, role_id) values ('sofiia.tkach.kn.2021@lpnu.ua','test3333','Sofiia Tkach','2022-04-21',1);
insert into user(email, password, username, registration_date, role_id) values ('ivan.dobrodieiev.kn.2021@lpnu.ua','test4444','Ivan Dobrodieiev','2022-05-01',1);
insert into user(email, password, username, registration_date, role_id) values ('yaroslav.makarovskyi.kn.2021@lpnu.ua','test5555','Yaroslav Makarovskyi','2022-02-07',1);
insert into user(email, password, username, registration_date, role_id) values ('marta.oliinyk.kn.2021@lpnu.ua','test6666','Marta Oliinyk','2022-08-26',1);
insert into user(email, password, username, registration_date, role_id) values ('olivia.smith@gmail.com','test1111','Olivia Smith','2022-09-09',1);
insert into user(email, password, username, registration_date, role_id) values ('tom.brown@gmail.com','test7777','Tom Brown','2022-01-01',1);
insert into user(email, password, username, registration_date, role_id) values ('bob.jhones@gmail.com','test8888','Bob Jhones','2022-01-21',1);
insert into user(email, password, username, registration_date, role_id) values ('lily.king@gmail.com','test9999','Lily King','2022-04-01',1);
insert into user(email, password, username, registration_date, role_id) values ('petro2001@gmail.com','test10101010','Perto2001','2022-06-30',1);
insert into user(email, password, username, registration_date, role_id) values ('marta.harris@gmail.com','qwerty1111','Marta Harris','2022-03-24',1);
insert into user(email, password, username, registration_date, role_id) values ('maria.fox@gmail.com','qwerty2222','Fox4789','2022-05-07',1);
insert into user(email, password, username, registration_date, role_id) values ('oliviablue789@gmail.com','qwerty3333','Olivia Blue','2022-05-30',1);
insert into user(email, password, username, registration_date, role_id) values ('jessica.lee@gmail.com','qwerty4444','Jessica Lee','2022-03-12',1);

insert into user(email, password, username, registration_date, role_id) values ('tom14567@gmail.com','admin1','Tom Admin','2022-02-07',2);
insert into user(email, password, username, registration_date, role_id) values ('walker123@gmail.com','admin2','Emily Walker','2022-03-09',2);
insert into user(email, password, username, registration_date, role_id) values ('clarke100@gmail.com','admin3','Clarke Griffin','2022-05-12',2);

insert into user(email, password, username, registration_date, role_id) values ('marta.blue24@gmail.com','zxcv1111','Marta Blue','2022-04-07',3);
insert into user(email, password, username, registration_date, role_id) values ('tomlee12@gmail.com','zxcv2222','Tom Lee','2022-06-13',3);
insert into user(email, password, username, registration_date, role_id) values ('petroking789@gmail.com','zxcv3333','Perto King','2022-05-14',3);
insert into user(email, password, username, registration_date, role_id) values ('white413@gmail.com','zxcv4444','Dmytro White','2022-08-18',3);
insert into user(email, password, username, registration_date, role_id) values ('denystlr200@gmail.com','zxcv5555','Denys Taylor','2022-04-17',3);
insert into user(email, password, username, registration_date, role_id) values ('ivanedw56@gmail.com','zxcv6666','Ivan Edwards','2022-01-12',3);
insert into user(email, password, username, registration_date, role_id) values ('coopersoffi@gmail.com','zxcv7777','Sofiia Cooper','2022-01-15',3);

#course
SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE course;

SET FOREIGN_KEY_CHECKS = 1;

insert into course(name, description, tag) values ('Super fitness', 'Really cool course', 'fitness');
insert into course(name, description, tag) values ('Box', 'Really cool course', 'box');
insert into course(name, description, tag) values ('Professional karate', 'Really cool course', 'karate');
insert into course(name, description, tag) values ('Relaxing yoga', 'Really cool course', 'yoga');
insert into course(name, description, tag) values ('Strength training', 'Really cool course', 'strength training');
insert into course(name, description, tag) values ('Super pilates', 'Really cool course', 'pilates');
insert into course(name, description, tag) values ('Fitness', 'Really cool course', 'fitness');
insert into course(name, description, tag) values ('Basic box', 'Really cool course', 'box');
insert into course(name, description, tag) values ('Karate', 'Really cool course', 'karate');
insert into course(name, description, tag) values ('Yoga', 'Really cool course', 'yoga');
insert into course(name, description, tag) values ('Professional strength training', 'Really cool course', 'strength training');
insert into course(name, description, tag) values ('Pilates', 'Really cool course', 'pilates');
insert into course(name, description, tag) values ('Streching', 'Really cool course', 'stretching');
insert into course(name, description, tag) values ('Aerobics', 'Really cool course', 'aerobics');

#subscription_type
SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE subscription_type;

SET FOREIGN_KEY_CHECKS = 1;

insert into subscription_type(session_count, duration, price, course_id) values (8, 30, 19.99, 1);
insert into subscription_type(session_count, duration, price, course_id) values (1, 7, 1.99, 1);
insert into subscription_type(session_count, duration, price, course_id) values (24, 90, 49.99, 1);
insert into subscription_type(session_count, duration, price, course_id) values (96, 365, 199.99, 1);

insert into subscription_type(session_count, duration, price, course_id) values (8, 30, 39.99, 2);
insert into subscription_type(session_count, duration, price, course_id) values (1, 7, 4.99, 2);
insert into subscription_type(session_count, duration, price, course_id) values (24, 90, 99.99, 2);

insert into subscription_type(session_count, duration, price, course_id) values (8, 30, 49.99, 3);

insert into subscription_type(session_count, duration, price, course_id) values (8, 30, 9.99, 4);
insert into subscription_type(session_count, duration, price, course_id) values (1, 7, 0.99, 4);
insert into subscription_type(session_count, duration, price, course_id) values (96, 365, 99.99, 4);

insert into subscription_type(session_count, duration, price, course_id) values (8, 30, 19.99, 5);
insert into subscription_type(session_count, duration, price, course_id) values (1, 7, 1.99, 5);
insert into subscription_type(session_count, duration, price, course_id) values (24, 90, 49.99, 5);

insert into subscription_type(session_count, duration, price, course_id) values (8, 30, 29.99, 6);
insert into subscription_type(session_count, duration, price, course_id) values (1, 7, 2.99, 6);

insert into subscription_type(session_count, duration, price, course_id) values (8, 30, 14.99, 7);
insert into subscription_type(session_count, duration, price, course_id) values (1, 7, 1.99, 7);
insert into subscription_type(session_count, duration, price, course_id) values (24, 90, 39.99, 7);

insert into subscription_type(session_count, duration, price, course_id) values (8, 30, 39.99, 8);
insert into subscription_type(session_count, duration, price, course_id) values (1, 7, 4.99, 8);
insert into subscription_type(session_count, duration, price, course_id) values (24, 90, 99.99, 8);
insert into subscription_type(session_count, duration, price, course_id) values (96, 365, 399.99, 8);

insert into subscription_type(session_count, duration, price, course_id) values (8, 30, 24.99, 9);
insert into subscription_type(session_count, duration, price, course_id) values (1, 7, 3.99, 9);
insert into subscription_type(session_count, duration, price, course_id) values (24, 90, 79.99, 9);

insert into subscription_type(session_count, duration, price, course_id) values (8, 30, 9.99, 10);
insert into subscription_type(session_count, duration, price, course_id) values (1, 7, 0.99, 10);
insert into subscription_type(session_count, duration, price, course_id) values (24, 90, 19.99, 10);

insert into subscription_type(session_count, duration, price, course_id) values (8, 30, 24.99, 11);
insert into subscription_type(session_count, duration, price, course_id) values (96, 365, 299.99, 11);
insert into subscription_type(session_count, duration, price, course_id) values (24, 90, 49.99, 11);

insert into subscription_type(session_count, duration, price, course_id) values (8, 30, 19.99, 12);
insert into subscription_type(session_count, duration, price, course_id) values (96, 365, 149.99, 12);
insert into subscription_type(session_count, duration, price, course_id) values (24, 90, 49.99, 12);

insert into subscription_type(session_count, duration, price, course_id) values (8, 30, 14.99, 13);
insert into subscription_type(session_count, duration, price, course_id) values (96, 365, 99.99, 13);
insert into subscription_type(session_count, duration, price, course_id) values (24, 90, 29.99, 13);

insert into subscription_type(session_count, duration, price, course_id) values (8, 30, 9.99, 14);
insert into subscription_type(session_count, duration, price, course_id) values (1, 7, 1.99, 14);
insert into subscription_type(session_count, duration, price, course_id) values (24, 90, 24.99, 14);


#user_has_course
SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE user_has_course;

SET FOREIGN_KEY_CHECKS = 1;

insert into user_has_course(user_id, course_id) values (1, 1);
insert into user_has_course(user_id, course_id) values (1, 4);
insert into user_has_course(user_id, course_id) values (1, 11);

insert into user_has_course(user_id, course_id) values (2, 5);

insert into user_has_course(user_id, course_id) values (3, 2);
insert into user_has_course(user_id, course_id) values (3, 3);

insert into user_has_course(user_id, course_id) values (4, 7);

insert into user_has_course(user_id, course_id) values (5, 8);
insert into user_has_course(user_id, course_id) values (5, 10);

insert into user_has_course(user_id, course_id) values (6, 9);

insert into user_has_course(user_id, course_id) values (7, 12);
insert into user_has_course(user_id, course_id) values (7, 1);

insert into user_has_course(user_id, course_id) values (8, 14);

insert into user_has_course(user_id, course_id) values (9, 4);

insert into user_has_course(user_id, course_id) values (10, 13);

insert into user_has_course(user_id, course_id) values (11, 9);
insert into user_has_course(user_id, course_id) values (11, 12);
insert into user_has_course(user_id, course_id) values (11, 1);

insert into user_has_course(user_id, course_id) values (12, 4);

insert into user_has_course(user_id, course_id) values (13, 6);

insert into user_has_course(user_id, course_id) values (14, 1);

insert into user_has_course(user_id, course_id) values (15, 7);

insert into user_has_course(user_id, course_id) values (19, 1);
insert into user_has_course(user_id, course_id) values (19, 7);

insert into user_has_course(user_id, course_id) values (20, 2);
insert into user_has_course(user_id, course_id) values (20, 6);

insert into user_has_course(user_id, course_id) values (21, 3);
insert into user_has_course(user_id, course_id) values (21, 4);

insert into user_has_course(user_id, course_id) values (22, 14);
insert into user_has_course(user_id, course_id) values (22, 8);
insert into user_has_course(user_id, course_id) values (22, 9);

insert into user_has_course(user_id, course_id) values (23, 10);
insert into user_has_course(user_id, course_id) values (23, 13);

insert into user_has_course(user_id, course_id) values (24, 11);

insert into user_has_course(user_id, course_id) values (25, 12);


#subscription
SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE subscription;

SET FOREIGN_KEY_CHECKS = 1;

insert into subscription(start, end, user_id, subscription_type_id) values ('2022-09-20', '2022-10-20', 1, 1);
insert into subscription(start, end, user_id, subscription_type_id) values ('2022-09-30', '2022-10-07', 1, 10);
insert into subscription(start, end, user_id, subscription_type_id) values ('2022-09-20', '2023-09-20', 1, 31);

insert into subscription(start, end, user_id, subscription_type_id) values ('2022-09-24', '2022-12-24', 2, 14);

insert into subscription(start, end, user_id, subscription_type_id) values ('2022-10-5', '2022-10-12', 3, 6);
insert into subscription(start, end, user_id, subscription_type_id) values ('2022-09-27', '2022-10-27', 3, 8);

insert into subscription(start, end, user_id, subscription_type_id) values ('2022-09-25', '2022-10-25', 4, 17);

insert into subscription(start, end, user_id, subscription_type_id) values ('2022-09-30', '2022-12-30', 5, 22);
insert into subscription(start, end, user_id, subscription_type_id) values ('2022-10-10', '2022-10-17', 5, 28);

insert into subscription(start, end, user_id, subscription_type_id) values ('2022-11-20', '2022-12-20', 6, 24);

insert into subscription(start, end, user_id, subscription_type_id) values ('2022-09-23', '2022-9-30', 7, 2);
insert into subscription(start, end, user_id, subscription_type_id) values ('2022-07-05', '2023-07-05', 7, 34);

insert into subscription(start, end, user_id, subscription_type_id) values ('2022-09-21', '2022-10-21', 8, 39);

insert into subscription(start, end, user_id, subscription_type_id) values ('2022-07-20', '2022-08-20', 9, 9);
insert into subscription(start, end, user_id, subscription_type_id) values ('2022-08-11', '2023-08-11', 9, 11);

insert into subscription(start, end, user_id, subscription_type_id) values ('2022-09-05', '2022-10-05', 10, 36);

insert into subscription(start, end, user_id, subscription_type_id) values ('2022-10-08', '2022-10-15', 11, 25);
insert into subscription(start, end, user_id, subscription_type_id) values ('2022-09-07', '2023-10-07', 11, 34);
insert into subscription(start, end, user_id, subscription_type_id) values ('2022-10-10', '2022-11-10', 11, 1);

insert into subscription(start, end, user_id, subscription_type_id) values ('2022-10-20', '2023-10-20', 12, 11);
insert into subscription(start, end, user_id, subscription_type_id) values ('2022-09-27', '2022-10-27', 12, 9);

insert into subscription(start, end, user_id, subscription_type_id) values ('2022-12-11', '2022-12-18', 13, 16);

insert into subscription(start, end, user_id, subscription_type_id) values ('2022-08-05', '2022-11-05', 14, 3);

insert into subscription(start, end, user_id, subscription_type_id) values ('2022-11-15', '2022-11-22', 15, 18);


#schedule
SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE schedule;

SET FOREIGN_KEY_CHECKS = 1;

insert into schedule(start, end, participants, course_id) values ('2022-11-15 13', '2022-11-15 18', 15, 1);
insert into schedule(start, end, participants, course_id) values ('2022-11-18 13', '2022-11-18 18', 10, 1);

insert into schedule(start, end, participants, course_id) values ('2022-10-14 12', '2022-10-14 18', 5, 2);
insert into schedule(start, end, participants, course_id) values ('2022-10-9 13', '2022-10-9 17', 15, 2);

insert into schedule(start, end, participants, course_id) values ('2022-10-17 13', '2022-10-17 17', 1, 3);
insert into schedule(start, end, participants, course_id) values ('2022-10-10 11', '2022-10-10 16', 1, 3);

insert into schedule(start, end, participants, course_id) values ('2022-10-15 14', '2022-10-15 18', 10, 4);

insert into schedule(start, end, participants, course_id) values ('2022-10-5 10', '2022-10-5 17', 15, 5);
insert into schedule(start, end, participants, course_id) values ('2022-10-9 13', '2022-10-9 18', 10, 5);

insert into schedule(start, end, participants, course_id) values ('2022-10-12 9', '2022-10-12 15', 15, 6);
insert into schedule(start, end, participants, course_id) values ('2022-10-17 14', '2022-10-17 18', 5, 6);
insert into schedule(start, end, participants, course_id) values ('2022-10-19 13', '2022-10-19 15', 15, 6);

insert into schedule(start, end, participants, course_id) values ('2022-10-20 14', '2022-10-20 19', 10, 7);
insert into schedule(start, end, participants, course_id) values ('2022-10-25 10', '2022-10-25 15', 15, 7);

insert into schedule(start, end, participants, course_id) values ('2022-10-04 15', '2022-10-04 18', 1, 8);
insert into schedule(start, end, participants, course_id) values ('2022-10-10 11', '2022-10-10 19', 1, 8);

insert into schedule(start, end, participants, course_id) values ('2022-10-11 13', '2022-10-11 18', 3, 9);
insert into schedule(start, end, participants, course_id) values ('2022-10-07 11', '2022-10-07 17', 3, 9);

insert into schedule(start, end, participants, course_id) values ('2022-10-24 10', '2022-10-24 14', 10, 10);
insert into schedule(start, end, participants, course_id) values ('2022-10-26 9', '2022-10-26 15', 5, 10);

insert into schedule(start, end, participants, course_id) values ('2022-10-17 11', '2022-10-17 19', 15, 11);
insert into schedule(start, end, participants, course_id) values ('2022-10-19 15', '2022-10-19 17', 15, 11);

insert into schedule(start, end, participants, course_id) values ('2022-10-27 16', '2022-10-27 20', 10, 12);
insert into schedule(start, end, participants, course_id) values ('2022-10-20 13', '2022-10-20 17', 10, 12);

insert into schedule(start, end, participants, course_id) values ('2022-10-21 10', '2022-10-21 17', 5, 13);

insert into schedule(start, end, participants, course_id) values ('2022-10-30 11', '2022-10-30 15', 15, 14);
insert into schedule(start, end, participants, course_id) values ('2022-10-25 12', '2022-10-25 16', 10, 14);
insert into schedule(start, end, participants, course_id) values ('2022-10-20 13', '2022-10-20 15', 5, 14);


#appointment
SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE appointment;

SET FOREIGN_KEY_CHECKS = 1;

insert into appointment(time, schedule_id, user_id) values ('2022-10-18 14', 2, 1);
insert into appointment(time, schedule_id, user_id) values ('2022-10-19 15', 22, 1);
insert into appointment(time, schedule_id, user_id) values ('2022-10-15 14', 7, 1);

insert into appointment(time, schedule_id, user_id) values ('2022-10-09 14', 9, 2);
insert into appointment(time, schedule_id, user_id) values ('2022-10-05 11', 8, 2);

insert into appointment(time, schedule_id, user_id) values ('2022-10-10 12', 6, 3);
insert into appointment(time, schedule_id, user_id) values ('2022-10-14 14', 3, 3);

insert into appointment(time, schedule_id, user_id) values ('2022-10-20 15', 13, 4);

insert into appointment(time, schedule_id, user_id) values ('2022-10-10 12', 16, 5);
insert into appointment(time, schedule_id, user_id) values ('2022-10-26 10', 20, 5);

insert into appointment(time, schedule_id, user_id) values ('2022-10-11 14', 17, 6);

insert into appointment(time, schedule_id, user_id) values ('2022-10-18 14', 2, 7);
insert into appointment(time, schedule_id, user_id) values ('2022-10-15 15', 1, 7);

insert into appointment(time, schedule_id, user_id) values ('2022-10-20 13', 28, 8);
insert into appointment(time, schedule_id, user_id) values ('2022-10-25 14', 27, 8);

insert into appointment(time, schedule_id, user_id) values ('2022-10-15 14', 7, 9);

insert into appointment(time, schedule_id, user_id) values ('2022-10-21 11', 25, 10);

insert into appointment(time, schedule_id, user_id) values ('2022-10-15 15', 1, 11);
insert into appointment(time, schedule_id, user_id) values ('2022-10-18 14', 2, 11);
insert into appointment(time, schedule_id, user_id) values ('2022-10-11 14', 17, 11);

insert into appointment(time, schedule_id, user_id) values ('2022-10-15 14', 7, 12);

insert into appointment(time, schedule_id, user_id) values ('2022-10-17 14', 11, 13);
insert into appointment(time, schedule_id, user_id) values ('2022-10-12 11', 10, 13);

insert into appointment(time, schedule_id, user_id) values ('2022-10-18 15', 1, 14);
insert into appointment(time, schedule_id, user_id) values ('2022-10-18 14', 2, 14);

insert into appointment(time, schedule_id, user_id) values ('2022-10-25 12', 14, 15);





