import ROOT
import os

path = os.path.dirname(os.path.abspath(__file__))

class sample:
    def __init__(self, color, style, fill, leglabel, label, name=""):
        self.color = color
        self.style = style
        self.fill = fill
        self.leglabel = leglabel
        self.label = label
        if name == "":
            self.name = label
        else:
            self.name = name

tag_2016  = 'RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8'
tag_2017  = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8'
tag1_2017 = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_v2_102X_mc2017_realistic_v8'
tag2_2017 = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8'
tag3_2017 = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8'
tag_2018 = 'RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21'

sampleDict = {'WpWpJJ_EWK_2017': 0, 'WpWpJJ_QCD_2017': 1, 'VBS_SSWW_SM_2017': 2, 'VBS_SSWW_LL_SM_2017': 3, 'VBS_SSWW_TL_SM_2017': 4, 'VBS_SSWW_TT_SM_2017': 5, 'VBS_SSWW_cHW_2017': 6, 'VBS_SSWW_cHW_BSM_2017': 7, 'VBS_SSWW_cHW_INT_2017': 8, 'VBS_SSWW_cW_2017': 9, 'VBS_SSWW_cW_BSM_2017': 10, 'VBS_SSWW_cW_INT_2017': 11, 'VBS_SSWW_cW_cHW_2017': 12, 'VBS_SSWW_DIM6_2017': 13, 'VBS_SSWW_DIM6_SM_2017': 14, 'VBS_SSWW_cHW_SM_2017': 15, 'VBS_SSWW_cW_SM_2017': 16, 'VBS_SSWW_aQGC_2017': 17, 'VBS_SSWW_FS0_25_BSM_2017': 18, 'VBS_SSWW_FS0_25_INT_2017': 19, 'VBS_SSWW_FS0_25_SM_2017': 20, 'VBS_SSWW_FS0_25_2017': 21, 'VBS_SSWW_FS0_5_BSM_2017': 22, 'VBS_SSWW_FS0_5_INT_2017': 23, 'VBS_SSWW_FS0_5_SM_2017': 24, 'VBS_SSWW_FS0_5_2017': 25, 'VBS_SSWW_FS0_0_2017': 26, 'VBS_SSWW_FS1_50_BSM_2017': 27, 'VBS_SSWW_FS1_50_INT_2017': 28, 'VBS_SSWW_FS1_50_SM_2017': 29, 'VBS_SSWW_FS1_50_2017': 30, 'VBS_SSWW_FS1_10_BSM_2017': 31, 'VBS_SSWW_FS1_10_INT_2017': 32, 'VBS_SSWW_FS1_10_SM_2017': 33, 'VBS_SSWW_FS1_10_2017': 34, 'VBS_SSWW_FS1_0_2017': 35, 'VBS_SSWW_FM0_25_BSM_2017': 36, 'VBS_SSWW_FM0_25_INT_2017': 37, 'VBS_SSWW_FM0_25_SM_2017': 38, 'VBS_SSWW_FM0_25_2017': 39, 'VBS_SSWW_FM0_5_BSM_2017': 40, 'VBS_SSWW_FM0_5_INT_2017': 41, 'VBS_SSWW_FM0_5_SM_2017': 42, 'VBS_SSWW_FM0_5_2017': 43, 'VBS_SSWW_FM0_0_2017': 44, 'VBS_SSWW_FM1_25_BSM_2017': 45, 'VBS_SSWW_FM1_25_INT_2017': 46, 'VBS_SSWW_FM1_25_SM_2017': 47, 'VBS_SSWW_FM1_25_2017': 48, 'VBS_SSWW_FM1_5_BSM_2017': 49, 'VBS_SSWW_FM1_5_INT_2017': 50, 'VBS_SSWW_FM1_5_SM_2017': 51, 'VBS_SSWW_FM1_5_2017': 52, 'VBS_SSWW_FM1_0_2017': 53, 'VBS_SSWW_FM6_25_BSM_2017': 54, 'VBS_SSWW_FM6_25_INT_2017': 55, 'VBS_SSWW_FM6_25_SM_2017': 56, 'VBS_SSWW_FM6_25_2017': 57, 'VBS_SSWW_FM6_5_BSM_2017': 58, 'VBS_SSWW_FM6_5_INT_2017': 59, 'VBS_SSWW_FM6_5_SM_2017': 60, 'VBS_SSWW_FM6_5_2017': 61, 'VBS_SSWW_FM6_0_2017': 62, 'VBS_SSWW_FM7_50_BSM_2017': 63, 'VBS_SSWW_FM7_50_INT_2017': 64, 'VBS_SSWW_FM7_50_SM_2017': 65, 'VBS_SSWW_FM7_50_2017': 66, 'VBS_SSWW_FM7_10_BSM_2017': 67, 'VBS_SSWW_FM7_10_INT_2017': 68, 'VBS_SSWW_FM7_10_SM_2017': 69, 'VBS_SSWW_FM7_10_2017': 70, 'VBS_SSWW_FM7_0_2017': 71, 'VBS_SSWW_FT0_2p5_BSM_2017': 72, 'VBS_SSWW_FT0_2p5_INT_2017': 73, 'VBS_SSWW_FT0_2p5_SM_2017': 74, 'VBS_SSWW_FT0_2p5_2017': 75, 'VBS_SSWW_FT0_0p5_BSM_2017': 76, 'VBS_SSWW_FT0_0p5_INT_2017': 77, 'VBS_SSWW_FT0_0p5_SM_2017': 78, 'VBS_SSWW_FT0_0p5_2017': 79, 'VBS_SSWW_FT0_0_2017': 80, 'VBS_SSWW_FT1_1_BSM_2017': 81, 'VBS_SSWW_FT1_1_INT_2017': 82, 'VBS_SSWW_FT1_1_SM_2017': 83, 'VBS_SSWW_FT1_1_2017': 84, 'VBS_SSWW_FT1_0p2_BSM_2017': 85, 'VBS_SSWW_FT1_0p2_INT_2017': 86, 'VBS_SSWW_FT1_0p2_SM_2017': 87, 'VBS_SSWW_FT1_0p2_2017': 88, 'VBS_SSWW_FT1_0_2017': 89, 'VBS_SSWW_FT2_2p5_BSM_2017': 90, 'VBS_SSWW_FT2_2p5_INT_2017': 91, 'VBS_SSWW_FT2_2p5_SM_2017': 92, 'VBS_SSWW_FT2_2p5_2017': 93, 'VBS_SSWW_FT2_0p5_BSM_2017': 94, 'VBS_SSWW_FT2_0p5_INT_2017': 95, 'VBS_SSWW_FT2_0p5_SM_2017': 96, 'VBS_SSWW_FT2_0p5_2017': 97, 'VBS_SSWW_FT2_0_2017': 98, 'DHiggsToWW_2017': 99, 'sm_2017': 100, 'sm_lin_quad_cW_2017': 101, 'quad_cW_2017': 102, 'sm_lin_quad_cHW_2017': 103, 'quad_cHW_2017': 104, 'QCD_2017': 105, 'QCDHT_100to200_2017': 106, 'QCDHT_200to300_2017': 107, 'QCDHT_300to500_2017': 108, 'QCDHT_500to700_2017': 109, 'QCDHT_700to1000_2017': 110, 'QCDHT_1000to1500_2017': 111, 'QCDHT_1500to2000_2017': 112, 'QCDHT_2000toInf_2017': 113, 'ZZtoLep_2017': 114, 'ZZTo2L2Nu_2017': 115, 'ZZJJTo4L_EWK_2017': 116, 'ZZJJTo4L_QCD_2017': 117, 'GluGluToContinToZZTo2e2nu_2017': 118, 'GluGluToContinToZZTo2e2mu_2017': 119, 'GluGluToContinToZZTo2e2tau_2017': 120, 'GluGluToContinToZZTo2mu2nu_2017': 121, 'GluGluToContinToZZTo2mu2tau_2017': 122, 'GluGluToContinToZZTo4e_2017': 123, 'GluGluToContinToZZTo4mu_2017': 124, 'GluGluToContinToZZTo4tau_2017': 125, 'GluGluToContinToZZTo4L_2017': 126, 'TT_2017': 127, 'TT_SemiLep2017': 128, 'TT_Had_2017': 129, 'TTTo2L2Nu_2017': 130, 'TT_beff_2017': 131, 'WJets_2017': 132, 'WJetsHT70to100_2017': 133, 'WJetsHT100to200_2017': 134, 'WJetsHT200to400_2017': 135, 'WJetsHT400to600_2017': 136, 'WJetsHT600to800_2017': 137, 'WJetsHT800to1200_2017': 138, 'WJetsHT1200to2500_2017': 139, 'WJetsHT2500toInf_2017': 140, 'WJets_Fake_2017': 141, 'WJetsHT70to100_Fake_2017': 142, 'WJetsHT100to200_Fake_2017': 143, 'WJetsHT200to400_Fake_2017': 144, 'WJetsHT400to600_Fake_2017': 145, 'WJetsHT600to800_Fake_2017': 146, 'WJetsHT800to1200_Fake_2017': 147, 'WJetsHT1200to2500_Fake_2017': 148, 'WJetsHT2500toInf_Fake_2017': 149, 'DYJetsToLL_2017': 150, 'DY1JetsToLL_2017': 151, 'DY2JetsToLL_2017': 152, 'DY3JetsToLL_2017': 153, 'DY4JetsToLL_2017': 154, 'DYJetsToLLM5to50_2017': 155, 'DYJetsToLL_Fake_2017': 156, 'DY1JetsToLL_Fake_2017': 157, 'DY2JetsToLL_Fake_2017': 158, 'DY3JetsToLL_Fake_2017': 159, 'DY4JetsToLL_Fake_2017': 160, 'VG_2017': 161, 'ZG_2017': 162, 'WG_2017': 163, 'TVX_2017': 164, 'TTGJets_2017': 165, 'TTZToQQ_2017': 166, 'TTZToLLNuNu_2017': 167, 'TTWJetsToQQ_2017': 168, 'TTWJetsToLNu_2017': 169, 'tZq_ll_4f_2017': 170, 'WrongSign_2017': 171, 'WWto2L2Nu_2017': 172, 'GluGluToWWToENuENu_2017': 173, 'GluGluToWWToENuMNu2017': 174, 'GluGluToWWToENuTNu2017': 175, 'GluGluToWWToMNuENu_2017': 176, 'GluGluToWWToMNuMNu2017': 177, 'GluGluToWWToMNuTNu2017': 178, 'GluGluToWWToTNuENu_2017': 179, 'GluGluToWWToTNuMNu2017': 180, 'GluGluToWWToTNuTNu2017': 181, 'STtW_top_2017': 182, 'GluGluHToWWTo2L2Nu_2017': 183, 'GluGluHToZZTo2L2Q_2017': 184, 'GluGluHToZZTo4L_2017': 185, 'GluGluHToTauTau_2017': 186, 'VBFHToWWTo2L2Nu_2017': 187, 'VBFHToTauTau_2017': 188, 'ttHToNonbb_2017': 189, 'VHToNonbb_2017': 190, 'OtherWS_2017': 191, 'Other_2017': 192, 'WWTo2L2Nu_DoubleScattering_2017': 193, 'WWW_4F_2017': 194, 'WWZTo3L1Nu2Q_2017': 195, 'WZZ_2017': 196, 'ZZZ_2017': 197, 'WWG_2017': 198, 'WZ_2017': 199, 'FakeMu_2017': 200, 'DataMu_2017': 201, 'DataMuB_2017': 202, 'DataMuC_2017': 203, 'DataMuD_2017': 204, 'DataMuE_2017': 205, 'DataMuF_2017': 206, 'DataMuFake_2017': 207, 'FakeEle_2017': 208, 'FakeMuPromptTau_2017': 209, 'PromptMuFakeTau_2017': 210, 'FakeMuFakeTau_2017': 211, 'DataEle_2017': 212, 'DataEleB_2017': 213, 'DataEleC_2017': 214, 'DataEleD_2017': 215, 'DataEleE_2017': 216, 'DataEleF_2017': 217, 'DataEleFake_2017': 218, 'MCFake_2017': 219, 'FakeElePromptTau_2017': 220, 'PromptEleFakeTau_2017': 221, 'FakeEleFakeTau_2017': 222, 'DataEleMu_2017': 223, 'FakeEleMu_2017': 224, 'DataTau_2017': 225, 'DataTauB_2017': 226, 'DataTauC_2017': 227, 'DataTauD_2017': 228, 'DataTauE_2017': 229, 'DataTauF_2017': 230, 'DataTauFake_2017': 231, 'DataHT_2017': 232, 'DataHTnoB_2017': 233, 'DataHTB_2017': 234, 'DataHTC_2017': 235, 'DataHTD_2017': 236, 'DataHTE_2017': 237, 'DataHTF_2017': 238, 'DataMET_2017': 239, 'DataMETB_2017': 240, 'DataMETC_2017': 241, 'DataMETD_2017': 242, 'DataMETE_2017': 243, 'DataMETF_2017': 244, 'SampleEleFake_2017': 245, 'SampleMuFake_2017': 246, 'SampleHTFake_2017': 247, 'SampleHTFakepart_2017': 248, 'WpWpJJ_EWK_2018': 249, 'WpWpJJ_QCD_2018': 250, 'VBS_SSWW_SM_2018': 251, 'VBS_SSWW_LL_SM_2018': 252, 'VBS_SSWW_TL_SM_2018': 253, 'VBS_SSWW_TT_SM_2018': 254, 'VBS_SSWW_cHW_2018': 255, 'VBS_SSWW_cHW_BSM_2018': 256, 'VBS_SSWW_cHW_INT_2018': 257, 'VBS_SSWW_cW_2018': 258, 'VBS_SSWW_cW_BSM_2018': 259, 'VBS_SSWW_cW_INT_2018': 260, 'VBS_SSWW_cW_cHW_2018': 261, 'VBS_SSWW_DIM6_2018': 262, 'VBS_SSWW_DIM6_SM_2018': 263, 'VBS_SSWW_cHW_SM_2018': 264, 'VBS_SSWW_cW_SM_2018': 265, 'VBS_SSWW_aQGC_2018': 266, 'VBS_SSWW_FS0_25_BSM_2018': 267, 'VBS_SSWW_FS0_25_INT_2018': 268, 'VBS_SSWW_FS0_25_SM_2018': 269, 'VBS_SSWW_FS0_25_2018': 270, 'VBS_SSWW_FS0_5_BSM_2018': 271, 'VBS_SSWW_FS0_5_INT_2018': 272, 'VBS_SSWW_FS0_5_SM_2018': 273, 'VBS_SSWW_FS0_5_2018': 274, 'VBS_SSWW_FS0_0_2018': 275, 'VBS_SSWW_FS1_50_BSM_2018': 276, 'VBS_SSWW_FS1_50_INT_2018': 277, 'VBS_SSWW_FS1_50_SM_2018': 278, 'VBS_SSWW_FS1_50_2018': 279, 'VBS_SSWW_FS1_10_BSM_2018': 280, 'VBS_SSWW_FS1_10_INT_2018': 281, 'VBS_SSWW_FS1_10_SM_2018': 282, 'VBS_SSWW_FS1_10_2018': 283, 'VBS_SSWW_FS1_0_2018': 284, 'VBS_SSWW_FM0_25_BSM_2018': 285, 'VBS_SSWW_FM0_25_INT_2018': 286, 'VBS_SSWW_FM0_25_SM_2018': 287, 'VBS_SSWW_FM0_25_2018': 288, 'VBS_SSWW_FM0_5_BSM_2018': 289, 'VBS_SSWW_FM0_5_INT_2018': 290, 'VBS_SSWW_FM0_5_SM_2018': 291, 'VBS_SSWW_FM0_5_2018': 292, 'VBS_SSWW_FM0_0_2018': 293, 'VBS_SSWW_FM1_25_BSM_2018': 294, 'VBS_SSWW_FM1_25_INT_2018': 295, 'VBS_SSWW_FM1_25_SM_2018': 296, 'VBS_SSWW_FM1_25_2018': 297, 'VBS_SSWW_FM1_5_BSM_2018': 298, 'VBS_SSWW_FM1_5_INT_2018': 299, 'VBS_SSWW_FM1_5_SM_2018': 300, 'VBS_SSWW_FM1_5_2018': 301, 'VBS_SSWW_FM1_0_2018': 302, 'VBS_SSWW_FM6_25_BSM_2018': 303, 'VBS_SSWW_FM6_25_INT_2018': 304, 'VBS_SSWW_FM6_25_SM_2018': 305, 'VBS_SSWW_FM6_25_2018': 306, 'VBS_SSWW_FM6_5_BSM_2018': 307, 'VBS_SSWW_FM6_5_INT_2018': 308, 'VBS_SSWW_FM6_5_SM_2018': 309, 'VBS_SSWW_FM6_5_2018': 310, 'VBS_SSWW_FM6_0_2018': 311, 'VBS_SSWW_FM7_50_BSM_2018': 312, 'VBS_SSWW_FM7_50_INT_2018': 313, 'VBS_SSWW_FM7_50_SM_2018': 314, 'VBS_SSWW_FM7_50_2018': 315, 'VBS_SSWW_FM7_10_BSM_2018': 316, 'VBS_SSWW_FM7_10_INT_2018': 317, 'VBS_SSWW_FM7_10_SM_2018': 318, 'VBS_SSWW_FM7_10_2018': 319, 'VBS_SSWW_FM7_0_2018': 320, 'VBS_SSWW_FT0_2p5_BSM_2018': 321, 'VBS_SSWW_FT0_2p5_INT_2018': 322, 'VBS_SSWW_FT0_2p5_SM_2018': 323, 'VBS_SSWW_FT0_2p5_2018': 324, 'VBS_SSWW_FT0_0p5_BSM_2018': 325, 'VBS_SSWW_FT0_0p5_INT_2018': 326, 'VBS_SSWW_FT0_0p5_SM_2018': 327, 'VBS_SSWW_FT0_0p5_2018': 328, 'VBS_SSWW_FT0_0_2018': 329, 'VBS_SSWW_FT1_1_BSM_2018': 330, 'VBS_SSWW_FT1_1_INT_2018': 331, 'VBS_SSWW_FT1_1_SM_2018': 332, 'VBS_SSWW_FT1_1_2018': 333, 'VBS_SSWW_FT1_0p2_BSM_2018': 334, 'VBS_SSWW_FT1_0p2_INT_2018': 335, 'VBS_SSWW_FT1_0p2_SM_2018': 336, 'VBS_SSWW_FT1_0p2_2018': 337, 'VBS_SSWW_FT1_0_2018': 338, 'VBS_SSWW_FT2_2p5_BSM_2018': 339, 'VBS_SSWW_FT2_2p5_INT_2018': 340, 'VBS_SSWW_FT2_2p5_SM_2018': 341, 'VBS_SSWW_FT2_2p5_2018': 342, 'VBS_SSWW_FT2_0p5_BSM_2018': 343, 'VBS_SSWW_FT2_0p5_INT_2018': 344, 'VBS_SSWW_FT2_0p5_SM_2018': 345, 'VBS_SSWW_FT2_0p5_2018': 346, 'VBS_SSWW_FT2_0_2018': 347, 'DHiggsToWW_2018': 348, 'sm_2018': 349, 'sm_lin_quad_cW_2018': 350, 'quad_cW_2018': 351, 'sm_lin_quad_cHW_2018': 352, 'quad_cHW_2018': 353, 'QCD_2018': 354, 'QCDHT_100to200_2018': 355, 'QCDHT_200to300_2018': 356, 'QCDHT_300to500_2018': 357, 'QCDHT_500to700_2018': 358, 'QCDHT_700to1000_2018': 359, 'QCDHT_1000to1500_2018': 360, 'QCDHT_1500to2000_2018': 361, 'QCDHT_2000toInf_2018': 362, 'ZZtoLep_2018': 363, 'ZZTo2L2Nu_2018': 364, 'ZZJJTo4L_EWK_2018': 365, 'ZZJJTo4L_QCD_2018': 366, 'GluGluToContinToZZTo2e2nu_2018': 367, 'GluGluToContinToZZTo2e2mu_2018': 368, 'GluGluToContinToZZTo2e2tau_2018': 369, 'GluGluToContinToZZTo2mu2nu_2018': 370, 'GluGluToContinToZZTo2mu2tau_2018': 371, 'GluGluToContinToZZTo4e_2018': 372, 'GluGluToContinToZZTo4mu_2018': 373, 'GluGluToContinToZZTo4tau_2018': 374, 'GluGluToContinToZZTo4L_2018': 375, 'TT_2018': 376, 'TT_SemiLep_2018': 377, 'TT_Had_2018': 378, 'WJets_2018': 379, 'WJetsHT70to100_2018': 380, 'WJetsHT100to200_2018': 381, 'WJetsHT200to400_2018': 382, 'WJetsHT400to600_2018': 383, 'WJetsHT600to800_2018': 384, 'WJetsHT800to1200_2018': 385, 'WJetsHT1200to2500_2018': 386, 'WJetsHT2500toInf_2018': 387, 'DYJetsToLL_2018': 388, 'DY1JetsToLL_2018': 389, 'DY2JetsToLL_2018': 390, 'DY3JetsToLL_2018': 391, 'DY4JetsToLL_2018': 392, 'SampleHTFake_2018': 393, 'VG_2018': 394, 'ZG_2018': 395, 'WG_2018': 396, 'TVX_2018': 397, 'TTGJets_2018': 398, 'TTZToQQ_2018': 399, 'TTZToLLNuNu_2018': 400, 'TTWJetsToQQ_2018': 401, 'TTWJetsToLNu_2018': 402, 'tZq_ll_4f_2018': 403, 'WrongSign_2018': 404, 'WWto2L2Nu_2018': 405, 'GluGluToWWToENuENu_2018': 406, 'GluGluToWWToMNuENu_2018': 407, 'GluGluToWWToTNuENu_2018': 408, 'STtW_top_2018': 409, 'GluGluHToWWTo2L2Nu_2018': 410, 'GluGluHToZZTo2L2Q_2018': 411, 'GluGluHToZZTo4L_2018': 412, 'GluGluHToTauTau_2018': 413, 'VBFHToWWTo2L2Nu_2018': 414, 'VBFHToTauTau_2018': 415, 'ttHToNonbb_2018': 416, 'VHToNonbb_2018': 417, 'OtherWS_2018': 418, 'Other_2018': 419, 'WWTo2L2Nu_DoubleScattering_2018': 420, 'WWW_4F_2018': 421, 'WWZTo3L1Nu2Q_2018': 422, 'WZZ_2018': 423, 'ZZZ_2018': 424, 'WWG_2018': 425, 'TTTo2L2Nu_2018': 426, 'WZ_2018': 427, 'FakeMu_2018': 428, 'DataMu_2018': 429, 'DataMuA_2018': 430, 'DataMuB_2018': 431, 'DataMuC_2018': 432, 'DataMuD_2018': 433, 'FakeEle_2018': 434, 'FakeMuPromptTau_2018': 435, 'PromptMuFakeTau_2018': 436, 'FakeMuFakeTau_2018': 437, 'DataEle_2018': 438, 'DataEleA_2018': 439, 'DataEleB_2018': 440, 'DataEleC_2018': 441, 'DataEleD_2018': 442, 'FakeElePromptTau_2018': 443, 'PromptEleFakeTau_2018': 444, 'FakeEleFakeTau_2018': 445, 'DataHT_2018': 446, 'DataHTA_2018': 447, 'DataHTB_2018': 448, 'DataHTC_2018': 449, 'DataHTD_2018': 450}

###################################################################################################################################################################
############################################################                                           ############################################################
############################################################                    2016                   ############################################################
############################################################                                           ############################################################
###################################################################################################################################################################
################################ TTbar ################################

'''
TT_DiLep_2016 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_DiLep_2016")
TT_DiLep_2016.sigma = 831.76 #pb
TT_DiLep_2016.year = 2016
TT_DiLep_2016.dataset = "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+tag_2016+"-v1/NANOAODSIM"
# /TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM
'''

################################ WJets ################################
WJetsHT70to100_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT70to100_2016")
WJetsHT70to100_2016.sigma = 1353.0 * 1.21 #pb
WJetsHT70to100_2016.year = 2016
WJetsHT70to100_2016.dataset = "/WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+tag_2016+"-v1/NANOAODSIM"
WJetsHT100to200_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT100to200_2016")
WJetsHT100to200_2016.sigma = 1345 * 1.21 #pb
WJetsHT100to200_2016.year = 2016
WJetsHT100to200_2016.dataset = "/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+tag_2016+"-v1/NANOAODSIM"
WJetsHT200to400_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT200to400_2016")
WJetsHT200to400_2016.sigma = 359.7 * 1.21 #pb
WJetsHT200to400_2016.year = 2016
WJetsHT200to400_2016.dataset = "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+tag_2016+"-v1/NANOAODSIM"
#WJetsHT200to400_2016.files = jr.json_reader(path+"/WJets_HT200To400_2016.json")
WJetsHT400to600_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT400to600_2016")
WJetsHT400to600_2016.sigma = 48.91 * 1.21 #pb
WJetsHT400to600_2016.year = 2016
WJetsHT400to600_2016.dataset = "/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+tag_2016+"-v1/NANOAODSIM"
#WJetsHT400to600_2016.files = jr.json_reader(path+"/WJets_HT400To600_2016.json")
WJetsHT600to800_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT600to800_2016")
WJetsHT600to800_2016.sigma = 12.05 * 1.21 #pb
WJetsHT600to800_2016.year = 2016
WJetsHT600to800_2016.dataset = "/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+tag_2016+"-v1/NANOAODSIM"
#WJetsHT600to800_2016.files = jr.json_reader(path+"/WJets_HT600To800_2016.json")
WJetsHT800to1200_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT800to1200_2016")
WJetsHT800to1200_2016.sigma = 5.501 * 1.21 #pb
WJetsHT800to1200_2016.year = 2016
WJetsHT800to1200_2016.dataset = "/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+tag_2016+"-v1/NANOAODSIM"
#WJetsHT800to1200_2016.files = jr.json_reader(path+"/WJets_HT800To1200_2016.json")
WJetsHT1200to2500_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT1200to2500_2016")
WJetsHT1200to2500_2016.sigma = 1.329 * 1.21 #pb
WJetsHT1200to2500_2016.year = 2016
WJetsHT1200to2500_2016.dataset = "/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+tag_2016+"-v1/NANOAODSIM"
#WJetsHT1200to2500_2016.files = jr.json_reader(path+"/WJets_HT1200To2500_2016.json")
WJetsHT2500toInf_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT2500toInf_2016")
WJetsHT2500toInf_2016.sigma = 0.03216 * 1.21 #pb
WJetsHT2500toInf_2016.year = 2016
WJetsHT2500toInf_2016.dataset = "/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+tag_2016+"-v1/NANOAODSIM"
#WJetsHT2500toInf_2016.files = jr.json_reader(path+"/WJets_HT2500ToInf_2016.json")

WJets_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJets_2016")
WJets_2016.year = 2016
WJets_2016.components = [WJetsHT70to100_2016, WJetsHT100to200_2016, WJetsHT200to400_2016, WJetsHT400to600_2016, WJetsHT600to800_2016, WJetsHT800to1200_2016, WJetsHT1200to2500_2016, WJetsHT2500toInf_2016]
#WJets_2016.components = [WJetsHT100to200_2016, WJetsHT200to400_2016, WJetsHT400to600_2016, WJetsHT600to800_2016, WJetsHT800to1200_2016, WJetsHT1200to2500_2016, WJetsHT2500toInf_2016]

################################ WZ ################################
WZ_2016 = sample(ROOT.kYellow, 1, 1001, "WZ", "WZ_2016")
WZ_2016.sigma = 47.13
WZ_2016.year = 2016
WZ_2016.dataset = "/WZ_TuneCUETP8M1_13TeV-pythia8/" + tag_2016 + "-v1/NANOAODSIM"

################################ DrellYan ################################
DY1JetsToLL_2016 = sample(ROOT.kAzure+6, 1, 1001, "DY + 1 Jet", "DY1JetsToLL_2016")
DY1JetsToLL_2016.sigma = 1012.0
DY1JetsToLL_2016.year = 2016
DY1JetsToLL_2016.dataset = "/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/" + tag_2016 + "-v1/NANOAODSIM"

DY2JetsToLL_2016 = sample(ROOT.kAzure+6, 1, 1001, "DY + 2 Jets", "DY2JetsToLL_2016")
DY2JetsToLL_2016.sigma = 330.4
DY2JetsToLL_2016.year = 2016
DY2JetsToLL_2016.dataset = "/DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/" + tag_2016 + "-v1/NANOAODSIM"

DY3JetsToLL_2016 = sample(ROOT.kAzure+6, 1, 1001, "DY + 3 Jets", "DY3JetsToLL_2016")
DY3JetsToLL_2016.sigma = 101.8
DY3JetsToLL_2016.year = 2016
DY3JetsToLL_2016.dataset = "/DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/" + tag_2016 + "-v1/NANOAODSIM"

DY4JetsToLL_2016 = sample(ROOT.kAzure+6, 1, 1001, "DY + 4+ Jets", "DY4JetsToLL_2016")
DY4JetsToLL_2016.sigma = 54.80
DY4JetsToLL_2016.year = 2016
DY4JetsToLL_2016.dataset = "/DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/" + tag_2016 + "-v1/NANOAODSIM"

DYJetsToLL_2016 = sample(ROOT.kAzure+6, 1, 1001, "DY + Jets", "DYJetsToLL_2016")
DYJetsToLL_2016.year = 2016
DYJetsToLL_2016.components = [DY1JetsToLL_2016, DY2JetsToLL_2016, DY3JetsToLL_2016, DY4JetsToLL_2016]

################################ ssWW EWK ################################
WpWpJJ_EWK_2016 = sample(ROOT.kRed, 1, 1001, "EW ssWW", "WpWpJJ_EWK_2016")
WpWpJJ_EWK_2016.sigma = 0.01927
WpWpJJ_EWK_2016.year = 2016
WpWpJJ_EWK_2016.dataset = "/WpWpJJ_EWK_TuneCUETP8M1_13TeV-powheg-pythia8/" + tag_2016 + "-v1/NANOAODSIM"

WpWpJJ_QCD_2016 = sample(ROOT.kBlue, 1, 1001, "QCD ssWW", "WpWpJJ_QCD_2016")
WpWpJJ_QCD_2016.sigma = 0.02612
WpWpJJ_QCD_2016.year = 2016
WpWpJJ_QCD_2016.dataset = "/WpWpJJ_QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/" + tag_2016 + "-v1/NANOAODSIM"

###################################################################################################################################################################
############################################################                                           ############################################################
############################################################                    2017                   ############################################################
############################################################                                           ############################################################
###################################################################################################################################################################

################################ QCD ################################
QCDHT_100to200_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_100to200_2017")
QCDHT_100to200_2017.year = 2017
QCDHT_100to200_2017.dataset = "/QCD_HT100to200_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"
QCDHT_100to200_2017.sigma = 23700000.0 #pb                                                     

QCDHT_200to300_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_200to300_2017")
QCDHT_200to300_2017.year = 2017
QCDHT_200to300_2017.dataset = "/QCD_HT200to300_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"
QCDHT_200to300_2017.sigma = 1547000.0 #pb                                                     

QCDHT_300to500_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_300to500_2017")
QCDHT_300to500_2017.year = 2017
QCDHT_300to500_2017.dataset = "/QCD_HT300to500_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"
QCDHT_300to500_2017.sigma = 322600.0 #pb                                                    

