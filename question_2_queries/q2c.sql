select
  batter,
  (sum(batter_runs)*100.0) / (count(*)-sum(case when wides>0 then 1 else 0 end)) as strike_rate
from
  ball_by_ball
where match_year = 2023
group by
  batter
having
  sum(batter_runs) > 10
order by
  sum(batter_runs) desc
limit 5;
