CREATE gramedia_db;

USE gramedia_db;

CREATE TABLE books_db(book_id INT NOT NULL AUTO_INCREMENT,
					title VARCHAR(50),
                    author_name VARCHAR(50),
                    released_year INT,
                    location VARCHAR(5),
                    stock_quantity INT,
                    price INT,
                    PRIMARY KEY(book_id));
                    
INSERT INTO books_db (title, author_name, released_year, location,  stock_quantity, price)
VALUES('Laut Bercerita', 'Leila S. Chudori', 2017, 'D-34',  16, 85000),
('Matematika Diskrit Revisi Enam', 'Rinaldi Munir', 2010, 'A-10', 4, 325000),
( 'We Are UI Family', 'Fauzhan M.S', 2011, 'A-11', 19, 30000),
('Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones', 'James Clear', 2018, 'C-01', 2, 78210),
('Rindu', 'Tere Liye', 2014, 'D-33', 6, 63000),
('Bumi', 'Tere Liye', 2014, 'D-32', 16, 81000),
('Bulan', 'Tere Liye', 2015, 'D-32', 16, 85000),
('Matahari', 'Tere Liye', 2016, 'D-32', 16, 90000),
('Bintang', 'Tere Liye', 2017, 'D-32', 16, 86000),
('Nebula', 'Tere Liye', 2020, 'D-32', 16, 92000),
('Lumpu', 'Tere Liye', 2020, 'D-32', 16, 87000),
('Komet', 'Tere Liye', 2018, 'D-32', 16, 93000),
('Komet Minor', 'Tere Liye', 2019, 'D-32', 16, 85000),
('Selana', 'Tere Liye', 2020, 'D-32', 16, 75000),
('Si Putih', 'Tere Liye', 2020, 'D-32', 16, 60000);