QCDHT_500to700_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_500to700_2017")
QCDHT_500to700_2017.year = 2017
QCDHT_500to700_2017.dataset = "/QCD_HT500to700_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"
QCDHT_500to700_2017.sigma = 29980.0 #pb                                                     

QCDHT_700to1000_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_700to1000_2017")
QCDHT_700to1000_2017.year = 2017
QCDHT_700to1000_2017.dataset = "/QCD_HT700to1000_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"
QCDHT_700to1000_2017.sigma = 6334.0 #pb                                                     

QCDHT_1000to1500_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1000to1500_2017")
QCDHT_1000to1500_2017.year = 2017
QCDHT_1000to1500_2017.dataset = "/QCD_HT1000to1500_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"
QCDHT_1000to1500_2017.sigma = 1088.0 #pb                                                     

QCDHT_1500to2000_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1500to2000_2017")
QCDHT_1500to2000_2017.year = 2017
QCDHT_1500to2000_2017.dataset = "/QCD_HT1500to2000_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"
QCDHT_1500to2000_2017.sigma = 99.11 #pb                                                     

QCDHT_2000toInf_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_2000toInf_2017")
QCDHT_2000toInf_2017.year = 2017
QCDHT_2000toInf_2017.dataset = "/QCD_HT2000toInf_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"
QCDHT_2000toInf_2017.sigma = 20.23 #pb                                                     

QCD_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2017")
QCD_2017.year = 2017
QCD_2017.components = [QCDHT_100to200_2017, QCDHT_200to300_2017, QCDHT_300to500_2017, QCDHT_500to700_2017, QCDHT_700to1000_2017, QCDHT_1000to1500_2017, QCDHT_1500to2000_2017, QCDHT_2000toInf_2017]

################################ ZZ ################################
ZZTo2L2Nu_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "ZZTo2L2Nu_2017")
ZZTo2L2Nu_2017.year = 2017
ZZTo2L2Nu_2017.dataset = "/ZZTo2L2Nu_13TeV_powheg_pythia8/" + tag_2017 + "-v1/NANOAODSIM"
ZZTo2L2Nu_2017.sigma = 0.5644 #pb                                                     

ZZJJTo4L_EWK_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "ZZJJTo4L_EWK_2017")
ZZJJTo4L_EWK_2017.year = 2017
ZZJJTo4L_EWK_2017.dataset = "/ZZJJTo4L_EWK_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"
ZZJJTo4L_EWK_2017.sigma = 0.0004536 #pb

ZZJJTo4L_QCD_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "ZZJJTo4L_QCD_2017")
ZZJJTo4L_QCD_2017.year = 2017
ZZJJTo4L_QCD_2017.dataset = "/ZZJJTo4L_QCD_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"
ZZJJTo4L_QCD_2017.sigma = 0.008348 #pb

GluGluToContinToZZTo2e2nu_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo2e2nu_2017")
GluGluToContinToZZTo2e2nu_2017.year = 2017
GluGluToContinToZZTo2e2nu_2017.dataset = "/GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8/" + tag3_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo2e2nu_2017.sigma = 14.93 #pb

GluGluToContinToZZTo2e2mu_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo2e2mu_2017")
GluGluToContinToZZTo2e2mu_2017.year = 2017
GluGluToContinToZZTo2e2mu_2017.dataset = "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/" + tag3_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo2e2mu_2017.sigma = 3.185 #pb

GluGluToContinToZZTo2e2tau_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo2e2tau_2017")
GluGluToContinToZZTo2e2tau_2017.year = 2017
GluGluToContinToZZTo2e2tau_2017.dataset = "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/" + tag3_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo2e2tau_2017.sigma = 3.185 #pb

GluGluToContinToZZTo2mu2nu_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo2mu2nu_2017")
GluGluToContinToZZTo2mu2nu_2017.year = 2017
GluGluToContinToZZTo2mu2nu_2017.dataset = "/GluGluToContinToZZTo2mu2nu_13TeV_MCFM701_pythia8/" + tag3_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo2mu2nu_2017.sigma = 14.93 #pb

GluGluToContinToZZTo2mu2tau_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo2mu2tau_2017")
GluGluToContinToZZTo2mu2tau_2017.year = 2017
GluGluToContinToZZTo2mu2tau_2017.dataset = "/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/" + tag3_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo2mu2tau_2017.sigma = 3.185 #pb

GluGluToContinToZZTo4e_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo4e_2017")
GluGluToContinToZZTo4e_2017.year = 2017
GluGluToContinToZZTo4e_2017.dataset = "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/" + tag3_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo4e_2017.sigma = 1.404 #pb

GluGluToContinToZZTo4mu_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo4mu_2017")
GluGluToContinToZZTo4mu_2017.year = 2017
GluGluToContinToZZTo4mu_2017.dataset = "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/" + tag3_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo4mu_2017.sigma = 1.404 #pb

GluGluToContinToZZTo4tau_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo4tau_2017")
GluGluToContinToZZTo4tau_2017.year = 2017
GluGluToContinToZZTo4tau_2017.dataset = "/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/" + tag_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo4tau_2017.sigma = 1.404 #pb

GluGluToContinToZZTo4L_2017 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo4L_2017")
GluGluToContinToZZTo4L_2017.year = 2017
GluGluToContinToZZTo4L_2017.dataset = "/GluGluToContinToZZTo4L_13TeV_TuneCP5_madgraphMLM_pythia8/" + tag_2017 + "-v1/NANOAODSIM"
GluGluToContinToZZTo4L_2017.sigma = 0.7882 #pb

ZZtoLep_2017 = sample(ROOT.kViolet-9, 1, 1001, "ZZ", "ZZtoLep_2017")
ZZtoLep_2017.year = 2017
ZZtoLep_2017.components = [ZZTo2L2Nu_2017, ZZJJTo4L_EWK_2017, ZZJJTo4L_QCD_2017, GluGluToContinToZZTo2e2nu_2017, GluGluToContinToZZTo2e2mu_2017, GluGluToContinToZZTo2e2tau_2017, GluGluToContinToZZTo2mu2nu_2017, GluGluToContinToZZTo2mu2tau_2017, GluGluToContinToZZTo4e_2017, GluGluToContinToZZTo4mu_2017, GluGluToContinToZZTo4tau_2017]

################################ TTbar ################################
TT_Mtt700to1000_2017 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t}", "TT_Mtt700to1000_2017")
TT_Mtt700to1000_2017.sigma = 80.5 #pb
TT_Mtt700to1000_2017.year = 2017
TT_Mtt700to1000_2017.dataset = "/TT_Mtt-700to1000_TuneCP5_PSweights_13TeV-powheg-pythia8/"+tag_2017+"-extv1/NANOAODSIM"
#TT_Mtt700to1000_2017.files = jr.json_reader(path+"/TT_Mtt700to1000_2017.json")

TT_Mtt1000toInf_2017 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t}", "TT_Mtt1000toInf_2017")
TT_Mtt1000toInf_2017.sigma = 21.3 #pb
TT_Mtt1000toInf_2017.year = 2017
TT_Mtt1000toInf_2017.dataset = "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#TT_Mtt1000toInf_2017.files = jr.json_reader(path+"/TT_Mtt1000toInf_2017.json")

TT_Mtt_2017 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t}", "TT_Mtt_2017")
TT_Mtt_2017.year = 2017
TT_Mtt_2017.components = [TT_Mtt700to1000_2017, TT_Mtt1000toInf_2017]

'''
TT_DiLep_2017 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t} DiLep", "TT_DiLep_2017")
TT_DiLep_2017.sigma =  88.287 #pb
TT_DiLep_2017.year = 2017
TT_DiLep_2017.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/"+tag2_2017+"-v1/NANOAODSIM"
'''

TT_SemiLep_2017 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t} SemiLep", "TT_SemiLep2017")
TT_SemiLep_2017.sigma = 365.3
TT_SemiLep_2017.year = 2017
TT_SemiLep_2017.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/"+tag2_2017+"-v1/NANOAODSIM"

TT_Had_2017 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t} had", "TT_Had_2017")
TT_Had_2017.sigma =  377.96 #pb
TT_Had_2017.year = 2017
TT_Had_2017.dataset = "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/"+tag2_2017+"-v2/NANOAODSIM"

TTTo2L2Nu_2017 = sample(ROOT.kAzure-9, 1, 1001, "t#bar{t} DiLep", "TTTo2L2Nu_2017")
TTTo2L2Nu_2017.sigma =  88.287 #pb
TTTo2L2Nu_2017.year = 2017
TTTo2L2Nu_2017.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/"+tag2_2017+"-v1/NANOAODSIM"

TT_2017 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t} FH+SL", "TT_2017")
TT_2017.year = 2017
TT_2017.components = [TT_SemiLep_2017, TT_Had_2017]#TT_DiLep_2017,

TT_beff_2017 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t} FH+SL", "TT_2017")
TT_beff_2017.year = 2017
TT_beff_2017.components = [TT_SemiLep_2017, TT_Had_2017, TTTo2L2Nu_2017]

###############################  NEW  ################################
###############################  TVX  ################################
TTGJets_2017 = sample(ROOT.kRed-2, 1, 1001, "t#bar{t}#gamma + jets", "TTGJets_2017")
TTGJets_2017.sigma = 4.078
TTGJets_2017.year = 2017
TTGJets_2017.dataset = "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/"+tag3_2017+"_ext1-v1/NANOAODSIM"

TTZToQQ_2017 = sample(ROOT.kRed-2, 1, 1001, "t#bar{t}Z->q#bar{q}", "TTZToQQ_2017")
TTZToQQ_2017.sigma = 0.5104
TTZToQQ_2017.year = 2017
TTZToQQ_2017.dataset = "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/"+tag_2017+"_ext1-v1/NANOAODSIM"

TTZToLLNuNu_2017 = sample(ROOT.kRed-2, 1, 1001, "t#bar{t}Z to #ell#ell#nu#nu ", "TTZToLLNuNu_2017")
TTZToLLNuNu_2017.sigma = 0.2432
TTZToLLNuNu_2017.year = 2017
TTZToLLNuNu_2017.dataset = "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/"+tag3_2017+"-v1/NANOAODSIM"

TTWJetsToQQ_2017 = sample(ROOT.kRed-2, 1, 1001, "t#bar{t}W + jets to qq ", "TTWJetsToQQ_2017")
TTWJetsToQQ_2017.sigma = 0.4316
TTWJetsToQQ_2017.year = 2017
TTWJetsToQQ_2017.dataset = "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/"+tag_2017+"-v1/NANOAODSIM"

TTWJetsToLNu_2017 = sample(ROOT.kRed-2, 1, 1001, "t#bar{t}W+jets to #ell#nu ", "TTWJetsToLNu_2017")
TTWJetsToLNu_2017.sigma = 0.2149
TTWJetsToLNu_2017.year = 2017
TTWJetsToLNu_2017.dataset = "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/"+tag3_2017+"-v1/NANOAODSIM"

tZq_ll_4f_2017 = sample(ROOT.kRed-2, 1, 1001, "tZq to #ell#ell ", "tZq_ll_4f_2017")
tZq_ll_4f_2017.sigma = 0.07358
tZq_ll_4f_2017.year = 2017
tZq_ll_4f_2017.dataset = "/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/"+tag2_2017+"-v1/NANOAODSIM"

TVX_2017 = sample(ROOT.kCyan-7, 1, 1001, "tVX", "TVX_2017")
TVX_2017.year = 2017
TVX_2017.components = [TTGJets_2017, TTZToQQ_2017, TTZToLLNuNu_2017, TTWJetsToQQ_2017, TTWJetsToLNu_2017, tZq_ll_4f_2017]

###############################  NEW     ################################
###############################  VGamma  ################################

ZG_2017 = sample(ROOT.kSpring+7, 1, 1001, "Z #gamma", "ZG_2017")
ZG_2017.sigma = 0.1097
ZG_2017.year = 2017
ZG_2017.dataset = "/LLAJJ_EWK_MLL-50_MJJ-120_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"_ext1-v1/NANOAODSIM"

WG_2017 = sample(ROOT.kSpring+7, 1, 1001, "W #gamma", "WG_2017")
WG_2017.sigma = 0.5439
WG_2017.year = 2017
WG_2017.dataset = "/LNuAJJ_EWK_MJJ-120_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

VG_2017 = sample(ROOT.kSpring+7, 1, 1001, "V#gamma", "VG_2017")
VG_2017.year = 2017
VG_2017.components = [ZG_2017, WG_2017]



###############################      NEW    ################################
###############################  Wrong Sign ################################

WWto2L2Nu_2017 = sample(ROOT.kAzure-9, 1, 1001, "WWto2L2Nu", "WWto2L2Nu_2017")
WWto2L2Nu_2017.sigma = 11.08
WWto2L2Nu_2017.year = 2017
WWto2L2Nu_2017.dataset = "/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToENuENu_2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToENuENu", "GluGluToWWToENuENu_2017")
GluGluToWWToENuENu_2017.sigma = 45.62 * 1./9. * 1.4
GluGluToWWToENuENu_2017.year = 2017
GluGluToWWToENuENu_2017.dataset = "/GluGluToWWToENEN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToENuMNu2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToENuENu", "GluGluToWWToENuMNu2017")
GluGluToWWToENuMNu2017.sigma = 45.62 * 1./9. * 1.4
GluGluToWWToENuMNu2017.year = 2017
GluGluToWWToENuMNu2017.dataset = "/GluGluToWWToENMN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToENuTNu2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToENuENu", "GluGluToWWToENuTNu2017")
GluGluToWWToENuTNu2017.sigma = 45.62 * 1./9. * 1.4
GluGluToWWToENuTNu2017.year = 2017
GluGluToWWToENuTNu2017.dataset = "/GluGluToWWToENTN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToMNuENu_2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToMNuENu", "GluGluToWWToMNuENu_2017")
GluGluToWWToMNuENu_2017.sigma = 45.62 * 1./9. * 1.4
GluGluToWWToMNuENu_2017.year = 2017
GluGluToWWToMNuENu_2017.dataset = "/GluGluToWWToMNEN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToMNuMNu2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToMNuENu", "GluGluToWWToMNuMNu2017")
GluGluToWWToMNuMNu2017.sigma = 45.62 * 1./9. * 1.4
GluGluToWWToMNuMNu2017.year = 2017
GluGluToWWToMNuMNu2017.dataset = "/GluGluToWWToMNMN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToMNuTNu2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToMNuENu", "GluGluToWWToMNuTNu2017")
GluGluToWWToMNuTNu2017.sigma = 45.62 * 1./9. * 1.4
GluGluToWWToMNuTNu2017.year = 2017
GluGluToWWToMNuTNu2017.dataset = "/GluGluToWWToMNTN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToTNuENu_2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToTNuENu", "GluGluToWWToTNuENu_2017")
GluGluToWWToTNuENu_2017.sigma = 45.62 * 1./9. * 1.4
GluGluToWWToTNuENu_2017.year = 2017
GluGluToWWToTNuENu_2017.dataset = "/GluGluToWWToTNEN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToTNuMNu2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToTNuENu", "GluGluToWWToTNuMNu2017")
GluGluToWWToTNuMNu2017.sigma = 45.62 * 1./9. * 1.4
GluGluToWWToTNuMNu2017.year = 2017
GluGluToWWToTNuMNu2017.dataset = "/GluGluToWWToTNMN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluToWWToTNuTNu2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToTNuENu", "GluGluToWWToTNuTNu2017")
GluGluToWWToTNuTNu2017.sigma = 45.62 * 1./9. * 1.4
GluGluToWWToTNuTNu2017.year = 2017
GluGluToWWToTNuTNu2017.dataset = "/GluGluToWWToTNTN_13TeV_MCFM701_pythia8/"+tag_2017+"-v1/NANOAODSIM"

STtW_top_2017 = sample(ROOT.kAzure-9, 1, 1001, "single t", "STtW_top_2017")
STtW_top_2017.sigma =  34.91#pb
STtW_top_2017.year = 2017
STtW_top_2017.dataset = "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/"+tag_2017+"-v1/NANOAODSIM"

STtW_antitop_2017 = sample(ROOT.kAzure-9, 1, 1001, "single t", "STtW_antitop_2017")
STtW_antitop_2017.sigma =  34.97#pb
STtW_antitop_2017.year = 2017
STtW_antitop_2017.dataset = "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluHToWWTo2L2Nu_2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluHToWWTo2L2Nu", "GluGluHToWWTo2L2Nu_2017")
GluGluHToWWTo2L2Nu_2017.sigma =  28.87#pb
GluGluHToWWTo2L2Nu_2017.year = 2017
GluGluHToWWTo2L2Nu_2017.dataset = "/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/"+tag_2017+"-v1/NANOAODSIM"

GluGluHToZZTo2L2Q_2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluHToZZTo2L2Q", "GluGluHToZZTo2L2Q_2017")
GluGluHToZZTo2L2Q_2017.sigma =  28.87#pb
GluGluHToZZTo2L2Q_2017.year = 2017
GluGluHToZZTo2L2Q_2017.dataset = "/GluGluHToZZTo2L2Q_M125_13TeV_powheg2_JHUGenV7011_pythia8/"+tag3_2017+"-v1/NANOAODSIM"

GluGluHToZZTo4L_2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluHToZZTo4L", "GluGluHToZZTo4L_2017")
GluGluHToZZTo4L_2017.sigma =  28.87#pb
GluGluHToZZTo4L_2017.year = 2017
GluGluHToZZTo4L_2017.dataset = "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/"+tag_2017+"_ext3-v1/NANOAODSIM"

GluGluHToTauTau_2017 = sample(ROOT.kAzure-9, 1, 1001, "GluGluHToTauTau", "GluGluHToTauTau_2017")
GluGluHToTauTau_2017.sigma =  30.52#pb
GluGluHToTauTau_2017.year = 2017
GluGluHToTauTau_2017.dataset = "/GluGluHToTauTau_M125_13TeV_powheg_pythia8/"+tag2_2017+"-v1/NANOAODSIM"

VBFHToWWTo2L2Nu_2017 = sample(ROOT.kAzure-9, 1, 1001, "VBFHToWWTo2L2Nu", "VBFHToWWTo2L2Nu_2017")
VBFHToWWTo2L2Nu_2017.sigma =  3.879#pb
VBFHToWWTo2L2Nu_2017.year = 2017
VBFHToWWTo2L2Nu_2017.dataset = "/VBFHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/"+tag_2017+"-v1/NANOAODSIM"

VBFHToTauTau_2017 = sample(ROOT.kAzure-9, 1, 1001, "VBFHToTauTau", "VBFHToTauTau_2017")
VBFHToTauTau_2017.sigma =  3.879#pb
VBFHToTauTau_2017.year = 2017
VBFHToTauTau_2017.dataset = "/VBFHToTauTau_M125_13TeV_amcatnloFXFX_pythia8/"+tag_2017+"-v1/NANOAODSIM"

ttHToNonbb_2017 = sample(ROOT.kAzure-9, 1, 1001, "ttHToNonbb", "ttHToNonbb_2017")
ttHToNonbb_2017.sigma =  0.5269#pb
ttHToNonbb_2017.year = 2017
ttHToNonbb_2017.dataset = "/ttHToNonbb_M125_TuneCP5_PSweights_13TeV-powheg-pythia8/"+tag_2017+"-v1/NANOAODSIM"

VHToNonbb_2017 = sample(ROOT.kAzure-9, 1, 1001, "VHToNonbb", "VHToNonbb_2017")
VHToNonbb_2017.sigma =  2.127#pb
VHToNonbb_2017.year = 2017
VHToNonbb_2017.dataset = "/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/"+tag_2017+"-v1/NANOAODSIM"

WrongSign_2017 = sample(ROOT.kGreen-10, 1, 1001, "Wrong Sign", "WrongSign_2017")
WrongSign_2017.year = 2017
WrongSign_2017.components = [WWto2L2Nu_2017, GluGluToWWToENuENu_2017, GluGluToWWToENuMNu2017, 
                            GluGluToWWToENuTNu2017, GluGluToWWToMNuENu_2017, GluGluToWWToMNuMNu2017, 
                            GluGluToWWToMNuTNu2017, GluGluToWWToTNuENu_2017, GluGluToWWToTNuMNu2017, 
                            GluGluToWWToTNuTNu2017, STtW_top_2017, GluGluHToWWTo2L2Nu_2017, 
                            GluGluHToZZTo2L2Q_2017, GluGluHToZZTo4L_2017, GluGluHToTauTau_2017, 
                            VBFHToWWTo2L2Nu_2017, VBFHToTauTau_2017, ttHToNonbb_2017, VHToNonbb_2017]


###############################      NEW    ################################
###############################     Other   ################################


WWTo2L2Nu_DoubleScattering_2017 = sample(ROOT.kOrange-4, 1, 1001, "WWTo2L2Nu_DoubleScattering", "WWTo2L2Nu_DoubleScattering_2017")
WWTo2L2Nu_DoubleScattering_2017.sigma =  0.1703#pb
WWTo2L2Nu_DoubleScattering_2017.year = 2017
WWTo2L2Nu_DoubleScattering_2017.dataset = "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/"+tag_2017+"-v1/NANOAODSIM"

WWW_4F_2017 = sample(ROOT.kOrange-4, 1, 1001, "WWW_4F", "WWW_4F_2017")
WWW_4F_2017.sigma =  0.2086#pb
WWW_4F_2017.year = 2017
WWW_4F_2017.dataset = "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/"+tag3_2017+"-v1/NANOAODSIM"

WWZTo3L1Nu2Q_2017 = sample(ROOT.kOrange-4, 1, 1001, "WWZTo3L1Nu2Q", "WWZTo3L1Nu2Q_2017")
WWZTo3L1Nu2Q_2017.sigma =  0.008039#pb
WWZTo3L1Nu2Q_2017.year = 2017
WWZTo3L1Nu2Q_2017.dataset = "/WWZTo3L1Nu2Q_4f_TuneCP5_13TeV_amcatnlo_pythia8/"+tag_2017+"-v1/NANOAODSIM"


WZZ_2017 = sample(ROOT.kOrange-4, 1, 1001, "WZZ", "WZZ_2017")
WZZ_2017.sigma =  0.05565#pb
WZZ_2017.year = 2017
WZZ_2017.dataset = "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/"+tag3_2017+"-v1/NANOAODSIM"


ZZZ_2017 = sample(ROOT.kOrange-4, 1, 1001, "ZZZ", "ZZZ_2017")
ZZZ_2017.sigma =  0.013989#pb
ZZZ_2017.year = 2017
ZZZ_2017.dataset = "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/"+tag3_2017+"-v1/NANOAODSIM"

WWG_2017 = sample(ROOT.kOrange-4, 1, 1001, "WWG", "WWG_2017")
WWG_2017.sigma =  0.2147#pb
WWG_2017.year = 2017
WWG_2017.dataset = "/WWG_TuneCP5_13TeV-amcatnlo-pythia8/"+tag3_2017+"-v1/NANOAODSIM"

Other_2017 = sample(ROOT.kOrange-4, 1, 1001, "Other", "Other_2017")
Other_2017.year = 2017
Other_2017.components = [WWTo2L2Nu_DoubleScattering_2017, WWW_4F_2017, WWZTo3L1Nu2Q_2017, WZZ_2017, ZZZ_2017, WWG_2017]

OtherWS_2017 = sample(ROOT.kOrange-4, 1, 1001, "Other + Wrong Sign", "OtherWS_2017")
OtherWS_2017.year = 2017
OtherWS_2017.components = [WWTo2L2Nu_DoubleScattering_2017, WWW_4F_2017, WWZTo3L1Nu2Q_2017, WZZ_2017, ZZZ_2017, WWG_2017,
                           WWto2L2Nu_2017, GluGluToWWToENuENu_2017, GluGluToWWToENuMNu2017, 
                           GluGluToWWToENuTNu2017, GluGluToWWToMNuENu_2017, GluGluToWWToMNuMNu2017, 
                           GluGluToWWToMNuTNu2017, GluGluToWWToTNuENu_2017, GluGluToWWToTNuMNu2017, 
                           GluGluToWWToTNuTNu2017, STtW_top_2017, GluGluHToWWTo2L2Nu_2017, 
                           GluGluHToZZTo2L2Q_2017, GluGluHToZZTo4L_2017, GluGluHToTauTau_2017, 
                           VBFHToWWTo2L2Nu_2017, VBFHToTauTau_2017, ttHToNonbb_2017, VHToNonbb_2017]
################################ WJets ################################
WJetsHT70to100_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT70to100_2017")
WJetsHT70to100_2017.sigma = 1353 * 1.21 #pb
WJetsHT70to100_2017.year = 2017
WJetsHT70to100_2017.dataset = "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

WJetsHT100to200_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT100to200_2017")
WJetsHT100to200_2017.sigma = 1345 * 1.21 #pb
WJetsHT100to200_2017.year = 2017
WJetsHT100to200_2017.dataset = "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

WJetsHT200to400_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT200to400_2017")
WJetsHT200to400_2017.sigma = 359.7 * 1.21 #pb
WJetsHT200to400_2017.year = 2017
WJetsHT200to400_2017.dataset = "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT200to400_2017.files = jr.json_reader(path+"/WJets_HT200To400_2017.json")

WJetsHT400to600_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT400to600_2017")
WJetsHT400to600_2017.sigma = 48.91 * 1.21 #pb
WJetsHT400to600_2017.year = 2017
WJetsHT400to600_2017.dataset = "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT400to600_2017.files = jr.json_reader(path+"/WJets_HT400To600_2017.json")

WJetsHT600to800_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT600to800_2017")
WJetsHT600to800_2017.sigma = 12.05 * 1.21 #pb
WJetsHT600to800_2017.year = 2017
WJetsHT600to800_2017.dataset = "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT600to800_2017.files = jr.json_reader(path+"/WJets_HT600To800_2017.json")

WJetsHT800to1200_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT800to1200_2017")
WJetsHT800to1200_2017.sigma = 5.501 * 1.21 #pb
WJetsHT800to1200_2017.year = 2017
WJetsHT800to1200_2017.dataset = "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT800to1200_2017.files = jr.json_reader(path+"/WJets_HT800To1200_2017.json")

WJetsHT1200to2500_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT1200to2500_2017")
WJetsHT1200to2500_2017.sigma = 1.329 * 1.21 #pb
WJetsHT1200to2500_2017.year = 2017
WJetsHT1200to2500_2017.dataset = "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT1200to2500_2017.files = jr.json_reader(path+"/WJets_HT1200To2500_2017.json")

WJetsHT2500toInf_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT2500toInf_2017")
WJetsHT2500toInf_2017.sigma = 0.03216 * 1.21 #pb
WJetsHT2500toInf_2017.year = 2017
WJetsHT2500toInf_2017.dataset = "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT2500toInf_2017.files = jr.json_reader(path+"/WJets_HT2500ToInf_2017.json")

WJets_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJets_2017")
WJets_2017.year = 2017
WJets_2017.components = [WJetsHT70to100_2017, WJetsHT100to200_2017, WJetsHT200to400_2017, WJetsHT400to600_2017, WJetsHT600to800_2017, WJetsHT800to1200_2017, WJetsHT1200to2500_2017, WJetsHT2500toInf_2017]

WJetsHT70to100_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT70to100_Fake_2017")
WJetsHT70to100_Fake_2017.sigma = 1353 * 1.21 #pb
WJetsHT70to100_Fake_2017.year = 2017
WJetsHT70to100_Fake_2017.dataset = "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

WJetsHT100to200_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT100to200_Fake_2017")
WJetsHT100to200_Fake_2017.sigma = 1345 * 1.21 #pb
WJetsHT100to200_Fake_2017.year = 2017
WJetsHT100to200_Fake_2017.dataset = "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

WJetsHT200to400_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT200to400_Fake_2017")
WJetsHT200to400_Fake_2017.sigma = 359.7 * 1.21 #pb
WJetsHT200to400_Fake_2017.year = 2017
WJetsHT200to400_Fake_2017.dataset = "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT200to400_Fake_2017.files = jr.json_reader(path+"/WJets_HT200To400_2017.json")

WJetsHT400to600_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT400to600_Fake_2017")
WJetsHT400to600_Fake_2017.sigma = 48.91 * 1.21 #pb
WJetsHT400to600_Fake_2017.year = 2017
WJetsHT400to600_Fake_2017.dataset = "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT400to600_Fake_2017.files = jr.json_reader(path+"/WJets_HT400To600_2017.json")

WJetsHT600to800_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT600to800_Fake_2017")
WJetsHT600to800_Fake_2017.sigma = 12.05 * 1.21 #pb
WJetsHT600to800_Fake_2017.year = 2017
WJetsHT600to800_Fake_2017.dataset = "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT600to800_Fake_2017.files = jr.json_reader(path+"/WJets_HT600To800_2017.json")

WJetsHT800to1200_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT800to1200_Fake_2017")
WJetsHT800to1200_Fake_2017.sigma = 5.501 * 1.21 #pb
WJetsHT800to1200_Fake_2017.year = 2017
WJetsHT800to1200_Fake_2017.dataset = "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT800to1200_Fake_2017.files = jr.json_reader(path+"/WJets_HT800To1200_2017.json")

WJetsHT1200to2500_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT1200to2500_Fake_2017")
WJetsHT1200to2500_Fake_2017.sigma = 1.329 * 1.21 #pb
WJetsHT1200to2500_Fake_2017.year = 2017
WJetsHT1200to2500_Fake_2017.dataset = "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT1200to2500_Fake_2017.files = jr.json_reader(path+"/WJets_HT1200To2500_2017.json")

WJetsHT2500toInf_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT2500toInf_Fake_2017")
WJetsHT2500toInf_Fake_2017.sigma = 0.03216 * 1.21 #pb
WJetsHT2500toInf_Fake_2017.year = 2017
WJetsHT2500toInf_Fake_2017.dataset = "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT2500toInf_Fake_2017.files = jr.json_reader(path+"/WJets_HT2500ToInf_2017.json")

WJets_Fake_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJets_Fake_2017")
WJets_Fake_2017.year = 2017
WJets_Fake_2017.components = [WJetsHT70to100_Fake_2017, WJetsHT100to200_Fake_2017, WJetsHT200to400_Fake_2017, WJetsHT400to600_Fake_2017, WJetsHT600to800_Fake_2017, WJetsHT800to1200_Fake_2017, WJetsHT1200to2500_Fake_2017, WJetsHT2500toInf_Fake_2017]


################################ WZ ################################
WZ_2017 = sample(ROOT.kYellow-4, 1, 1001, "WZ", "WZ_2017")
WZ_2017.sigma = 47.13
WZ_2017.year = 2017
WZ_2017.dataset = "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_PU2017_EXT_102X_mc2017_realistic_v8-v1/NANOAODSIM"

################################ DrellYan ################################
DY1JetsToLL_2017 = sample(ROOT.kCyan, 1, 1001, "DY + 1 Jet", "DY1JetsToLL_2017")
DY1JetsToLL_2017.sigma = 1012.0
DY1JetsToLL_2017.year = 2017
DY1JetsToLL_2017.dataset = "/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag2_2017 + "-v1/NANOAODSIM"

DY2JetsToLL_2017 = sample(ROOT.kCyan, 1, 1001, "DY + 2 Jets", "DY2JetsToLL_2017")
DY2JetsToLL_2017.sigma = 330.4
DY2JetsToLL_2017.year = 2017
DY2JetsToLL_2017.dataset = "/DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag2_2017 + "_ext1-v1/NANOAODSIM"

