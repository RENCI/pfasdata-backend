python ingestPfasSamples.py --landingTableName landing_ahhs_water_data --study AHHS --pi HUD --measurement 'Water Sample' --medium water --sgidcname water_sample_id
python ingestPfasSamples.py --landingTableName landing_ahhs_dust_data --study AHHS --pi HUD --measurement 'Dust Sample' --medium dust --sgidcname dust_sample_id
python ingestPfasSamples.py --landingTableName landing_ncsserum_data --study ncsSerum --pi 'EPA' --measurement 'Serum Sample' --medium blood --sgidcname serum_sample_id
python ingestPfasSamples.py --landingTableName landing_ncsdust_data --study ncsDust --pi 'EPA' --measurement 'Dust Sample' --medium dust --sgidcname dust_sample_id
python ingestPfasUSGSSamples.py --pi USGS --measurement 'Water Sample' --medium water
