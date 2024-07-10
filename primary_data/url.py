import pandas as pd

# import file as csv with url
nfl_2023 = pd.read_csv('https://nflsavant.com/pbp_data.php?year=2023')
# delete every undesired (empty) columns
nfl_2023 = nfl_2023.loc[:, ~nfl_2023.columns.str.contains('^Unnamed')]
# saving the dataframe with csv
nfl_2023.to_csv(r'~/PycharmProjects/CAP/primary_data/nfl_2023.csv')

# year 2022
nfl_2022 = pd.read_csv('https://nflsavant.com/pbp_data.php?year=2022')
nfl_2022 = nfl_2022.loc[:, ~nfl_2022.columns.str.contains('^Unnamed')]
nfl_2022.to_csv(r'~/PycharmProjects/CAP/primary_data/nfl_2022.csv')
# year 2021
nfl_2021 = pd.read_csv('https://nflsavant.com/pbp_data.php?year=2021')
nfl_2021 = nfl_2021.loc[:, ~nfl_2021.columns.str.contains('^Unnamed')]
nfl_2021.to_csv(r'~/PycharmProjects/CAP/primary_data/nfl_2021.csv')
# year 2020
nfl_2020 = pd.read_csv('https://nflsavant.com/pbp_data.php?year=2020')
nfl_2020 = nfl_2020.loc[:, ~nfl_2020.columns.str.contains('^Unnamed')]
nfl_2020.to_csv(r'~/PycharmProjects/CAP/primary_data/nfl_2020.csv')
# year 2019
nfl_2019 = pd.read_csv('https://nflsavant.com/pbp_data.php?year=2019')
nfl_2019 = nfl_2019.loc[:, ~nfl_2019.columns.str.contains('^Unnamed')]
nfl_2019.to_csv(r'~/PycharmProjects/CAP/primary_data/nfl_2019.csv')
# year 2018
nfl_2018 = pd.read_csv('https://nflsavant.com/pbp_data.php?year=2018')
nfl_2018 = nfl_2018.loc[:, ~nfl_2018.columns.str.contains('^Unnamed')]
nfl_2018.to_csv(r'~/PycharmProjects/CAP/primary_data/nfl_2018.csv')
# year 2017
nfl_2017 = pd.read_csv('https://nflsavant.com/pbp_data.php?year=2017')
nfl_2017 = nfl_2017.loc[:, ~nfl_2017.columns.str.contains('^Unnamed')]
nfl_2017.to_csv(r'~/PycharmProjects/CAP/primary_data/nfl_2017.csv')
# year 2016
nfl_2016 = pd.read_csv('https://nflsavant.com/pbp_data.php?year=2016')
nfl_2016 = nfl_2016.loc[:, ~nfl_2016.columns.str.contains('^Unnamed')]
nfl_2016.to_csv(r'~/PycharmProjects/CAP/primary_data/nfl_2016.csv')
# year 2015
nfl_2015 = pd.read_csv('https://nflsavant.com/pbp_data.php?year=2015')
nfl_2015 = nfl_2015.loc[:, ~nfl_2015.columns.str.contains('^Unnamed')]
nfl_2015.to_csv(r'~/PycharmProjects/CAP/primary_data/nfl_2015.csv')
# year 2014
nfl_2014 = pd.read_csv('https://nflsavant.com/pbp_data.php?year=2014')
nfl_2014 = nfl_2014.loc[:, ~nfl_2014.columns.str.contains('^Unnamed')]
nfl_2014.to_csv(r'~/PycharmProjects/CAP/primary_data/nfl_2014.csv')