DY3JetsToLL_2017 = sample(ROOT.kCyan, 1, 1001, "DY + 3 Jets", "DY3JetsToLL_2017")
DY3JetsToLL_2017.sigma = 101.8
DY3JetsToLL_2017.year = 2017
DY3JetsToLL_2017.dataset = "/DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

DY4JetsToLL_2017 = sample(ROOT.kCyan, 1, 1001, "DY + 4+ Jets", "DY4JetsToLL_2017")
DY4JetsToLL_2017.sigma = 54.80
DY4JetsToLL_2017.year = 2017
DY4JetsToLL_2017.dataset = "/DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag1_2017 + "-v1/NANOAODSIM"

DYJetsToLLM5to50_2017 = sample(ROOT.kCyan, 1, 1001, "DY M5to50", "DYJetsToLLM5to50_2017")
DYJetsToLLM5to50_2017.sigma = 81880.0
DYJetsToLLM5to50_2017.year = 2017
DYJetsToLLM5to50_2017.dataset = "/DYJetsToLL_M-5to50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

DYJetsToLLM50_2017 = sample(ROOT.kCyan, 1, 1001, "DY M50", "DYJetsToLLM50_2017")
DYJetsToLLM50_2017.sigma = 6529.0
DYJetsToLLM50_2017.year = 2017
DYJetsToLLM50_2017.dataset = "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/" + tag2_2017 + "_ext1-v1/NANOAODSIM"

DYJetsToLL_2017 = sample(ROOT.kCyan, 1, 1001, "DY + Jets", "DYJetsToLL_2017")
DYJetsToLL_2017.year = 2017
DYJetsToLL_2017.components = [DY1JetsToLL_2017, DY2JetsToLL_2017, DY3JetsToLL_2017, DY4JetsToLL_2017, DYJetsToLLM5to50_2017]

DY1JetsToLL_Fake_2017 = sample(ROOT.kCyan, 1, 1001, "DY + 1 Jet", "DY1JetsToLL_Fake_2017")
DY1JetsToLL_Fake_2017.sigma = 1012.0
DY1JetsToLL_Fake_2017.year = 2017
DY1JetsToLL_Fake_2017.dataset = "/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag2_2017 + "-v1/NANOAODSIM"

DY2JetsToLL_Fake_2017 = sample(ROOT.kCyan, 1, 1001, "DY + 2 Jets", "DY2JetsToLL_Fake_2017")
DY2JetsToLL_Fake_2017.sigma = 330.4
DY2JetsToLL_Fake_2017.year = 2017
DY2JetsToLL_Fake_2017.dataset = "/DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag2_2017 + "_ext1-v1/NANOAODSIM"

DY3JetsToLL_Fake_2017 = sample(ROOT.kCyan, 1, 1001, "DY + 3 Jets", "DY3JetsToLL_Fake_2017")
DY3JetsToLL_Fake_2017.sigma = 101.8
DY3JetsToLL_Fake_2017.year = 2017
DY3JetsToLL_Fake_2017.dataset = "/DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

DY4JetsToLL_Fake_2017 = sample(ROOT.kCyan, 1, 1001, "DY + 4+ Jets", "DY4JetsToLL_Fake_2017")
DY4JetsToLL_Fake_2017.sigma = 54.80
DY4JetsToLL_Fake_2017.year = 2017
DY4JetsToLL_Fake_2017.dataset = "/DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag1_2017 + "-v1/NANOAODSIM"

DYJetsToLL_Fake_2017 = sample(ROOT.kCyan, 1, 1001, "DY + Jets", "DYJetsToLL_Fake_2017")
DYJetsToLL_Fake_2017.year = 2017
DYJetsToLL_Fake_2017.components = [DY1JetsToLL_Fake_2017, DY2JetsToLL_Fake_2017, DY3JetsToLL_Fake_2017, DY4JetsToLL_Fake_2017]

DYJetsToLL_Old_2017 = sample(ROOT.kCyan, 1, 1001, "DY + Jets", "DYJetsToLL_2017")
DYJetsToLL_Old_2017.year = 2017
DYJetsToLL_Old_2017.components = [DY1JetsToLL_2017, DY2JetsToLL_2017, DY3JetsToLL_2017, DY4JetsToLL_2017]

DYJetsM_2017 = sample(ROOT.kCyan, 1, 1001, "DY + Jets (M)", "DYJetsM_2017")
DYJetsM_2017.year = 2017
DYJetsM_2017.components = [DYJetsToLLM5to50_2017, DYJetsToLLM50_2017]

################################ ssWW EWK ################################
WpWpJJ_EWK_2017 = sample(ROOT.kRed, 1, 1001, "EW ssWW", "WpWpJJ_EWK_2017")
WpWpJJ_EWK_2017.sigma = 0.02064
WpWpJJ_EWK_2017.year = 2017
WpWpJJ_EWK_2017.dataset = "/WpWpJJ_EWK_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

WpWpJJ_QCD_2017 = sample(ROOT.kPink+1, 1, 1001, "QCD ssWW", "WpWpJJ_QCD_2017")
WpWpJJ_QCD_2017.sigma = 0.01538
WpWpJJ_QCD_2017.year = 2017
WpWpJJ_QCD_2017.dataset = "/WpWpJJ_QCD_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_LL_SM_2017 = sample(ROOT.kBlack, 1, 1001, "VBS ssWW LL", "VBS_SSWW_LL_SM_2017")
VBS_SSWW_LL_SM_2017.sigma = 0.002014
VBS_SSWW_LL_SM_2017.year = 2017
VBS_SSWW_LL_SM_2017.dataset = "/VBS_SSWW_LL_polarization_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_TL_SM_2017 = sample(ROOT.kBlack, 1, 1001, "VBS ssWW TL", "VBS_SSWW_TL_SM_2017")
VBS_SSWW_TL_SM_2017.sigma = 0.01036
VBS_SSWW_TL_SM_2017.year = 2017
VBS_SSWW_TL_SM_2017.dataset = "/VBS_SSWW_TL_polarization_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_TT_SM_2017 = sample(ROOT.kBlack, 1, 1001, "VBS ssWW TT", "VBS_SSWW_TT_SM_2017")
VBS_SSWW_TT_SM_2017.sigma = 0.01595
VBS_SSWW_TT_SM_2017.year = 2017
VBS_SSWW_TT_SM_2017.dataset = "/VBS_SSWW_TT_polarization_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_SM_2017 = sample(ROOT.kRed, 1, 1001, "VBS ssWW", "VBS_SSWW_SM_2017")
VBS_SSWW_SM_2017.year = 2017
VBS_SSWW_SM_2017.components = [VBS_SSWW_LL_SM_2017, VBS_SSWW_TL_SM_2017, VBS_SSWW_TT_SM_2017]

VBS_SSWW_cHW_BSM_2017 = sample(ROOT.kGreen+3, 1, 1001, "VBS ssWW c_{HW} (only BSM)", "VBS_SSWW_cHW_BSM_2017")
VBS_SSWW_cHW_BSM_2017.sigma = 0.002014
VBS_SSWW_cHW_BSM_2017.year = 2017
VBS_SSWW_cHW_BSM_2017.dataset = "/VBS_SSWW_cHW_BSM_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_cHW_INT_2017 = sample(ROOT.kGreen+3, 1, 1001, "VBS ssWW c_{HW} (only INT)", "VBS_SSWW_cHW_INT_2017")
VBS_SSWW_cHW_INT_2017.sigma = 0.002014
VBS_SSWW_cHW_INT_2017.year = 2017
VBS_SSWW_cHW_INT_2017.dataset = "/VBS_SSWW_cHW_INT_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_cHW_2017 = sample(ROOT.kMagenta+3, 1, 1001, "VBS ssWW c_{HW} (BSM+INT)", "VBS_SSWW_cHW_2017")
VBS_SSWW_cHW_2017.year = 2017
VBS_SSWW_cHW_2017.components = [VBS_SSWW_cHW_BSM_2017, VBS_SSWW_cHW_INT_2017]

VBS_SSWW_cHW_SM_2017 = sample(ROOT.kGreen+2, 1, 1001, "VBS ssWW c_{HW} + SM", "VBS_SSWW_cHW_SM_2017")
VBS_SSWW_cHW_SM_2017.year = 2017
VBS_SSWW_cHW_SM_2017.components = [VBS_SSWW_cHW_BSM_2017, VBS_SSWW_cHW_INT_2017, VBS_SSWW_LL_SM_2017, VBS_SSWW_TL_SM_2017, VBS_SSWW_TT_SM_2017]

VBS_SSWW_cW_BSM_2017 = sample(ROOT.kMagenta+3, 1, 1001, "VBS ssWW c_{W} (only BSM)", "VBS_SSWW_cW_BSM_2017")
VBS_SSWW_cW_BSM_2017.sigma = 0.002014
VBS_SSWW_cW_BSM_2017.year = 2017
VBS_SSWW_cW_BSM_2017.dataset = "/VBS_SSWW_cW_BSM_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_cW_INT_2017 = sample(ROOT.kMagenta+3, 1, 1001, "VBS ssWW c_{W} (only INT)", "VBS_SSWW_cW_INT_2017")
VBS_SSWW_cW_INT_2017.sigma = 0.002014
VBS_SSWW_cW_INT_2017.year = 2017
VBS_SSWW_cW_INT_2017.dataset = "/VBS_SSWW_cW_INT_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_cW_2017 = sample(ROOT.kMagenta, 1, 1001, "VBS ssWW c_{W} (BSM+INT)", "VBS_SSWW_cW_2017")
VBS_SSWW_cW_2017.year = 2017
VBS_SSWW_cW_2017.components = [VBS_SSWW_cW_BSM_2017, VBS_SSWW_cW_INT_2017]

VBS_SSWW_cW_SM_2017 = sample(ROOT.kGreen+2, 1, 1001, "VBS ssWW c_{W} + SM", "VBS_SSWW_cW_SM_2017")
VBS_SSWW_cW_SM_2017.year = 2017
VBS_SSWW_cW_SM_2017.components = [VBS_SSWW_cW_BSM_2017, VBS_SSWW_cW_INT_2017, VBS_SSWW_LL_SM_2017, VBS_SSWW_TL_SM_2017, VBS_SSWW_TT_SM_2017]

VBS_SSWW_cW_cHW_2017 = sample(ROOT.kAzure+3, 1, 1001, "VBS ssWW c_{HW} + c_{W}", "VBS_SSWW_cW_cHW_2017")
VBS_SSWW_cW_cHW_2017.sigma = 0.002014
VBS_SSWW_cW_cHW_2017.year = 2017
VBS_SSWW_cW_cHW_2017.dataset = "/VBS_SSWW_cW_cHW_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

VBS_SSWW_DIM6_2017 = sample(ROOT.kGreen+3, 1, 1001, "VBS ssWW dim-6 EFT", "VBS_SSWW_DIM6_2017")
VBS_SSWW_DIM6_2017.year = 2017
VBS_SSWW_DIM6_2017.components = [VBS_SSWW_cHW_BSM_2017, VBS_SSWW_cW_BSM_2017, VBS_SSWW_cW_cHW_2017]

VBS_SSWW_DIM6_SM_2017 = sample(ROOT.kGreen+2, 1, 1001, "VBS ssWW dim-6 EFT + SM", "VBS_SSWW_DIM6_SM_2017")
VBS_SSWW_DIM6_SM_2017.year = 2017
VBS_SSWW_DIM6_SM_2017.components = [VBS_SSWW_cHW_BSM_2017, VBS_SSWW_cHW_INT_2017, VBS_SSWW_cW_BSM_2017, VBS_SSWW_cW_INT_2017, VBS_SSWW_cW_cHW_2017, VBS_SSWW_LL_SM_2017, VBS_SSWW_TL_SM_2017, VBS_SSWW_TT_SM_2017]

VBS_SSWW_aQGC_2017 = sample(ROOT.kGreen, 1, 1001, "VBS ssWW dim-8 EFT", "VBS_SSWW_aQGC_2017")
VBS_SSWW_aQGC_2017.sigma = 0.1191
VBS_SSWW_aQGC_2017.year = 2017
VBS_SSWW_aQGC_2017.dataset = "/WWJJ_SS_WToLNu_EWK_aQGC-FT-FS-FM_TuneCP5_13TeV_madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

###### f_{s0} #######
VBS_SSWW_FS0_25_BSM_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 25 TeV^{-4} BSM", "VBS_SSWW_FS0_25_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS0_25_BSM_2017.sigma = 0.1191
VBS_SSWW_FS0_25_BSM_2017.year = 2017

VBS_SSWW_FS0_25_INT_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 25 TeV^{-4} INT", "VBS_SSWW_FS0_25_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS0_25_INT_2017.sigma = 0.1191
VBS_SSWW_FS0_25_INT_2017.year = 2017

VBS_SSWW_FS0_25_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 25 TeV^{-4}", "VBS_SSWW_FS0_25_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS0_25_2017.year = 2017
VBS_SSWW_FS0_25_2017.components = [VBS_SSWW_FS0_25_BSM_2017, VBS_SSWW_FS0_25_INT_2017]

VBS_SSWW_FS0_5_BSM_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 5 TeV^{-4} BSM", "VBS_SSWW_FS0_5_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS0_5_BSM_2017.sigma = 0.1191
VBS_SSWW_FS0_5_BSM_2017.year = 2017

VBS_SSWW_FS0_5_INT_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 5 TeV^{-4} INT", "VBS_SSWW_FS0_5_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS0_5_INT_2017.sigma = 0.1191
VBS_SSWW_FS0_5_INT_2017.year = 2017

VBS_SSWW_FS0_5_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 5 TeV^{-4}", "VBS_SSWW_FS0_5_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS0_5_2017.year = 2017
VBS_SSWW_FS0_5_2017.components = [VBS_SSWW_FS0_5_BSM_2017, VBS_SSWW_FS0_5_INT_2017]

VBS_SSWW_FS0_0_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FS0_0_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS0_0_2017.sigma = 0.1191
VBS_SSWW_FS0_0_2017.year = 2017

VBS_SSWW_FS0_25_SM_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 25 TeV^{-4}", "VBS_SSWW_FS0_25_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS0_25_SM_2017.year = 2017
VBS_SSWW_FS0_25_SM_2017.components = [VBS_SSWW_FS0_25_BSM_2017, VBS_SSWW_FS0_25_INT_2017, VBS_SSWW_FS0_0_2017]

VBS_SSWW_FS0_5_SM_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 5 TeV^{-4}", "VBS_SSWW_FS0_5_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS0_5_SM_2017.year = 2017
VBS_SSWW_FS0_5_SM_2017.components = [VBS_SSWW_FS0_5_BSM_2017, VBS_SSWW_FS0_5_INT_2017, VBS_SSWW_FS0_0_2017]

###### f_{s1} #######
VBS_SSWW_FS1_50_BSM_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 50 TeV^{-4} BSM", "VBS_SSWW_FS1_50_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS1_50_BSM_2017.sigma = 0.1191
VBS_SSWW_FS1_50_BSM_2017.year = 2017

VBS_SSWW_FS1_50_INT_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 50 TeV^{-4} INT", "VBS_SSWW_FS1_50_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS1_50_INT_2017.sigma = 0.1191
VBS_SSWW_FS1_50_INT_2017.year = 2017

VBS_SSWW_FS1_50_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 50 TeV^{-4}", "VBS_SSWW_FS1_50_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS1_50_2017.year = 2017
VBS_SSWW_FS1_50_2017.components = [VBS_SSWW_FS1_50_BSM_2017, VBS_SSWW_FS1_50_INT_2017]

VBS_SSWW_FS1_10_BSM_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 10 TeV^{-4} BSM", "VBS_SSWW_FS1_10_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS1_10_BSM_2017.sigma = 0.1191
VBS_SSWW_FS1_10_BSM_2017.year = 2017

VBS_SSWW_FS1_10_INT_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 10 TeV^{-4} INT", "VBS_SSWW_FS1_10_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS1_10_INT_2017.sigma = 0.1191
VBS_SSWW_FS1_10_INT_2017.year = 2017

VBS_SSWW_FS1_10_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 10 TeV^{-4}", "VBS_SSWW_FS1_10_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS1_10_2017.year = 2017
VBS_SSWW_FS1_10_2017.components = [VBS_SSWW_FS1_10_BSM_2017, VBS_SSWW_FS1_10_INT_2017]

VBS_SSWW_FS1_0_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FS1_0_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS1_0_2017.sigma = 0.1191
VBS_SSWW_FS1_0_2017.year = 2017

VBS_SSWW_FS1_50_SM_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 50 TeV^{-4}", "VBS_SSWW_FS1_50_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS1_50_SM_2017.year = 2017
VBS_SSWW_FS1_50_SM_2017.components = [VBS_SSWW_FS1_50_BSM_2017, VBS_SSWW_FS1_50_INT_2017, VBS_SSWW_FS1_0_2017]

VBS_SSWW_FS1_10_SM_2017 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 10 TeV^{-4}", "VBS_SSWW_FS1_10_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FS1_10_SM_2017.year = 2017
VBS_SSWW_FS1_10_SM_2017.components = [VBS_SSWW_FS1_10_BSM_2017, VBS_SSWW_FS1_10_INT_2017, VBS_SSWW_FS1_0_2017]

###### f_{m0} #######
VBS_SSWW_FM0_25_BSM_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 25 TeV^{-4} BSM", "VBS_SSWW_FM0_25_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM0_25_BSM_2017.sigma = 0.1191
VBS_SSWW_FM0_25_BSM_2017.year = 2017

VBS_SSWW_FM0_25_INT_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 25 TeV^{-4} INT", "VBS_SSWW_FM0_25_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM0_25_INT_2017.sigma = 0.1191
VBS_SSWW_FM0_25_INT_2017.year = 2017

VBS_SSWW_FM0_25_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 25 TeV^{-4}", "VBS_SSWW_FM0_25_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM0_25_2017.year = 2017
VBS_SSWW_FM0_25_2017.components = [VBS_SSWW_FM0_25_BSM_2017, VBS_SSWW_FM0_25_INT_2017]

VBS_SSWW_FM0_5_BSM_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 5 TeV^{-4} BSM", "VBS_SSWW_FM0_5_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM0_5_BSM_2017.sigma = 0.1191
VBS_SSWW_FM0_5_BSM_2017.year = 2017

VBS_SSWW_FM0_5_INT_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 5 TeV^{-4} INT", "VBS_SSWW_FM0_5_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM0_5_INT_2017.sigma = 0.1191
VBS_SSWW_FM0_5_INT_2017.year = 2017

VBS_SSWW_FM0_5_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 5 TeV^{-4}", "VBS_SSWW_FM0_5_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM0_5_2017.year = 2017
VBS_SSWW_FM0_5_2017.components = [VBS_SSWW_FM0_5_BSM_2017, VBS_SSWW_FM0_5_INT_2017]

VBS_SSWW_FM0_0_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FM0_0_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM0_0_2017.sigma = 0.1191
VBS_SSWW_FM0_0_2017.year = 2017

VBS_SSWW_FM0_25_SM_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 25 TeV^{-4}", "VBS_SSWW_FM0_25_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM0_25_SM_2017.year = 2017
VBS_SSWW_FM0_25_SM_2017.components = [VBS_SSWW_FM0_25_BSM_2017, VBS_SSWW_FM0_25_INT_2017, VBS_SSWW_FM0_0_2017]

VBS_SSWW_FM0_5_SM_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 5 TeV^{-4}", "VBS_SSWW_FM0_5_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM0_5_SM_2017.year = 2017
VBS_SSWW_FM0_5_SM_2017.components = [VBS_SSWW_FM0_5_BSM_2017, VBS_SSWW_FM0_5_INT_2017, VBS_SSWW_FM0_0_2017]

###### f_{m1} #######
VBS_SSWW_FM1_25_BSM_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 25 TeV^{-4} BSM", "VBS_SSWW_FM1_25_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM1_25_BSM_2017.sigma = 0.1191
VBS_SSWW_FM1_25_BSM_2017.year = 2017

VBS_SSWW_FM1_25_INT_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 25 TeV^{-4} INT", "VBS_SSWW_FM1_25_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM1_25_INT_2017.sigma = 0.1191
VBS_SSWW_FM1_25_INT_2017.year = 2017

VBS_SSWW_FM1_25_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 25 TeV^{-4}", "VBS_SSWW_FM1_25_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM1_25_2017.year = 2017
VBS_SSWW_FM1_25_2017.components = [VBS_SSWW_FM1_25_BSM_2017, VBS_SSWW_FM1_25_INT_2017]

VBS_SSWW_FM1_5_BSM_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 10 TeV^{-4} BSM", "VBS_SSWW_FM1_5_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM1_5_BSM_2017.sigma = 0.1191
VBS_SSWW_FM1_5_BSM_2017.year = 2017

VBS_SSWW_FM1_5_INT_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 10 TeV^{-4} INT", "VBS_SSWW_FM1_5_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM1_5_INT_2017.sigma = 0.1191
VBS_SSWW_FM1_5_INT_2017.year = 2017

VBS_SSWW_FM1_5_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 10 TeV^{-4}", "VBS_SSWW_FM1_5_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM1_5_2017.year = 2017
VBS_SSWW_FM1_5_2017.components = [VBS_SSWW_FM1_5_BSM_2017, VBS_SSWW_FM1_5_INT_2017]

VBS_SSWW_FM1_0_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FM1_0_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM1_0_2017.sigma = 0.1191
VBS_SSWW_FM1_0_2017.year = 2017

VBS_SSWW_FM1_25_SM_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 25 TeV^{-4}", "VBS_SSWW_FM1_25_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM1_25_SM_2017.year = 2017
VBS_SSWW_FM1_25_SM_2017.components = [VBS_SSWW_FM1_25_BSM_2017, VBS_SSWW_FM1_25_INT_2017, VBS_SSWW_FM1_0_2017]

VBS_SSWW_FM1_5_SM_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 10 TeV^{-4}", "VBS_SSWW_FM1_5_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM1_5_SM_2017.year = 2017
VBS_SSWW_FM1_5_SM_2017.components = [VBS_SSWW_FM1_5_BSM_2017, VBS_SSWW_FM1_5_INT_2017, VBS_SSWW_FM1_0_2017]

###### f_{m6} #######
VBS_SSWW_FM6_25_BSM_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 25 TeV^{-4} BSM", "VBS_SSWW_FM6_25_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM6_25_BSM_2017.sigma = 0.1191
VBS_SSWW_FM6_25_BSM_2017.year = 2017

VBS_SSWW_FM6_25_INT_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 25 TeV^{-4} INT", "VBS_SSWW_FM6_25_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM6_25_INT_2017.sigma = 0.1191
VBS_SSWW_FM6_25_INT_2017.year = 2017

VBS_SSWW_FM6_25_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 25 TeV^{-4}", "VBS_SSWW_FM6_25_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM6_25_2017.year = 2017
VBS_SSWW_FM6_25_2017.components = [VBS_SSWW_FM6_25_BSM_2017, VBS_SSWW_FM6_25_INT_2017]

VBS_SSWW_FM6_5_BSM_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 5 TeV^{-4} BSM", "VBS_SSWW_FM6_5_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM6_5_BSM_2017.sigma = 0.1191
VBS_SSWW_FM6_5_BSM_2017.year = 2017

VBS_SSWW_FM6_5_INT_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 5 TeV^{-4} INT", "VBS_SSWW_FM6_5_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM6_5_INT_2017.sigma = 0.1191
VBS_SSWW_FM6_5_INT_2017.year = 2017

VBS_SSWW_FM6_5_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 5 TeV^{-4}", "VBS_SSWW_FM6_5_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM6_5_2017.year = 2017
VBS_SSWW_FM6_5_2017.components = [VBS_SSWW_FM6_5_BSM_2017, VBS_SSWW_FM6_5_INT_2017]

VBS_SSWW_FM6_0_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FM6_0_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM6_0_2017.sigma = 0.1191
VBS_SSWW_FM6_0_2017.year = 2017

VBS_SSWW_FM6_25_SM_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 25 TeV^{-4}", "VBS_SSWW_FM6_25_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM6_25_SM_2017.year = 2017
VBS_SSWW_FM6_25_SM_2017.components = [VBS_SSWW_FM6_25_BSM_2017, VBS_SSWW_FM6_25_INT_2017, VBS_SSWW_FM6_0_2017]

VBS_SSWW_FM6_5_SM_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 5 TeV^{-4}", "VBS_SSWW_FM6_5_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM6_5_SM_2017.year = 2017
VBS_SSWW_FM6_5_SM_2017.components = [VBS_SSWW_FM6_5_BSM_2017, VBS_SSWW_FM6_5_INT_2017, VBS_SSWW_FM6_0_2017]

###### f_{m7} #######
VBS_SSWW_FM7_50_BSM_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 50 TeV^{-4} BSM", "VBS_SSWW_FM7_50_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM7_50_BSM_2017.sigma = 0.1191
VBS_SSWW_FM7_50_BSM_2017.year = 2017

VBS_SSWW_FM7_50_INT_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 50 TeV^{-4} INT", "VBS_SSWW_FM7_50_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM7_50_INT_2017.sigma = 0.1191
VBS_SSWW_FM7_50_INT_2017.year = 2017

VBS_SSWW_FM7_50_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 50 TeV^{-4}", "VBS_SSWW_FM7_50_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM7_50_2017.year = 2017
VBS_SSWW_FM7_50_2017.components = [VBS_SSWW_FM7_50_BSM_2017, VBS_SSWW_FM7_50_INT_2017]

VBS_SSWW_FM7_10_BSM_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 10 TeV^{-4} BSM", "VBS_SSWW_FM7_10_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM7_10_BSM_2017.sigma = 0.1191
VBS_SSWW_FM7_10_BSM_2017.year = 2017

VBS_SSWW_FM7_10_INT_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 10 TeV^{-4} INT", "VBS_SSWW_FM7_10_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM7_10_INT_2017.sigma = 0.1191
VBS_SSWW_FM7_10_INT_2017.year = 2017

VBS_SSWW_FM7_10_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 10 TeV^{-4}", "VBS_SSWW_FM7_10_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM7_10_2017.year = 2017
VBS_SSWW_FM7_10_2017.components = [VBS_SSWW_FM7_10_BSM_2017, VBS_SSWW_FM7_10_INT_2017]

VBS_SSWW_FM7_0_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FM7_0_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM7_0_2017.sigma = 0.1191
VBS_SSWW_FM7_0_2017.year = 2017

VBS_SSWW_FM7_50_SM_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 50 TeV^{-4}", "VBS_SSWW_FM7_50_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM7_50_SM_2017.year = 2017
VBS_SSWW_FM7_50_SM_2017.components = [VBS_SSWW_FM7_50_BSM_2017, VBS_SSWW_FM7_50_INT_2017, VBS_SSWW_FM7_0_2017]

VBS_SSWW_FM7_10_SM_2017 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 10 TeV^{-4}", "VBS_SSWW_FM7_10_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FM7_10_SM_2017.year = 2017
VBS_SSWW_FM7_10_SM_2017.components = [VBS_SSWW_FM7_10_BSM_2017, VBS_SSWW_FM7_10_INT_2017, VBS_SSWW_FM7_0_2017]

###### f_{t0} #######
VBS_SSWW_FT0_2p5_BSM_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 2.5 TeV^{-4} BSM", "VBS_SSWW_FT0_2p5_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT0_2p5_BSM_2017.sigma = 0.1191
VBS_SSWW_FT0_2p5_BSM_2017.year = 2017

VBS_SSWW_FT0_2p5_INT_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 2.5 TeV^{-4} INT", "VBS_SSWW_FT0_2p5_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT0_2p5_INT_2017.sigma = 0.1191
VBS_SSWW_FT0_2p5_INT_2017.year = 2017

VBS_SSWW_FT0_2p5_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 2.5 TeV^{-4}", "VBS_SSWW_FT0_2p5_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT0_2p5_2017.year = 2017
VBS_SSWW_FT0_2p5_2017.components = [VBS_SSWW_FT0_2p5_BSM_2017, VBS_SSWW_FT0_2p5_INT_2017]

VBS_SSWW_FT0_0p5_BSM_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 0.5 TeV^{-4} BSM", "VBS_SSWW_FT0_0p5_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT0_0p5_BSM_2017.sigma = 0.1191
VBS_SSWW_FT0_0p5_BSM_2017.year = 2017

VBS_SSWW_FT0_0p5_INT_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 0.5 TeV^{-4} INT", "VBS_SSWW_FT0_0p5_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT0_0p5_INT_2017.sigma = 0.1191
VBS_SSWW_FT0_0p5_INT_2017.year = 2017

VBS_SSWW_FT0_0p5_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 0.5 TeV^{-4}", "VBS_SSWW_FT0_0p5_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT0_0p5_2017.year = 2017
VBS_SSWW_FT0_0p5_2017.components = [VBS_SSWW_FT0_0p5_BSM_2017, VBS_SSWW_FT0_0p5_INT_2017]

VBS_SSWW_FT0_0_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FT0_0_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT0_0_2017.sigma = 0.1191
VBS_SSWW_FT0_0_2017.year = 2017

VBS_SSWW_FT0_2p5_SM_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 2.5 TeV^{-4}", "VBS_SSWW_FT0_2p5_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT0_2p5_SM_2017.year = 2017
VBS_SSWW_FT0_2p5_SM_2017.components = [VBS_SSWW_FT0_2p5_BSM_2017, VBS_SSWW_FT0_2p5_INT_2017, VBS_SSWW_FT0_0_2017]

VBS_SSWW_FT0_0p5_SM_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 0.5 TeV^{-4}", "VBS_SSWW_FT0_0p5_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT0_0p5_SM_2017.year = 2017
VBS_SSWW_FT0_0p5_SM_2017.components = [VBS_SSWW_FT0_0p5_BSM_2017, VBS_SSWW_FT0_0p5_INT_2017, VBS_SSWW_FT0_0_2017]

###### f_{t1} #######
VBS_SSWW_FT1_1_BSM_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 1 TeV^{-4} BSM", "VBS_SSWW_FT1_1_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT1_1_BSM_2017.sigma = 0.1191
VBS_SSWW_FT1_1_BSM_2017.year = 2017

VBS_SSWW_FT1_1_INT_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 1 TeV^{-4} INT", "VBS_SSWW_FT1_1_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT1_1_INT_2017.sigma = 0.1191
VBS_SSWW_FT1_1_INT_2017.year = 2017

VBS_SSWW_FT1_1_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 1 TeV^{-4}", "VBS_SSWW_FT1_1_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT1_1_2017.year = 2017
VBS_SSWW_FT1_1_2017.components = [VBS_SSWW_FT1_1_BSM_2017, VBS_SSWW_FT1_1_INT_2017]

VBS_SSWW_FT1_0p2_BSM_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 0.2 TeV^{-4} BSM", "VBS_SSWW_FT1_0p2_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT1_0p2_BSM_2017.sigma = 0.1191
VBS_SSWW_FT1_0p2_BSM_2017.year = 2017

VBS_SSWW_FT1_0p2_INT_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 0.2 TeV^{-4} INT", "VBS_SSWW_FT1_0p2_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT1_0p2_INT_2017.sigma = 0.1191
VBS_SSWW_FT1_0p2_INT_2017.year = 2017

VBS_SSWW_FT1_0p2_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 0.2 TeV^{-4}", "VBS_SSWW_FT1_0p2_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT1_0p2_2017.year = 2017
VBS_SSWW_FT1_0p2_2017.components = [VBS_SSWW_FT1_0p2_BSM_2017, VBS_SSWW_FT1_0p2_INT_2017]

