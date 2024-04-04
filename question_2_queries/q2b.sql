with
  teams as (
    SELECT DISTINCT team_1 AS team FROM matches
    UNION
    SELECT DISTINCT team_2 AS team FROM matches
  ),
  match_results as (
    select
      match_id,
      match_year,
      match_gender,
      team_1,
      team_2,
      winning_team
    from
      matches
    where
      match_result = 'winner decided'
      and not is_dl
      and not is_tie
  )

  select
    *
  from
    (
      select
        *,
        rank() over (partition by match_year, match_gender order by win_percentage desc) as year_gender_rank

      from
        (
          select
            match_results.match_year,
            match_results.match_gender,
            teams.team,
            sum(case when teams.team = match_results.winning_team then 1 else 0 end) as matchs_won,
            round(100*(1.0*sum(case when teams.team = match_results.winning_team then 1 else 0 end) / (1.0*count(*))),2) as win_percentage
          from
            teams
          left join match_results
            on teams.team = team_1
            or teams.team = team_2
          group by
            teams.team,
            match_results.match_gender,
            match_results.match_year
          order by match_year, match_gender, win_percentage desc
        )
      where
        match_year = 2019
    )
  where year_gender_rank = 1
;
