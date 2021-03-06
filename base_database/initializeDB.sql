DROP DATABASE IF EXISTS covid19_vaccines_information;
CREATE DATABASE covid19_vaccines_information;

USE covid19_vaccines_information;

CREATE TABLE Country (
	CountryCode CHAR(3) PRIMARY KEY,
    CountryName VARCHAR(50) UNIQUE NOT NULL,
    CountryVaccinated BIGINT UNSIGNED
);

CREATE TABLE Sponsor (
	SponsorID INTEGER AUTO_INCREMENT PRIMARY KEY,
	SponsorName VARCHAR(80),
    SponsorCountry CHAR(3),
    FOREIGN KEY (SponsorCountry) REFERENCES Country(CountryCode)
    		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Vaccine (
	VaccineID INTEGER AUTO_INCREMENT PRIMARY KEY,
	VaccineName VARCHAR(20),
    VaccineMechanism VARCHAR(80),
    VaccineStatus VARCHAR(20),
    VaccineDetails TEXT
);

CREATE TABLE SponsorManufacturesVaccine (
	ManufacturingID INTEGER AUTO_INCREMENT PRIMARY KEY,
	SponsorID INTEGER,
    VaccineID INTEGER,
    CONSTRAINT UC_Manufacture UNIQUE (SponsorID, VaccineID),
    FOREIGN KEY (SponsorID) REFERENCES Sponsor(SponsorID)
		ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (VaccineID) REFERENCES Vaccine(VaccineID)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE VaccineTrialsInCountry (
	TrialID INTEGER AUTO_INCREMENT PRIMARY KEY,
	VaccineID INTEGER,
    CountryCode CHAR(3),
    CONSTRAINT UC_Trial UNIQUE (VaccineID, CountryCode),
    FOREIGN KEY (VaccineID) REFERENCES Vaccine(VaccineID)
		ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (CountryCode) REFERENCES Country(CountryCode)
    		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE tb_user 
(
  username VARCHAR(50) primary key,
  `password` VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL
);

INSERT INTO country (CountryCode, CountryName, CountryVaccinated)
VALUES ('CHN', 'China', 223000000), ('USA', 'United States', 185424899), ('DEU', 'Germany', 49632810);

INSERT INTO sponsor (SponsorName, SponsorCountry)
VALUES ('CanSino Biologics', 'CHN'), ('Moderna', 'USA'), ('BioNTech', 'DEU');

INSERT INTO vaccine (VaccineName, VaccineMechanism, VaccineStatus, VaccineDetails)
VALUES ('Ad5-nCoV', 'Recombinant vaccine (adenovirus type 5 vector)', 'Phase 3','Background: China&rsquo;s CanSino Biologics has developed a recombinant novel coronavirus vaccine that incorporates the adenovirus type 5 vector (Ad5) named Ad5-nCoV. Trials: Multiple trials are in various stages of recruitment and completion: - A Phase 1 clinical trial in China of 108 participants between 18 and 60 years old who will receive low, medium, and high doses of Ad5-nCoV is active, but not recruiting (NCT04313127). - A Phase 1 trial in China is evaluating intramuscular vaccination and mucosal vaccination of Ad5-nCoV across two doses (NCT04552366). - A Phase 1/2 trial of up to 696 participants in Canada (NCT04398147). - A Phase 2 double-blind, placebo-controlled trial of up to 508 participants in China (NCT04341389) is active, but not recruiting. - A Phase 2b trial in China evaluating safety and immunogenicity of Ad5-nCoV in participants 6 years and older (NCT04566770). - A Phase 3 trial in Russia of up to 500 participants across multiple study centers (NCT04540419). - A Phase 3 trial of up to 40,000 participants internationally, including Pakistan, Saudi Arabia and Mexico (NCT04526990). Outcomes: A single dose of Ad5-nCoV protected against upper respiratory infection of SARS-CoV-2 in ferrets, according to a paper published 14 August in Nature Communications. Results from a Phase 1 trial show a humoral and immunogenic response to the vaccine, according to a paper published in The Lancet. Adverse reactions such as pain (54%), fever (46%), fatigue (44%), headache (39%), and muscle pain (17%) occurred in 83% of patients in the low and medium dose groups and 75% of patients in the high dose group. In the Phase 2 trial, neutralizing antibodies and specific interferon ?? enzyme-linked immunospot assay responses were observed at all dose levels for most participants. Status: On 25 June, China???s Central Military Commission announced the military had been approved to use Ad5-nCoV for a period of 1 year, according to reporting in Reuters.'),
		('mRNA-1273', 'mRNA-based vaccine', 'Phase 3', 'Background: mRNA-1273 was developed by Moderna based on prior studies of related coronaviruses such as those that cause severe acute respiratory syndrome (SARS) and Middle East respiratory syndrome (MERS).\n\nStudy Design: A Phase 3 trial of 30,000 participants at high risk for SARS-CoV-2 infection is underway. Participants will receive a 100 &micro;g dose of mRNA-1273 or placebo and then be&nbsp;followed for up to 2 years (COVE trial;&nbsp;NCT04470427). Moderna&nbsp;posted&nbsp;the full trial protocol for COVE on 17 September. Previously, a Phase 1 trial (NCT04283461) of 105 healthy participants provided the basis for Moderna&rsquo;s investigational new drug application (IND), which was successfully reviewed by the FDA and set the stage for Phase 2 testing. A Phase 2 trial of 600 healthy participants evaluating 25 &micro;g, 100 &micro;g, and 250 &micro;g dose levels of the vaccine was completed.&nbsp;(NCT04405076).\n\nOutcomes:\nHuman studies - An&nbsp;interim analysis of 95 participants in the Phase 3 COVE trial was released by Moderna on 16 November. The non-peer-reviewed data indicate mRNA-1273 has an efficacy of 94.5%. There were no severe cases of COVID-19 in the vaccinated group compared with 11 cases in the placebo group. Overall, the company said the vaccine was tolerated well with no &ldquo;significant safety concerns.&rdquo; Additionally, Phase 1 data&nbsp;published&nbsp;in the&nbsp;New England Journal of Medicine&nbsp;showed mRNA-1273 successfully produced neutralizing antibody titers in 8 participants who received either 25 &micro;g or 100 &micro;g doses. The response was dose dependent in 45 participants across 25 &micro;g, 100 &micro;g, and 250 &micro;g dose levels. In participants with available antibody data, neutralizing antibody titers were on par with what has been seen in convalescent sera from people who have successfully fought off COVID-19. The vaccine also appears to be safe for older adults, with participants who received two 25 &mu;g or 100 &mu;g doses of the vaccine experiencing mild or moderate effects consisting of fatigue, chills, headache, myalgia, and injection site pain, according to data from the Phase 1 trial&nbsp;published&nbsp;in the&nbsp;New England Journal of Medicine.\n\nAnimal studies - Results from a challenge in a mouse model showed mRNA-1273 prevented viral replication in the lungs, and neutralizing titers in the mouse model were similar in participants receiving 25 &micro;g or 100 &micro;g doses of the vaccine. A&nbsp;study&nbsp;of nonhuman primates challenged with SARS-CoV-2 published in the&nbsp;New England Journal of Medicine&nbsp;had neutralizing activity, and limited inflammation and lung activity after being administered the vaccine. A paper&nbsp;published&nbsp;in&nbsp;Nature&nbsp;also showed mRNA-1273 induced neutralizing antibodies in mice.\n\nStatus: Moderna requested that the FDA issue an EUA for mRNA-1273 on 30 November; an advisory committee meeting is scheduled for 17 December. Moderna requested conditional marketing authorization from EMA for mRNA-1273 on 1 December. On 12 May, the&nbsp;FDA granted&nbsp;Fast Track designation to mRNA-1273. A Phase 3 trial of the vaccine is&nbsp;underway, which is being funded by Operation Warp Speed. The UK&rsquo;s Medicines and Healthcare products Regulatory Agency (MHRA) has&nbsp;begun&nbsp;a real-time review of mRNA-1273, which will allow a quicker approval process for the vaccine. A rolling review by regulator Swissmedic in Switzerland has also begun.'),
        ('BNT162', 'mRNA-based vaccine', 'Phase 3', 'Background: Pfizer and BioNtech are&nbsp;collaborating&nbsp;to develop BNT162, a series of vaccine candidates for COVID-19. BNT162 was initially four candidates developed by BioNTech, two candidates consisting of nucleoside modified mRNA-based (modRNA), one of uridine containing mRNA-based (uRNA), and the fourth candidate of self-amplifying mRNA-based (saRNA). Pre-clinical results of the modRNA candidate BNT162b2&nbsp;posted&nbsp;to the pre-print server&nbsp;bioRxiv&nbsp;showed the vaccine had &quot;protective anti-viral effects in rhesus macaques, with concomitant high neutralizing antibody titers and a TH1-biased cellular response in rhesus macaques and mice.&quot; The companies have selected BNT162b2 to move forward in a Phase 2/3 trial.\n\nRegulatory Actions: BNT162b was&nbsp;authorized by the Medicines and Healthcare products Regulatory Agency (MHRA) for use in the UK&nbsp;on 2 December after a rolling review of vaccine data submitted by Pfizer and BioNTech.\n\nStudy Designs: The pivotal Phase 2/3 trial of about 32,000 healthy participants&nbsp;(NCT04368728) still is recruiting, as is a Phase 1/2 trial in the US and Germany of 200 healthy participants between aged 18-55 years (NCT04380701).&nbsp;Pfizer and BioNTech also are planning&nbsp;a combined Phase 1/2 trial of 160 participants between 20-85 years old (NCT04588480). In China, BioNTech and Shanghai Fosun Pharmaceutical are conducting a Phase 2 trial of BNT162b in 960 healthy participants at the Jiangsu Provincial Center for Disease Control and Prevention (NCT04649021).\n\nOutcomes: On 9 November, Pfizer and BioNTech&nbsp;announced&nbsp;interim results by press release of 94 Phase 3 trial participants, which showed BNT162b2 was more than 90% effective in protecting participants who had never been infected with SARS-CoV-2 at 7 days after the second dose. Those results are backed up by Phase 1&nbsp;data&nbsp;published in&nbsp;The New England Journal of Medicine&nbsp;showing similar immunogenicity between BNT162b1 and BNT162b2 but fewer adverse effects with BNT162b2. Another study of Phase 1/2 data for BNT162b1 was&nbsp;published&nbsp;in the journal&nbsp;Nature. Robust immunogenicity was seen after vaccination at all three doses (10 &mu;g, 30 &mu;g and 100 &mu;g). Adverse events were elevated at the highest dose; therefore, participants did not receive a second dose at that level. Participants in Phase 1/2 trials who received two doses between 1 and 50 &micro;g of BNT162b1 had &quot;robust RBD-specific antibody, T-cell and favourable cytokine responses,&quot; according to a paper&nbsp;published&nbsp;in&nbsp;Nature&nbsp;on 30 September.\n\nStatus: In the US,&nbsp;Pfizer and BioNTech have requested that the FDA issue an EUA for BNT162b2; an advisory committee meeting is scheduled for 10 December. BNT162b1 and BNT162b2 received&nbsp;FDA Fast Track designation for BNT162b1 and BNT162b2. The companies requested conditional marketing authority from EMA on 1 December; EMA&#39;s rolling&nbsp;review&nbsp;of BNT162b2 could accelerate that authorization.&nbsp;In Australia, BNT162b2 received&nbsp;provisional determination&nbsp;from Australia&rsquo;s Therapeutic Goods Administration (TGA), which is the first step on the road for approval for the vaccine in the country. BioNTech&#39;s partner in China, Shanghai Fosun Pharmaceutical Group,&nbsp;announced&nbsp;it is seeking approval for BNT162b2 in China but would no longer be pursuing clinical trials for BNT162b1.');

INSERT INTO sponsormanufacturesvaccine (SponsorID, VaccineID)
VALUES (1, 1), (2, 2), (3, 3);

INSERT INTO vaccinetrialsincountry (VaccineID, CountryCode)
VALUES (1, 'CHN'), (2, 'USA'), (3, 'DEU');

INSERT INTO tb_user (username, password, email)
VALUES ('wmobei2', 'KSA', 'wmobei2@uic.edu'), ('aalzah23', 'KSA', 'aalzah23@uic.edu'), ('ecarra6', 'USA', 'ecarra6@uic.edu');