VBS_SSWW_FT1_0_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FT1_0_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT1_0_2017.sigma = 0.1191
VBS_SSWW_FT1_0_2017.year = 2017

VBS_SSWW_FT1_1_SM_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 1 TeV^{-4}", "VBS_SSWW_FT1_1_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT1_1_SM_2017.year = 2017
VBS_SSWW_FT1_1_SM_2017.components = [VBS_SSWW_FT1_1_BSM_2017, VBS_SSWW_FT1_1_INT_2017, VBS_SSWW_FT1_0_2017]

VBS_SSWW_FT1_0p2_SM_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 0.2 TeV^{-4}", "VBS_SSWW_FT1_0p2_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT1_0p2_SM_2017.year = 2017
VBS_SSWW_FT1_0p2_SM_2017.components = [VBS_SSWW_FT1_0p2_BSM_2017, VBS_SSWW_FT1_0p2_INT_2017, VBS_SSWW_FT1_0_2017]

###### f_{t2} #######
VBS_SSWW_FT2_2p5_BSM_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 2.5 TeV^{-4} BSM", "VBS_SSWW_FT2_2p5_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT2_2p5_BSM_2017.sigma = 0.1191
VBS_SSWW_FT2_2p5_BSM_2017.year = 2017

VBS_SSWW_FT2_2p5_INT_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 2.5 TeV^{-4} INT", "VBS_SSWW_FT2_2p5_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT2_2p5_INT_2017.sigma = 0.1191
VBS_SSWW_FT2_2p5_INT_2017.year = 2017

VBS_SSWW_FT2_2p5_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 2.5 TeV^{-4}", "VBS_SSWW_FT2_2p5_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT2_2p5_2017.year = 2017
VBS_SSWW_FT2_2p5_2017.components = [VBS_SSWW_FT2_2p5_BSM_2017, VBS_SSWW_FT2_2p5_INT_2017]

VBS_SSWW_FT2_0p5_BSM_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 0.5 TeV^{-4} BSM", "VBS_SSWW_FT2_0p5_BSM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT2_0p5_BSM_2017.sigma = 0.1191
VBS_SSWW_FT2_0p5_BSM_2017.year = 2017

VBS_SSWW_FT2_0p5_INT_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 0.5 TeV^{-4} INT", "VBS_SSWW_FT2_0p5_INT_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT2_0p5_INT_2017.sigma = 0.1191
VBS_SSWW_FT2_0p5_INT_2017.year = 2017

VBS_SSWW_FT2_0p5_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 0.5 TeV^{-4}", "VBS_SSWW_FT2_0p5_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT2_0p5_2017.year = 2017
VBS_SSWW_FT2_0p5_2017.components = [VBS_SSWW_FT2_0p5_BSM_2017, VBS_SSWW_FT2_0p5_INT_2017]

VBS_SSWW_FT2_0_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FT2_0_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT2_0_2017.sigma = 0.1191
VBS_SSWW_FT2_0_2017.year = 2017

VBS_SSWW_FT2_2p5_SM_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 2.5 TeV^{-4}", "VBS_SSWW_FT2_2p5_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT2_2p5_SM_2017.year = 2017
VBS_SSWW_FT2_2p5_SM_2017.components = [VBS_SSWW_FT2_2p5_BSM_2017, VBS_SSWW_FT2_2p5_INT_2017, VBS_SSWW_FT2_0_2017]

VBS_SSWW_FT2_0p5_SM_2017 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 0.5 TeV^{-4}", "VBS_SSWW_FT2_0p5_SM_2017", "VBS_SSWW_aQGC_2017")
VBS_SSWW_FT2_0p5_SM_2017.year = 2017
VBS_SSWW_FT2_0p5_SM_2017.components = [VBS_SSWW_FT2_0p5_BSM_2017, VBS_SSWW_FT2_0p5_INT_2017, VBS_SSWW_FT2_0_2017]

DHiggsToWW_2017 = sample(ROOT.kAzure, 1, 1001, "m_{H} = 200 m_{X} = 150 m_{Z'} = 2e3", "DHiggsToWW_2017")
DHiggsToWW_2017.sigma = 0.0002014
DHiggsToWW_2017.year = 2017
DHiggsToWW_2017.dataset = "/DarkHiggs_MonoHs_HsToWWTo2l2nu_mhs_200_mx_150_mZp_2000_TuneCP5_13TeV-madgraph-pythia8/" + tag_2017 + "-v1/NANOAODSIM"

####################### for likelihood scan ###############################################
sm_2017 = sample(ROOT.kRed+2, 1, 1001, "VBS ssWW SM", "sm_2017")
sm_2017.year = 2017
sm_2017.components = [VBS_SSWW_LL_SM_2017, VBS_SSWW_TL_SM_2017, VBS_SSWW_TT_SM_2017]

sm_lin_quad_cW_2017 = sample(ROOT.kGreen+2, 1, 1001, "VBS ssWW (c_{W} + SM + INT)", "sm_lin_quad_cW_2017")
sm_lin_quad_cW_2017.year = 2017
sm_lin_quad_cW_2017.components = [VBS_SSWW_cW_BSM_2017, VBS_SSWW_cW_INT_2017, VBS_SSWW_LL_SM_2017, VBS_SSWW_TL_SM_2017, VBS_SSWW_TT_SM_2017]

quad_cW_2017 = sample(ROOT.kMagenta+1, 1, 1001, "VBS ssWW c_{W} (BSM+INT)", "quad_cW_2017")
quad_cW_2017.year = 2017
quad_cW_2017.components = [VBS_SSWW_cW_BSM_2017]

sm_lin_quad_cHW_2017 = sample(ROOT.kGreen+2, 1, 1001, "VBS ssWW (c_{W} + SM + INT)", "sm_lin_quad_cHW_2017")
sm_lin_quad_cHW_2017.year = 2017
sm_lin_quad_cHW_2017.components = [VBS_SSWW_cHW_BSM_2017, VBS_SSWW_cHW_INT_2017, VBS_SSWW_LL_SM_2017, VBS_SSWW_TL_SM_2017, VBS_SSWW_TT_SM_2017]

quad_cHW_2017 = sample(ROOT.kMagenta+1, 1, 1001, "VBS ssWW c_{W} (BSM+INT)", "quad_cHW_2017")
quad_cHW_2017.year = 2017
quad_cHW_2017.components = [VBS_SSWW_cHW_BSM_2017]

###################################################################################################################################################################
############################################################                                           ############################################################
############################################################                    2018                   ############################################################
############################################################                                           ############################################################
###################################################################################################################################################################
################################ QCD ################################
QCDHT_100to200_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_100to200_2018")
QCDHT_100to200_2018.sigma = 347700 #pb
QCDHT_100to200_2018.year = 2018
QCDHT_100to200_2018.dataset = "/QCD_HT100to200_BGenFilter_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCDHT_200to300_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_200to300_2018")
QCDHT_200to300_2018.sigma = 347700 #pb
QCDHT_200to300_2018.year = 2018
QCDHT_200to300_2018.dataset = "/QCD_HT200to300_BGenFilter_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCDHT_300to500_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_300to500_2018")
QCDHT_300to500_2018.sigma = 347700 #pb
QCDHT_300to500_2018.year = 2018
QCDHT_300to500_2018.dataset = "/QCD_HT300to500_BGenFilter_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCDHT_500to700_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_500to700_2018")
QCDHT_500to700_2018.sigma = 32100 #pb
QCDHT_500to700_2018.year = 2018
QCDHT_500to700_2018.dataset = "/QCD_HT500to700_BGenFilter_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCDHT_700to1000_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_700to1000_2018")
QCDHT_700to1000_2018.sigma = 6831 #pb
QCDHT_700to1000_2018.year = 2018
QCDHT_700to1000_2018.dataset = "/QCD_HT700to1000_BGenFilter_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCDHT_1000to1500_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1000to1500_2018")
QCDHT_1000to1500_2018.sigma = 1207 #pb
QCDHT_1000to1500_2018.year = 2018
QCDHT_1000to1500_2018.dataset = "/QCD_HT1000to1500_BGenFilter_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCDHT_1500to2000_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1500to2000_2018")
QCDHT_1500to2000_2018.sigma = 119.9 #pb
QCDHT_1500to2000_2018.year = 2018
QCDHT_1500to2000_2018.dataset = "/QCD_HT1500to2000_BGenFilter_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCDHT_2000toInf_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_2000toInf_2018")
QCDHT_2000toInf_2018.sigma = 25.24 #pb
QCDHT_2000toInf_2018.year = 2018
QCDHT_2000toInf_2018.dataset = "/QCD_HT2000toInf_BGenFilter_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCD_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2018")
QCD_2018.year = 2018
QCD_2018.components = [QCDHT_100to200_2018, QCDHT_200to300_2018, QCDHT_300to500_2018, QCDHT_500to700_2018, QCDHT_700to1000_2018, QCDHT_1000to1500_2018, QCDHT_1500to2000_2018, QCDHT_2000toInf_2018]

################################ ZZ ################################
ZZTo2L2Nu_2018 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "ZZTo2L2Nu_2018")
ZZTo2L2Nu_2018.year = 2018
ZZTo2L2Nu_2018.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/" + tag_2018 + "_ext1-v1/NANOAODSIM"
ZZTo2L2Nu_2018.sigma = 0.5644 #pb                                                     

ZZJJTo4L_EWK_2018 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "ZZJJTo4L_EWK_2018")
ZZJJTo4L_EWK_2018.year = 2018
ZZJJTo4L_EWK_2018.dataset = "/ZZJJTo4L_EWK_TuneCP5_13TeV-madgraph-pythia8/" + tag_2018 + "-v1/NANOAODSIM"
ZZJJTo4L_EWK_2018.sigma = 0.0004536 #pb

ZZJJTo4L_QCD_2018 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "ZZJJTo4L_QCD_2018")
ZZJJTo4L_QCD_2018.year = 2018
ZZJJTo4L_QCD_2018.dataset = "/ZZJJTo4L_QCD_TuneCP5_13TeV-madgraph-pythia8/" + tag_2018 + "-v1/NANOAODSIM"
ZZJJTo4L_QCD_2018.sigma = 0.008348 #pb

GluGluToContinToZZTo2e2nu_2018 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo2e2nu_2018")
GluGluToContinToZZTo2e2nu_2018.year = 2018
GluGluToContinToZZTo2e2nu_2018.dataset = "/GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8/" + tag_2018 + "-v1/NANOAODSIM"
GluGluToContinToZZTo2e2nu_2018.sigma = 14.93 #pb

GluGluToContinToZZTo2e2mu_2018 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo2e2mu_2018")
GluGluToContinToZZTo2e2mu_2018.year = 2018
GluGluToContinToZZTo2e2mu_2018.dataset = "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/" + tag_2018 + "-v1/NANOAODSIM"
GluGluToContinToZZTo2e2mu_2018.sigma = 3.185 #pb

GluGluToContinToZZTo2e2tau_2018 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo2e2tau_2018")
GluGluToContinToZZTo2e2tau_2018.year = 2018
GluGluToContinToZZTo2e2tau_2018.dataset = "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/" + tag_2018 + "-v1/NANOAODSIM"
GluGluToContinToZZTo2e2tau_2018.sigma = 3.185 #pb

GluGluToContinToZZTo2mu2nu_2018 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo2mu2nu_2018")
GluGluToContinToZZTo2mu2nu_2018.year = 2018
GluGluToContinToZZTo2mu2nu_2018.dataset = "/GluGluToContinToZZTo2mu2nu_13TeV_MCFM701_pythia8/" + tag_2018 + "-v1/NANOAODSIM"
GluGluToContinToZZTo2mu2nu_2018.sigma = 14.93 #pb

GluGluToContinToZZTo2mu2tau_2018 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo2mu2tau_2018")
GluGluToContinToZZTo2mu2tau_2018.year = 2018
GluGluToContinToZZTo2mu2tau_2018.dataset = "/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/" + tag_2018 + "-v1/NANOAODSIM"
GluGluToContinToZZTo2mu2tau_2018.sigma = 3.185 #pb

GluGluToContinToZZTo4e_2018 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo4e_2018")
GluGluToContinToZZTo4e_2018.year = 2018
GluGluToContinToZZTo4e_2018.dataset = "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/" + tag_2018 + "-v1/NANOAODSIM"
GluGluToContinToZZTo4e_2018.sigma = 1.404 #pb

GluGluToContinToZZTo4mu_2018 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo4mu_2018")
GluGluToContinToZZTo4mu_2018.year = 2018
GluGluToContinToZZTo4mu_2018.dataset = "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/" + tag_2018 + "-v1/NANOAODSIM"
GluGluToContinToZZTo4mu_2018.sigma = 1.404 #pb

GluGluToContinToZZTo4tau_2018 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo4tau_2018")
GluGluToContinToZZTo4tau_2018.year = 2018
GluGluToContinToZZTo4tau_2018.dataset = "/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/" + tag_2018 + "-v1/NANOAODSIM"
GluGluToContinToZZTo4tau_2018.sigma = 1.404 #pb

GluGluToContinToZZTo4L_2018 = sample(ROOT.kGray+2, 1, 1001, "ZZ", "GluGluToContinToZZTo4L_2018")
GluGluToContinToZZTo4L_2018.year = 2018
GluGluToContinToZZTo4L_2018.dataset = "/GluGluToContinToZZTo4L_13TeV_TuneCP5_madgraphMLM_pythia8/" + tag_2018 + "-v1/NANOAODSIM"
GluGluToContinToZZTo4L_2018.sigma = 0.7882 #pb

ZZtoLep_2018 = sample(ROOT.kViolet-9, 1, 1001, "ZZ", "ZZtoLep_2018")
ZZtoLep_2018.year = 2018
ZZtoLep_2018.components = [ZZTo2L2Nu_2018, ZZJJTo4L_EWK_2018, ZZJJTo4L_QCD_2018, GluGluToContinToZZTo2e2nu_2018, GluGluToContinToZZTo2e2mu_2018, GluGluToContinToZZTo2e2tau_2018, GluGluToContinToZZTo2mu2nu_2018, GluGluToContinToZZTo2mu2tau_2018, GluGluToContinToZZTo4e_2018, GluGluToContinToZZTo4mu_2018, GluGluToContinToZZTo4tau_2018]

################################ TTbar ################################

'''
TT_DiLep_2018 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t}", "TT_DiLep_2018")
TT_DiLep_2018.sigma =  88.287 #pb
TT_DiLep_2018.year = 2018
TT_DiLep_2018.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v1/NANOAODSIM"
'''

TT_SemiLep_2018 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t}", "TT_SemiLep_2018")
TT_SemiLep_2018.sigma = 365.3 #pb
TT_SemiLep_2018.year = 2018
TT_SemiLep_2018.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

TT_Had_2018 = sample(ROOT.kRed+2, 1, 1001, "t#bar{t} had", "TT_Had_2018")
TT_Had_2018.sigma =  377.96 #pb
TT_Had_2018.year = 2018
TT_Had_2018.dataset = "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v1/NANOAODSIM"

TT_2018 = sample(ROOT.kRed+3, 1, 1001, "t#bar{t}", "TT_2018")
TT_2018.year = 2018
TT_2018.components = [TT_SemiLep_2018, TT_Had_2018] #TT_DiLep_2018,

###############################  TVX  ################################
TTGJets_2018 = sample(ROOT.kRed-2, 1, 1001, "t#bar{t}#gamma + jets", "TTGJets_2018")
TTGJets_2018.sigma = 4.078
TTGJets_2018.year = 2018
TTGJets_2018.dataset = "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/"+tag_2018+"-v1/NANOAODSIM"

TTZToQQ_2018 = sample(ROOT.kRed-2, 1, 1001, "t#bar{t}Z->q#bar{q}", "TTZToQQ_2018")
TTZToQQ_2018.sigma = 0.5104
TTZToQQ_2018.year = 2018
TTZToQQ_2018.dataset = "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/"+tag_2018+"_ext1-v1/NANOAODSIM"

TTZToLLNuNu_2018 = sample(ROOT.kRed-2, 1, 1001, "t#bar{t}Z to #ell#ell#nu#nu ", "TTZToLLNuNu_2018")
TTZToLLNuNu_2018.sigma = 0.2432
TTZToLLNuNu_2018.year = 2018
TTZToLLNuNu_2018.dataset = "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/"+tag_2018+"_ext1-v1/NANOAODSIM"

TTWJetsToQQ_2018 = sample(ROOT.kRed-2, 1, 1001, "t#bar{t}W + jets to qq ", "TTWJetsToQQ_2018")
TTWJetsToQQ_2018.sigma = 0.4316
TTWJetsToQQ_2018.year = 2018
TTWJetsToQQ_2018.dataset = "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/"+tag_2018+"-v1/NANOAODSIM"

TTWJetsToLNu_2018 = sample(ROOT.kRed-2, 1, 1001, "t#bar{t}W+jets to #ell#nu ", "TTWJetsToLNu_2018")
TTWJetsToLNu_2018.sigma = 0.2149
TTWJetsToLNu_2018.year = 2018
TTWJetsToLNu_2018.dataset = "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/"+tag_2018+"_ext1-v1/NANOAODSIM"

tZq_ll_4f_2018 = sample(ROOT.kRed-2, 1, 1001, "tZq to #ell#ell ", "tZq_ll_4f_2018")
tZq_ll_4f_2018.sigma = 0.07358
tZq_ll_4f_2018.year = 2018
tZq_ll_4f_2018.dataset = "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"_ext1-v1/NANOAODSIM"

TVX_2018 = sample(ROOT.kCyan-7, 1, 1001, "tVX", "TVX_2018")
TVX_2018.year = 2018
TVX_2018.components = [TTGJets_2018, TTZToQQ_2018, TTZToLLNuNu_2018, TTWJetsToQQ_2018, TTWJetsToLNu_2018, tZq_ll_4f_2018]

###############################  VGamma  ################################

ZG_2018 = sample(ROOT.kSpring+7, 1, 1001, "Z #gamma", "ZG_2018")
ZG_2018.sigma = 0.1097
ZG_2018.year = 2018
ZG_2018.dataset = "/LLAJJ_EWK_MLL-50_MJJ-120_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"_ext1-v1/NANOAODSIM"

WG_2018 = sample(ROOT.kSpring+7, 1, 1001, "W #gamma", "WG_2018")
WG_2018.sigma = 0.5439
WG_2018.year = 2018
WG_2018.dataset = "/LNuAJJ_EWK_MJJ-120_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

VG_2018 = sample(ROOT.kSpring+7, 1, 1001, "V#gamma", "VG_2018")
VG_2018.year = 2018
VG_2018.components = [ZG_2018, WG_2018]

###############################  Wrong Sign ################################

WWto2L2Nu_2018 = sample(ROOT.kAzure-9, 1, 1001, "WWto2L2Nu", "WWto2L2Nu_2018")
WWto2L2Nu_2018.sigma = 11.08
WWto2L2Nu_2018.year = 2018
WWto2L2Nu_2018.dataset = "/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v1/NANOAODSIM"

GluGluToWWToENuENu_2018 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToENuENu", "GluGluToWWToENuENu_2018")
GluGluToWWToENuENu_2018.sigma = 45.62
GluGluToWWToENuENu_2018.year = 2018
GluGluToWWToENuENu_2018.dataset = "/GluGluToWWToENEN_TuneCP5_13TeV_MCFM701_pythia8/"+tag_2018+"-v1/NANOAODSIM"

GluGluToWWToENuMNu2018 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToENuENu", "GluGluToWWToENuMNu2018")
GluGluToWWToENuMNu2018.sigma = 45.62
GluGluToWWToENuMNu2018.year = 2018
GluGluToWWToENuMNu2018.dataset = "/GluGluToWWToENMN_TuneCP5_13TeV_MCFM701_pythia8/"+tag_2018+"-v1/NANOAODSIM"

GluGluToWWToENuTNu2018 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToENuENu", "GluGluToWWToENuTNu2018")
GluGluToWWToENuTNu2018.sigma = 45.62
GluGluToWWToENuTNu2018.year = 2018
GluGluToWWToENuTNu2018.dataset = "/GluGluToWWToENTN_TuneCP5_13TeV_MCFM701_pythia8/"+tag_2018+"-v1/NANOAODSIM"

GluGluToWWToMNuENu_2018 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToMNuENu", "GluGluToWWToMNuENu_2018")
GluGluToWWToMNuENu_2018.sigma = 45.62
GluGluToWWToMNuENu_2018.year = 2018
GluGluToWWToMNuENu_2018.dataset = "/GluGluToWWToMNEN_TuneCP5_13TeV_MCFM701_pythia8/"+tag_2018+"-v1/NANOAODSIM"

GluGluToWWToMNuMNu2018 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToMNuENu", "GluGluToWWToMNuMNu2018")
GluGluToWWToMNuMNu2018.sigma = 45.62
GluGluToWWToMNuMNu2018.year = 2018
GluGluToWWToMNuMNu2018.dataset = "/GluGluToWWToMNMN_TuneCP5_13TeV_MCFM701_pythia8/"+tag_2018+"-v1/NANOAODSIM"

GluGluToWWToMNuTNu2018 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToMNuENu", "GluGluToWWToMNuTNu2018")
GluGluToWWToMNuTNu2018.sigma = 45.62
GluGluToWWToMNuTNu2018.year = 2018
GluGluToWWToMNuTNu2018.dataset = "/GluGluToWWToMNTN_TuneCP5_13TeV_MCFM701_pythia8/"+tag_2018+"-v1/NANOAODSIM"

GluGluToWWToTNuENu_2018 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToTNuENu", "GluGluToWWToTNuENu_2018")
GluGluToWWToTNuENu_2018.sigma = 45.62
GluGluToWWToTNuENu_2018.year = 2018
GluGluToWWToTNuENu_2018.dataset = "/GluGluToWWToTNEN_TuneCP5_13TeV_MCFM701_pythia8/"+tag_2018+"-v1/NANOAODSIM"

GluGluToWWToTNuMNu2018 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToTNuENu", "GluGluToWWToTNuMNu2018")
GluGluToWWToTNuMNu2018.sigma = 45.62
GluGluToWWToTNuMNu2018.year = 2018
GluGluToWWToTNuMNu2018.dataset = "/GluGluToWWToTNMN_TuneCP5_13TeV_MCFM701_pythia8/"+tag_2018+"-v1/NANOAODSIM"

GluGluToWWToTNuTNu2018 = sample(ROOT.kAzure-9, 1, 1001, "GluGluToWWToTNuENu", "GluGluToWWToTNuTNu2018")
GluGluToWWToTNuTNu2018.sigma = 45.62
GluGluToWWToTNuTNu2018.year = 2018
GluGluToWWToTNuTNu2018.dataset = "/GluGluToWWToTNTN_TuneCP5_13TeV_MCFM701_pythia8/"+tag_2018+"-v1/NANOAODSIM"

TTTo2L2Nu_2018 = sample(ROOT.kAzure-9, 1, 1001, "t#bar{t} DiLep", "TTTo2L2Nu_2018")
TTTo2L2Nu_2018.sigma =  88.287 #pb
TTTo2L2Nu_2018.year = 2018
TTTo2L2Nu_2018.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v1/NANOAODSIM"

STtW_top_2018 = sample(ROOT.kAzure-9, 1, 1001, "single t", "STtW_top_2018")
STtW_top_2018.sigma =  34.91#pb
STtW_top_2018.year = 2018
STtW_top_2018.dataset = "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"_ext1-v1/NANOAODSIM"

STtW_antitop_2018 = sample(ROOT.kAzure-9, 1, 1001, "single t", "STtW_antitop_2018")
STtW_antitop_2018.sigma =  34.97#pb
STtW_antitop_2018.year = 2018
STtW_antitop_2018.dataset = "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"_ext1-v1/NANOAODSIM"

GluGluHToWWTo2L2Nu_2018 = sample(ROOT.kAzure-9, 1, 1001, "GluGluHToWWTo2L2Nu", "GluGluHToWWTo2L2Nu_2018")
GluGluHToWWTo2L2Nu_2018.sigma =  28.87#pb
GluGluHToWWTo2L2Nu_2018.year = 2018
GluGluHToWWTo2L2Nu_2018.dataset = "/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/"+tag_2018+"-v1/NANOAODSIM"

GluGluHToZZTo2L2Q_2018 = sample(ROOT.kAzure-9, 1, 1001, "GluGluHToZZTo2L2Q", "GluGluHToZZTo2L2Q_2018")
GluGluHToZZTo2L2Q_2018.sigma =  28.87#pb
GluGluHToZZTo2L2Q_2018.year = 2018
GluGluHToZZTo2L2Q_2018.dataset = "/GluGluHToZZTo2L2Q_M125_13TeV_powheg2_JHUGenV7011_pythia8/"+tag_2018+"-v1/NANOAODSIM"

GluGluHToZZTo4L_2018 = sample(ROOT.kAzure-9, 1, 1001, "GluGluHToZZTo4L", "GluGluHToZZTo4L_2018")
GluGluHToZZTo4L_2018.sigma =  28.87#pb
GluGluHToZZTo4L_2018.year = 2018
GluGluHToZZTo4L_2018.dataset = "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/"+tag_2018+"-v1/NANOAODSIM"

GluGluHToTauTau_2018 = sample(ROOT.kAzure-9, 1, 1001, "GluGluHToTauTau", "GluGluHToTauTau_2018")
GluGluHToTauTau_2018.sigma =  30.52#pb
GluGluHToTauTau_2018.year = 2018
GluGluHToTauTau_2018.dataset = "/GluGluHToTauTau_M125_13TeV_powheg_pythia8/"+tag_2018+"-v1/NANOAODSIM"

VBFHToWWTo2L2Nu_2018 = sample(ROOT.kAzure-9, 1, 1001, "VBFHToWWTo2L2Nu", "VBFHToWWTo2L2Nu_2018")
VBFHToWWTo2L2Nu_2018.sigma =  3.879#pb
VBFHToWWTo2L2Nu_2018.year = 2018
VBFHToWWTo2L2Nu_2018.dataset = "/VBFHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/"+tag_2018+"-v1/NANOAODSIM"

VBFHToTauTau_2018 = sample(ROOT.kAzure-9, 1, 1001, "VBFHToTauTau", "VBFHToTauTau_2018")
VBFHToTauTau_2018.sigma =  3.879#pb
VBFHToTauTau_2018.year = 2018
VBFHToTauTau_2018.dataset = "/VBFHToTauTau_M125_13TeV_powheg_pythia8"+tag_2018+"_ext1-v1/NANOAODSIM"

ttHToNonbb_2018 = sample(ROOT.kAzure-9, 1, 1001, "ttHToNonbb", "ttHToNonbb_2018")
ttHToNonbb_2018.sigma =  0.5269#pb
ttHToNonbb_2018.year = 2018
ttHToNonbb_2018.dataset = "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v1/NANOAODSIM"

VHToNonbb_2018 = sample(ROOT.kAzure-9, 1, 1001, "VHToNonbb", "VHToNonbb_2018")
VHToNonbb_2018.sigma =  2.127#pb
VHToNonbb_2018.year = 2018
VHToNonbb_2018.dataset = "/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/"+tag_2018+"-v1/NANOAODSIM"

WrongSign_2018 = sample(ROOT.kAzure-9, 1, 1001, "Leptonic t#bar{t} + WS", "WrongSign_2018")
WrongSign_2018.year = 2018
WrongSign_2018.components = [WWto2L2Nu_2018, GluGluToWWToENuENu_2018, GluGluToWWToENuMNu2018, 
                            GluGluToWWToENuTNu2018, GluGluToWWToMNuENu_2018, GluGluToWWToMNuMNu2018, 
                            GluGluToWWToMNuTNu2018, GluGluToWWToTNuENu_2018, GluGluToWWToTNuMNu2018, 
                            GluGluToWWToTNuTNu2018, STtW_top_2018, GluGluHToWWTo2L2Nu_2018, 
                            GluGluHToZZTo2L2Q_2018, GluGluHToZZTo4L_2018, GluGluHToTauTau_2018, 
                            VBFHToWWTo2L2Nu_2018, VBFHToTauTau_2018, ttHToNonbb_2018, VHToNonbb_2018]


###############################     Other   ################################


WWTo2L2Nu_DoubleScattering_2018 = sample(ROOT.kOrange-4, 1, 1001, "WWTo2L2Nu_DoubleScattering", "WWTo2L2Nu_DoubleScattering_2018")
WWTo2L2Nu_DoubleScattering_2018.sigma =  0.1703#pb
WWTo2L2Nu_DoubleScattering_2018.year = 2018
WWTo2L2Nu_DoubleScattering_2018.dataset = "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/"+tag_2018+"-v1/NANOAODSIM"

WWW_4F_2018 = sample(ROOT.kOrange-4, 1, 1001, "WWW_4F", "WWW_4F_2018")
WWW_4F_2018.sigma =  0.2086#pb
WWW_4F_2018.year = 2018
WWW_4F_2018.dataset = "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/"+tag_2018+"_ext1-v1/NANOAODSIM"

WWZTo3L1Nu2Q_2018 = sample(ROOT.kOrange-4, 1, 1001, "WWZTo3L1Nu2Q", "WWZTo3L1Nu2Q_2018")
WWZTo3L1Nu2Q_2018.sigma =  0.008039#pb
WWZTo3L1Nu2Q_2018.year = 2018
WWZTo3L1Nu2Q_2018.dataset = "/WWZTo3L1Nu2Q_4f_TuneCP5_13TeV_amcatnlo_pythia8/"+tag_2018+"-v1/NANOAODSIM"


WZZ_2018 = sample(ROOT.kOrange-4, 1, 1001, "WZZ", "WZZ_2018")
WZZ_2018.sigma =  0.05565#pb
WZZ_2018.year = 2018
WZZ_2018.dataset = "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/"+tag_2018+"_ext1-v1/NANOAODSIM"


ZZZ_2018 = sample(ROOT.kOrange-4, 1, 1001, "ZZZ", "ZZZ_2018")
ZZZ_2018.sigma =  0.013989#pb
ZZZ_2018.year = 2018
ZZZ_2018.dataset = "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/"+tag_2018+"_ext1-v1/NANOAODSIM"

WWG_2018 = sample(ROOT.kOrange-4, 1, 1001, "WWG", "WWG_2018")
WWG_2018.sigma =  0.2147#pb
WWG_2018.year = 2018
WWG_2018.dataset = "/WWG_TuneCP5_13TeV-amcatnlo-pythia8/"+tag_2018+"_ext1-v1/NANOAODSIM"

Other_2018 = sample(ROOT.kOrange-4, 1, 1001, "Other", "Other_2018")
Other_2018.year = 2018
Other_2018.components = [WWTo2L2Nu_DoubleScattering_2018, WWW_4F_2018, WWZTo3L1Nu2Q_2018, WZZ_2018, ZZZ_2018, WWG_2018]

OtherWS_2018 = sample(ROOT.kOrange-4, 1, 1001, "Other + Wrong Sign", "OtherWS_2018")
OtherWS_2018.year = 2018
OtherWS_2018.components = [WWTo2L2Nu_DoubleScattering_2018, WWW_4F_2018, WWZTo3L1Nu2Q_2018, WZZ_2018, ZZZ_2018, WWG_2018,
                           WWto2L2Nu_2018, GluGluToWWToENuENu_2018, GluGluToWWToENuMNu2018, 
                           GluGluToWWToENuTNu2018, GluGluToWWToMNuENu_2018, GluGluToWWToMNuMNu2018, 
                           GluGluToWWToMNuTNu2018, GluGluToWWToTNuENu_2018, GluGluToWWToTNuMNu2018, 
                           GluGluToWWToTNuTNu2018, STtW_top_2018, GluGluHToWWTo2L2Nu_2018, 
                           GluGluHToZZTo2L2Q_2018, GluGluHToZZTo4L_2018, GluGluHToTauTau_2018, 
                           VBFHToWWTo2L2Nu_2018, VBFHToTauTau_2018, ttHToNonbb_2018, VHToNonbb_2018]

