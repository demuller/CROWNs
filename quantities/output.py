from code_generation.quantity import Quantity

lumi = Quantity("lumi")
prefireweight = Quantity("prefiring_wgt")

base_taus_mask = Quantity("base_taus_mask")
good_taus_mask = Quantity("good_taus_mask")
#veto_muons_mask = Quantity("veto_muons_mask")
#veto_muons_mask_2 = Quantity("veto_muons_mask_2")
#muon_veto_flag = Quantity("extramuon_veto")
#veto_electrons_mask = Quantity("veto_electrons_mask")
#veto_electrons_mask_2 = Quantity("veto_electrons_mask_2")
#electron_veto_flag = Quantity("extraelec_veto")
jet_eta_mask = Quantity("jet_eta_mask")
jet_id_mask = Quantity("jet_id_mask")
jet_puid_mask = Quantity("jet_puid_mask")
jet_overlap_veto_mask = Quantity("jet_overlap_veto_mask")
good_jets_mask = Quantity("good_jets_mask")
good_jetslowpt_mask = Quantity("good_jetslowpt_mask")
good_nonbjets_mask = Quantity("good_nonbjets_mask")
good_bjets_mask = Quantity("good_bjets_mask")
Tau_pt_ele_corrected = Quantity("Tau_pt_ele_corrected")
Tau_pt_ele_mu_corrected = Quantity("Tau_pt_mu_corrected")
Tau_pt_corrected = Quantity("Tau_pt_corrected")
Tau_mass_corrected = Quantity("Tau_mass_corrected")
Jet_pt_corrected = Quantity("Jet_pt_corrected")
Jet_mass_corrected = Quantity("Jet_mass_corrected")
dileptonpair = Quantity("dileptonpair")
gen_dileptonpair = Quantity("gen_dileptonpair")
truegenpair = Quantity("truegenpair")
good_jet_collection = Quantity("good_jet_collection")
good_jetlowpt_collection = Quantity("good_jetlowpt_collection")
good_nonbjet_collection = Quantity("good_nonbjet_collection")
good_bjet_collection = Quantity("good_bjet_collection")

ntaus = Quantity("ntaus")
p4_1 = Quantity("p4_1")
p4_1_uncorrected = Quantity("p4_1_uncorrected")
pt_1 = Quantity("pt_1")
eta_1 = Quantity("eta_1")
phi_1 = Quantity("phi_1")
p4_2 = Quantity("p4_2")
p4_2_uncorrected = Quantity("p4_2_uncorrected")
pt_2 = Quantity("pt_2")
eta_2 = Quantity("eta_2")
phi_2 = Quantity("phi_2")
mass_1 = Quantity("mass_1")
mass_2 = Quantity("mass_2")
dxy_1 = Quantity("dxy_1")
dxy_2 = Quantity("dxy_2")
dz_1 = Quantity("dz_1")
dz_2 = Quantity("dz_2")
q_1 = Quantity("q_1")
q_2 = Quantity("q_2")
iso_1 = Quantity("iso_1")
iso_2 = Quantity("iso_2")
is_global_1 = Quantity("is_global_1")
is_global_2 = Quantity("is_global_2")
decaymode_1 = Quantity("decaymode_1")
decaymode_2 = Quantity("decaymode_2")
gen_match_1 = Quantity("gen_match_1")
gen_match_2 = Quantity("gen_match_2")
tau_gen_match_1 = Quantity("tau_gen_match_1")
tau_gen_match_2 = Quantity("tau_gen_match_2")
gen_tau_pt_1 = Quantity("gen_tau_pt_1")
gen_tau_pt_2 = Quantity("gen_tau_pt_2")
gen_tau_eta_1 = Quantity("gen_tau_eta_1")
gen_tau_eta_2 = Quantity("gen_tau_eta_2")
gen_tau_phi_1 = Quantity("gen_tau_phi_1")
gen_tau_phi_2 = Quantity("gen_tau_phi_2")
taujet_pt_1 = Quantity("taujet_pt_1")
taujet_pt_2 = Quantity("taujet_pt_2")
gen_taujet_pt_1 = Quantity("gen_taujet_pt_1")
gen_taujet_pt_2 = Quantity("gen_taujet_pt_2")

