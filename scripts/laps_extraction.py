import fastf1
import pandas as pd
import time

# Set your FastF1 cache location
fastf1.Cache.enable_cache('your_path')
fastf1.ergast.interface.BASE_URL = "https://api.jolpi.ca/ergast/f1"

lap_rows = []
seasons = range(2018, 2025)  # Adjust if needed

for season in seasons:
    try:
        schedule = fastf1.get_event_schedule(season)
    except Exception as e:
        print(f"Could not load schedule for {season}: {e}")
        continue

    for idx, gp in schedule.iterrows():
        if 'Testing' in gp['EventName']:
            print(f"Skipped: {season} {gp['EventName']} (testing)")
            continue
        try:
            session = fastf1.get_session(season, gp['EventName'], 'R')
            session.load()
            if session.laps is None or len(session.laps) == 0:
                print(f"  Skipped: No laps data.")
                continue
            # Make a copy and add season/race info
            race_laps = session.laps.copy()
            race_laps['Season'] = season
            race_laps['Race'] = gp['EventName']
            lap_rows.append(race_laps)
        except Exception as e:
            print(f"Could not process {season} {gp['EventName']}: {e}")
            continue
        time.sleep(3)  # Rate limiting

# Combine all laps into a single DataFrame
if lap_rows:
    laps_df = pd.concat(lap_rows, ignore_index=True)
    laps_df.to_csv('../data/features/lap_level_data_2018_2024.csv', index=False)
    print(f"Wrote {len(laps_df)} lap rows to ../data/features/lap_level_data_2018_2024.csv")
    print(laps_df.head())
else:
    print("No lap data was extracted.")