################################ WJets ################################
WJetsHT70to100_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT70to100_2018")
WJetsHT70to100_2018.sigma = 1353 * 1.21 #pb
WJetsHT70to100_2018.year = 2018
WJetsHT70to100_2018.dataset = "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

WJetsHT100to200_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT100to200_2018")
WJetsHT100to200_2018.sigma = 1345 * 1.21 #pb
WJetsHT100to200_2018.year = 2018
WJetsHT100to200_2018.dataset = "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

WJetsHT200to400_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT200to400_2018")
WJetsHT200to400_2018.sigma = 359.7 * 1.21 #pb
WJetsHT200to400_2018.year = 2018
WJetsHT200to400_2018.dataset = "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#WJetsHT200to400_2018.files = jr.json_reader(path+"/WJets_HT200To400_2018.json")

WJetsHT400to600_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT400to600_2018")
WJetsHT400to600_2018.sigma = 48.91 * 1.21 #pb
WJetsHT400to600_2018.year = 2018
WJetsHT400to600_2018.dataset = "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#WJetsHT400to600_2018.files = jr.json_reader(path+"/WJets_HT400To600_2018.json")

WJetsHT600to800_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT600to800_2018")
WJetsHT600to800_2018.sigma = 12.05 * 1.21 #pb
WJetsHT600to800_2018.year = 2018
WJetsHT600to800_2018.dataset = "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#WJetsHT600to800_2018.files = jr.json_reader(path+"/WJets_HT600To800_2018.json")

WJetsHT800to1200_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT800to1200_2018")
WJetsHT800to1200_2018.sigma = 5.501 * 1.21 #pb
WJetsHT800to1200_2018.year = 2018
WJetsHT800to1200_2018.dataset = "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#WJetsHT800to1200_2018.files = jr.json_reader(path+"/WJets_HT800To1200_2018.json")

WJetsHT1200to2500_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT1200to2500_2018")
WJetsHT1200to2500_2018.sigma = 1.329 * 1.21 #pb
WJetsHT1200to2500_2018.year = 2018
WJetsHT1200to2500_2018.dataset = "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#WJetsHT1200to2500_2018.files = jr.json_reader(path+"/WJets_HT1200To2500_2018.json")

WJetsHT2500toInf_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT2500toInf_2018")
WJetsHT2500toInf_2018.sigma = 0.03216 * 1.2 #pb
WJetsHT2500toInf_2018.year = 2018
WJetsHT2500toInf_2018.dataset = "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#WJetsHT2500toInf_2018.files = jr.json_reader(path+"/WJets_HT2500ToInf_2018.json")

WJets_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJets_2018")
WJets_2018.year = 2018
WJets_2018.components = [WJetsHT70to100_2018, WJetsHT100to200_2018, WJetsHT200to400_2018, WJetsHT400to600_2018, WJetsHT600to800_2018, WJetsHT800to1200_2018, WJetsHT1200to2500_2018, WJetsHT2500toInf_2018]

################################ WZ ################################
WZ_2018 = sample(ROOT.kYellow-7, 1, 1001, "WZ", "WZ_2018")
WZ_2018.sigma = 47.13
WZ_2018.year = 2018
WZ_2018.dataset = "/WZ_TuneCP5_13TeV-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

################################ DrellYan ################################
DY1JetsToLL_2018 = sample(ROOT.kAzure+6, 1, 1001, "DY + 1 Jet", "DY1JetsToLL_2018")
DY1JetsToLL_2018.sigma = 1012.0
DY1JetsToLL_2018.year = 2018
DY1JetsToLL_2018.dataset = "/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

DY2JetsToLL_2018 = sample(ROOT.kAzure+6, 1, 1001, "DY + 2 Jets", "DY2JetsToLL_2018")
DY2JetsToLL_2018.sigma = 330.4
DY2JetsToLL_2018.year = 2018
DY2JetsToLL_2018.dataset = "/DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

DY3JetsToLL_2018 = sample(ROOT.kAzure+6, 1, 1001, "DY + 3 Jets", "DY3JetsToLL_2018")
DY3JetsToLL_2018.sigma = 101.8
DY3JetsToLL_2018.year = 2018
DY3JetsToLL_2018.dataset = "/DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

DY4JetsToLL_2018 = sample(ROOT.kAzure+6, 1, 1001, "DY + 4+ Jets", "DY4JetsToLL_2018")
DY4JetsToLL_2018.sigma = 54.80
DY4JetsToLL_2018.year = 2018
DY4JetsToLL_2018.dataset = "/DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

DYJetsToLL_2018 = sample(ROOT.kAzure+6, 1, 1001, "DY + Jets", "DYJetsToLL_2018")
DYJetsToLL_2018.year = 2018
DYJetsToLL_2018.components = [DY1JetsToLL_2018, DY2JetsToLL_2018, DY3JetsToLL_2018, DY4JetsToLL_2018]

################################ ssWW EWK ################################
WpWpJJ_EWK_2018 = sample(ROOT.kBlue, 1, 1001, "EW ssWW", "WpWpJJ_EWK_2018")
WpWpJJ_EWK_2018.sigma = 0.02064
WpWpJJ_EWK_2018.year = 2018
WpWpJJ_EWK_2018.dataset = "/WpWpJJ_EWK_TuneCP5_13TeV-madgraph-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

WpWpJJ_QCD_2018 = sample(ROOT.kBlue, 1, 1001, "QCD ssWW", "WpWpJJ_QCD_2018")
WpWpJJ_QCD_2018.sigma = 0.01538
WpWpJJ_QCD_2018.year = 2018
WpWpJJ_QCD_2018.dataset = "/WpWpJJ_QCD_TuneCP5_13TeV-madgraph-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

VBS_SSWW_LL_SM_2018 = sample(ROOT.kBlack, 1, 1001, "VBS ssWW LL", "VBS_SSWW_LL_SM_2018")
VBS_SSWW_LL_SM_2018.sigma = 0.002014
VBS_SSWW_LL_SM_2018.year = 2018
VBS_SSWW_LL_SM_2018.dataset = "/VBS_SSWW_LL_polarization_TuneCP5_13TeV-madgraph-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

VBS_SSWW_TL_SM_2018 = sample(ROOT.kBlack, 1, 1001, "VBS ssWW TL", "VBS_SSWW_TL_SM_2018")
VBS_SSWW_TL_SM_2018.sigma = 0.01036
VBS_SSWW_TL_SM_2018.year = 2018
VBS_SSWW_TL_SM_2018.dataset = "/VBS_SSWW_TL_polarization_TuneCP5_13TeV-madgraph-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

VBS_SSWW_TT_SM_2018 = sample(ROOT.kBlack, 1, 1001, "VBS ssWW TT", "VBS_SSWW_TT_SM_2018")
VBS_SSWW_TT_SM_2018.sigma = 0.01595
VBS_SSWW_TT_SM_2018.year = 2018
VBS_SSWW_TT_SM_2018.dataset = "/VBS_SSWW_TT_polarization_TuneCP5_13TeV-madgraph-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

VBS_SSWW_SM_2018 = sample(ROOT.kRed+2, 1, 1001, "VBS ssWW", "VBS_SSWW_SM_2018")
VBS_SSWW_SM_2018.year = 2018
VBS_SSWW_SM_2018.components = [VBS_SSWW_LL_SM_2018, VBS_SSWW_TL_SM_2018, VBS_SSWW_TT_SM_2018]

VBS_SSWW_cHW_BSM_2018 = sample(ROOT.kGreen+3, 1, 1001, "VBS ssWW c_{HW} (only BSM)", "VBS_SSWW_cHW_BSM_2018")
VBS_SSWW_cHW_BSM_2018.sigma = 0.002014
VBS_SSWW_cHW_BSM_2018.year = 2018
VBS_SSWW_cHW_BSM_2018.dataset = "/VBS_SSWW_cHW_BSM_TuneCP5_13TeV-madgraph-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

VBS_SSWW_cHW_INT_2018 = sample(ROOT.kGreen+3, 1, 1001, "VBS ssWW c_{HW} (only INT)", "VBS_SSWW_cHW_INT_2018")
VBS_SSWW_cHW_INT_2018.sigma = 0.002014
VBS_SSWW_cHW_INT_2018.year = 2018
VBS_SSWW_cHW_INT_2018.dataset = "/VBS_SSWW_cHW_INT_TuneCP5_13TeV-madgraph-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

VBS_SSWW_cHW_2018 = sample(ROOT.kMagenta+2, 1, 1001, "VBS ssWW c_{HW} (BSM+INT)", "VBS_SSWW_cHW_2018")
VBS_SSWW_cHW_2018.year = 2018
VBS_SSWW_cHW_2018.components = [VBS_SSWW_cHW_BSM_2018]#, VBS_SSWW_cHW_INT_2018]

VBS_SSWW_cW_BSM_2018 = sample(ROOT.kMagenta+3, 1, 1001, "VBS ssWW c_{W} (only BSM)", "VBS_SSWW_cW_BSM_2018")
VBS_SSWW_cW_BSM_2018.sigma = 0.002014
VBS_SSWW_cW_BSM_2018.year = 2018
VBS_SSWW_cW_BSM_2018.dataset = "/VBS_SSWW_cW_BSM_TuneCP5_13TeV-madgraph-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

VBS_SSWW_cW_INT_2018 = sample(ROOT.kMagenta+3, 1, 1001, "VBS ssWW c_{W} (only INT)", "VBS_SSWW_cW_INT_2018")
VBS_SSWW_cW_INT_2018.sigma = 0.002014
VBS_SSWW_cW_INT_2018.year = 2018
VBS_SSWW_cW_INT_2018.dataset = "/VBS_SSWW_cW_INT_TuneCP5_13TeV-madgraph-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

VBS_SSWW_cW_2018 = sample(ROOT.kMagenta+1, 1, 1001, "VBS ssWW c_{W} (BSM+INT)", "VBS_SSWW_cW_2018")
VBS_SSWW_cW_2018.year = 2018
VBS_SSWW_cW_2018.components = [VBS_SSWW_cW_BSM_2018]#, VBS_SSWW_cW_INT_2018]

VBS_SSWW_cW_cHW_2018 = sample(ROOT.kAzure+3, 1, 1001, "VBS ssWW c_{HW} + c_{W}", "VBS_SSWW_cW_cHW_2018")
VBS_SSWW_cW_cHW_2018.sigma = 0.002014
VBS_SSWW_cW_cHW_2018.year = 2018
VBS_SSWW_cW_cHW_2018.dataset = "/VBS_SSWW_cW_cHW_TuneCP5_13TeV-madgraph-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

VBS_SSWW_DIM6_2018 = sample(ROOT.kGreen+3, 1, 1001, "VBS ssWW dim-6 EFT", "VBS_SSWW_DIM6_2018")
VBS_SSWW_DIM6_2018.year = 2018
VBS_SSWW_DIM6_2018.components = [VBS_SSWW_cHW_BSM_2018, VBS_SSWW_cW_BSM_2018, VBS_SSWW_cW_cHW_2018]

VBS_SSWW_DIM6_SM_2018 = sample(ROOT.kGreen+2, 1, 1001, "VBS ssWW dim-6 EFT + SM", "VBS_SSWW_DIM6_SM_2018")
VBS_SSWW_DIM6_SM_2018.year = 2018
VBS_SSWW_DIM6_SM_2018.components = [VBS_SSWW_cHW_BSM_2018, VBS_SSWW_cHW_INT_2018, VBS_SSWW_cW_BSM_2018, VBS_SSWW_cW_INT_2018, VBS_SSWW_cW_cHW_2018, VBS_SSWW_LL_SM_2018, VBS_SSWW_TL_SM_2018, VBS_SSWW_TT_SM_2018]

VBS_SSWW_cHW_SM_2018 = sample(ROOT.kGreen+2, 1, 1001, "VBS ssWW c_{HW} + SM", "VBS_SSWW_cHW_SM_2018")
VBS_SSWW_cHW_SM_2018.year = 2018
VBS_SSWW_cHW_SM_2018.components = [VBS_SSWW_cHW_BSM_2018, VBS_SSWW_cHW_INT_2018, VBS_SSWW_LL_SM_2018, VBS_SSWW_TL_SM_2018, VBS_SSWW_TT_SM_2018]

VBS_SSWW_cW_SM_2018 = sample(ROOT.kGreen+2, 1, 1001, "VBS ssWW c_{W} + SM", "VBS_SSWW_cW_SM_2018")
VBS_SSWW_cW_SM_2018.year = 2018
VBS_SSWW_cW_SM_2018.components = [VBS_SSWW_cW_BSM_2018, VBS_SSWW_cW_INT_2018, VBS_SSWW_LL_SM_2018, VBS_SSWW_TL_SM_2018, VBS_SSWW_TT_SM_2018]

VBS_SSWW_aQGC_2018 = sample(ROOT.kGreen, 1, 1001, "VBS ssWW dim-8 EFT", "VBS_SSWW_aQGC_2018")
VBS_SSWW_aQGC_2018.sigma = 0.1191
VBS_SSWW_aQGC_2018.year = 2018
VBS_SSWW_aQGC_2018.dataset = "/WWJJ_SS_WToLNu_EWK_aQGC-FT-FS-FM_TuneCP5_13TeV_madgraph-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

###### f_{s0} #######
VBS_SSWW_FS0_25_BSM_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 25 TeV^{-4} BSM", "VBS_SSWW_FS0_25_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS0_25_BSM_2018.sigma = 0.1191
VBS_SSWW_FS0_25_BSM_2018.year = 2018

VBS_SSWW_FS0_25_INT_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 25 TeV^{-4} INT", "VBS_SSWW_FS0_25_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS0_25_INT_2018.sigma = 0.1191
VBS_SSWW_FS0_25_INT_2018.year = 2018

VBS_SSWW_FS0_25_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 25 TeV^{-4}", "VBS_SSWW_FS0_25_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS0_25_2018.year = 2018
VBS_SSWW_FS0_25_2018.components = [VBS_SSWW_FS0_25_BSM_2018, VBS_SSWW_FS0_25_INT_2018]

VBS_SSWW_FS0_5_BSM_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 5 TeV^{-4} BSM", "VBS_SSWW_FS0_5_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS0_5_BSM_2018.sigma = 0.1191
VBS_SSWW_FS0_5_BSM_2018.year = 2018

VBS_SSWW_FS0_5_INT_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 5 TeV^{-4} INT", "VBS_SSWW_FS0_5_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS0_5_INT_2018.sigma = 0.1191
VBS_SSWW_FS0_5_INT_2018.year = 2018

VBS_SSWW_FS0_5_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 5 TeV^{-4}", "VBS_SSWW_FS0_5_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS0_5_2018.year = 2018
VBS_SSWW_FS0_5_2018.components = [VBS_SSWW_FS0_5_BSM_2018, VBS_SSWW_FS0_5_INT_2018]

VBS_SSWW_FS0_0_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FS0_0_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS0_0_2018.sigma = 0.1191
VBS_SSWW_FS0_0_2018.year = 2018

VBS_SSWW_FS0_25_SM_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 25 TeV^{-4}", "VBS_SSWW_FS0_25_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS0_25_SM_2018.year = 2018
VBS_SSWW_FS0_25_SM_2018.components = [VBS_SSWW_FS0_25_BSM_2018, VBS_SSWW_FS0_25_INT_2018, VBS_SSWW_FS0_0_2018]

VBS_SSWW_FS0_5_SM_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s0}/#Lambda^{4} = 5 TeV^{-4}", "VBS_SSWW_FS0_5_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS0_5_SM_2018.year = 2018
VBS_SSWW_FS0_5_SM_2018.components = [VBS_SSWW_FS0_5_BSM_2018, VBS_SSWW_FS0_5_INT_2018, VBS_SSWW_FS0_0_2018]

###### f_{s1} #######
VBS_SSWW_FS1_50_BSM_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 50 TeV^{-4} BSM", "VBS_SSWW_FS1_50_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS1_50_BSM_2018.sigma = 0.1191
VBS_SSWW_FS1_50_BSM_2018.year = 2018

VBS_SSWW_FS1_50_INT_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 50 TeV^{-4} INT", "VBS_SSWW_FS1_50_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS1_50_INT_2018.sigma = 0.1191
VBS_SSWW_FS1_50_INT_2018.year = 2018

VBS_SSWW_FS1_50_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 50 TeV^{-4}", "VBS_SSWW_FS1_50_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS1_50_2018.year = 2018
VBS_SSWW_FS1_50_2018.components = [VBS_SSWW_FS1_50_BSM_2018, VBS_SSWW_FS1_50_INT_2018]

VBS_SSWW_FS1_10_BSM_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 10 TeV^{-4} BSM", "VBS_SSWW_FS1_10_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS1_10_BSM_2018.sigma = 0.1191
VBS_SSWW_FS1_10_BSM_2018.year = 2018

VBS_SSWW_FS1_10_INT_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 10 TeV^{-4} INT", "VBS_SSWW_FS1_10_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS1_10_INT_2018.sigma = 0.1191
VBS_SSWW_FS1_10_INT_2018.year = 2018

VBS_SSWW_FS1_10_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 10 TeV^{-4}", "VBS_SSWW_FS1_10_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS1_10_2018.year = 2018
VBS_SSWW_FS1_10_2018.components = [VBS_SSWW_FS1_10_BSM_2018, VBS_SSWW_FS1_10_INT_2018]

VBS_SSWW_FS1_0_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FS1_0_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS1_0_2018.sigma = 0.1191
VBS_SSWW_FS1_0_2018.year = 2018

VBS_SSWW_FS1_50_SM_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 50 TeV^{-4}", "VBS_SSWW_FS1_50_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS1_50_SM_2018.year = 2018
VBS_SSWW_FS1_50_SM_2018.components = [VBS_SSWW_FS1_50_BSM_2018, VBS_SSWW_FS1_50_INT_2018, VBS_SSWW_FS1_0_2018]

VBS_SSWW_FS1_10_SM_2018 = sample(ROOT.kAzure, 1, 1001, "f_{s1}/#Lambda^{4} = 10 TeV^{-4}", "VBS_SSWW_FS1_10_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FS1_10_SM_2018.year = 2018
VBS_SSWW_FS1_10_SM_2018.components = [VBS_SSWW_FS1_10_BSM_2018, VBS_SSWW_FS1_10_INT_2018, VBS_SSWW_FS1_0_2018]

###### f_{m0} #######
VBS_SSWW_FM0_25_BSM_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 25 TeV^{-4} BSM", "VBS_SSWW_FM0_25_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM0_25_BSM_2018.sigma = 0.1191
VBS_SSWW_FM0_25_BSM_2018.year = 2018

VBS_SSWW_FM0_25_INT_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 25 TeV^{-4} INT", "VBS_SSWW_FM0_25_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM0_25_INT_2018.sigma = 0.1191
VBS_SSWW_FM0_25_INT_2018.year = 2018

VBS_SSWW_FM0_25_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 25 TeV^{-4}", "VBS_SSWW_FM0_25_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM0_25_2018.year = 2018
VBS_SSWW_FM0_25_2018.components = [VBS_SSWW_FM0_25_BSM_2018, VBS_SSWW_FM0_25_INT_2018]

VBS_SSWW_FM0_5_BSM_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 5 TeV^{-4} BSM", "VBS_SSWW_FM0_5_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM0_5_BSM_2018.sigma = 0.1191
VBS_SSWW_FM0_5_BSM_2018.year = 2018

VBS_SSWW_FM0_5_INT_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 5 TeV^{-4} INT", "VBS_SSWW_FM0_5_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM0_5_INT_2018.sigma = 0.1191
VBS_SSWW_FM0_5_INT_2018.year = 2018

VBS_SSWW_FM0_5_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 5 TeV^{-4}", "VBS_SSWW_FM0_5_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM0_5_2018.year = 2018
VBS_SSWW_FM0_5_2018.components = [VBS_SSWW_FM0_5_BSM_2018, VBS_SSWW_FM0_5_INT_2018]

VBS_SSWW_FM0_0_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FM0_0_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM0_0_2018.sigma = 0.1191
VBS_SSWW_FM0_0_2018.year = 2018

VBS_SSWW_FM0_25_SM_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 25 TeV^{-4}", "VBS_SSWW_FM0_25_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM0_25_SM_2018.year = 2018
VBS_SSWW_FM0_25_SM_2018.components = [VBS_SSWW_FM0_25_BSM_2018, VBS_SSWW_FM0_25_INT_2018, VBS_SSWW_FM0_0_2018]

VBS_SSWW_FM0_5_SM_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m0}/#Lambda^{4} = 5 TeV^{-4}", "VBS_SSWW_FM0_5_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM0_5_SM_2018.year = 2018
VBS_SSWW_FM0_5_SM_2018.components = [VBS_SSWW_FM0_5_BSM_2018, VBS_SSWW_FM0_5_INT_2018, VBS_SSWW_FM0_0_2018]

###### f_{m1} #######
VBS_SSWW_FM1_25_BSM_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 25 TeV^{-4} BSM", "VBS_SSWW_FM1_25_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM1_25_BSM_2018.sigma = 0.1191
VBS_SSWW_FM1_25_BSM_2018.year = 2018

VBS_SSWW_FM1_25_INT_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 25 TeV^{-4} INT", "VBS_SSWW_FM1_25_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM1_25_INT_2018.sigma = 0.1191
VBS_SSWW_FM1_25_INT_2018.year = 2018

VBS_SSWW_FM1_25_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 25 TeV^{-4}", "VBS_SSWW_FM1_25_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM1_25_2018.year = 2018
VBS_SSWW_FM1_25_2018.components = [VBS_SSWW_FM1_25_BSM_2018, VBS_SSWW_FM1_25_INT_2018]

VBS_SSWW_FM1_5_BSM_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 10 TeV^{-4} BSM", "VBS_SSWW_FM1_5_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM1_5_BSM_2018.sigma = 0.1191
VBS_SSWW_FM1_5_BSM_2018.year = 2018

VBS_SSWW_FM1_5_INT_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 10 TeV^{-4} INT", "VBS_SSWW_FM1_5_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM1_5_INT_2018.sigma = 0.1191
VBS_SSWW_FM1_5_INT_2018.year = 2018

VBS_SSWW_FM1_5_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 10 TeV^{-4}", "VBS_SSWW_FM1_5_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM1_5_2018.year = 2018
VBS_SSWW_FM1_5_2018.components = [VBS_SSWW_FM1_5_BSM_2018, VBS_SSWW_FM1_5_INT_2018]

VBS_SSWW_FM1_0_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FM1_0_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM1_0_2018.sigma = 0.1191
VBS_SSWW_FM1_0_2018.year = 2018

VBS_SSWW_FM1_25_SM_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 25 TeV^{-4}", "VBS_SSWW_FM1_25_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM1_25_SM_2018.year = 2018
VBS_SSWW_FM1_25_SM_2018.components = [VBS_SSWW_FM1_25_BSM_2018, VBS_SSWW_FM1_25_INT_2018, VBS_SSWW_FM1_0_2018]

VBS_SSWW_FM1_5_SM_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m1}/#Lambda^{4} = 10 TeV^{-4}", "VBS_SSWW_FM1_5_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM1_5_SM_2018.year = 2018
VBS_SSWW_FM1_5_SM_2018.components = [VBS_SSWW_FM1_5_BSM_2018, VBS_SSWW_FM1_5_INT_2018, VBS_SSWW_FM1_0_2018]

###### f_{m6} #######
VBS_SSWW_FM6_25_BSM_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 25 TeV^{-4} BSM", "VBS_SSWW_FM6_25_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM6_25_BSM_2018.sigma = 0.1191
VBS_SSWW_FM6_25_BSM_2018.year = 2018

VBS_SSWW_FM6_25_INT_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 25 TeV^{-4} INT", "VBS_SSWW_FM6_25_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM6_25_INT_2018.sigma = 0.1191
VBS_SSWW_FM6_25_INT_2018.year = 2018

VBS_SSWW_FM6_25_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 25 TeV^{-4}", "VBS_SSWW_FM6_25_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM6_25_2018.year = 2018
VBS_SSWW_FM6_25_2018.components = [VBS_SSWW_FM6_25_BSM_2018, VBS_SSWW_FM6_25_INT_2018]

VBS_SSWW_FM6_5_BSM_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 5 TeV^{-4} BSM", "VBS_SSWW_FM6_5_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM6_5_BSM_2018.sigma = 0.1191
VBS_SSWW_FM6_5_BSM_2018.year = 2018

VBS_SSWW_FM6_5_INT_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 5 TeV^{-4} INT", "VBS_SSWW_FM6_5_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM6_5_INT_2018.sigma = 0.1191
VBS_SSWW_FM6_5_INT_2018.year = 2018

VBS_SSWW_FM6_5_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 5 TeV^{-4}", "VBS_SSWW_FM6_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM6_5_2018.year = 2018
VBS_SSWW_FM6_5_2018.components = [VBS_SSWW_FM6_5_BSM_2018, VBS_SSWW_FM6_5_INT_2018]

VBS_SSWW_FM6_0_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FM6_0_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM6_0_2018.sigma = 0.1191
VBS_SSWW_FM6_0_2018.year = 2018

VBS_SSWW_FM6_25_SM_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 25 TeV^{-4}", "VBS_SSWW_FM6_25_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM6_25_SM_2018.year = 2018
VBS_SSWW_FM6_25_SM_2018.components = [VBS_SSWW_FM6_25_BSM_2018, VBS_SSWW_FM6_25_INT_2018, VBS_SSWW_FM6_0_2018]

VBS_SSWW_FM6_5_SM_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m6}/#Lambda^{4} = 5 TeV^{-4}", "VBS_SSWW_FM6_5_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM6_5_SM_2018.year = 2018
VBS_SSWW_FM6_5_SM_2018.components = [VBS_SSWW_FM6_5_BSM_2018, VBS_SSWW_FM6_5_INT_2018, VBS_SSWW_FM6_0_2018]

###### f_{m7} #######
VBS_SSWW_FM7_50_BSM_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 50 TeV^{-4} BSM", "VBS_SSWW_FM7_50_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM7_50_BSM_2018.sigma = 0.1191
VBS_SSWW_FM7_50_BSM_2018.year = 2018

VBS_SSWW_FM7_50_INT_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 50 TeV^{-4} INT", "VBS_SSWW_FM7_50_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM7_50_INT_2018.sigma = 0.1191
VBS_SSWW_FM7_50_INT_2018.year = 2018

VBS_SSWW_FM7_50_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 50 TeV^{-4}", "VBS_SSWW_FM7_50_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM7_50_2018.year = 2018
VBS_SSWW_FM7_50_2018.components = [VBS_SSWW_FM7_50_BSM_2018, VBS_SSWW_FM7_50_INT_2018]

VBS_SSWW_FM7_10_BSM_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 10 TeV^{-4} BSM", "VBS_SSWW_FM7_10_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM7_10_BSM_2018.sigma = 0.1191
VBS_SSWW_FM7_10_BSM_2018.year = 2018

VBS_SSWW_FM7_10_INT_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 10 TeV^{-4} INT", "VBS_SSWW_FM7_10_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM7_10_INT_2018.sigma = 0.1191
VBS_SSWW_FM7_10_INT_2018.year = 2018

VBS_SSWW_FM7_10_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 10 TeV^{-4}", "VBS_SSWW_FM7_10_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM7_10_2018.year = 2018
VBS_SSWW_FM7_10_2018.components = [VBS_SSWW_FM7_10_BSM_2018, VBS_SSWW_FM7_10_INT_2018]

VBS_SSWW_FM7_0_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FM7_0_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM7_0_2018.sigma = 0.1191
VBS_SSWW_FM7_0_2018.year = 2018

VBS_SSWW_FM7_50_SM_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 50 TeV^{-4}", "VBS_SSWW_FM7_50_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM7_50_SM_2018.year = 2018
VBS_SSWW_FM7_50_SM_2018.components = [VBS_SSWW_FM7_50_BSM_2018, VBS_SSWW_FM7_50_INT_2018, VBS_SSWW_FM7_0_2018]

VBS_SSWW_FM7_10_SM_2018 = sample(ROOT.kGreen+3, 1, 1001, "f_{m7}/#Lambda^{4} = 10 TeV^{-4}", "VBS_SSWW_FM7_10_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FM7_10_SM_2018.year = 2018
VBS_SSWW_FM7_10_SM_2018.components = [VBS_SSWW_FM7_10_BSM_2018, VBS_SSWW_FM7_10_INT_2018, VBS_SSWW_FM7_0_2018]

###### f_{t0} #######
VBS_SSWW_FT0_2p5_BSM_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 2.5 TeV^{-4} BSM", "VBS_SSWW_FT0_2p5_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT0_2p5_BSM_2018.sigma = 0.1191
VBS_SSWW_FT0_2p5_BSM_2018.year = 2018

VBS_SSWW_FT0_2p5_INT_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 2.5 TeV^{-4} INT", "VBS_SSWW_FT0_2p5_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT0_2p5_INT_2018.sigma = 0.1191
VBS_SSWW_FT0_2p5_INT_2018.year = 2018

VBS_SSWW_FT0_2p5_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 2.5 TeV^{-4}", "VBS_SSWW_FT0_2p5_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT0_2p5_2018.year = 2018
VBS_SSWW_FT0_2p5_2018.components = [VBS_SSWW_FT0_2p5_BSM_2018, VBS_SSWW_FT0_2p5_INT_2018]

VBS_SSWW_FT0_0p5_BSM_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 0.5 TeV^{-4} BSM", "VBS_SSWW_FT0_0p5_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT0_0p5_BSM_2018.sigma = 0.1191
VBS_SSWW_FT0_0p5_BSM_2018.year = 2018

VBS_SSWW_FT0_0p5_INT_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 0.5 TeV^{-4} INT", "VBS_SSWW_FT0_0p5_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT0_0p5_INT_2018.sigma = 0.1191
VBS_SSWW_FT0_0p5_INT_2018.year = 2018

VBS_SSWW_FT0_0p5_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 0.5 TeV^{-4}", "VBS_SSWW_FT0_0p5_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT0_0p5_2018.year = 2018
VBS_SSWW_FT0_0p5_2018.components = [VBS_SSWW_FT0_0p5_BSM_2018, VBS_SSWW_FT0_0p5_INT_2018]

VBS_SSWW_FT0_0_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FT0_0_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT0_0_2018.sigma = 0.1191
VBS_SSWW_FT0_0_2018.year = 2018

VBS_SSWW_FT0_2p5_SM_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 2.5 TeV^{-4}", "VBS_SSWW_FT0_2p5_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT0_2p5_SM_2018.year = 2018
VBS_SSWW_FT0_2p5_SM_2018.components = [VBS_SSWW_FT0_2p5_BSM_2018, VBS_SSWW_FT0_2p5_INT_2018, VBS_SSWW_FT0_0_2018]

VBS_SSWW_FT0_0p5_SM_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t0}/#Lambda^{4} = 0.5 TeV^{-4}", "VBS_SSWW_FT0_0p5_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT0_0p5_SM_2018.year = 2018
VBS_SSWW_FT0_0p5_SM_2018.components = [VBS_SSWW_FT0_0p5_BSM_2018, VBS_SSWW_FT0_0p5_INT_2018, VBS_SSWW_FT0_0_2018]

