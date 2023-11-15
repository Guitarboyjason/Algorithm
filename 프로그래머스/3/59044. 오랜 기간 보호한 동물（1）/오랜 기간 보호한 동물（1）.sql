-- 코드를 입력하세요
# SELECT * 
# from animal_ins ins join animal_outs outs
# on ins.ANIMAL_ID = outs.ANIMAL_ID
# order by 

select name,datetime from animal_ins
where animal_id not in 
(
select animal_id from animal_outs
)
order by  datetime limit 3