# Combined event quantities
m_vis = Quantity("m_vis")
pt_vis = Quantity("pt_vis")
pzetamissvis = Quantity("pzetamissvis")
mTdileptonMET = Quantity("mTdileptonMET")
mt_1 = Quantity("mt_1")
mt_2 = Quantity("mt_2")
pt_tt = Quantity("pt_tt")
pt_ttjj = Quantity("pt_ttjj")
mt_tot = Quantity("mt_tot")
deltaR_ditaupair = Quantity("deltaR_ditaupair")

n_jets = Quantity("n_jets")
jet_1_p4 = Quantity("jet_1_p4")
jet_1_pt = Quantity("jet_1_pt")
jet_1_eta = Quantity("jet_1_eta")
jet_1_phi = Quantity("jet_1_phi")
jet_1_mass = Quantity("jet_1_mass")
jet_1_btag = Quantity("jet_1_btag")
jet_1_flavor = Quantity("jet_1_flavor")
jet_2_p4 = Quantity("jet_2_p4")
jet_2_pt = Quantity("jet_2_pt")
jet_2_eta = Quantity("jet_2_eta")
jet_2_phi = Quantity("jet_2_phi")
jet_2_mass = Quantity("jet_2_mass")
jet_2_btag = Quantity("jet_2_btag")
jet_2_flavor = Quantity("jet_2_flavor")
jet_3_p4 = Quantity("jet_3_p4")
jet_3_pt = Quantity("jet_3_pt")
jet_3_eta = Quantity("jet_3_eta")
jet_3_phi = Quantity("jet_3_phi")
jet_3_mass = Quantity("jet_3_mass")
jet_3_btag = Quantity("jet_3_btag")
jet_3_flavor = Quantity("jet_3_flavor")
mjj = Quantity("mjj")

n_bjets = Quantity("n_bjets")
bjet_1_p4 = Quantity("bjet_1_p4")
bjet_1_pt = Quantity("bjet_1_pt")
bjet_1_eta = Quantity("bjet_1_eta")
bjet_1_phi = Quantity("bjet_1_phi")
bjet_1_mass = Quantity("bjet_1_mass")
bjet_1_btag = Quantity("bjet_1_btag")
bjet_1_flavor = Quantity("bjet_1_flavor")
bjet_2_p4 = Quantity("bjet_2_p4")
bjet_2_pt = Quantity("bjet_2_pt")
bjet_2_eta = Quantity("bjet_2_eta")
bjet_2_phi = Quantity("bjet_2_phi")
bjet_2_mass = Quantity("bjet_2_mass")
bjet_2_btag = Quantity("bjet_2_btag")
bjet_2_flavor = Quantity("bjet_2_flavor")

n_nonbjets = Quantity("n_nonbjets")
nonbjet_1_p4 = Quantity("nonbjet_1_p4")
nonbjet_1_pt = Quantity("nonbjet_1_pt")
nonbjet_1_eta = Quantity("nonbjet_1_eta")
nonbjet_1_phi = Quantity("nonbjet_1_phi")
nonbjet_1_mass = Quantity("nonbjet_1_mass")
nonbjet_1_btag = Quantity("nonbjet_1_btag")
nonbjet_1_flavor = Quantity("nonbjet_1_flavor")
nonbjet_2_p4 = Quantity("nonbjet_2_p4")
nonbjet_2_pt = Quantity("nonbjet_2_pt")
nonbjet_2_eta = Quantity("nonbjet_2_eta")
nonbjet_2_phi = Quantity("nonbjet_2_phi")
nonbjet_2_mass = Quantity("nonbjet_2_mass")
nonbjet_2_btag = Quantity("nonbjet_2_btag")
nonbjet_2_flavor = Quantity("nonbjet_2_flavor")


