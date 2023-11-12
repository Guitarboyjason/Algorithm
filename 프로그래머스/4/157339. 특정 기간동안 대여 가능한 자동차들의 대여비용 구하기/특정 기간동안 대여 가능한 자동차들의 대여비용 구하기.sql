-- 코드를 입력하세요

-- 대여중인 자동차 : CAR_RENTAL_COMPANY_CAR
-- 세단, suv, 승합차, 트럭, 리무진 옵션들이 있다.
-- 자동차 대여 기록 정보 : CAR_RENTAL_COMPANY_RENTAL_HISTORY
-- 자동차 종류 별 대여 기간, 종류별 할인 정책 정보 : CAR_RENTAL_COMPANY_DISCOUNT_PLAN
-- 할인율이 적용되는 대여 기간 종류 : 7일 이상, 30일 이상, 90일 이상

-- 자동차 종류가 세단, suv 중 11월 1일부터 11월 30일까지 대여 가능, 30일간의 대여 금액이 50~ 200인 자동차에 대해 [자동차 ID, 자동차 종류, 대여금액] 을 출력하는 SQL
-- 대여 금액을 기준 내림차순, 같은 경우 자동차 종류를 기준 오름차순, 같은 경우 자동차 ID를 기준 내림차순

-- car type은 출력할 필요 없음
-- start_date와 end_date를 확인하고 얘네에서 한번 걸러보자

# select distinct sub.car_id CAR_ID,sub.car_type CAR_TYPE, discount.discount_rate * sub.daily_fee*30 FEE
# from 
# (
#     SELECT car.car_id,car.car_type,car.DAILY_FEE,history.history_id,history.START_DATE,history.end_date
# from car_rental_company_car car, CAR_RENTAL_COMPANY_RENTAL_HISTORY history
# where car.car_id = history.car_id
#  and (datediff(history.start_date, "2022-11-30") > 0)
#  or (datediff(history.end_date, "2022-11-01") < 0)
# ) sub
# , CAR_RENTAL_COMPANY_DISCOUNT_PLAN discount
# where discount.car_type = sub.car_type 
# and discount.discount_rate * sub.daily_fee*30 < 2000000
# and discount.discount_rate * sub.daily_fee*30 >=500000
# order by discount.discount_rate * sub.daily_fee*30 desc,CAR_TYPE,CAR_ID desc


# select datediff(start_date, "2022-11-30") from CAR_RENTAL_COMPANY_RENTAL_HISTORY

-- not in으로 해당 기간에 사용할 수 없는 애들을 걸러내자
# TODO
select subsubsub.car_id CAR_ID, subsubsub.car_type CAR_TYPE, floor(subsubsub.FEE) FEE  from(
select * ,subsub.daily_fee * (100-subsub.discount_rate) / 100 * 30 FEE  from 
(
select distinct sub.car_id, sub.car_type, sub.daily_fee,discount.discount_rate ,discount.duration_type from 
(
SELECT distinct car.car_id,car.car_type,car.DAILY_FEE,history.history_id,history.START_DATE,history.end_date
from car_rental_company_car car, CAR_RENTAL_COMPANY_RENTAL_HISTORY history
where car.car_id = history.car_id
and car.car_id not in
(select 
        car_id
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where
    datediff(start_date, "2022-11-30") *
    datediff(end_date, "2022-11-01") <=0
) 

    ) sub, 
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN discount
    where sub.car_type = discount.car_type
    and discount.duration_type like "3%"
    ) subsub) subsubsub
    # where subsub.daily_fee * (100-subsub.discount_rate) * 100
where subsubsub.FEE >= 500000
and subsubsub.FEE < 2000000
order by subsubsub.FEE desc, subsubsub.car_type, subsubsub.car_id desc

# select car_id
# from 
# select 
#         car_id, start_date ,end_date
#         from CAR_RENTAL_COMPANY_RENTAL_HISTORY
#         where
#     datediff(start_date, "2022-11-30") *
#     datediff(end_date, "2022-11-01") <=0