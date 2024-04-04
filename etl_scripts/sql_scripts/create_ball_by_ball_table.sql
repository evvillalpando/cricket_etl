DROP TABLE IF EXISTS ball_by_ball;
CREATE TABLE ball_by_ball (
  match_id int,
  match_start_date date,
  match_year int,
  batting_team text,
  over int,
  batter text,
  bowler text,
  non_striker text,
  batter_runs int,
  extra_runs int,
  total_runs int,
  wides int,
  load_to_db_timestamp timestamp
);
