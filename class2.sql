select product_name,quantity_per_unit from products;
select product_name,id from products
 where discontinued = "false" 
 order by product_name;
 select product_name,list_price 
 from products order by product_name ;
 
 select product_name, list_price
 from products
where discontinued = 1 
order by product_name ;

select product_name,list_price 
from products order by list_price desc ;
select sum(quantity) as total_quantity from orderdetail;
 SELECT * FROM Product
WHERE unitPrice > (SELECT AVG(unitPrice) FROM Product);
