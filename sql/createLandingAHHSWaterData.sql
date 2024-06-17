CREATE TABLE IF NOT EXISTS landing_ahhs_water_data (
    id SERIAL PRIMARY KEY,
    sample_id VARCHAR(30),
    pfna_concentration NUMERIC,
    pfna_mrl NUMERIC,
    pfna_dl NUMERIC,
    pfna_flags VARCHAR(6),
    pfds_concentration NUMERIC,
    pfds_mrl NUMERIC,
    pfds_dl NUMERIC,
    pfds_flags VARCHAR(6),
    pfhxa_concentration NUMERIC,
    pfhxa_mrl NUMERIC,
    pfhxa_dl NUMERIC,
    pfhxa_flags VARCHAR(6),
    pfoa_concentration NUMERIC,
    pfoa_mrl NUMERIC,
    pfoa_dl NUMERIC,
    pfoa_flags VARCHAR(6),
    pfos_concentration NUMERIC,
    pfos_mrl NUMERIC,
    pfos_dl NUMERIC,
    pfos_flags VARCHAR(6),
    pfba_concentration NUMERIC,
    pfba_mrl NUMERIC,
    pfba_dl NUMERIC,
    pfba_flags VARCHAR(6),
    pfdoa_concentration NUMERIC,
    pfdoa_mrl NUMERIC,
    pfdoa_dl NUMERIC,
    pfdoa_flags VARCHAR(6),
    pfpea_concentration NUMERIC,
    pfpea_mrl NUMERIC,
    pfpea_dl NUMERIC,
    pfpea_flags VARCHAR(6),
    pfhps_concentration NUMERIC,
    pfhps_mrl NUMERIC,
    pfhps_dl NUMERIC,
    pfhps_flags VARCHAR(6),
    pfunda_concentration NUMERIC,
    pfunda_mrl NUMERIC,
    pfunda_dl NUMERIC,
    pfunda_flags VARCHAR(6),
    pfbs_concentration NUMERIC,
    pfbs_mrl NUMERIC,
    pfbs_dl NUMERIC,
    pfbs_flags VARCHAR(6),
    pfpes_concentration NUMERIC,
    pfpes_mrl NUMERIC,
    pfpes_dl NUMERIC,
    pfpes_flags VARCHAR(6),
    pfns_concentration NUMERIC,
    pfns_mrl NUMERIC,
    pfns_dl NUMERIC,
    pfns_flags VARCHAR(6),
    pfhpa_concentration NUMERIC,
    pfhpa_mrl NUMERIC,
    pfhpa_dl NUMERIC,
    pfhpa_flags VARCHAR(6),
    pfhxs_concentration NUMERIC,
    pfhxs_mrl NUMERIC,
    pfhxs_dl NUMERIC,
    pfhxs_flags VARCHAR(6),
    pfda_concentration NUMERIC,
    pfda_mrl NUMERIC,
    pfda_dl NUMERIC,
    pfda_flags VARCHAR(6)
);
