import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
from flashgg.MetaData.MetaConditionsReader import *


"""
Standard configuration
"""
process = cms.Process("VertexInvestigationAnalysis")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")

process.source = cms.Source("PoolSource",
                            fileNames=cms.untracked.vstring(
                                "/store/user/spigazzi/flashgg/Era2016_RR-07Aug17_v1/legacyRun2TestV1/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/Era2016_RR-07Aug17_v1-legacyRun2TestV1-v0-RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/190228_142907/0000/myMicroAODOutputFile_610.root"
                                )
                            )
process.TFileService = cms.Service("TFileService", fileName=cms.string("test.root"))

process.options = cms.untracked.PSet(wantSummary=cms.untracked.bool(True))
process.options.allowUnscheduled = cms.untracked.bool(True)
process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)


"""
Process Customization
"""
from flashgg.MetaData.JobConfig import customize

customize.setDefault("maxEvents", 10000)
customize.setDefault("targetLumi", 1.e+3)
customize.parse()
customize.metaConditions = MetaConditionsReader(customize.metaConditions)


"""
Global tags
"""
from Configuration.AlCa.GlobalTag import GlobalTag

if customize.processId == "Data":
    process.GlobalTag.globaltag = str(
        customize.metaConditions['globalTags']['data'])
else:
    process.GlobalTag.globaltag = str(
        customize.metaConditions['globalTags']['MC'])


"""
Preselection
"""
from flashgg.Taggers.flashggPreselectedDiPhotons_cfi import flashggPreselectedDiPhotons
process.flashggPreselectedDiPhotons = flashggPreselectedDiPhotons.clone(
        src=cms.InputTag("flashggDiPhotons")
        )


"""
Systematics
"""


"""
Load and configure dumper
"""
from flashgg.Taggers.diphotonDumper_cfi import diphotonDumper
process.diphotonDumper = diphotonDumper.clone(
        src = cms.InputTag("flashggPreselectedDiPhotons"),
        dumpTrees = cms.untracked.bool(True)
        )


"""
Categories
"""
import flashgg.Taggers.dumperConfigTools as cfgTools

variables = ["mass", "pt", "eta", "leadPt := leadingPhoton.pt", "subleadPt := subLeadingPhoton.pt"]

cfgTools.addCategories(
        process.diphotonDumper,
        [("All", "1", 0)],
        variables=variables,
        histograms=[]
        )

"""
Schedule process
"""
process.p = cms.Path(
        process.flashggPreselectedDiPhotons
        * process.diphotonDumper
        )

customize(process)
