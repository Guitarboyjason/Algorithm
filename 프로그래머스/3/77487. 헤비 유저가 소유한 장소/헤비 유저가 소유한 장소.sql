-- 코드를 입력하세요
-- 공간을 둘 이상 등록한 사람이 등록한 공간의 정보를 아이디 순
# SELECT id,name
# from PLACES
# group by host_id
# having count(*) >= 2

select * 
from places 
where host_id in (
select host_id
from places
group by host_id
having count(*) >= 2
) 
order by id