select
  game_id,
  info ->> 'balls_per_over' as balls_per_over,
  info ->> 'city' as game_city,
  info -> 'dates' ->> 0 as game_start_date,
  strftime('%Y', info -> 'dates' ->> 0) as game_year,
  info ->> 'dates' as game_dates,
  info -> 'event' ->> 'name' as event_name,
  info -> 'event' ->> 'match_number' as match_number,
  info ->> 'gender' as game_gender,
  -- info -> '' as ,
  -- info -> '' as ,
  -- info -> '' as ,
  -- info -> '' as ,
  -- info -> '' as ,
  -- info -> '' as ,
  -- info -> '' as ,
  -- info -> '' as ,
  -- info -> '' as ,
  -- info -> '' as ,
from
  load_game_data
limit 10;
