insert into ball_by_ball
select
  match_id,
  match_start_date,
  match_year,
  batting_team,
  over,
  delivery.value ->> 'batter' as batter,
  delivery.value ->> 'bowler' as bowler,
  delivery.value ->> 'non_striker' as non_striker,
  delivery.value -> 'runs' ->> 'batter' as batter_runs,
  delivery.value -> 'runs' ->> 'extras' as extra_runs,
  delivery.value -> 'runs' ->> 'total' as total_runs,
  delivery.value -> 'extras' ->> 'wides' as wides,
  current_timestamp
from
  (
    select
      match_id,
      match_start_date,
      match_year,
      batting_team,
      overs.value ->> 'over' as over,
      overs.value -> 'deliveries' as deliveries
    from
      (
        select
          match_id,
          info -> 'dates' ->> 0 as match_start_date,
          strftime('%Y', info -> 'dates' ->> 0) as match_year,
          innings.value ->> 'team' as batting_team,
          innings.value -> 'overs' as overs
        from
          load_match_data,
          json_each(innings) innings
      ),
      json_each(overs) overs
  ) innings,
  json_each(deliveries) delivery
;