###### f_{t1} #######
VBS_SSWW_FT1_1_BSM_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 1 TeV^{-4} BSM", "VBS_SSWW_FT1_1_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT1_1_BSM_2018.sigma = 0.1191
VBS_SSWW_FT1_1_BSM_2018.year = 2018

VBS_SSWW_FT1_1_INT_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 1 TeV^{-4} INT", "VBS_SSWW_FT1_1_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT1_1_INT_2018.sigma = 0.1191
VBS_SSWW_FT1_1_INT_2018.year = 2018

VBS_SSWW_FT1_1_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 1 TeV^{-4}", "VBS_SSWW_FT1_1_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT1_1_2018.year = 2018
VBS_SSWW_FT1_1_2018.components = [VBS_SSWW_FT1_1_BSM_2018, VBS_SSWW_FT1_1_INT_2018]

VBS_SSWW_FT1_0p2_BSM_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 0.2 TeV^{-4} BSM", "VBS_SSWW_FT1_0p2_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT1_0p2_BSM_2018.sigma = 0.1191
VBS_SSWW_FT1_0p2_BSM_2018.year = 2018

VBS_SSWW_FT1_0p2_INT_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 0.2 TeV^{-4} INT", "VBS_SSWW_FT1_0p2_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT1_0p2_INT_2018.sigma = 0.1191
VBS_SSWW_FT1_0p2_INT_2018.year = 2018

VBS_SSWW_FT1_0p2_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 0.2 TeV^{-4}", "VBS_SSWW_FT1_0p2_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT1_0p2_2018.year = 2018
VBS_SSWW_FT1_0p2_2018.components = [VBS_SSWW_FT1_0p2_BSM_2018, VBS_SSWW_FT1_0p2_INT_2018]

VBS_SSWW_FT1_0_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FT1_0_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT1_0_2018.sigma = 0.1191
VBS_SSWW_FT1_0_2018.year = 2018

VBS_SSWW_FT1_1_SM_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 1 TeV^{-4}", "VBS_SSWW_FT1_1_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT1_1_SM_2018.year = 2018
VBS_SSWW_FT1_1_SM_2018.components = [VBS_SSWW_FT1_1_BSM_2018, VBS_SSWW_FT1_1_INT_2018, VBS_SSWW_FT1_0_2018]

VBS_SSWW_FT1_0p2_SM_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t1}/#Lambda^{4} = 0.2 TeV^{-4}", "VBS_SSWW_FT1_0p2_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT1_0p2_SM_2018.year = 2018
VBS_SSWW_FT1_0p2_SM_2018.components = [VBS_SSWW_FT1_0p2_BSM_2018, VBS_SSWW_FT1_0p2_INT_2018, VBS_SSWW_FT1_0_2018]

###### f_{t2} #######
VBS_SSWW_FT2_2p5_BSM_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 2.5 TeV^{-4} BSM", "VBS_SSWW_FT2_2p5_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT2_2p5_BSM_2018.sigma = 0.1191
VBS_SSWW_FT2_2p5_BSM_2018.year = 2018

VBS_SSWW_FT2_2p5_INT_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 2.5 TeV^{-4} INT", "VBS_SSWW_FT2_2p5_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT2_2p5_INT_2018.sigma = 0.1191
VBS_SSWW_FT2_2p5_INT_2018.year = 2018

VBS_SSWW_FT2_2p5_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 2.5 TeV^{-4}", "VBS_SSWW_FT2_2p5_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT2_2p5_2018.year = 2018
VBS_SSWW_FT2_2p5_2018.components = [VBS_SSWW_FT2_2p5_BSM_2018, VBS_SSWW_FT2_2p5_INT_2018]

VBS_SSWW_FT2_0p5_BSM_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 0.5 TeV^{-4} BSM", "VBS_SSWW_FT2_0p5_BSM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT2_0p5_BSM_2018.sigma = 0.1191
VBS_SSWW_FT2_0p5_BSM_2018.year = 2018

VBS_SSWW_FT2_0p5_INT_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 0.5 TeV^{-4} INT", "VBS_SSWW_FT2_0p5_INT_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT2_0p5_INT_2018.sigma = 0.1191
VBS_SSWW_FT2_0p5_INT_2018.year = 2018

VBS_SSWW_FT2_0p5_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 0.5 TeV^{-4}", "VBS_SSWW_FT2_0p5_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT2_0p5_2018.year = 2018
VBS_SSWW_FT2_0p5_2018.components = [VBS_SSWW_FT2_0p5_BSM_2018, VBS_SSWW_FT2_0p5_INT_2018]

VBS_SSWW_FT2_0_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 0 TeV^{-4}", "VBS_SSWW_FT2_0_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT2_0_2018.sigma = 0.1191
VBS_SSWW_FT2_0_2018.year = 2018

VBS_SSWW_FT2_2p5_SM_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 2.5 TeV^{-4}", "VBS_SSWW_FT2_2p5_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT2_2p5_SM_2018.year = 2018
VBS_SSWW_FT2_2p5_SM_2018.components = [VBS_SSWW_FT2_2p5_BSM_2018, VBS_SSWW_FT2_2p5_INT_2018, VBS_SSWW_FT2_0_2018]

VBS_SSWW_FT2_0p5_SM_2018 = sample(ROOT.kBlue+3, 1, 1001, "f_{t2}/#Lambda^{4} = 0.5 TeV^{-4}", "VBS_SSWW_FT2_0p5_SM_2018", "VBS_SSWW_aQGC_2018")
VBS_SSWW_FT2_0p5_SM_2018.year = 2018
VBS_SSWW_FT2_0p5_SM_2018.components = [VBS_SSWW_FT2_0p5_BSM_2018, VBS_SSWW_FT2_0p5_INT_2018, VBS_SSWW_FT2_0_2018]

DHiggsToWW_2018 = sample(ROOT.kAzure, 1, 1001, "m_{H} = 200 m_{X} = 150 m_{Z'} = 2e3", "DHiggsToWW_2018")
DHiggsToWW_2018.sigma = 0.0002014
DHiggsToWW_2018.year = 2018
DHiggsToWW_2018.dataset = "/DarkHiggs_MonoHs_HsToWWTo2l2nu_mhs_200_mx_150_mZp_2000_TuneCP5_13TeV-madgraph-pythia8/" + tag_2018 + "-v1/NANOAODSIM"

####################### for likelihood scan ###############################################
sm_2018 = sample(ROOT.kRed+2, 1, 1001, "VBS ssWW SM", "sm_2018")
sm_2018.year = 2018
sm_2018.components = [VBS_SSWW_LL_SM_2018, VBS_SSWW_TL_SM_2018, VBS_SSWW_TT_SM_2018]

sm_lin_quad_cW_2018 = sample(ROOT.kGreen+2, 1, 1001, "VBS ssWW (c_{W} + SM + INT)", "sm_lin_quad_cW_2018")
sm_lin_quad_cW_2018.year = 2018
sm_lin_quad_cW_2018.components = [VBS_SSWW_cW_BSM_2018, VBS_SSWW_cW_INT_2018, VBS_SSWW_LL_SM_2018, VBS_SSWW_TL_SM_2018, VBS_SSWW_TT_SM_2018]

quad_cW_2018 = sample(ROOT.kMagenta+1, 1, 1001, "VBS ssWW c_{W} (BSM+INT)", "quad_cW_2018")
quad_cW_2018.year = 2018
quad_cW_2018.components = [VBS_SSWW_cW_BSM_2018]

sm_lin_quad_cHW_2018 = sample(ROOT.kGreen+2, 1, 1001, "VBS ssWW (c_{W} + SM + INT)", "sm_lin_quad_cHW_2018")
sm_lin_quad_cHW_2018.year = 2018
sm_lin_quad_cHW_2018.components = [VBS_SSWW_cHW_BSM_2018, VBS_SSWW_cHW_INT_2018, VBS_SSWW_LL_SM_2018, VBS_SSWW_TL_SM_2018, VBS_SSWW_TT_SM_2018]

quad_cHW_2018 = sample(ROOT.kMagenta+1, 1, 1001, "VBS ssWW c_{W} (BSM+INT)", "quad_cHW_2018")
quad_cHW_2018.year = 2018
quad_cHW_2018.components = [VBS_SSWW_cHW_BSM_2018]


####################################################### Data #####################################################################################
#tag_data = 'Nano25Oct2019'
tag_data = '02Apr2020'

DataMuB_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuB_2016")
DataMuB_2016.runP = 'B'
DataMuB_2016.year = 2016
DataMuB_2016.dataset = '/SingleMuon/Run2016B-'+tag_data + '_ver2-v1/NANOAOD'
DataMuC_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuC_2016")
DataMuC_2016.runP = 'C'
DataMuC_2016.year = 2016
DataMuC_2016.dataset = '/SingleMuon/Run2016C-'+tag_data + '-v1/NANOAOD'
DataMuD_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuD_2016")
DataMuD_2016.runP = 'D'
DataMuD_2016.year = 2016
DataMuD_2016.dataset = '/SingleMuon/Run2016D-'+tag_data + '-v1/NANOAOD'
DataMuE_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuE_2016")
DataMuE_2016.runP = 'E'
DataMuE_2016.year = 2016
DataMuE_2016.dataset = '/SingleMuon/Run2016E-'+tag_data + '-v1/NANOAOD'
DataMuF_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuF_2016")
DataMuF_2016.runP = 'F'
DataMuF_2016.year = 2016
DataMuF_2016.dataset = '/SingleMuon/Run2016F-'+tag_data + '-v1/NANOAOD'
DataMuG_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuG_2016")
DataMuG_2016.runP = 'G'
DataMuG_2016.year = 2016
DataMuG_2016.dataset = '/SingleMuon/Run2016G-'+tag_data + '-v1/NANOAOD'
DataMuH_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuH_2016")
DataMuH_2016.runP = 'H'
DataMuH_2016.year = 2016
DataMuH_2016.dataset = '/SingleMuon/Run2016H-'+tag_data + '-v1/NANOAOD'
DataMu_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_2016")
DataMu_2016.year = 2016
DataMu_2016.components = [DataMuB_2016, DataMuC_2016, DataMuD_2016, DataMuE_2016, DataMuF_2016, DataMuG_2016, DataMuH_2016]

DataEleB_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleB_2016")
DataEleB_2016.runP = 'B'
DataEleB_2016.year = 2016
DataEleB_2016.dataset = '/SingleElectron/Run2016B-'+tag_data + '_ver2-v1/NANOAOD'
DataEleC_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleC_2016")
DataEleC_2016.runP = 'C'
DataEleC_2016.year = 2016
DataEleC_2016.dataset = '/SingleElectron/Run2016C-'+tag_data + '-v1/NANOAOD'
DataEleD_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleD_2016")
DataEleD_2016.runP = 'D'
DataEleD_2016.year = 2016
DataEleD_2016.dataset = '/SingleElectron/Run2016D-'+tag_data + '-v1/NANOAOD'
DataEleE_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleE_2016")
DataEleE_2016.runP = 'E'
DataEleE_2016.year = 2016
DataEleE_2016.dataset = '/SingleElectron/Run2016E-'+tag_data + '-v1/NANOAOD'
DataEleF_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleF_2016")
DataEleF_2016.runP = 'F'
DataEleF_2016.year = 2016
DataEleF_2016.dataset = '/SingleElectron/Run2016F-'+tag_data + '-v1/NANOAOD'
DataEleG_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleG_2016")
DataEleG_2016.runP = 'G'
DataEleG_2016.year = 2016
DataEleG_2016.dataset = '/SingleElectron/Run2016G-'+tag_data + '-v1/NANOAOD'
DataEleH_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleH_2016")
DataEleH_2016.runP = 'H'
DataEleH_2016.year = 2016
DataEleH_2016.dataset = '/SingleElectron/Run2016H-'+tag_data + '-v1/NANOAOD'
DataEle_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_2016")
DataEle_2016.year = 2016
DataEle_2016.components = [DataEleB_2016, DataEleC_2016, DataEleD_2016, DataEleE_2016, DataEleF_2016, DataEleG_2016, DataEleH_2016]

DataHTB_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTB_2016")
DataHTB_2016.runP = 'B'
DataHTB_2016.year = 2016
DataHTB_2016.dataset = '/JetHT/Run2016B-'+tag_data + '_ver2-v1/NANOAOD'
DataHTC_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTC_2016")
DataHTC_2016.runP = 'C'
DataHTC_2016.year = 2016
DataHTC_2016.dataset = '/JetHT/Run2016C-'+tag_data + '-v1/NANOAOD'
DataHTD_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTD_2016")
DataHTD_2016.runP = 'D'
DataHTD_2016.year = 2016
DataHTD_2016.dataset = '/JetHT/Run2016D-'+tag_data + '-v1/NANOAOD'
DataHTE_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTE_2016")
DataHTE_2016.runP = 'E'
DataHTE_2016.year = 2016
DataHTE_2016.dataset = '/JetHT/Run2016E-'+tag_data + '-v1/NANOAOD'
DataHTF_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTF_2016")
DataHTF_2016.runP = 'F'
DataHTF_2016.year = 2016
DataHTF_2016.dataset = '/JetHT/Run2016F-'+tag_data + '-v1/NANOAOD'
DataHTG_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTG_2016")
DataHTG_2016.runP = 'G'
DataHTG_2016.year = 2016
DataHTG_2016.dataset = '/JetHT/Run2016G-'+tag_data + '-v1/NANOAOD'
DataHTH_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTH_2016")
DataHTH_2016.runP = 'H'
DataHTH_2016.year = 2016
DataHTH_2016.dataset = '/JetHT/Run2016H-'+tag_data + '-v1/NANOAOD'
DataHT_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_2016")
DataHT_2016.year = 2016
DataHT_2016.components = [DataHTB_2016, DataHTC_2016, DataHTD_2016, DataHTE_2016, DataHTF_2016, DataHTG_2016, DataHTH_2016]

DataTauB_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataTauB_2017")
DataTauB_2017.runP = 'B'
DataTauB_2017.year = 2017
DataTauB_2017.dataset = '/Tau/Run2017B-'+tag_data + '-v1/NANOAOD'
DataTauC_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataTauC_2017")
DataTauC_2017.runP = 'C'
DataTauC_2017.year = 2017
DataTauC_2017.dataset = '/Tau/Run2017C-'+tag_data + '-v1/NANOAOD'
DataTauD_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataTauD_2017")
DataTauD_2017.runP = 'D'
DataTauD_2017.year = 2017
DataTauD_2017.dataset = '/Tau/Run2017D-'+tag_data + '-v1/NANOAOD'
DataTauE_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataTauE_2017")
DataTauE_2017.runP = 'E'
DataTauE_2017.year = 2017
DataTauE_2017.dataset = '/Tau/Run2017E-'+tag_data + '-v1/NANOAOD'
DataTauF_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataTauF_2017")
DataTauF_2017.runP = 'F'
DataTauF_2017.year = 2017
DataTauF_2017.dataset = '/Tau/Run2017F-'+tag_data + '-v1/NANOAOD'
DataTau_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataTau_2017")
DataTau_2017.year = 2017
DataTau_2017.components = [DataTauB_2017, DataTauC_2017, DataTauD_2017, DataTauE_2017, DataTauF_2017]
DataTauFake_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataTauFake_2017")
DataTauFake_2017.year = 2017
DataTauFake_2017.components = [DataTauB_2017, DataTauC_2017, DataTauD_2017, DataTauE_2017, DataTauF_2017]

DataMuB_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuB_2017")
DataMuB_2017.runP = 'B'
DataMuB_2017.year = 2017
DataMuB_2017.dataset = '/SingleMuon/Run2017B-'+tag_data + '-v1/NANOAOD'
DataMuC_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuC_2017")
DataMuC_2017.runP = 'C'
DataMuC_2017.year = 2017
DataMuC_2017.dataset = '/SingleMuon/Run2017C-'+tag_data + '-v1/NANOAOD'
DataMuD_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuD_2017")
DataMuD_2017.runP = 'D'
DataMuD_2017.year = 2017
DataMuD_2017.dataset = '/SingleMuon/Run2017D-'+tag_data + '-v1/NANOAOD'
DataMuE_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuE_2017")
DataMuE_2017.runP = 'E'
DataMuE_2017.year = 2017
DataMuE_2017.dataset = '/SingleMuon/Run2017E-'+tag_data + '-v1/NANOAOD'
DataMuF_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuF_2017")
DataMuF_2017.runP = 'F'
DataMuF_2017.year = 2017
DataMuF_2017.dataset = '/SingleMuon/Run2017F-'+tag_data + '-v1/NANOAOD'
DataMu_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_2017")
DataMu_2017.year = 2017
DataMu_2017.components = [DataMuB_2017, DataMuC_2017, DataMuD_2017, DataMuE_2017, DataMuF_2017]
DataMuFake_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuFake_2017")
DataMuFake_2017.year = 2017
DataMuFake_2017.components = [DataMuC_2017, DataMuD_2017, DataMuE_2017, DataMuF_2017]

DataEleB_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleB_2017")
DataEleB_2017.runP = 'B'
DataEleB_2017.year = 2017
DataEleB_2017.dataset = '/SingleElectron/Run2017B-'+tag_data + '-v1/NANOAOD'
DataEleC_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleC_2017")
DataEleC_2017.runP = 'C'
DataEleC_2017.year = 2017
DataEleC_2017.dataset = '/SingleElectron/Run2017C-'+tag_data + '-v1/NANOAOD'
DataEleD_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleD_2017")
DataEleD_2017.runP = 'D'
DataEleD_2017.year = 2017
DataEleD_2017.dataset = '/SingleElectron/Run2017D-'+tag_data + '-v1/NANOAOD'
DataEleE_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleE_2017")
DataEleE_2017.runP = 'E'
DataEleE_2017.year = 2017
DataEleE_2017.dataset = '/SingleElectron/Run2017E-'+tag_data + '-v1/NANOAOD'
DataEleF_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleF_2017")
DataEleF_2017.runP = 'F'
DataEleF_2017.year = 2017
DataEleF_2017.dataset = '/SingleElectron/Run2017F-'+tag_data + '-v1/NANOAOD'
DataEle_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_2017")
DataEle_2017.year = 2017
DataEle_2017.components = [DataEleB_2017, DataEleC_2017, DataEleD_2017, DataEleE_2017, DataEleF_2017]

DataEleMu_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleMu_2017")
DataEleMu_2017.year = 2017
DataEleMu_2017.components = [DataEleB_2017, DataEleC_2017, DataEleD_2017, DataEleE_2017, DataEleF_2017, DataMuB_2017, DataMuC_2017, DataMuD_2017, DataMuE_2017, DataMuF_2017]

DataEleFake_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleFake_2017")
DataEleFake_2017.year = 2017
DataEleFake_2017.components = [DataEleC_2017, DataEleD_2017, DataEleE_2017, DataEleF_2017]


SampleEleFake_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleFake_2017")
SampleEleFake_2017.year = 2017
SampleEleFake_2017.components = [DataEleC_2017, DataEleD_2017, DataEleE_2017, DataEleF_2017, WJetsHT70to100_2017, WJetsHT100to200_2017, WJetsHT200to400_2017, WJetsHT400to600_2017, WJetsHT600to800_2017, WJetsHT800to1200_2017, WJetsHT1200to2500_2017, WJetsHT2500toInf_2017, DY1JetsToLL_2017, DY2JetsToLL_2017, DY3JetsToLL_2017, DY4JetsToLL_2017, DYJetsToLLM5to50_2017]
SampleMuFake_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleFake_2017")
SampleMuFake_2017.year = 2017
SampleMuFake_2017.components = [DataMuC_2017, DataMuD_2017, DataMuE_2017, DataMuF_2017, WJetsHT70to100_2017, WJetsHT100to200_2017, WJetsHT200to400_2017, WJetsHT400to600_2017, WJetsHT600to800_2017, WJetsHT800to1200_2017, WJetsHT1200to2500_2017, WJetsHT2500toInf_2017, DY1JetsToLL_2017, DY2JetsToLL_2017, DY3JetsToLL_2017, DY4JetsToLL_2017, DYJetsToLLM5to50_2017]


MCFake_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "MCFake_2017")
MCFake_2017.year = 2017
MCFake_2017.components = [WJetsHT70to100_2017, WJetsHT100to200_2017, WJetsHT200to400_2017, WJetsHT400to600_2017, WJetsHT600to800_2017, WJetsHT800to1200_2017, WJetsHT1200to2500_2017, WJetsHT2500toInf_2017, DY1JetsToLL_2017, DY2JetsToLL_2017, DY3JetsToLL_2017, DY4JetsToLL_2017, DYJetsToLLM5to50_2017]

DataHTB_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTB_2017")
DataHTB_2017.runP = 'B'
DataHTB_2017.year = 2017
DataHTB_2017.dataset = '/JetHT/Run2017B-'+tag_data + '-v1/NANOAOD'
DataHTC_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTC_2017")
DataHTC_2017.runP = 'C'
DataHTC_2017.year = 2017
DataHTC_2017.dataset = '/JetHT/Run2017C-'+tag_data + '-v1/NANOAOD'
DataHTD_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTD_2017")
DataHTD_2017.runP = 'D'
DataHTD_2017.year = 2017
DataHTD_2017.dataset = '/JetHT/Run2017D-'+tag_data + '-v1/NANOAOD'
DataHTE_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTE_2017")
DataHTE_2017.runP = 'E'
DataHTE_2017.year = 2017
DataHTE_2017.dataset = '/JetHT/Run2017E-'+tag_data + '-v1/NANOAOD'
DataHTF_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTF_2017")
DataHTF_2017.runP = 'F'
DataHTF_2017.year = 2017
DataHTF_2017.dataset = '/JetHT/Run2017F-'+tag_data + '-v1/NANOAOD'
DataHT_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_2017")
DataHT_2017.year = 2017
DataHT_2017.components = [DataHTB_2017, DataHTC_2017, DataHTD_2017, DataHTE_2017, DataHTF_2017]

DataHTnoB_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_2017")
DataHTnoB_2017.year = 2017
DataHTnoB_2017.components = [DataHTC_2017, DataHTD_2017, DataHTE_2017, DataHTF_2017]

SampleHTFake_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "SampleHTFake_2017")
SampleHTFake_2017.year = 2017
SampleHTFake_2017.components = [DataHTB_2017, DataHTC_2017, DataHTD_2017, DataHTE_2017, DataHTF_2017, WJetsHT70to100_2017, WJetsHT100to200_2017, WJetsHT200to400_2017, WJetsHT400to600_2017, WJetsHT600to800_2017, WJetsHT800to1200_2017, WJetsHT1200to2500_2017, WJetsHT2500toInf_2017, DY1JetsToLL_2017, DY2JetsToLL_2017, DY3JetsToLL_2017, DY4JetsToLL_2017, DYJetsToLLM5to50_2017, ZZTo2L2Nu_2017, ZZJJTo4L_EWK_2017, ZZJJTo4L_QCD_2017, GluGluToContinToZZTo2e2nu_2017, GluGluToContinToZZTo2e2mu_2017, GluGluToContinToZZTo2e2tau_2017, GluGluToContinToZZTo2mu2nu_2017, GluGluToContinToZZTo2mu2tau_2017, GluGluToContinToZZTo4e_2017, GluGluToContinToZZTo4mu_2017, GluGluToContinToZZTo4tau_2017]

SampleHTFakepart_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "SampleHTFake_2017")
SampleHTFakepart_2017.year = 2017
SampleHTFakepart_2017.components = [ WJetsHT70to100_2017, WJetsHT100to200_2017, WJetsHT200to400_2017, WJetsHT400to600_2017, WJetsHT600to800_2017, WJetsHT800to1200_2017, WJetsHT1200to2500_2017, WJetsHT2500toInf_2017, DY1JetsToLL_2017, DY2JetsToLL_2017, DY3JetsToLL_2017, DY4JetsToLL_2017, DYJetsToLLM5to50_2017, ZZTo2L2Nu_2017, ZZJJTo4L_EWK_2017, ZZJJTo4L_QCD_2017, GluGluToContinToZZTo2e2nu_2017, GluGluToContinToZZTo2e2mu_2017, GluGluToContinToZZTo2e2tau_2017, GluGluToContinToZZTo2mu2nu_2017, GluGluToContinToZZTo2mu2tau_2017, GluGluToContinToZZTo4e_2017, GluGluToContinToZZTo4mu_2017, GluGluToContinToZZTo4tau_2017]

FakeElePromptTau_2017 = sample(ROOT.kGray+1, 1, 1001, "Fake e Prompt #tau", "FakeElePromptTau_2017")
FakeElePromptTau_2017.year = 2017
FakeElePromptTau_2017.components = [DataEle_2017, DataHT_2017, WJets_2017, DYJetsToLL_2017]

PromptEleFakeTau_2017 = sample(ROOT.kGray+2, 1, 1001, "Prompt e Fake #tau", "PromptEleFakeTau_2017")
PromptEleFakeTau_2017.year = 2017
PromptEleFakeTau_2017.components = [DataEle_2017, DataHT_2017, WJets_2017, DYJetsToLL_2017]

FakeEleFakeTau_2017 = sample(ROOT.kGray+3, 1, 1001, "Fake e Fake #tau", "FakeEleFakeTau_2017")
FakeEleFakeTau_2017.year = 2017
FakeEleFakeTau_2017.components = [DataEle_2017, DataHT_2017, WJets_2017, DYJetsToLL_2017]

FakeEle_2017 = sample(ROOT.kGray, 1, 1001, "Fake Leptons", "FakeEle_2017")
FakeEle_2017.year = 2017
FakeEle_2017.components = [DataEle_2017, DataHT_2017, WJets_2017, DYJetsToLL_2017]

FakeMuPromptTau_2017 = sample(ROOT.kGray+1, 1, 1001, "Fake #mu Prompt #tau", "FakeMuPromptTau_2017")
FakeMuPromptTau_2017.year = 2017
FakeMuPromptTau_2017.components = [DataMu_2017, DataHT_2017, WJets_2017, DYJetsToLL_2017]

PromptMuFakeTau_2017 = sample(ROOT.kGray+2, 1, 1001, "Prompt #mu Fake #tau", "PromptMuFakeTau_2017")
PromptMuFakeTau_2017.year = 2017
PromptMuFakeTau_2017.components = [DataMu_2017, DataHT_2017, WJets_2017, DYJetsToLL_2017]

FakeMuFakeTau_2017 = sample(ROOT.kGray+3, 1, 1001, "Fake #mu Fake #tau", "FakeMuFakeTau_2017")
FakeMuFakeTau_2017.year = 2017
FakeMuFakeTau_2017.components = [DataMu_2017, DataHT_2017, WJets_2017, DYJetsToLL_2017]

FakeMu_2017 = sample(ROOT.kGray, 1, 1001, "Fake Leptons", "FakeMu_2017")
FakeMu_2017.year = 2017
FakeMu_2017.components = [DataMu_2017, DataHT_2017, WJets_2017, DYJetsToLL_2017]

FakeEleMu_2017 = sample(ROOT.kGray, 1, 1001, "Fake Leptons", "FakeEleMu_2017")
FakeEleMu_2017.year = 2017
FakeEleMu_2017.components = [DataEleMu_2017]

DataMETB_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETB_2017")
DataMETB_2017.runP = 'B'
DataMETB_2017.year = 2017
DataMETB_2017.dataset = '/MET/Run2017B-'+tag_data + '-v1/NANOAOD'
DataMETC_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETC_2017")
DataMETC_2017.runP = 'C'
DataMETC_2017.year = 2017
DataMETC_2017.dataset = '/MET/Run2017C-'+tag_data + '-v1/NANOAOD'
DataMETD_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETD_2017")
DataMETD_2017.runP = 'D'
DataMETD_2017.year = 2017
DataMETD_2017.dataset = '/MET/Run2017D-'+tag_data + '-v1/NANOAOD'
DataMETE_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETE_2017")
DataMETE_2017.runP = 'E'
DataMETE_2017.year = 2017
DataMETE_2017.dataset = '/MET/Run2017E-'+tag_data + '-v1/NANOAOD'
DataMETF_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETF_2017")
DataMETF_2017.runP = 'F'
DataMETF_2017.year = 2017
DataMETF_2017.dataset = '/MET/Run2017F-'+tag_data + '-v1/NANOAOD'
DataMET_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMET_2017")
DataMET_2017.year = 2017
DataMET_2017.components = [DataMETB_2017, DataMETC_2017, DataMETD_2017, DataMETE_2017, DataMETF_2017]

DataMuA_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuA_2018")
DataMuA_2018.runP = 'A'
DataMuA_2018.year = 2018
DataMuA_2018.dataset = '/SingleMuon/Run2018A-'+tag_data + '-v1/NANOAOD'
DataMuB_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuB_2018")
DataMuB_2018.runP = 'B'
DataMuB_2018.year = 2018
DataMuB_2018.dataset = '/SingleMuon/Run2018B-'+tag_data + '-v1/NANOAOD'
DataMuC_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuC_2018")
DataMuC_2018.runP = 'C'
DataMuC_2018.year = 2018
DataMuC_2018.dataset = '/SingleMuon/Run2018C-'+tag_data + '-v1/NANOAOD'
DataMuD_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuD_2018")
DataMuD_2018.runP = 'D'
DataMuD_2018.year = 2018
DataMuD_2018.dataset = '/SingleMuon/Run2018D-'+tag_data + '-v1/NANOAOD'
DataMu_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_2018")
DataMu_2018.year = 2018
DataMu_2018.components = [DataMuA_2018, DataMuB_2018, DataMuC_2018, DataMuD_2018]

DataEleA_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleA_2018")
DataEleA_2018.runP = 'A'
DataEleA_2018.year = 2018
DataEleA_2018.dataset = '/EGamma/Run2018A-'+tag_data + '-v1/NANOAOD'
DataEleB_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleB_2018")
DataEleB_2018.runP = 'B'
DataEleB_2018.year = 2018
DataEleB_2018.dataset = '/EGamma/Run2018B-'+tag_data + '-v1/NANOAOD'
DataEleC_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleC_2018")
DataEleC_2018.runP = 'C'
DataEleC_2018.year = 2018
DataEleC_2018.dataset = '/EGamma/Run2018C-'+tag_data + '-v1/NANOAOD'
DataEleD_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleD_2018")
DataEleD_2018.runP = 'D'
DataEleD_2018.year = 2018
DataEleD_2018.dataset = '/EGamma/Run2018D-'+tag_data + '-v1/NANOAOD'
DataEle_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_2018")
DataEle_2018.year = 2018
DataEle_2018.components = [DataEleA_2018, DataEleB_2018, DataEleC_2018, DataEleD_2018]

DataHTA_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTA_2018")
DataHTA_2018.runP = 'A'
DataHTA_2018.year = 2018
DataHTA_2018.dataset = '/JetHT/Run2018A-'+tag_data + '-v1/NANOAOD'
DataHTB_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTB_2018")
DataHTB_2018.runP = 'B'
DataHTB_2018.year = 2018
DataHTB_2018.dataset = '/JetHT/Run2018B-'+tag_data + '-v1/NANOAOD'
DataHTC_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTC_2018")
DataHTC_2018.runP = 'C'
DataHTC_2018.year = 2018
DataHTC_2018.dataset = '/JetHT/Run2018C-'+tag_data + '-v1/NANOAOD'
DataHTD_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTD_2018")
DataHTD_2018.runP = 'D'
DataHTD_2018.year = 2018
DataHTD_2018.dataset = '/JetHT/Run2018D-'+tag_data + '-v1/NANOAOD'
DataHT_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_2018")
DataHT_2018.year = 2018
DataHT_2018.components = [DataHTA_2018, DataHTB_2018, DataHTC_2018, DataHTD_2018]



