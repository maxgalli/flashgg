#!/bin/bash

outDir=$1
if [[ -z $outDir ]]; then
    echo "usage: $0 <outDir>"
    exit -1
fi


mkdir -p /eos/cms/store/group/phys_higgs/cmshgg/gallim/TnPProduction/${outDir}_mc_UL18
fggRunJobs.py --load jobs_UL18_MC.json -x cmsRun tagAndProbe_test.py -d ${outDir}_mc_UL18 maxEvents=-1 useAAA=1 doPhoIdInputsCorrections=1 -q tomorrow --make-light-tarball --stage-to=/eos/cms/store/group/phys_higgs/cmshgg/gallim/TnPProduction/${outDir}_mc_UL18/ -n 500 --no-copy-proxy -H &

mkdir -p /eos/cms/store/group/phys_higgs/cmshgg/gallim/TnPProduction/${outDir}_data_UL18
fggRunJobs.py --load jobs_UL18_data.json -x cmsRun tagAndProbe_test.py -d ${outDir}_data_UL18 maxEvents=-1 useAAA=1 doPhoIdInputsCorrections=1 -q tomorrow --make-light-tarball --stage-to=/eos/cms/store/group/phys_higgs/cmshgg/gallim/TnPProduction/${outDir}_data_UL18 -n 500 --no-copy-proxy -H &
