-- 코드를 입력하세요
SELECT COUNT(*)
from USER_INFO
where DATE_FORMAT(JOINED,'%Y')='2021' and
AGE <=29 and AGE >=20;