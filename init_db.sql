CREATE TABLE orders (id INTEGER PRIMARY KEY, data TEXT);
CREATE TABLE feedbacks (id INTEGER PRIMARY KEY, data TEXT);
CREATE TABLE goods (id INTEGER PRIMARY KEY, data TEXT);

INSERT INTO goods (data) VALUES ('{"id": 1, "name": "Кофе американо", "price": 150, "category": "напитки", "in_stock": true}');
INSERT INTO goods (data) VALUES ('{"id": 2, "name": "Капучино", "price": 180, "category": "напитки", "in_stock": true}');
INSERT INTO goods (data) VALUES ('{"id": 3, "name": "Круассан", "price": 120, "category": "выпечка", "in_stock": true}');
INSERT INTO goods (data) VALUES ('{"id": 4, "name": "Сэндвич с курицей", "price": 220, "category": "закуски", "in_stock": false}');
INSERT INTO goods (data) VALUES ('{"id": 5, "name": "Салат Цезарь", "price": 280, "category": "закуски", "in_stock": true}');
INSERT INTO goods (data) VALUES ('{"id": 6, "name": "Минеральная вода", "price": 90, "category": "напитки", "in_stock": true}');
INSERT INTO goods (data) VALUES ('{"id": 7, "name": "Чизкейк", "price": 200, "category": "десерты", "in_stock": true}');