dielectron_veto = Quantity("dielectron_veto")
dimuon_veto = Quantity("dimuon_veto")
dilepton_veto = Quantity("dilepton_veto")

## Gen Quantities
gen_p4_1 = Quantity("gen_p4_1")
gen_pt_1 = Quantity("gen_pt_1")
gen_eta_1 = Quantity("gen_eta_1")
gen_phi_1 = Quantity("gen_phi_1")
gen_mass_1 = Quantity("gen_mass_1")
gen_pdgid_1 = Quantity("gen_pdgid_1")

gen_p4_2 = Quantity("gen_p4_2")
gen_pt_2 = Quantity("gen_pt_2")
gen_eta_2 = Quantity("gen_eta_2")
gen_phi_2 = Quantity("gen_phi_2")
gen_mass_2 = Quantity("gen_mass_2")
gen_pdgid_2 = Quantity("gen_pdgid_2")
gen_m_vis = Quantity("gen_m_vis")

hadronic_gen_taus = Quantity("hadronic_gen_taus")

topPtReweightWeight = Quantity("topPtReweightWeight")
ZPtMassReweightWeight = Quantity("ZPtMassReweightWeight")

## HTXS quantities
ggh_NNLO_weight = Quantity("ggh_NNLO_weight")
THU_ggH_Mu = Quantity("THU_ggH_Mu")
THU_ggH_Res = Quantity("THU_ggH_Res")
THU_ggH_Mig01 = Quantity("THU_ggH_Mig01")
THU_ggH_Mig12 = Quantity("THU_ggH_Mig12")
THU_ggH_VBF2j = Quantity("THU_ggH_VBF2j")
THU_ggH_VBF3j = Quantity("THU_ggH_VBF3j")
THU_ggH_PT60 = Quantity("THU_ggH_PT60")
THU_ggH_PT120 = Quantity("THU_ggH_PT120")
THU_ggH_qmtop = Quantity("THU_ggH_qmtop")
THU_qqH_TOT = Quantity("THU_qqH_TOT")
THU_qqH_PTH200 = Quantity("THU_qqH_PTH200")
THU_qqH_Mjj60 = Quantity("THU_qqH_Mjj60")
THU_qqH_Mjj120 = Quantity("THU_qqH_Mjj120")
THU_qqH_Mjj350 = Quantity("THU_qqH_Mjj350")
THU_qqH_Mjj700 = Quantity("THU_qqH_Mjj700")
THU_qqH_Mjj1000 = Quantity("THU_qqH_Mjj1000")
THU_qqH_Mjj1500 = Quantity("THU_qqH_Mjj1500")
THU_qqH_25 = Quantity("THU_qqH_25")
THU_qqH_JET01 = Quantity("THU_qqH_JET01")

## MET quantities
met_p4 = Quantity("met_p4")
recoil_genboson_p4_vec = Quantity("recoil_genboson_p4_vec")
genbosonmass = Quantity("genbosonmass")
npartons = Quantity("npartons")
met_p4_leptoncorrected = Quantity("met_p4_leptoncorrected")
met_p4_jetcorrected = Quantity("met_p4_jetcorrected")
met_p4_recoilcorrected = Quantity("met_p4_recoilcorrected")
met = Quantity("met")
metphi = Quantity("metphi")
metSumEt = Quantity("metSumEt")
metcov00 = Quantity("metcov00")
metcov01 = Quantity("metcov01")
metcov10 = Quantity("metcov10")
metcov11 = Quantity("metcov11")
met_uncorrected = Quantity("met_uncorrected")
metphi_uncorrected = Quantity("metphi_uncorrected")

## PFMET quantities
pfmet = Quantity("PFMET_pt")
pfmet_p4 = Quantity("pfmet_p4")
pfmetphi = Quantity("PFMET_phi")
pfmet_uncorrected = Quantity("pfmet_uncorrected")
pfmetphi_uncorrected = Quantity("pfmetphi_uncorrected")
pfmet_p4_leptoncorrected = Quantity("pfmet_p4_leptoncorrected")
pfmet_p4_jetcorrected = Quantity("pfmet_p4_jetcorrected")
pfmet_p4_recoilcorrected = Quantity("pfmet_p4_recoilcorrected")

