orders:
	id		ordered_at		delivered_at		delivered_to
	
order_items
	id		order_id		name				amount_paid
	
select
  case name
    when 'kale-smoothie'    then 'smoothie'
    when 'banana-smoothie'  then 'smoothie'
    when 'orange-juice'     then 'drink'
    when 'soda'             then 'drink'
    when 'blt'              then 'sandwich'
    when 'grilled-cheese'   then 'sandwich'
    when 'tikka-masala'     then 'dinner'
    when 'chicken-parm'     then 'dinner'
    else 'other'
  end as category,
  round( 1.0*sum(amount_paid) / 
        (select sum(amount_paid) from order_items)*100, 2)
from order_items
group by 1
order by 2 desc;


# Recorder Rates
select 
	name, 
	round( 1.0*count(distinct orders.id) /
        count(distinct orders.delivered_to), 2) as recorder_rate
from order_items join orders
on orders.id = order_items.order_id
group by 1
order by 2 desc;