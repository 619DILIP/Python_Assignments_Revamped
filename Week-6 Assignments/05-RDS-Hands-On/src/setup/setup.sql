-- Run this after connecting with psql to create and populate a starter table.
CREATE TABLE practice_orders (
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(100),
    quantity INT,
    price DECIMAL(10,2)
);

INSERT INTO practice_orders (item_name, quantity, price) VALUES
    ('Widget', 5, 12.50),
    ('Gadget', 2, 45.00),
    ('Gizmo', 10, 3.75);
