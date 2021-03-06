"""
Name: website_sources.py
Created: 2019-09-28
Purpose: Store/return reference website for data.
"""


def return_websites(year):
    websites = {
        "team_site1": "http://www.basketball-reference.com/play-index/tsl_finder.cgi?"
                      "request=1&match=single&type=team_per_game&lg_id=&year_min="
                      + str(year) + "&year_max=" + str(year) +
                      "&franch_id=&c1stat=&c1comp=gt&c1val=&c2stat=&c2comp=gt&c2val=&c3stat=&c3comp=gt&c3val=&c4stat="
                      "&c4comp=gt&c4val=&order_by=team_name&order_by_asc=Y",
        "team_site2": "http://www.basketball-reference.com/play-index/tsl_finder.cgi?"
                      "request=1&match=single&type=advanced&lg_id=&year_min="
                      + str(year) + "&year_max=" + str(year) +
                      "&franch_id=&c1stat=&c1comp=gt&c1val=&c2stat=&c2comp=gt&c2val=&c3stat=&c3comp=gt&c3val=&c4stat="
                      "&c4comp=gt&c4val=&order_by=team_name&order_by_asc=Y",
        "player_site1": "http://www.basketball-reference.com/play-index/psl_finder.cgi?request=1&match=single&type="
                        "totals&per_minute_base=36&lg_id=&is_playoffs=N&year_min="
                        + str(year) + "&year_max=" + str(year) +
                        "&franch_id=&season_start=1&season_end=-1&age_min=0&age_max=99&height_min=0&height_max=99&"
                        "birth_country_is=Y&birth_country=&is_active=Y&is_hof=&is_as=&as_comp=gt&as_val=&pos_is_g=Y&"
                        "pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&qual=&c1stat=&c1comp="
                        "gt&c1val=&c2stat=&c2comp=gt&c2val=&c3stat=&c3comp=gt&c3val=&c4stat=&c4comp=gt&c4val=&c5stat="
                        "&c5comp=gt&c6mult=1.0&c6stat=&order_by=player&order_by_asc=Y",
        "player_site2": "http://www.basketball-reference.com/play-index/psl_finder.cgi?request=1&match=single&"
                        "per_minute_base=36&type=advanced&lg_id=&is_playoffs=N&year_min="
                        + str(year) + "&year_max=" + str(year) +
                        "&franch_id=&season_start=1&season_end=-1&age_min=0&age_max=99&height_min=0&height_max=99&"
                        "birth_country_is=Y&birth_country=&is_active=Y&is_hof=&is_as=&as_comp=gt&as_val=&pos_is_g=Y&"
                        "pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&qual=&c1stat=&c1comp=gt&"
                        "c1val=&c2stat=&c2comp=gt&c2val=&c3stat=&c3comp=gt&c3val=&c4stat=&c4comp=gt&c4val=&c5stat=&"
                        "c5comp=gt&c6mult=1.0&c6stat=&order_by=player&order_by_asc=Y",
        "schedule_site": "http://www.basketball-reference.com/leagues/NBA_" + str(year) + "_games-",
        "health_site": "http://espn.go.com/nba/injuries",
        "odds_site": "http://espn.go.com/nba/lines",
    }
    return websites