# sample flags
is_singletop = Quantity("is_singletop")
# is_single_s = Quantity("is_single_s")
# is_single_t = Quantity("is_single_t")
# is_single_tw = Quantity("is_single_tw")
is_ttbar = Quantity("is_ttbar")
is_diboson = Quantity("is_diboson")
is_dyjets = Quantity("is_dyjets")
is_wjets = Quantity("is_wjets")
is_qcd = Quantity("is_qcd")
is_data = Quantity("is_data")

# Electron Weights
id_wgt_ele_wp90nonIso_1 = Quantity("id_wgt_ele_wp90nonIso_1")
id_wgt_ele_wp90nonIso_2 = Quantity("id_wgt_ele_wp90nonIso_2")
id_wgt_ele_wp80nonIso_1 = Quantity("id_wgt_ele_wp80nonIso_1")
id_wgt_ele_wp80nonIso_2 = Quantity("id_wgt_ele_wp80nonIso_2")
# Muon weights
id_wgt_mu_1 = Quantity("id_wgt_mu_1")
id_wgt_mu_2 = Quantity("id_wgt_mu_2")
iso_wgt_mu_1 = Quantity("iso_wgt_mu_1")
iso_wgt_mu_2 = Quantity("iso_wgt_mu_2")
# btag weight
btag_weight = Quantity("btag_weight")




# el
base_muons_mask = Quantity("base_muons_mask")
loose_muons_mask = Quantity("loose_muons_mask")
tight_muons_mask = Quantity("tight_muons_mask")
antiloose_muons_mask = Quantity("antiloose_muons_mask")
antitight_muons_mask = Quantity("antitight_muons_mask")
n_loose_el = Quantity("n_loose_el")
n_tight_el = Quantity("n_tight_el")
n_antitight_el = Quantity("n_antitight_el")


# mu
base_electrons_mask = Quantity("base_electrons_mask")
loose_electrons_mask = Quantity("loose_electrons_mask")
tight_electrons_mask = Quantity("tight_electrons_mask")
antiloose_electrons_mask = Quantity("antiloose_electrons_mask")
antitight_electrons_mask = Quantity("antitight_electrons_mask")
n_loose_mu = Quantity("n_loose_mu")
n_tight_mu = Quantity("n_tight_mu")
n_antitight_mu = Quantity("n_antitight_mu")


# good lepton
n_loose_lep = Quantity("n_loose_lep")
n_tight_lep = Quantity("n_tight_lep")
n_antitight_lep = Quantity("n_antitight_lep")
tight_leptons_mask = Quantity("tight_leptons_mask")
lep_is_mu = Quantity("lep_is_mu")
lep_is_el = Quantity("lep_is_el")
lep_is_iso = Quantity("lep_is_iso")
lep_is_antiiso = Quantity("lep_is_antiiso")
lep_p4 = Quantity("lep_p4")
lep_p4_uncorrected = Quantity("lep_p4_uncorrected")
lep_pt = Quantity("lep_pt")
lep_eta = Quantity("lep_eta")
lep_sceta = Quantity("lep_sceta")
lep_phi = Quantity("lep_phi")
lep_mass = Quantity("lep_mass")
lep_e = Quantity("lep_e")
lep_charge = Quantity("lep_charge")
lep_mu_index = Quantity("lep_mu_index")
lep_el_index = Quantity("lep_el_index")



# W reco
wlep_p4 = Quantity("wlep_p4")
wlep_pt = Quantity("wlep_pt")
wlep_eta = Quantity("wlep_eta")
wlep_phi = Quantity("wlep_phi")
wlep_mass = Quantity("wlep_mass")
wlep_e = Quantity("wlep_e")
wlep_mt = Quantity("wlep_mt")

