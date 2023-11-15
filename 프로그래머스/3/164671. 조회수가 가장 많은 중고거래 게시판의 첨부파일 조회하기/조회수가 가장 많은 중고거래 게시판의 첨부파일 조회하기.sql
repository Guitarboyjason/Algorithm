-- 코드를 입력하세요
SELECT concat("/home/grep/src/",board.board_id,"/",file.file_id,file.file_name,file.file_ext) as FILE_PATH from 
USED_GOODS_BOARD board join USED_GOODS_FILE file
on board.board_id = file.board_id
where board.views = (
    select max(views) from USED_GOODS_BOARD
)
order by file.file_id desc