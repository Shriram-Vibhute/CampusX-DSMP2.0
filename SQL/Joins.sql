select * 
from flipcart.users as users
inner join flipcart.orders as orders
on users.user_id = orders.user_id
inner join flipcart.order_details as order_details
on order_details.order_id = orders.order_id
inner join flipcart.category as category
on category.category_id = order_details.category_id;

-- Find all orders placed in pune
select * from flipcart.users as users
inner join flipcart.orders as orders
on users.user_id = orders.user_id
where users.city = 'pune';

-- Find all profitable orders
select orders.order_id, sum(od.amount) as profit from flipcart.users as users
inner join flipcart.orders as orders
on users.user_id = orders.user_id
inner join flipcart.order_details as od
on od.order_id = orders.order_id
group by orders.order_id
having sum(od.amount) > 0; 

-- Find the name of customer who has places max number of orders
select users.name, count(users.city) as ct from flipcart.users as users
inner join flipcart.orders as orders
on users.user_id = orders.user_id
group by users.user_id, users.name
order by ct desc
limit 1;