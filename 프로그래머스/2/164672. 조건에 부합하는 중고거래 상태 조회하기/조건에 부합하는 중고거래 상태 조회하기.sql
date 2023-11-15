-- 코드를 입력하세요
SELECT board.BOARD_ID,board.WRITER_ID,board.TITLE,board.PRICE,
case board.status 
when "SALE" then "판매중" 
when "RESERVED" then "예약중"
when "DONE" then "거래완료" end STATUS

from USED_GOODS_BOARD board
where created_date like "2022-10-05%"
order by board.board_id desc