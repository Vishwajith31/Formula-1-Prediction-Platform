import fastf1
import pandas as pd
import signal
import time

# Enable FastF1 cache (update with your preferred path)
fastf1.Cache.enable_cache('your_path') 

# Point FastF1 at jolpica-f1 API for results (replace Ergast)
fastf1.ergast.interface.BASE_URL = "https://api.jolpi.ca/ergast/f1"

seasons = range(2018, 2025)  # 2018–2024 inclusive
all_features = []

for season in seasons:
    try:
        schedule = fastf1.get_event_schedule(season)
    except Exception as e:
        print(f"Could not load schedule for {season} due to {e}")
        continue

    for idx, gp in schedule.iterrows():
        print(f"\n=== {season} {gp['EventName']} ===")
        # Filter pre-season testing (no pitstop/race relevance)
        if 'Testing' in gp['EventName']:
            print(f"  Skipped: Testing session")
            continue
        try:
            session = fastf1.get_session(season, gp['EventName'], 'R')
            session.load()
            if session.laps is None or len(session.laps) == 0:
                print(f"  Skipped: No laps data.")
                continue
            if session.results is None or session.results.empty:
                print(f"  Skipped: No results data.")
                continue

            # Weather (session averages)
            air_temp = track_temp = humidity = rainfall = None
            if session.weather_data is not None and not session.weather_data.empty:
                weather = session.weather_data.mean(numeric_only=True)
                air_temp = weather.get('AirTemp', None)
                track_temp = weather.get('TrackTemp', None)
                humidity = weather.get('Humidity', None)
                rainfall = session.weather_data['Rainfall'].max() > 0

            for drv in session.laps['Driver'].unique():
                drv_laps = session.laps[session.laps['Driver'] == drv]
                if drv_laps.empty:
                    continue
                team_row = session.results[session.results['Abbreviation'] == drv]
                if team_row.empty:
                    continue

                # Pit stops: Only extract if attribute exists and is not empty
                pit_lap_numbers, pit_compounds, pit_durations, avg_pit_duration = [], [], [], None
                if hasattr(session, 'pit_stops') and session.pit_stops is not None and not session.pit_stops.empty:
                    drv_pitstops = session.pit_stops[session.pit_stops['Driver'] == drv]
                    pit_lap_numbers = drv_pitstops['Lap'].tolist()
                    pit_compounds = drv_pitstops['Compound'].dropna().unique().tolist()
                    pit_durations = drv_pitstops['PitStopTime'].tolist()
                    avg_pit_duration = sum(pit_durations) / len(pit_durations) if len(pit_durations) > 0 else None

                features = {
                    'Season': season,
                    'Race': gp['EventName'],
                    'Driver': drv,
                    'Team': team_row['TeamName'].values[0],
                    'Grid': team_row['GridPosition'].values[0],
                    'Position': team_row['Position'].values[0],
                    'MeanLapTime': drv_laps['LapTime'].mean(),
                    # Weather
                    'AirTemp': air_temp,
                    'TrackTemp': track_temp,
                    'Humidity': humidity,
                    'Rainfall': rainfall,
                    # Pit stops
                    'NumPitstops': len(pit_lap_numbers),
                    'PitStopLaps': ','.join(map(str, pit_lap_numbers)),
                    'PitCompounds': ','.join(map(str, pit_compounds)),
                    'AvgPitStopDuration': avg_pit_duration
                }
                all_features.append(features)

            time.sleep(3)  # Avoid API rate limit
        except Exception as e:
            print(f"Could not process {season} {gp['EventName']} due to {e}")
            continue

# Create and save DataFrame, filtering pre-season testing once again if needed
df_features = pd.DataFrame(all_features)
df_features = df_features[~df_features['Race'].str.contains('Testing')]
outpath = '../data/features/driver_features_2018_2024.csv'
df_features.to_csv(outpath, index=False)
print(f"\nWrote {len(df_features)} rows to {outpath}")
print(df_features.head())
