delimiter $$
CREATE TRIGGER after_transaction_insert
    AFTER INSERT ON `pfinancedb`.transaction
    FOR EACH ROW
    Begin
		DECLARE amount decimal(20,2);
        
		SELECT a.balance_total 
        into amount 
        FROM pfinancedb.trans_total_balance_view as a where a.idbalance=New.idbalance;
        
		UPDATE `pfinancedb`.`balance` as b
		SET
		b.`amount` = amount
		WHERE b.`id` = NEW.idbalance;
	end$$
delimiter ;

DROP TRIGGER after_transaction_insert;