SampleHTFake_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "SampleHTFake_2018")
SampleHTFake_2018.year = 2017
SampleHTFake_2018.components = [DataHTB_2018, DataHTC_2018, DataHTD_2018, WJetsHT70to100_2018, WJetsHT100to200_2018, WJetsHT200to400_2018, WJetsHT400to600_2018, WJetsHT600to800_2018, WJetsHT800to1200_2018, WJetsHT1200to2500_2018, WJetsHT2500toInf_2018, DY1JetsToLL_2018, DY2JetsToLL_2018, DY3JetsToLL_2018, DY4JetsToLL_2018, ZZTo2L2Nu_2018, ZZJJTo4L_EWK_2018, ZZJJTo4L_QCD_2018, GluGluToContinToZZTo2e2nu_2018, GluGluToContinToZZTo2e2mu_2018, GluGluToContinToZZTo2e2tau_2018, GluGluToContinToZZTo2mu2nu_2018, GluGluToContinToZZTo2mu2tau_2018, GluGluToContinToZZTo4e_2018, GluGluToContinToZZTo4mu_2018, GluGluToContinToZZTo4tau_2018]


FakeElePromptTau_2018 = sample(ROOT.kGray+1, 1, 1001, "Fake e Prompt #tau", "FakeElePromptTau_2018")
FakeElePromptTau_2018.year = 2018
FakeElePromptTau_2018.components = [DataEle_2018, DataHT_2018, WJets_2018, DYJetsToLL_2018]

PromptEleFakeTau_2018 = sample(ROOT.kGray+2, 1, 1001, "Prompt e Fake #tau", "PromptEleFakeTau_2018")
PromptEleFakeTau_2018.year = 2018
PromptEleFakeTau_2018.components = [DataEle_2018, DataHT_2018, WJets_2018, DYJetsToLL_2018]

FakeEleFakeTau_2018 = sample(ROOT.kGray+3, 1, 1001, "Fake e Fake #tau", "FakeEleFakeTau_2018")
FakeEleFakeTau_2018.year = 2018
FakeEleFakeTau_2018.components = [DataEle_2018, DataHT_2018, WJets_2018, DYJetsToLL_2018]

FakeEle_2018 = sample(ROOT.kGray, 1, 1001, "Fake Leptons", "FakeEle_2018")
FakeEle_2018.year = 2018
FakeEle_2018.components = [DataEle_2018, DataHT_2018, WJets_2018, DYJetsToLL_2018]

FakeMuPromptTau_2018 = sample(ROOT.kGray+1, 1, 1001, "Fake #mu Prompt #tau", "FakeMuPromptTau_2018")
FakeMuPromptTau_2018.year = 2018
FakeMuPromptTau_2018.components = [DataMu_2018, DataHT_2018, WJets_2018, DYJetsToLL_2018]

PromptMuFakeTau_2018 = sample(ROOT.kGray+2, 1, 1001, "Prompt #mu Fake #tau", "PromptMuFakeTau_2018")
PromptMuFakeTau_2018.year = 2018
PromptMuFakeTau_2018.components = [DataMu_2018, DataHT_2018, WJets_2018, DYJetsToLL_2018]

FakeMuFakeTau_2018 = sample(ROOT.kGray+3, 1, 1001, "Fake #mu Fake #tau", "FakeMuFakeTau_2018")
FakeMuFakeTau_2018.year = 2018
FakeMuFakeTau_2018.components = [DataMu_2018, DataHT_2018, WJets_2018, DYJetsToLL_2018]

FakeMu_2018 = sample(ROOT.kGray, 1, 1001, "Fake Leptons", "FakeMu_2018")
FakeMu_2018.year = 2018
FakeMu_2018.components = [DataMu_2018, DataHT_2018, WJets_2018, DYJetsToLL_2018]


sample_dict={
    ##### 2017 #####
    'WpWpJJ_EWK_2017':WpWpJJ_EWK_2017,
    'WpWpJJ_QCD_2017':WpWpJJ_QCD_2017,
    'VBS_SSWW_SM_2017':VBS_SSWW_SM_2017, 'VBS_SSWW_LL_SM_2017':VBS_SSWW_LL_SM_2017, 'VBS_SSWW_TL_SM_2017':VBS_SSWW_TL_SM_2017, 'VBS_SSWW_TT_SM_2017':VBS_SSWW_TT_SM_2017,
    'VBS_SSWW_cHW_2017':VBS_SSWW_cHW_2017, 'VBS_SSWW_cHW_BSM_2017':VBS_SSWW_cHW_BSM_2017, 'VBS_SSWW_cHW_INT_2017':VBS_SSWW_cHW_INT_2017,
    'VBS_SSWW_cW_2017':VBS_SSWW_cW_2017, 'VBS_SSWW_cW_BSM_2017':VBS_SSWW_cW_BSM_2017, 'VBS_SSWW_cW_INT_2017':VBS_SSWW_cW_INT_2017,
    'VBS_SSWW_cW_cHW_2017':VBS_SSWW_cW_cHW_2017,
    'VBS_SSWW_DIM6_2017':VBS_SSWW_DIM6_2017,
    'VBS_SSWW_DIM6_SM_2017':VBS_SSWW_DIM6_SM_2017,
    'VBS_SSWW_cHW_SM_2017':VBS_SSWW_cHW_SM_2017,
    'VBS_SSWW_cW_SM_2017':VBS_SSWW_cW_SM_2017,
    'VBS_SSWW_aQGC_2017':VBS_SSWW_aQGC_2017,
    'VBS_SSWW_FS0_25_BSM_2017':VBS_SSWW_FS0_25_BSM_2017,
    'VBS_SSWW_FS0_25_INT_2017':VBS_SSWW_FS0_25_INT_2017,
    'VBS_SSWW_FS0_25_SM_2017':VBS_SSWW_FS0_25_SM_2017,
    'VBS_SSWW_FS0_25_2017':VBS_SSWW_FS0_25_2017,
    'VBS_SSWW_FS0_5_BSM_2017':VBS_SSWW_FS0_5_BSM_2017,
    'VBS_SSWW_FS0_5_INT_2017':VBS_SSWW_FS0_5_INT_2017,
    'VBS_SSWW_FS0_5_SM_2017':VBS_SSWW_FS0_5_SM_2017,
    'VBS_SSWW_FS0_5_2017':VBS_SSWW_FS0_5_2017,
    'VBS_SSWW_FS0_0_2017':VBS_SSWW_FS0_0_2017,
    'VBS_SSWW_FS1_50_BSM_2017':VBS_SSWW_FS1_50_BSM_2017,
    'VBS_SSWW_FS1_50_INT_2017':VBS_SSWW_FS1_50_INT_2017,
    'VBS_SSWW_FS1_50_SM_2017':VBS_SSWW_FS1_50_SM_2017,
    'VBS_SSWW_FS1_50_2017':VBS_SSWW_FS1_50_2017,
    'VBS_SSWW_FS1_10_BSM_2017':VBS_SSWW_FS1_10_BSM_2017,
    'VBS_SSWW_FS1_10_INT_2017':VBS_SSWW_FS1_10_INT_2017,
    'VBS_SSWW_FS1_10_SM_2017':VBS_SSWW_FS1_10_SM_2017,
    'VBS_SSWW_FS1_10_2017':VBS_SSWW_FS1_10_2017,
    'VBS_SSWW_FS1_0_2017':VBS_SSWW_FS1_0_2017,
    'VBS_SSWW_FM0_25_BSM_2017':VBS_SSWW_FM0_25_BSM_2017,
    'VBS_SSWW_FM0_25_INT_2017':VBS_SSWW_FM0_25_INT_2017,
    'VBS_SSWW_FM0_25_SM_2017':VBS_SSWW_FM0_25_SM_2017,
    'VBS_SSWW_FM0_25_2017':VBS_SSWW_FM0_25_2017,
    'VBS_SSWW_FM0_5_BSM_2017':VBS_SSWW_FM0_5_BSM_2017,
    'VBS_SSWW_FM0_5_INT_2017':VBS_SSWW_FM0_5_INT_2017,
    'VBS_SSWW_FM0_5_SM_2017':VBS_SSWW_FM0_5_SM_2017,
    'VBS_SSWW_FM0_5_2017':VBS_SSWW_FM0_5_2017,
    'VBS_SSWW_FM0_0_2017':VBS_SSWW_FM0_0_2017,
    'VBS_SSWW_FM1_25_BSM_2017':VBS_SSWW_FM1_25_BSM_2017,
    'VBS_SSWW_FM1_25_INT_2017':VBS_SSWW_FM1_25_INT_2017,
    'VBS_SSWW_FM1_25_SM_2017':VBS_SSWW_FM1_25_SM_2017,
    'VBS_SSWW_FM1_25_2017':VBS_SSWW_FM1_25_2017,
    'VBS_SSWW_FM1_5_BSM_2017':VBS_SSWW_FM1_5_BSM_2017,
    'VBS_SSWW_FM1_5_INT_2017':VBS_SSWW_FM1_5_INT_2017,
    'VBS_SSWW_FM1_5_SM_2017':VBS_SSWW_FM1_5_SM_2017,
    'VBS_SSWW_FM1_5_2017':VBS_SSWW_FM1_5_2017,
    'VBS_SSWW_FM1_0_2017':VBS_SSWW_FM1_0_2017,
    'VBS_SSWW_FM6_25_BSM_2017':VBS_SSWW_FM6_25_BSM_2017,
    'VBS_SSWW_FM6_25_INT_2017':VBS_SSWW_FM6_25_INT_2017,
    'VBS_SSWW_FM6_25_SM_2017':VBS_SSWW_FM6_25_SM_2017,
    'VBS_SSWW_FM6_25_2017':VBS_SSWW_FM6_25_2017,
    'VBS_SSWW_FM6_5_BSM_2017':VBS_SSWW_FM6_5_BSM_2017,
    'VBS_SSWW_FM6_5_INT_2017':VBS_SSWW_FM6_5_INT_2017,
    'VBS_SSWW_FM6_5_SM_2017':VBS_SSWW_FM6_5_SM_2017,
    'VBS_SSWW_FM6_5_2017':VBS_SSWW_FM6_5_2017,
    'VBS_SSWW_FM6_0_2017':VBS_SSWW_FM6_0_2017,
    'VBS_SSWW_FM7_50_BSM_2017':VBS_SSWW_FM7_50_BSM_2017,
    'VBS_SSWW_FM7_50_INT_2017':VBS_SSWW_FM7_50_INT_2017,
    'VBS_SSWW_FM7_50_SM_2017':VBS_SSWW_FM7_50_SM_2017,
    'VBS_SSWW_FM7_50_2017':VBS_SSWW_FM7_50_2017,
    'VBS_SSWW_FM7_10_BSM_2017':VBS_SSWW_FM7_10_BSM_2017,
    'VBS_SSWW_FM7_10_INT_2017':VBS_SSWW_FM7_10_INT_2017,
    'VBS_SSWW_FM7_10_SM_2017':VBS_SSWW_FM7_10_SM_2017,
    'VBS_SSWW_FM7_10_2017':VBS_SSWW_FM7_10_2017,
    'VBS_SSWW_FM7_0_2017':VBS_SSWW_FM7_0_2017,
    'VBS_SSWW_FT0_2p5_BSM_2017':VBS_SSWW_FT0_2p5_BSM_2017,
    'VBS_SSWW_FT0_2p5_INT_2017':VBS_SSWW_FT0_2p5_INT_2017,
    'VBS_SSWW_FT0_2p5_SM_2017':VBS_SSWW_FT0_2p5_SM_2017,
    'VBS_SSWW_FT0_2p5_2017':VBS_SSWW_FT0_2p5_2017,
    'VBS_SSWW_FT0_0p5_BSM_2017':VBS_SSWW_FT0_0p5_BSM_2017,
    'VBS_SSWW_FT0_0p5_INT_2017':VBS_SSWW_FT0_0p5_INT_2017,
    'VBS_SSWW_FT0_0p5_SM_2017':VBS_SSWW_FT0_0p5_SM_2017,
    'VBS_SSWW_FT0_0p5_2017':VBS_SSWW_FT0_0p5_2017,
    'VBS_SSWW_FT0_0_2017':VBS_SSWW_FT0_0_2017,
    'VBS_SSWW_FT1_1_BSM_2017':VBS_SSWW_FT1_1_BSM_2017,
    'VBS_SSWW_FT1_1_INT_2017':VBS_SSWW_FT1_1_INT_2017,
    'VBS_SSWW_FT1_1_SM_2017':VBS_SSWW_FT1_1_SM_2017,
    'VBS_SSWW_FT1_1_2017':VBS_SSWW_FT1_1_2017,
    'VBS_SSWW_FT1_0p2_BSM_2017':VBS_SSWW_FT1_0p2_BSM_2017,
    'VBS_SSWW_FT1_0p2_INT_2017':VBS_SSWW_FT1_0p2_INT_2017,
    'VBS_SSWW_FT1_0p2_SM_2017':VBS_SSWW_FT1_0p2_SM_2017,
    'VBS_SSWW_FT1_0p2_2017':VBS_SSWW_FT1_0p2_2017,
    'VBS_SSWW_FT1_0_2017':VBS_SSWW_FT1_0_2017,
    'VBS_SSWW_FT2_2p5_BSM_2017':VBS_SSWW_FT2_2p5_BSM_2017,
    'VBS_SSWW_FT2_2p5_INT_2017':VBS_SSWW_FT2_2p5_INT_2017,
    'VBS_SSWW_FT2_2p5_SM_2017':VBS_SSWW_FT2_2p5_SM_2017,
    'VBS_SSWW_FT2_2p5_2017':VBS_SSWW_FT2_2p5_2017,
    'VBS_SSWW_FT2_0p5_BSM_2017':VBS_SSWW_FT2_0p5_BSM_2017,
    'VBS_SSWW_FT2_0p5_INT_2017':VBS_SSWW_FT2_0p5_INT_2017,
    'VBS_SSWW_FT2_0p5_SM_2017':VBS_SSWW_FT2_0p5_SM_2017,
    'VBS_SSWW_FT2_0p5_2017':VBS_SSWW_FT2_0p5_2017,
    'VBS_SSWW_FT2_0p5_2017':VBS_SSWW_FT2_0p5_2017,
    'VBS_SSWW_FT2_0_2017':VBS_SSWW_FT2_0_2017,
    'DHiggsToWW_2017':DHiggsToWW_2017,
    'sm_2017':sm_2017,
    'sm_lin_quad_cW_2017':sm_lin_quad_cW_2017,
    'quad_cW_2017':quad_cW_2017,
    'sm_lin_quad_cHW_2017':sm_lin_quad_cHW_2017,
    'quad_cHW_2017':quad_cHW_2017,
    ### fake contributions form here...
    'QCD_2017':QCD_2017, 'QCDHT_100to200_2017':QCDHT_100to200_2017, 'QCDHT_200to300_2017':QCDHT_200to300_2017, 'QCDHT_300to500_2017':QCDHT_300to500_2017, 'QCDHT_500to700_2017':QCDHT_500to700_2017, 'QCDHT_700to1000_2017':QCDHT_700to1000_2017, 'QCDHT_1000to1500_2017':QCDHT_1000to1500_2017, 'QCDHT_1500to2000_2017':QCDHT_1500to2000_2017, 'QCDHT_2000toInf_2017':QCDHT_2000toInf_2017,
    'ZZtoLep_2017':ZZtoLep_2017, 'ZZTo2L2Nu_2017':ZZTo2L2Nu_2017, 'ZZJJTo4L_EWK_2017':ZZJJTo4L_EWK_2017, 'ZZJJTo4L_QCD_2017':ZZJJTo4L_QCD_2017, 'GluGluToContinToZZTo2e2nu_2017':GluGluToContinToZZTo2e2nu_2017, 'GluGluToContinToZZTo2e2mu_2017':GluGluToContinToZZTo2e2mu_2017, 'GluGluToContinToZZTo2e2tau_2017':GluGluToContinToZZTo2e2tau_2017, 'GluGluToContinToZZTo2mu2nu_2017':GluGluToContinToZZTo2mu2nu_2017, 'GluGluToContinToZZTo2mu2tau_2017':GluGluToContinToZZTo2mu2tau_2017, 'GluGluToContinToZZTo4e_2017':GluGluToContinToZZTo4e_2017, 'GluGluToContinToZZTo4mu_2017':GluGluToContinToZZTo4mu_2017, 'GluGluToContinToZZTo4tau_2017':GluGluToContinToZZTo4tau_2017,
    'GluGluToContinToZZTo4L_2017':GluGluToContinToZZTo4L_2017,
    'TT_2017':TT_2017, 'TT_SemiLep2017':TT_SemiLep_2017, 'TT_Had_2017':TT_Had_2017,
    'TTTo2L2Nu_2017':TTTo2L2Nu_2017,
    'TT_beff_2017':TT_beff_2017,
    'WJets_2017':WJets_2017, 'WJetsHT70to100_2017':WJetsHT70to100_2017, 'WJetsHT100to200_2017':WJetsHT100to200_2017, 'WJetsHT200to400_2017':WJetsHT200to400_2017, 'WJetsHT400to600_2017':WJetsHT400to600_2017, 'WJetsHT600to800_2017':WJetsHT600to800_2017, 'WJetsHT800to1200_2017':WJetsHT800to1200_2017, 'WJetsHT1200to2500_2017':WJetsHT1200to2500_2017, 'WJetsHT2500toInf_2017':WJetsHT2500toInf_2017,
    'WJets_Fake_2017':WJets_Fake_2017, 'WJetsHT70to100_Fake_2017':WJetsHT70to100_Fake_2017, 'WJetsHT100to200_Fake_2017':WJetsHT100to200_Fake_2017, 'WJetsHT200to400_Fake_2017':WJetsHT200to400_Fake_2017, 'WJetsHT400to600_Fake_2017':WJetsHT400to600_Fake_2017, 'WJetsHT600to800_Fake_2017':WJetsHT600to800_Fake_2017, 'WJetsHT800to1200_Fake_2017':WJetsHT800to1200_Fake_2017, 'WJetsHT1200to2500_Fake_2017':WJetsHT1200to2500_Fake_2017, 'WJetsHT2500toInf_Fake_2017':WJetsHT2500toInf_Fake_2017,
    'DYJetsToLL_2017':DYJetsToLL_2017, 'DY1JetsToLL_2017':DY1JetsToLL_2017, 'DY2JetsToLL_2017':DY2JetsToLL_2017, 'DY3JetsToLL_2017':DY3JetsToLL_2017, 'DY4JetsToLL_2017':DY4JetsToLL_2017, 'DYJetsToLLM5to50_2017':DYJetsToLLM5to50_2017,
    'DYJetsToLL_Fake_2017':DYJetsToLL_Fake_2017, 'DY1JetsToLL_Fake_2017':DY1JetsToLL_Fake_2017, 'DY2JetsToLL_Fake_2017':DY2JetsToLL_Fake_2017, 'DY3JetsToLL_Fake_2017':DY3JetsToLL_Fake_2017, 'DY4JetsToLL_Fake_2017':DY4JetsToLL_Fake_2017,
    #'DYJetsM_2017':DYJetsM_2017, 'DYJetsToLLM5to50_2017':DYJetsToLLM5to50_2017, 'DYJetsToLLM50_2017':DYJetsToLLM50_2017,
    # to here
    'VG_2017':VG_2017, 'ZG_2017':ZG_2017, 'WG_2017':WG_2017,
    'TVX_2017':TVX_2017, 'TTGJets_2017':TTGJets_2017, 'TTZToQQ_2017':TTZToQQ_2017, 'TTZToLLNuNu_2017':TTZToLLNuNu_2017, 'TTWJetsToQQ_2017':TTWJetsToQQ_2017, 'TTWJetsToLNu_2017':TTWJetsToLNu_2017, 'tZq_ll_4f_2017':tZq_ll_4f_2017,
    'WrongSign_2017': WrongSign_2017, 'WWto2L2Nu_2017':WWto2L2Nu_2017, 'GluGluToWWToENuENu_2017':GluGluToWWToENuENu_2017, 'GluGluToWWToENuMNu2017':GluGluToWWToENuMNu2017, 'GluGluToWWToENuTNu2017':GluGluToWWToENuTNu2017, 'GluGluToWWToMNuENu_2017':GluGluToWWToMNuENu_2017, 'GluGluToWWToMNuMNu2017':GluGluToWWToMNuMNu2017, 'GluGluToWWToMNuTNu2017':GluGluToWWToMNuTNu2017, 'GluGluToWWToTNuENu_2017':GluGluToWWToTNuENu_2017, 'GluGluToWWToTNuMNu2017':GluGluToWWToTNuMNu2017, 'GluGluToWWToTNuTNu2017':GluGluToWWToTNuTNu2017, 'STtW_top_2017':STtW_top_2017, 'GluGluHToWWTo2L2Nu_2017':GluGluHToWWTo2L2Nu_2017, 'GluGluHToZZTo2L2Q_2017':GluGluHToZZTo2L2Q_2017, 'GluGluHToZZTo4L_2017':GluGluHToZZTo4L_2017, 'GluGluHToTauTau_2017':GluGluHToTauTau_2017, 'VBFHToWWTo2L2Nu_2017':VBFHToWWTo2L2Nu_2017, 'VBFHToTauTau_2017':VBFHToTauTau_2017, 'ttHToNonbb_2017':ttHToNonbb_2017, 'VHToNonbb_2017':VHToNonbb_2017,
    'OtherWS_2017':OtherWS_2017,
    'Other_2017':Other_2017, 'WWTo2L2Nu_DoubleScattering_2017':WWTo2L2Nu_DoubleScattering_2017, 'WWW_4F_2017':WWW_4F_2017, 'WWZTo3L1Nu2Q_2017':WWZTo3L1Nu2Q_2017, 'WZZ_2017':WZZ_2017, 'ZZZ_2017':ZZZ_2017, 'WWG_2017':WWG_2017,
    'WZ_2017':WZ_2017,
    'FakeMu_2017':FakeMu_2017,
    'DataMu_2017':DataMu_2017, 'DataMuB_2017':DataMuB_2017, 'DataMuC_2017':DataMuC_2017, 'DataMuD_2017':DataMuD_2017, 'DataMuE_2017':DataMuE_2017, 'DataMuF_2017':DataMuF_2017, 'DataMuFake_2017': DataMuFake_2017,
    'FakeEle_2017':FakeEle_2017,
    'FakeMuPromptTau_2017':FakeMuPromptTau_2017, 'PromptMuFakeTau_2017':PromptMuFakeTau_2017, 'FakeMuFakeTau_2017':FakeMuFakeTau_2017,
    'DataEle_2017':DataEle_2017, 'DataEleB_2017':DataEleB_2017, 'DataEleC_2017':DataEleC_2017, 'DataEleD_2017':DataEleD_2017, 'DataEleE_2017':DataEleE_2017, 'DataEleF_2017':DataEleF_2017, 'DataEleFake_2017': DataEleFake_2017, 'MCFake_2017': MCFake_2017,
    'FakeElePromptTau_2017':FakeElePromptTau_2017, 'PromptEleFakeTau_2017':PromptEleFakeTau_2017, 'FakeEleFakeTau_2017':FakeEleFakeTau_2017,
    'DataEleMu_2017':DataEleMu_2017,
    'FakeEleMu_2017':FakeEleMu_2017,
    'DataTau_2017':DataTau_2017, 'DataTauB_2017':DataTauB_2017, 'DataTauC_2017':DataTauC_2017, 'DataTauD_2017':DataTauD_2017, 'DataTauE_2017':DataTauE_2017, 'DataTauF_2017':DataTauF_2017, 'DataTauFake_2017': DataTauFake_2017,
    'DataHT_2017':DataHT_2017, 'DataHTnoB_2017':DataHTnoB_2017, 'DataHTB_2017':DataHTB_2017, 'DataHTC_2017':DataHTC_2017, 'DataHTD_2017':DataHTD_2017, 'DataHTE_2017':DataHTE_2017, 'DataHTF_2017':DataHTF_2017,
    'DataMET_2017':DataMET_2017, 'DataMETB_2017':DataMETB_2017, 'DataMETC_2017':DataMETC_2017, 'DataMETD_2017':DataMETD_2017, 'DataMETE_2017':DataMETE_2017, 'DataMETF_2017':DataMETF_2017,

    'SampleEleFake_2017': SampleEleFake_2017, 'SampleMuFake_2017': SampleMuFake_2017, 'SampleHTFake_2017': SampleHTFake_2017, 'SampleHTFakepart_2017': SampleHTFakepart_2017, 

    ###### 2018 ######
    'WpWpJJ_EWK_2018':WpWpJJ_EWK_2018,
    'WpWpJJ_QCD_2018':WpWpJJ_QCD_2018,
    'VBS_SSWW_SM_2018':VBS_SSWW_SM_2018, 'VBS_SSWW_LL_SM_2018':VBS_SSWW_LL_SM_2018, 'VBS_SSWW_TL_SM_2018':VBS_SSWW_TL_SM_2018, 'VBS_SSWW_TT_SM_2018':VBS_SSWW_TT_SM_2018,
    'VBS_SSWW_cHW_2018':VBS_SSWW_cHW_2018, 'VBS_SSWW_cHW_BSM_2018':VBS_SSWW_cHW_BSM_2018, 'VBS_SSWW_cHW_INT_2018':VBS_SSWW_cHW_INT_2018,
    'VBS_SSWW_cW_2018':VBS_SSWW_cW_2018, 'VBS_SSWW_cW_BSM_2018':VBS_SSWW_cW_BSM_2018, 'VBS_SSWW_cW_INT_2018':VBS_SSWW_cW_INT_2018,
    'VBS_SSWW_cW_cHW_2018':VBS_SSWW_cW_cHW_2018,
    'VBS_SSWW_DIM6_2018':VBS_SSWW_DIM6_2018,
    'VBS_SSWW_DIM6_SM_2018':VBS_SSWW_DIM6_SM_2018,
    'VBS_SSWW_cHW_SM_2018':VBS_SSWW_cHW_SM_2018,
    'VBS_SSWW_cW_SM_2018':VBS_SSWW_cW_SM_2018,
    'VBS_SSWW_aQGC_2018':VBS_SSWW_aQGC_2018,
    'VBS_SSWW_FS0_25_BSM_2018':VBS_SSWW_FS0_25_BSM_2018,
    'VBS_SSWW_FS0_25_INT_2018':VBS_SSWW_FS0_25_INT_2018,
    'VBS_SSWW_FS0_25_SM_2018':VBS_SSWW_FS0_25_SM_2018,
    'VBS_SSWW_FS0_25_2018':VBS_SSWW_FS0_25_2018,
    'VBS_SSWW_FS0_5_BSM_2018':VBS_SSWW_FS0_5_BSM_2018,
    'VBS_SSWW_FS0_5_INT_2018':VBS_SSWW_FS0_5_INT_2018,
    'VBS_SSWW_FS0_5_SM_2018':VBS_SSWW_FS0_5_SM_2018,
    'VBS_SSWW_FS0_5_2018':VBS_SSWW_FS0_5_2018,
    'VBS_SSWW_FS0_0_2018':VBS_SSWW_FS0_0_2018,
    'VBS_SSWW_FS1_50_BSM_2018':VBS_SSWW_FS1_50_BSM_2018,
    'VBS_SSWW_FS1_50_INT_2018':VBS_SSWW_FS1_50_INT_2018,
    'VBS_SSWW_FS1_50_SM_2018':VBS_SSWW_FS1_50_SM_2018,
    'VBS_SSWW_FS1_50_2018':VBS_SSWW_FS1_50_2018,
    'VBS_SSWW_FS1_10_BSM_2018':VBS_SSWW_FS1_10_BSM_2018,
    'VBS_SSWW_FS1_10_INT_2018':VBS_SSWW_FS1_10_INT_2018,
    'VBS_SSWW_FS1_10_SM_2018':VBS_SSWW_FS1_10_SM_2018,
    'VBS_SSWW_FS1_10_2018':VBS_SSWW_FS1_10_2018,
    'VBS_SSWW_FS1_0_2018':VBS_SSWW_FS1_0_2018,
    'VBS_SSWW_FM0_25_BSM_2018':VBS_SSWW_FM0_25_BSM_2018,
    'VBS_SSWW_FM0_25_INT_2018':VBS_SSWW_FM0_25_INT_2018,
    'VBS_SSWW_FM0_25_SM_2018':VBS_SSWW_FM0_25_SM_2018,
    'VBS_SSWW_FM0_25_2018':VBS_SSWW_FM0_25_2018,
    'VBS_SSWW_FM0_5_BSM_2018':VBS_SSWW_FM0_5_BSM_2018,
    'VBS_SSWW_FM0_5_INT_2018':VBS_SSWW_FM0_5_INT_2018,
    'VBS_SSWW_FM0_5_SM_2018':VBS_SSWW_FM0_5_SM_2018,
    'VBS_SSWW_FM0_5_2018':VBS_SSWW_FM0_5_2018,
    'VBS_SSWW_FM0_0_2018':VBS_SSWW_FM0_0_2018,
    'VBS_SSWW_FM1_25_BSM_2018':VBS_SSWW_FM1_25_BSM_2018,
    'VBS_SSWW_FM1_25_INT_2018':VBS_SSWW_FM1_25_INT_2018,
    'VBS_SSWW_FM1_25_SM_2018':VBS_SSWW_FM1_25_SM_2018,
    'VBS_SSWW_FM1_25_2018':VBS_SSWW_FM1_25_2018,
    'VBS_SSWW_FM1_5_BSM_2018':VBS_SSWW_FM1_5_BSM_2018,
    'VBS_SSWW_FM1_5_INT_2018':VBS_SSWW_FM1_5_INT_2018,
    'VBS_SSWW_FM1_5_SM_2018':VBS_SSWW_FM1_5_SM_2018,
    'VBS_SSWW_FM1_5_2018':VBS_SSWW_FM1_5_2018,
    'VBS_SSWW_FM1_0_2018':VBS_SSWW_FM1_0_2018,
    'VBS_SSWW_FM6_25_BSM_2018':VBS_SSWW_FM6_25_BSM_2018,
    'VBS_SSWW_FM6_25_INT_2018':VBS_SSWW_FM6_25_INT_2018,
    'VBS_SSWW_FM6_25_SM_2018':VBS_SSWW_FM6_25_SM_2018,
    'VBS_SSWW_FM6_25_2018':VBS_SSWW_FM6_25_2018,
    'VBS_SSWW_FM6_5_BSM_2018':VBS_SSWW_FM6_5_BSM_2018,
    'VBS_SSWW_FM6_5_INT_2018':VBS_SSWW_FM6_5_INT_2018,
    'VBS_SSWW_FM6_5_SM_2018':VBS_SSWW_FM6_5_SM_2018,
    'VBS_SSWW_FM6_5_2018':VBS_SSWW_FM6_5_2018,
    'VBS_SSWW_FM6_0_2018':VBS_SSWW_FM6_0_2018,
    'VBS_SSWW_FM7_50_BSM_2018':VBS_SSWW_FM7_50_BSM_2018,
    'VBS_SSWW_FM7_50_INT_2018':VBS_SSWW_FM7_50_INT_2018,
    'VBS_SSWW_FM7_50_SM_2018':VBS_SSWW_FM7_50_SM_2018,
    'VBS_SSWW_FM7_50_2018':VBS_SSWW_FM7_50_2018,
    'VBS_SSWW_FM7_10_BSM_2018':VBS_SSWW_FM7_10_BSM_2018,
    'VBS_SSWW_FM7_10_INT_2018':VBS_SSWW_FM7_10_INT_2018,
    'VBS_SSWW_FM7_10_SM_2018':VBS_SSWW_FM7_10_SM_2018,
    'VBS_SSWW_FM7_10_2018':VBS_SSWW_FM7_10_2018,
    'VBS_SSWW_FM7_0_2018':VBS_SSWW_FM7_0_2018,
    'VBS_SSWW_FT0_2p5_BSM_2018':VBS_SSWW_FT0_2p5_BSM_2018,
    'VBS_SSWW_FT0_2p5_INT_2018':VBS_SSWW_FT0_2p5_INT_2018,
    'VBS_SSWW_FT0_2p5_SM_2018':VBS_SSWW_FT0_2p5_SM_2018,
    'VBS_SSWW_FT0_2p5_2018':VBS_SSWW_FT0_2p5_2018,
    'VBS_SSWW_FT0_0p5_BSM_2018':VBS_SSWW_FT0_0p5_BSM_2018,
    'VBS_SSWW_FT0_0p5_INT_2018':VBS_SSWW_FT0_0p5_INT_2018,
    'VBS_SSWW_FT0_0p5_SM_2018':VBS_SSWW_FT0_0p5_SM_2018,
    'VBS_SSWW_FT0_0p5_2018':VBS_SSWW_FT0_0p5_2018,
    'VBS_SSWW_FT0_0_2018':VBS_SSWW_FT0_0_2018,
    'VBS_SSWW_FT1_1_BSM_2018':VBS_SSWW_FT1_1_BSM_2018,
    'VBS_SSWW_FT1_1_INT_2018':VBS_SSWW_FT1_1_INT_2018,
    'VBS_SSWW_FT1_1_SM_2018':VBS_SSWW_FT1_1_SM_2018,
    'VBS_SSWW_FT1_1_2018':VBS_SSWW_FT1_1_2018,
    'VBS_SSWW_FT1_0p2_BSM_2018':VBS_SSWW_FT1_0p2_BSM_2018,
    'VBS_SSWW_FT1_0p2_INT_2018':VBS_SSWW_FT1_0p2_INT_2018,
    'VBS_SSWW_FT1_0p2_SM_2018':VBS_SSWW_FT1_0p2_SM_2018,
    'VBS_SSWW_FT1_0p2_2018':VBS_SSWW_FT1_0p2_2018,
    'VBS_SSWW_FT1_0_2018':VBS_SSWW_FT1_0_2018,
    'VBS_SSWW_FT2_2p5_BSM_2018':VBS_SSWW_FT2_2p5_BSM_2018,
    'VBS_SSWW_FT2_2p5_INT_2018':VBS_SSWW_FT2_2p5_INT_2018,
    'VBS_SSWW_FT2_2p5_SM_2018':VBS_SSWW_FT2_2p5_SM_2018,
    'VBS_SSWW_FT2_2p5_2018':VBS_SSWW_FT2_2p5_2018,
    'VBS_SSWW_FT2_0p5_BSM_2018':VBS_SSWW_FT2_0p5_BSM_2018,
    'VBS_SSWW_FT2_0p5_INT_2018':VBS_SSWW_FT2_0p5_INT_2018,
    'VBS_SSWW_FT2_0p5_SM_2018':VBS_SSWW_FT2_0p5_SM_2018,
    'VBS_SSWW_FT2_0p5_2018':VBS_SSWW_FT2_0p5_2018,
    'VBS_SSWW_FT2_0p5_2018':VBS_SSWW_FT2_0p5_2018,
    'VBS_SSWW_FT2_0_2018':VBS_SSWW_FT2_0_2018,
    'DHiggsToWW_2018':DHiggsToWW_2018,
    'sm_2018':sm_2018,
    'sm_lin_quad_cW_2018':sm_lin_quad_cW_2018,
    'quad_cW_2018':quad_cW_2018,
    'sm_lin_quad_cHW_2018':sm_lin_quad_cHW_2018,
    'quad_cHW_2018':quad_cHW_2018,

    ### fake contributions form here...
    'QCD_2018':QCD_2018, 'QCDHT_100to200_2018':QCDHT_100to200_2018, 'QCDHT_200to300_2018':QCDHT_200to300_2018, 'QCDHT_300to500_2018':QCDHT_300to500_2018, 'QCDHT_500to700_2018':QCDHT_500to700_2018, 'QCDHT_700to1000_2018':QCDHT_700to1000_2018, 'QCDHT_1000to1500_2018':QCDHT_1000to1500_2018, 'QCDHT_1500to2000_2018':QCDHT_1500to2000_2018, 'QCDHT_2000toInf_2018':QCDHT_2000toInf_2018,
    'ZZtoLep_2018':ZZtoLep_2018, 'ZZTo2L2Nu_2018':ZZTo2L2Nu_2018, 'ZZJJTo4L_EWK_2018':ZZJJTo4L_EWK_2018, 'ZZJJTo4L_QCD_2018':ZZJJTo4L_QCD_2018, 'GluGluToContinToZZTo2e2nu_2018':GluGluToContinToZZTo2e2nu_2018, 'GluGluToContinToZZTo2e2mu_2018':GluGluToContinToZZTo2e2mu_2018, 'GluGluToContinToZZTo2e2tau_2018':GluGluToContinToZZTo2e2tau_2018, 'GluGluToContinToZZTo2mu2nu_2018':GluGluToContinToZZTo2mu2nu_2018, 'GluGluToContinToZZTo2mu2tau_2018':GluGluToContinToZZTo2mu2tau_2018, 'GluGluToContinToZZTo4e_2018':GluGluToContinToZZTo4e_2018, 'GluGluToContinToZZTo4mu_2018':GluGluToContinToZZTo4mu_2018, 'GluGluToContinToZZTo4tau_2018':GluGluToContinToZZTo4tau_2018,
    'GluGluToContinToZZTo4L_2018':GluGluToContinToZZTo4L_2018,
    'TT_2018':TT_2018, 'TT_SemiLep_2018':TT_SemiLep_2018, 'TT_Had_2018':TT_Had_2018,#'TT_DiLep_2018':TT_DiLep_2018, 
    'WJets_2018':WJets_2018, 'WJetsHT70to100_2018':WJetsHT70to100_2018, 'WJetsHT100to200_2018':WJetsHT100to200_2018, 'WJetsHT200to400_2018':WJetsHT200to400_2018, 'WJetsHT400to600_2018':WJetsHT400to600_2018, 'WJetsHT600to800_2018':WJetsHT600to800_2018, 'WJetsHT800to1200_2018':WJetsHT800to1200_2018, 'WJetsHT1200to2500_2018':WJetsHT1200to2500_2018, 'WJetsHT2500toInf_2018':WJetsHT2500toInf_2018,
    'DYJetsToLL_2018':DYJetsToLL_2018, 'DY1JetsToLL_2018':DY1JetsToLL_2018, 'DY2JetsToLL_2018':DY2JetsToLL_2018, 'DY3JetsToLL_2018':DY3JetsToLL_2018, 'DY4JetsToLL_2018':DY4JetsToLL_2018, 
    'SampleHTFake_2018': SampleHTFake_2018,
    #'DYJetsToLL_Fake_2018':DYJetsToLL_Fake_2018, 'DY1JetsToLL_Fake_2018':DY1JetsToLL_Fake_2018, 'DY2JetsToLL_Fake_2018':DY2JetsToLL_Fake_2018, 'DY3JetsToLL_Fake_2018':DY3JetsToLL_Fake_2018, 'DY4JetsToLL_Fake_2018':DY4JetsToLL_Fake_2018,
    #'DYJetsM_2018':DYJetsM_2018, 'DYJetsToLLM5to50_2018':DYJetsToLLM5to50_2018, 'DYJetsToLLM50_2018':DYJetsToLLM50_2018,
    # to here
    'VG_2018':VG_2018, 'ZG_2018':ZG_2018, 'WG_2018':WG_2018,
    'TVX_2018':TVX_2018, 'TTGJets_2018':TTGJets_2018, 'TTZToQQ_2018':TTZToQQ_2018, 'TTZToLLNuNu_2018':TTZToLLNuNu_2018, 'TTWJetsToQQ_2018':TTWJetsToQQ_2018, 'TTWJetsToLNu_2018':TTWJetsToLNu_2018, 'tZq_ll_4f_2018':tZq_ll_4f_2018,
    'WrongSign_2018': WrongSign_2018, 'WWto2L2Nu_2018':WWto2L2Nu_2018, 'GluGluToWWToENuENu_2018':GluGluToWWToENuENu_2018, 'GluGluToWWToENuMNu2017':GluGluToWWToENuMNu2017, 'GluGluToWWToENuTNu2017':GluGluToWWToENuTNu2017, 'GluGluToWWToMNuENu_2018':GluGluToWWToMNuENu_2018, 'GluGluToWWToMNuMNu2017':GluGluToWWToMNuMNu2017, 'GluGluToWWToMNuTNu2017':GluGluToWWToMNuTNu2017, 'GluGluToWWToTNuENu_2018':GluGluToWWToTNuENu_2018, 'GluGluToWWToTNuMNu2017':GluGluToWWToTNuMNu2017, 'GluGluToWWToTNuTNu2017':GluGluToWWToTNuTNu2017, 'STtW_top_2018':STtW_top_2018, 'GluGluHToWWTo2L2Nu_2018':GluGluHToWWTo2L2Nu_2018, 'GluGluHToZZTo2L2Q_2018':GluGluHToZZTo2L2Q_2018, 'GluGluHToZZTo4L_2018':GluGluHToZZTo4L_2018, 'GluGluHToTauTau_2018':GluGluHToTauTau_2018, 'VBFHToWWTo2L2Nu_2018':VBFHToWWTo2L2Nu_2018, 'VBFHToTauTau_2018':VBFHToTauTau_2018, 'ttHToNonbb_2018':ttHToNonbb_2018, 'VHToNonbb_2018':VHToNonbb_2018,
    'OtherWS_2018':OtherWS_2018,
    'Other_2018':Other_2018, 'WWTo2L2Nu_DoubleScattering_2018':WWTo2L2Nu_DoubleScattering_2018, 'WWW_4F_2018':WWW_4F_2018, 'WWZTo3L1Nu2Q_2018':WWZTo3L1Nu2Q_2018, 'WZZ_2018':WZZ_2018, 'ZZZ_2018':ZZZ_2018, 'WWG_2018':WWG_2018,
    'TTTo2L2Nu_2018':TTTo2L2Nu_2018,
    'WZ_2018':WZ_2018,
    'FakeMu_2018':FakeMu_2018,
    'DataMu_2018':DataMu_2018, 'DataMuA_2018':DataMuA_2018, 'DataMuB_2018':DataMuB_2018, 'DataMuC_2018':DataMuC_2018, 'DataMuD_2018':DataMuD_2018,
    'FakeEle_2018':FakeEle_2018,
    'FakeMuPromptTau_2018':FakeMuPromptTau_2018, 'PromptMuFakeTau_2018':PromptMuFakeTau_2018, 'FakeMuFakeTau_2018':FakeMuFakeTau_2018,
    'DataEle_2018':DataEle_2018, 'DataEleA_2018':DataEleA_2018, 'DataEleB_2018':DataEleB_2018, 'DataEleC_2018':DataEleC_2018, 'DataEleD_2018':DataEleD_2018,
    'FakeElePromptTau_2018':FakeElePromptTau_2018, 'PromptEleFakeTau_2018':PromptEleFakeTau_2018, 'FakeEleFakeTau_2018':FakeEleFakeTau_2018,
    'DataHT_2018':DataHT_2018, 'DataHTA_2018':DataHTA_2018, 'DataHTB_2018':DataHTB_2018, 'DataHTC_2018':DataHTC_2018, 'DataHTD_2018':DataHTD_2018,
    #'SampleEleFake_2018': SampleEleFake_2018, 'SampleMuFake_2018': SampleMuFake_2018, 'SampleHTFake_2018': SampleHTFake_2018,

}