# top
is_reco = Quantity("is_reco")
is_jjb = Quantity("is_jjb")
is_jjbb = Quantity("is_jjbb")
is_jjjb = Quantity("is_jjjb")
is_jjjbb = Quantity("is_jjjbb")
reco_p4s = Quantity("reco_p4s")
top_p4 = Quantity("top_p4")
top_pt = Quantity("top_pt")
top_eta = Quantity("top_eta")
top_phi = Quantity("top_phi")
top_mass = Quantity("top_mass")
tb_p4 = Quantity("tb_p4")
tb_pt = Quantity("tb_pt")
tb_eta = Quantity("tb_eta")
tb_phi = Quantity("tb_phi")
tb_mass = Quantity("tb_mass")
sb_p4 = Quantity("sb_p4")
sb_pt = Quantity("sb_pt")
sb_eta = Quantity("sb_eta")
sb_phi = Quantity("sb_phi")
sb_mass = Quantity("sb_mass")

#systs
PSWeight = Quantity("PSWeight_vector")
LHEScaleWeight = Quantity("LHEScaleWeight_vector")
LHEPdfWeight = Quantity("LHEPdfWeight_vector")
puweight = Quantity("puweight")
puweight_up = Quantity("puweight_up")
puweight_down = Quantity("puweight_down")



# DNN vars
dphi_top_b1 = Quantity("DNN_dphi_top_b1")
deta_top_sb = Quantity("DNN_deta_top_sb")
dphi_b1_b2 = Quantity("DNN_dphi_b1_b2")
deta_lep_b1 = Quantity("DNN_deta_lep_b1")
m_lep_b2 = Quantity("DNN_m_lep_b2")
pt_b1_b2 = Quantity("DNN_pt_b1_b2")
costhetastar = Quantity("DNN_costhetastar")
sumht = Quantity("DNN_sumht")
wolfram = Quantity("DNN_wolfram")
deta_topb2_b1 = Quantity("DNN_deta_topb2_b1")

# transformed input vars for DNN evaluation
transformed_pfmet = Quantity("transformed_pfmet")
transformed_top_mass = Quantity("transformed_top_mass")
transformed_dphi_top_b1 = Quantity("transformed_DNN_dphi_top_b1")
transformed_wolfram = Quantity("transformed_DNN_wolfram")
transformed_deta_topb2_b1 = Quantity("transformed_DNN_deta_topb2_b1")
transformed_deta_top_sb = Quantity("transformed_DNN_deta_top_sb")
transformed_dphi_b1_b2 = Quantity("transformed_DNN_dphi_b1_b2")
transformed_lep_pt = Quantity("transformed_lep_pt")
transformed_deta_lep_b1 = Quantity("transformed_DNN_deta_lep_b1")
transformed_m_lep_b2 = Quantity("transformed_DNN_m_lep_b2")
transformed_pt_b1_b2 = Quantity("transformed_DNN_pt_b1_b2")
transformed_costhetastar = Quantity("transformed_DNN_costhetastar")
transformed_sumht = Quantity("transformed_DNN_sumht")
transformed_lep_charge = Quantity("transformed_lep_charge")
transformed_bjet_1_pt = Quantity("transformed_bjet_1_pt")
transformed_bjet_1_eta = Quantity("transformed_bjet_1_eta")
transformed_bjet_2_pt = Quantity("transformed_bjet_2_pt")
transformed_bjet_2_eta = Quantity("transformed_bjet_2_eta")


# lep SFs
lep_sf_mu_trigger_nom = Quantity("lep_sf_mu_trigger_nom")
lep_sf_mu_trigger_up = Quantity("lep_sf_mu_trigger_up")
lep_sf_mu_trigger_down = Quantity("lep_sf_mu_trigger_down")
lep_sf_mu_iso_nom = Quantity("lep_sf_mu_iso_nom")
lep_sf_mu_iso_up = Quantity("lep_sf_mu_iso_up")
lep_sf_mu_iso_down = Quantity("lep_sf_mu_iso_down")
lep_sf_mu_id_nom = Quantity("lep_sf_mu_id_nom")
lep_sf_mu_id_up = Quantity("lep_sf_mu_id_up")
lep_sf_mu_id_down = Quantity("lep_sf_mu_id_down")

