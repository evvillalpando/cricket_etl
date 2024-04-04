drop view view_question_2b;
create view view_question_2b as
  select
    *
  from
    (
      select
        *,
        rank() over (partition by match_year, match_gender order by win_percentage desc) as year_gender_rank

      from
        view_question_2a
      where
        match_year = 2019
    )
  where year_gender_rank = 1
;