condor_dict={
    'WpWpJJ_QCD_2017':WpWpJJ_QCD_2017,
    'VBS_SSWW_SM_2017':VBS_SSWW_SM_2017,
    'VBS_SSWW_DIM6_SM_2017':VBS_SSWW_DIM6_SM_2017,
    #'VBS_SSWW_FS0_25_SM_2017':VBS_SSWW_FS0_25_SM_2017,
    #'VBS_SSWW_FS0_5_SM_2017':VBS_SSWW_FS0_5_SM_2017,
    #'VBS_SSWW_FS0_0_2017':VBS_SSWW_FS0_0_2017,
    #'VBS_SSWW_FS1_50_SM_2017':VBS_SSWW_FS1_50_SM_2017,
    #'VBS_SSWW_FS1_10_SM_2017':VBS_SSWW_FS1_10_SM_2017,
    #'VBS_SSWW_FS1_0_2017':VBS_SSWW_FS1_0_2017,
    #'VBS_SSWW_FM0_25_SM_2017':VBS_SSWW_FM0_25_SM_2017,
    #'VBS_SSWW_FM0_5_SM_2017':VBS_SSWW_FM0_5_SM_2017,
    #'VBS_SSWW_FM0_0_2017':VBS_SSWW_FM0_0_2017,
    #'VBS_SSWW_FM1_25_SM_2017':VBS_SSWW_FM1_25_SM_2017,
    #'VBS_SSWW_FM1_5_SM_2017':VBS_SSWW_FM1_5_SM_2017,
    #'VBS_SSWW_FM1_0_2017':VBS_SSWW_FM1_0_2017,
    #'VBS_SSWW_FM6_25_SM_2017':VBS_SSWW_FM6_25_SM_2017,
    #'VBS_SSWW_FM6_5_SM_2017':VBS_SSWW_FM6_5_SM_2017,
    #'VBS_SSWW_FM6_0_2017':VBS_SSWW_FM6_0_2017,
    #'VBS_SSWW_FM7_50_SM_2017':VBS_SSWW_FM7_50_SM_2017,
    #'VBS_SSWW_FM7_10_SM_2017':VBS_SSWW_FM7_10_SM_2017,
    #'VBS_SSWW_FM7_0_2017':VBS_SSWW_FM7_0_2017,
    #'VBS_SSWW_FT0_2p5_SM_2017':VBS_SSWW_FT0_2p5_SM_2017,
    #'VBS_SSWW_FT0_0p5_SM_2017':VBS_SSWW_FT0_0p5_SM_2017,
    #'VBS_SSWW_FT0_0_2017':VBS_SSWW_FT0_0_2017,
    #'VBS_SSWW_FT1_1_SM_2017':VBS_SSWW_FT1_1_SM_2017,
    #'VBS_SSWW_FT1_0p2_SM_2017':VBS_SSWW_FT1_0p2_SM_2017,
    #'VBS_SSWW_FT1_0_2017':VBS_SSWW_FT1_0_2017,
    #'VBS_SSWW_FT2_2p5_SM_2017':VBS_SSWW_FT2_2p5_SM_2017,
    #'VBS_SSWW_FT2_0p5_SM_2017':VBS_SSWW_FT2_0p5_SM_2017,
    #'VBS_SSWW_FT2_0_2017':VBS_SSWW_FT2_0_2017,
    'VBS_SSWW_aQGC_2017':VBS_SSWW_aQGC_2017,
    ### fake contributions from here...
    #'QCD_2017':QCD_2017,
    'ZZtoLep_2017':ZZtoLep_2017,
    #'TT_2017':TT_2017,
    #'WJets_2017':WJets_2017,
    #'DYJetsToLL_2017':DYJetsToLL_2017,
    # to here
    'VG_2017':VG_2017,
    'TVX_2017':TVX_2017,
    'OtherWS_2017':OtherWS_2017,
    'TTTo2L2Nu_2017':TTTo2L2Nu_2017,
    #'TT_beff_2017':TT_beff_2017,
    'WZ_2017':WZ_2017,
    'DataMu_2017':DataMu_2017,
    'DataEle_2017':DataEle_2017,
    #'DataHT_2017':DataHT_2017,
}

merge_dict={
    'WpWpJJ_QCD_2017':WpWpJJ_QCD_2017,
    'VBS_SSWW_SM_2017':VBS_SSWW_SM_2017,
    'VBS_SSWW_cHW_2017':VBS_SSWW_cHW_2017,
    #'VBS_SSWW_cHW_BSM_2017':VBS_SSWW_cHW_BSM_2017,
    #'VBS_SSWW_cHW_SM_2017':VBS_SSWW_cHW_SM_2017,
    'VBS_SSWW_cW_2017':VBS_SSWW_cW_2017,
    #'VBS_SSWW_cW_BSM_2017':VBS_SSWW_cW_BSM_2017,
    #'VBS_SSWW_cW_SM_2017':VBS_SSWW_cW_SM_2017,
    #'VBS_SSWW_cW_cHW_2017':VBS_SSWW_cW_cHW_2017,
    'VBS_SSWW_DIM6_2017':VBS_SSWW_DIM6_2017,
    #'VBS_SSWW_DIM6_SM_2017':VBS_SSWW_DIM6_SM_2017,
    #'VBS_SSWW_cHW_SM_2017':VBS_SSWW_cHW_SM_2017,
    #'VBS_SSWW_cW_SM_2017':VBS_SSWW_cW_SM_2017,
    'VBS_SSWW_aQGC_2017':VBS_SSWW_aQGC_2017,
    #'VBS_SSWW_FS0_25_SM_2017':VBS_SSWW_FS0_25_SM_2017,
    #'VBS_SSWW_FS0_5_SM_2017':VBS_SSWW_FS0_5_SM_2017,
    #'VBS_SSWW_FS0_25_BSM_2017':VBS_SSWW_FS0_25_BSM_2017,
    #'VBS_SSWW_FS0_5_BSM_2017':VBS_SSWW_FS0_5_BSM_2017,
    #'VBS_SSWW_FS0_25_2017':VBS_SSWW_FS0_25_2017,
    #'VBS_SSWW_FS0_5_2017':VBS_SSWW_FS0_5_2017,
    #'VBS_SSWW_FS0_0_2017':VBS_SSWW_FS0_0_2017,
    #'VBS_SSWW_FS1_50_SM_2017':VBS_SSWW_FS1_50_SM_2017,
    #'VBS_SSWW_FS1_10_SM_2017':VBS_SSWW_FS1_10_SM_2017,
    #'VBS_SSWW_FS1_50_BSM_2017':VBS_SSWW_FS1_50_BSM_2017,
    #'VBS_SSWW_FS1_10_BSM_2017':VBS_SSWW_FS1_10_BSM_2017,
    #'VBS_SSWW_FS1_50_2017':VBS_SSWW_FS1_50_2017,
    #'VBS_SSWW_FS1_10_2017':VBS_SSWW_FS1_10_2017,
    #'VBS_SSWW_FS1_0_2017':VBS_SSWW_FS1_0_2017,
    #'VBS_SSWW_FM0_25_SM_2017':VBS_SSWW_FM0_25_SM_2017,
    #'VBS_SSWW_FM0_5_SM_2017':VBS_SSWW_FM0_5_SM_2017,
    #'VBS_SSWW_FM0_25_BSM_2017':VBS_SSWW_FM0_25_BSM_2017,
    #'VBS_SSWW_FM0_5_BSM_2017':VBS_SSWW_FM0_5_BSM_2017,
    #'VBS_SSWW_FM0_25_2017':VBS_SSWW_FM0_25_2017,
    #'VBS_SSWW_FM0_5_2017':VBS_SSWW_FM0_5_2017,
    #'VBS_SSWW_FM0_0_2017':VBS_SSWW_FM0_0_2017,
    #'VBS_SSWW_FM1_25_SM_2017':VBS_SSWW_FM1_25_SM_2017,
    #'VBS_SSWW_FM1_5_SM_2017':VBS_SSWW_FM1_5_SM_2017,
    #'VBS_SSWW_FM1_25_BSM_2017':VBS_SSWW_FM1_25_BSM_2017,
    #'VBS_SSWW_FM1_5_BSM_2017':VBS_SSWW_FM1_5_BSM_2017,
    #'VBS_SSWW_FM1_25_2017':VBS_SSWW_FM1_25_2017,
    #'VBS_SSWW_FM1_5_2017':VBS_SSWW_FM1_5_2017,
    #'VBS_SSWW_FM1_0_2017':VBS_SSWW_FM1_0_2017,
    #'VBS_SSWW_FM6_25_SM_2017':VBS_SSWW_FM6_25_SM_2017,
    #'VBS_SSWW_FM6_5_SM_2017':VBS_SSWW_FM6_5_SM_2017,
    #'VBS_SSWW_FM6_25_BSM_2017':VBS_SSWW_FM6_25_BSM_2017,
    #'VBS_SSWW_FM6_5_BSM_2017':VBS_SSWW_FM6_5_BSM_2017,
    #'VBS_SSWW_FM6_25_2017':VBS_SSWW_FM6_25_2017,
    #'VBS_SSWW_FM6_5_2017':VBS_SSWW_FM6_5_2017,
    #'VBS_SSWW_FM6_0_2017':VBS_SSWW_FM6_0_2017,
    #'VBS_SSWW_FM7_50_SM_2017':VBS_SSWW_FM7_50_SM_2017,
    #'VBS_SSWW_FM7_10_SM_2017':VBS_SSWW_FM7_10_SM_2017,
    #'VBS_SSWW_FM7_50_BSM_2017':VBS_SSWW_FM7_50_BSM_2017,
    #'VBS_SSWW_FM7_10_BSM_2017':VBS_SSWW_FM7_10_BSM_2017,
    #'VBS_SSWW_FM7_50_2017':VBS_SSWW_FM7_50_2017,
    #'VBS_SSWW_FM7_10_2017':VBS_SSWW_FM7_10_2017,
    #'VBS_SSWW_FM7_0_2017':VBS_SSWW_FM7_0_2017,
    #'VBS_SSWW_FT0_2p5_SM_2017':VBS_SSWW_FT0_2p5_SM_2017,
    #'VBS_SSWW_FT0_0p5_SM_2017':VBS_SSWW_FT0_0p5_SM_2017,
    #'VBS_SSWW_FT0_2p5_BSM_2017':VBS_SSWW_FT0_2p5_BSM_2017,
    #'VBS_SSWW_FT0_0p5_BSM_2017':VBS_SSWW_FT0_0p5_BSM_2017,
    #'VBS_SSWW_FT0_2p5_2017':VBS_SSWW_FT0_2p5_2017,
    #'VBS_SSWW_FT0_0p5_2017':VBS_SSWW_FT0_0p5_2017,
    #'VBS_SSWW_FT0_0_2017':VBS_SSWW_FT0_0_2017,
    #'VBS_SSWW_FT1_1_SM_2017':VBS_SSWW_FT1_1_SM_2017,
    #'VBS_SSWW_FT1_0p2_SM_2017':VBS_SSWW_FT1_0p2_SM_2017,
    #'VBS_SSWW_FT1_1_BSM_2017':VBS_SSWW_FT1_1_BSM_2017,
    #'VBS_SSWW_FT1_0p2_BSM_2017':VBS_SSWW_FT1_0p2_BSM_2017,
    #'VBS_SSWW_FT1_1_2017':VBS_SSWW_FT1_1_2017,
    #'VBS_SSWW_FT1_0p2_2017':VBS_SSWW_FT1_0p2_2017,
    #'VBS_SSWW_FT1_0_2017':VBS_SSWW_FT1_0_2017,
    #'VBS_SSWW_FT2_2p5_SM_2017':VBS_SSWW_FT2_2p5_SM_2017,
    #'VBS_SSWW_FT2_0p5_SM_2017':VBS_SSWW_FT2_0p5_SM_2017,
    #'VBS_SSWW_FT2_2p5_BSM_2017':VBS_SSWW_FT2_2p5_BSM_2017,
    #'VBS_SSWW_FT2_0p5_BSM_2017':VBS_SSWW_FT2_0p5_BSM_2017,
    #'VBS_SSWW_FT2_2p5_2017':VBS_SSWW_FT2_2p5_2017,
    #'VBS_SSWW_FT2_0p5_2017':VBS_SSWW_FT2_0p5_2017,
    #'VBS_SSWW_FT2_0_2017':VBS_SSWW_FT2_0_2017,
    'VBS_SSWW_aQGC_2017':VBS_SSWW_aQGC_2017,
    ### fake contributions from here...
    #'QCD_2017':QCD_2017,
    'ZZtoLep_2017':ZZtoLep_2017,
    #'TT_2017':TT_2017,
    #'WJets_2017':WJets_2017,
    #'DYJetsToLL_2017':DYJetsToLL_2017,
    # to here
    'VG_2017':VG_2017,
    'TVX_2017':TVX_2017,
    'OtherWS_2017':OtherWS_2017,
    'Other_2017':Other_2017,
    'WrongSign_2017':WrongSign_2017,
    'TTTo2L2Nu_2017':TTTo2L2Nu_2017,
    'TT_beff_2017':TT_beff_2017,
    'WZ_2017':WZ_2017,
    'DataMu_2017':DataMu_2017,
    'DataEle_2017':DataEle_2017,
    'DataHT_2017':DataHT_2017,
    'DataEleMu_2017':DataEleMu_2017,
}


class_list=[
    #WpWpJJ_EWK_2017,
    VBS_SSWW_LL_SM_2017,
    VBS_SSWW_TL_SM_2017,
    VBS_SSWW_TT_SM_2017,
    VBS_SSWW_SM_2017,
    VBS_SSWW_cHW_2017,
    VBS_SSWW_cHW_BSM_2017,
    VBS_SSWW_cHW_SM_2017,
    VBS_SSWW_cW_2017,
    VBS_SSWW_cW_BSM_2017,
    VBS_SSWW_cW_SM_2017,
    #VBS_SSWW_cW_cHW_2017,
    #VBS_SSWW_DIM6_2017,
    #VBS_SSWW_DIM6_SM_2017,
    #VBS_SSWW_aQGC_2017,
    #VBS_SSWW_FS0_25_SM_2017,
    VBS_SSWW_FS0_5_SM_2017,
    #VBS_SSWW_FS0_25_BSM_2017,
    VBS_SSWW_FS0_5_BSM_2017,
    ##VBS_SSWW_FS0_25_2017,
    VBS_SSWW_FS0_5_2017,
    VBS_SSWW_FS0_0_2017,
    #VBS_SSWW_FS1_50_SM_2017,
    #VBS_SSWW_FS1_10_SM_2017,
    #VBS_SSWW_FS1_50_BSM_2017,
    #VBS_SSWW_FS1_10_BSM_2017,
    #VBS_SSWW_FS1_50_2017,
    #VBS_SSWW_FS1_10_2017,
    #VBS_SSWW_FS1_0_2017,
    #VBS_SSWW_FM0_25_SM_2017,
    #VBS_SSWW_FM0_5_SM_2017,
    #VBS_SSWW_FM0_25_BSM_2017,
    #VBS_SSWW_FM0_5_BSM_2017,
    #VBS_SSWW_FM0_25_2017,
    #VBS_SSWW_FM0_5_2017,
    #VBS_SSWW_FM0_0_2017,
    #VBS_SSWW_FM1_25_SM_2017,
    VBS_SSWW_FM1_5_SM_2017,
    #VBS_SSWW_FM1_25_BSM_2017,
    VBS_SSWW_FM1_5_BSM_2017,
    #VBS_SSWW_FM1_25_2017,
    VBS_SSWW_FM1_5_2017,
    VBS_SSWW_FM1_0_2017,
    #VBS_SSWW_FM6_25_SM_2017,
    #VBS_SSWW_FM6_5_SM_2017,
    #VBS_SSWW_FM6_25_BSM_2017,
    #VBS_SSWW_FM6_5_BSM_2017,
    #VBS_SSWW_FM6_25_2017,
    #VBS_SSWW_FM6_5_2017,
    #VBS_SSWW_FM6_0_2017,
    #VBS_SSWW_FM7_50_SM_2017,
    #VBS_SSWW_FM7_10_SM_2017,
    #VBS_SSWW_FM7_50_BSM_2017,
    #VBS_SSWW_FM7_10_BSM_2017,
    #VBS_SSWW_FM7_50_2017,
    #VBS_SSWW_FM7_10_2017,
    #VBS_SSWW_FM7_0_2017,
    #VBS_SSWW_FT0_2p5_SM_2017,
    #VBS_SSWW_FT0_0p5_SM_2017,
    #VBS_SSWW_FT0_2p5_BSM_2017,
    #VBS_SSWW_FT0_0p5_BSM_2017,
    #VBS_SSWW_FT0_2p5_2017,
    #VBS_SSWW_FT0_0p5_2017,
    #VBS_SSWW_FT0_0_2017,
    #VBS_SSWW_FT1_1_SM_2017,
    #VBS_SSWW_FT1_0p2_SM_2017,
    #VBS_SSWW_FT1_1_BSM_2017,
    #VBS_SSWW_FT1_0p2_BSM_2017,
    #VBS_SSWW_FT1_1_2017,
    #VBS_SSWW_FT1_0p2_2017,
    #VBS_SSWW_FT1_0_2017,
    #VBS_SSWW_FT2_2p5_SM_2017,
    VBS_SSWW_FT2_0p5_SM_2017,
    #VBS_SSWW_FT2_2p5_BSM_2017,
    VBS_SSWW_FT2_0p5_BSM_2017,
    #VBS_SSWW_FT2_2p5_2017,
    VBS_SSWW_FT2_0p5_2017,
    VBS_SSWW_FT2_0_2017,
    VG_2017,
    WpWpJJ_QCD_2017,
    TVX_2017,
    Other_2017,
    TTTo2L2Nu_2017,
    WZ_2017,
    #OtherWS_2017,
    WrongSign_2017,
    ZZtoLep_2017,
    ##DYJetsToLL_2017,
    ##DYJetsToLL_Fake_2017,
    ##DYJetsM_2017,
    ##TT_2017,
    ##QCD_2017,
    #W#Jets_2017,
    FakeMu_2017,
    FakeMuPromptTau_2017,
    PromptMuFakeTau_2017,
    FakeMuFakeTau_2017,
    DataMu_2017,
    FakeEle_2017,
    FakeEleFakeTau_2017,
    FakeElePromptTau_2017,
    PromptEleFakeTau_2017,
    DataEle_2017,
    ##DataHT_2017,
    DataEleMu_2017,
    FakeEleMu_2017,
]

class_list_bis = [
    WWto2L2Nu_2017,
    GluGluToWWToENuENu_2017,
    GluGluToWWToENuMNu2017,
    GluGluToWWToENuTNu2017,
    GluGluToWWToMNuENu_2017,
    GluGluToWWToMNuMNu2017,
    GluGluToWWToMNuTNu2017,
    GluGluToWWToTNuENu_2017,
    GluGluToWWToTNuMNu2017,
    GluGluToWWToTNuTNu2017,
    STtW_top_2017,
    GluGluHToWWTo2L2Nu_2017,
    GluGluHToZZTo2L2Q_2017,
    GluGluHToZZTo4L_2017,
    GluGluHToTauTau_2017,
    VBFHToWWTo2L2Nu_2017,
    VBFHToTauTau_2017,
    ttHToNonbb_2017,
    VHToNonbb_2017,
]