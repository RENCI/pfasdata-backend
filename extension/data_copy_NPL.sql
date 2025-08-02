COPY superfund_albers_national_priorities_list(ogc_fid,objectid,site_name,site_score,site_epa_i,sems_id,sits_id,region_id,state,city,county,status,longitude,latitude,proposed_d,listing_da,constructi,construc_1,noid_date,deletion_d,site_listi,site_progr,notice_of_,proposed_f,deletion_f,final_fr_n,noid_fr_no,restoratio,site_has_h,creationda,creator,editdate,editor,objectid2,wkb_geometry,pfas)
FROM '/projects/pfas/data/superfund_albers_national_priorities_list.csv'
DELIMITER ','
CSV HEADER;