lep_sf_el_trigger_nom = Quantity("lep_sf_el_trigger_nom")
lep_sf_el_trigger_up = Quantity("lep_sf_el_trigger_up")
lep_sf_el_trigger_down = Quantity("lep_sf_el_trigger_down")
lep_sf_el_id_nom = Quantity("lep_sf_el_id_nom")
lep_sf_el_id_up = Quantity("lep_sf_el_id_up")
lep_sf_el_id_down = Quantity("lep_sf_el_id_down")
lep_sf_el_reco_nom = Quantity("lep_sf_el_reco_nom")
lep_sf_el_reco_up = Quantity("lep_sf_el_reco_up")
lep_sf_el_reco_down = Quantity("lep_sf_el_reco_down")

# HLT
HLT_match = Quantity("HLT_match")
HLT_Mu20_prescale = Quantity("HLT_Mu20_prescale")

TriggerObject_filterBits_vector = Quantity("TrigObj_filterBits_vector")
TriggerObject_pt_vector = Quantity("TrigObj_pt_vector")
TriggerObject_eta_vector = Quantity("TrigObj_eta_vector")
TriggerObject_phi_vector = Quantity("TrigObj_phi_vector")
TriggerObject_id_vector = Quantity("TrigObj_id_vector")

btag_sf_vec = Quantity("btag_sf_vec")
btag_sf_nom = Quantity("btag_sf_nom")
btag_sf_HFup_corr= Quantity("btag_sf_HFup_corr")
btag_sf_HFup_uncorr= Quantity("btag_sf_HFup_uncorr")
btag_sf_HFdown_corr= Quantity("btag_sf_HFdown_corr")
btag_sf_HFdown_uncorr= Quantity("btag_sf_HFdown_uncorr")
btag_sf_LFup_corr= Quantity("btag_sf_LFup_corr")
btag_sf_LFup_uncorr= Quantity("btag_sf_LFup_uncorr")
btag_sf_LFdown_corr= Quantity("btag_sf_LFdown_corr")
btag_sf_LFdown_uncorr= Quantity("btag_sf_LFdown_uncorr")

nano_mu_pt = Quantity("Nano_Muon_pt")
nano_mu_eta = Quantity("Nano_Muon_eta")
nano_mu_phi = Quantity("Nano_Muon_phi")
nano_mu_mass = Quantity("Nano_Muon_mass")
nano_mu_iso = Quantity("Nano_Muon_pfRelIso04_all")
nano_mu_miniiso = Quantity("Nano_Muon_miniPFRelIso_all")
nano_mu_tightid = Quantity("Nano_Muon_tightId")
nano_el_pt = Quantity("Nano_Electron_pt")
nano_el_eta = Quantity("Nano_Electron_eta")
nano_el_phi = Quantity("Nano_Electron_phi")
nano_el_mass = Quantity("Nano_Electron_mass")
nano_el_detasc = Quantity("Nano_Electron_deltaEtaSC")
nano_el_dxy = Quantity("Nano_Electron_dxy")
nano_el_dz = Quantity("Nano_Electron_dz")
nano_el_iso = Quantity("Nano_Electron_pfRelIso03_all")
nano_el_cutbasedid = Quantity("Nano_Electron_cutBased")
nano_jet_pt = Quantity("Nano_Jet_pt")
nano_jet_eta = Quantity("Nano_Jet_eta")
nano_jet_phi = Quantity("Nano_Jet_phi")
nano_jet_mass = Quantity("Nano_Jet_mass")
nano_jet_btag = Quantity("Nano_Jet_btagDeepFlavB")
nano_jet_id = Quantity("Nano_Jet_jetId")

dnn_output = Quantity("DNN_output")
