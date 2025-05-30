INSERT INTO podm_pfas_data2 (sample_id,pfmpa_concentration,pfmpa_mrl,pfmba_concentration,pfmba_mrl,pfta_concentration,pfta_mrl,netfosaa_concentration,netfosaa_mrl,x82fts_concentration,x82fts_mrl,hfpoda_concentration,hfpoda_mrl,x62fts_concentration,x62fts_mrl,nfdha_concentration,nfdha_mrl,pfuna_concentration,pfuna_mrl,pfeesa_concentration,pfeesa_mrl,nmefosaa_concentration,nmefosaa_mrl,x9clpf3ons_concentration,x9clpf3ons_mrl,x11clpf3ouds_concentration,x11clpf3ouds_mrl,adona_concentration,adona_mrl,x42fts_concentration,x42fts_mrl,pftrda_concentration,pftrda_mrl)
SELECT unique_id AS sample_id, 
      pfmpa_concentration_ngl AS pfmpa_concentration,
      pfmpa_mrl_ngl AS pfmpa_mrl,
      pfmba_concentration_ngl AS pfmba_concentration,
      pfmba_mrl_ngl AS pfmba_mrl,
      pfta_concentration_ngl AS pfta_concentration,
      pfta_mrl_ngl AS pfta_mrl,
      netfosaa_concentration_ngl AS netfosaa_concentration,
      netfosaa_mrl_ngl AS netfosaa_mrl,
      x82fts_concentration_ngl AS x82fts_concentration,
      x82fts_mrl_ngl AS x82fts_mrl,
      hfpoda_concentration_ngl AS hfpoda_concentration,
      hfpoda_mrl_ngl AS hfpoda_mrl,
      x62fts_concentration_ngl AS x62fts_concentration,
      x62fts_mrl_ngl ASx62fts_mrl,
      nfdha_concentration_ngl AS nfdha_concentration,
      nfdha_mrl_ngl AS nfdha_mrl,
      pfuna_concentration_ngl AS pfuna_concentration,
      pfuna_mrl_ngl AS pfuna_mrl,
      pfeesa_concentration_ngl AS pfeesa_concentration,
      pfeesa_mrl_ngl AS pfeesa_mrl,
      nmefosaa_concentration_ngl AS nmefosaa_concentration,
      nmefosaa_mrl_ngl AS nmefosaa_mrl,
      x9clpf3ons_concentration_ngl AS x9clpf3ons_concentration,
      x9clpf3ons_mrl_ngl AS x9clpf3ons_mrl,
      x11clpf3ouds_concentration_ngl AS x11clpf3ouds_concentration,
      x11clpf3ouds_mrl_ngl AS x11clpf3ouds_mrl,
      adona_concentration_ngl AS adona_concentration,
      adona_mrl_ngl AS adona_mrl,
      x42fts_concentration_ngl AS x42fts_concentration,
      x42fts_mrl_ngl AS x42fts_mrl,
      pftrda_concentration_ngl AS pftrda_concentration,
      pftrda_mrl_ngl AS pftrda_mrl
FROM landing_usmr5_data;
