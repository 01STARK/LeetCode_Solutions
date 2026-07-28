select a.id
from Weather a left join Weather b on a.recordDate = DATE_ADD(b.recordDate, INTERVAL
1 DAY) where a.temperature > b.temperature