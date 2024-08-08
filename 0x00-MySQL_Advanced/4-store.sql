-- Creates a trigger that decreases the quantity
-- of an item after adding a new order.
-- L12: Drops trigger 'reduce_quantity'
-- L13: Defines delimiter as '$$'
-- L14 to L20: Creates trigger
-- L15: Specifies the trigger action.
-- L16: Begins trigger block.
-- L17: Updates 'quantity'
-- L18: Filters the 'items' table.
-- L21: Ends trigger block.
-- L22: Resets delimiter to ';'.
DROP TRIGGER IF EXISTS reduce_quantity;
DELIMITER $$
CREATE TRIGGER reduce_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
        SET quantity = quantity - NEW.number
        WHERE name = NEW.item_name;
END $$
DELIMITER ;
