-- 코드를 입력하세요
SELECT a.FLAVOR FROM ICECREAM_INFO a
JOIN FIRST_HALF b ON b.FLAVOR = a.FLAVOR
WHERE a.INGREDIENT_TYPE = 'fruit_based' AND b.TOTAL_ORDER >3000
ORDER BY b.TOTAL_ORDER DESC