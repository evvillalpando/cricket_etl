insert into players
select
  distinct player_team,
  player_list.value as player
from
  (
    select
      players.key as player_team,
      players.value as players
    from
      load_match_data,
      json_each(info->'players') players
  ), json_each(players) player_list
;
