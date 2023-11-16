# -- 코드를 입력하세요

# with sale as (select car_type, REGEXP_REPLACE(duration_type ,"[ |가-훼]*",'') duration,discount_rate from CAR_RENTAL_COMPANY_DISCOUNT_PLAN )

# select * from sale 
# where car_type = "트럭" 
#  where duration = "90"

# SELECT history.history_id, datediff(history.end_date,history.start_date) * 
# case when datediff(history.end_date,history.start_date) >= 90 then (select discount_rate from sale where car_type "트럭", where duration = 90),history.start_date,history.end_date
# from 
# CAR_RENTAL_COMPANY_CAR car join CAR_RENTAL_COMPANY_RENTAL_HISTORY history
# join CAR_RENTAL_COMPANY_DISCOUNT_PLAN plan 
# on plan.car_type = car.car_type
# on car.car_id = history.car_id
# where car_type="트럭"

select sub.history_id,
case when duration_type is null then sub.price
else floor(sub.price * (1-plan.discount_rate/100)) end fee
# select sub.price
from 
(select history.history_id, car.daily_fee,history.start_date,history.end_date ,
case when (datediff(history.end_date,history.start_date)+1) >= 90 then '90일 이상'
when (datediff(history.end_date,history.start_date)+1) >= 30 then "30일 이상"
when (datediff(history.end_date,history.start_date)+1) >= 7 then "7일 이상"
else 'X' end length, 
(datediff(history.end_date,history.start_date)+1) * car.daily_fee price

from CAR_RENTAL_COMPANY_RENTAL_HISTORY history join CAR_RENTAL_COMPANY_CAR car 
on history.car_id = car.car_id
where car.car_type = '트럭' ) sub left outer join (
    select duration_type, discount_rate 
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    where CAR_TYPE = '트럭') plan
on sub.length = plan.DURATION_TYPE
order by fee desc, history_id desc
# and 
# where car_id in ( 
# select car_id from CAR_RENTAL_COMPANY_CAR 
# where car_type = "트럭"
# )