COPY podm_pfas_name_classification_info(abbreviation,chemical_name,casrn,dtxsid,nhanes,carbon_atoms,formula,pfaa,pfca,pfsa,precursor,ftbs,dipap,ftoh,acid_ftca,acid_fts,substances_pasf,sulfonamides_fasa,ethanols_fase,pfeca,pfesa,cl_pfesa,carboxylic_acid,sulfonic_acid)
FROM '/projects/pfas/data/PFASNamingClassificationInformationShortX.csv'
DELIMITER ','
CSV HEADER;
